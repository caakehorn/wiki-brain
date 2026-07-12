#!/usr/bin/env python3
"""Personal Wiki — single-file local app (v2 GUI).

Run:  python3 app.py   (or double-click Wiki.command / the Dock app)
Serves http://127.0.0.1:8477 — Python stdlib only, localhost only.

Tabs: Wiki (browse / edit / rename), Capture (notes + @-targets + upload),
Ingest (prompt-pack / apply loop for any LLM), Export. Header shows git
sync state; Sync commits, pulls --rebase, and pushes to origin.
All data stays in the plain Markdown files of this repository.
"""
import datetime
import json
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = ROOT / "inbox"
WIKI = ROOT / "wiki"
PORT = 8477
TEXT_EXT = {".md", ".txt", ".csv", ".json", ".html", ".rtf", ".yaml", ".yml"}
_vis_cache = {"checked": False, "public": None, "repo": None}


# ---------------------------------------------------------------- helpers

def safe(path_str):
    p = (ROOT / path_str).resolve()
    if not str(p).startswith(str(ROOT) + "/") and p != ROOT:
        raise PermissionError(path_str)
    return p


def slugify(text, maxlen=60):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:maxlen].rstrip("-") or "note"


def stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")


def log_line(op, domain, desc):
    today = datetime.date.today().isoformat()
    with open(ROOT / "log.md", "a", encoding="utf-8") as f:
        f.write(f"## [{today}] {op} | {domain} | {desc}\n")


def save_note(body, title=None, tags=None, targets=None):
    INBOX.mkdir(exist_ok=True)
    title = (title or body.strip().splitlines()[0][:60]).strip()
    path = INBOX / f"{stamp()}_{slugify(title, 40)}.md"
    words = len(body.split())
    kind = "correction" if targets else ("story" if words > 150 else "fact")
    front = [
        "---",
        f"captured: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"title: {title}",
        f"type: {kind}",
        f"tags: [{', '.join(tags or [])}]",
    ]
    if targets:
        front.append(f"targets: [{', '.join(targets)}]")
    front += ["source: wiki-app", "---", ""]
    path.write_text("\n".join(front) + body.strip() + "\n", encoding="utf-8")
    return {"saved": str(path.relative_to(ROOT)), "words": words, "kind": kind}


def save_page(rel_path, content):
    p = safe(rel_path)
    if not (str(p).startswith(str(WIKI) + "/") and p.suffix == ".md" and p.exists()):
        raise PermissionError("can only edit existing wiki/*.md pages")
    today = datetime.date.today().isoformat()
    content = re.sub(r"(?m)^date_modified: .*$", f"date_modified: {today}",
                     content, count=1)
    p.write_text(content, encoding="utf-8")
    domain = rel_path.split("/")[1] if rel_path.count("/") >= 2 else "all"
    log_line("edit", domain, f"human edit via app: {rel_path}")
    return {"saved": rel_path}


def rename_page(rel_path, new_name):
    """Rename a wiki page and rewrite every inbound reference."""
    p = safe(rel_path)
    if not (str(p).startswith(str(WIKI) + "/") and p.suffix == ".md" and p.exists()):
        raise PermissionError("can only rename existing wiki/*.md pages")
    if p.name == "index.md":
        raise PermissionError("index pages cannot be renamed")
    new_slug = slugify(new_name)
    if not new_slug:
        raise PermissionError("empty new name")
    new_p = p.parent / (new_slug + ".md")
    if new_p.exists():
        raise PermissionError(f"target already exists: {new_p.relative_to(ROOT)}")

    old_ref = str(p.relative_to(ROOT))[:-3]      # wiki/people/foo
    new_ref = str(new_p.relative_to(ROOT))[:-3]
    p.rename(new_p)

    pat = re.compile(re.escape(old_ref) + r"(?![-\w])")
    updated = []
    for f in list(WIKI.rglob("*.md")) + [ROOT / "index.md"]:
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        t2 = pat.sub(new_ref, t)
        if t2 != t:
            f.write_text(t2, encoding="utf-8")
            updated.append(str(f.relative_to(ROOT)))
    # touch date_modified on the page itself
    t = new_p.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^date_modified: .*$",
               f"date_modified: {datetime.date.today().isoformat()}", t, count=1)
    new_p.write_text(t, encoding="utf-8")
    domain = new_ref.split("/")[1]
    log_line("rename", domain, f"{old_ref}.md -> {new_ref}.md ({len(updated)} pages relinked) via app")
    return {"newPath": new_ref + ".md", "linksUpdated": len(updated), "files": updated}


def tree():
    def entry(p):
        return {"path": str(p.relative_to(ROOT)), "name": p.name,
                "size": p.stat().st_size}
    wiki_files = [entry(p) for p in sorted(WIKI.rglob("*.md"))]
    meta = [entry(ROOT / n) for n in
            ("index.md", "README.md", "STYLE_GUIDE.md", "INGEST_PROTOCOL.md",
             "LLM_HANDOFF.md", "task.md", "queue.md", "log.md", "contact-review.md",
             "CLAUDE.md") if (ROOT / n).exists()]
    inbox = []
    if INBOX.exists():
        for p in sorted(INBOX.iterdir()):
            if p.name.startswith("."):
                continue
            size = (sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
                    if p.is_dir() else p.stat().st_size)
            inbox.append({"path": str(p.relative_to(ROOT)), "name": p.name,
                          "size": size, "dir": p.is_dir()})
    return {"wiki": wiki_files, "meta": meta, "inbox": inbox}


def search(q):
    q = q.lower()
    hits = []
    files = sorted(WIKI.rglob("*.md")) + [ROOT / n for n in ("index.md", "log.md", "queue.md")]
    for f in files:
        if not f.exists():
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lines = [(i + 1, l.strip()) for i, l in enumerate(text.splitlines()) if q in l.lower()]
        if lines:
            hits.append({"path": str(f.relative_to(ROOT)),
                         "matches": [{"line": n, "text": t[:200]} for n, t in lines[:5]],
                         "count": len(lines)})
        if len(hits) >= 50:
            break
    return hits


def run(cmd, timeout=120):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, timeout=timeout)
    return r.returncode, (r.stdout + r.stderr).strip()


def export(opts):
    cmd = [sys.executable, str(ROOT / "bin" / "export-corpus")]
    if opts.get("raw"): cmd.append("--raw")
    if opts.get("inbox"): cmd.append("--inbox")
    if opts.get("domain"): cmd += ["--domain", opts["domain"]]
    _, out = run(cmd)
    m = re.search(r"-> (\S+)", out)
    return {"message": out, "file": m.group(1) if m else None}


def ingest_pack(item):
    code, out = run([sys.executable, str(ROOT / "bin" / "ingest-pack"), item])
    prompt_file = ROOT / "exports" / "ingest-prompt.md"
    prompt = prompt_file.read_text(encoding="utf-8") if prompt_file.exists() and code == 0 else ""
    return {"message": out, "prompt": prompt, "ok": code == 0}


def ingest_apply(response_text, commit):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     dir=str(ROOT / "exports")) as f:
        f.write(response_text)
        tmp = f.name
    try:
        cmd = [sys.executable, str(ROOT / "bin" / "ingest-apply"), tmp]
        if commit:
            cmd.append("--commit")
        code, out = run(cmd)
        return {"message": out, "ok": code == 0}
    finally:
        Path(tmp).unlink(missing_ok=True)


def git_status():
    _, branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    _, dirty = run(["git", "status", "--porcelain"])
    run(["git", "fetch", "--quiet"], timeout=15)
    _, counts = run(["git", "rev-list", "--left-right", "--count", "HEAD...@{upstream}"])
    ahead = behind = 0
    if counts and "\t" in counts:
        a, b = counts.split("\t")
        ahead, behind = int(a), int(b)
    _, remote = run(["git", "remote", "get-url", "origin"])
    remote_disp = re.sub(r"//[^@]+@", "//", remote)  # strip embedded credentials
    public = None
    m = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", remote)
    if m:
        repo = m.group(1)
        if _vis_cache["repo"] != repo or not _vis_cache["checked"]:
            try:
                req = urllib.request.Request(f"https://api.github.com/repos/{repo}",
                                             headers={"User-Agent": "wiki-app"})
                with urllib.request.urlopen(req, timeout=4) as r:
                    public = (r.status == 200)
            except Exception:
                public = False  # 404 for private repos when unauthenticated
            _vis_cache.update(checked=True, public=public, repo=repo)
        public = _vis_cache["public"]
    return {"branch": branch, "dirty": len(dirty.splitlines()) if dirty else 0,
            "ahead": ahead, "behind": behind, "remote": remote_disp, "public": public}


def git_sync(message):
    steps = []
    _, dirty = run(["git", "status", "--porcelain"])
    if dirty:
        run(["git", "add", "-A"])
        code, out = run(["git", "commit", "-m", message or "edit: app sync commit"])
        steps.append(out.splitlines()[0] if out else "committed")
        if code != 0:
            return {"ok": False, "message": "\n".join(steps)}
    code, out = run(["git", "pull", "--rebase", "--quiet"], timeout=120)
    steps.append("pulled" if code == 0 else f"pull failed: {out[-300:]}")
    if code != 0:
        return {"ok": False, "message": "\n".join(steps)}
    code, out = run(["git", "push", "--quiet"], timeout=120)
    steps.append("pushed" if code == 0 else f"push failed: {out[-300:]}")
    return {"ok": code == 0, "message": "\n".join(steps)}


# ---------------------------------------------------------------- server

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body, ctype="application/json", extra=None):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def body_json(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(url.query)
        try:
            if url.path == "/":
                self.send(200, PAGE.encode(), "text/html; charset=utf-8")
            elif url.path == "/api/tree":
                self.send(200, tree())
            elif url.path == "/api/file":
                p = safe(qs["path"][0])
                if p.is_dir():
                    self.send(200, {"path": qs["path"][0], "dir": True,
                                    "content": "\n".join(f.name for f in sorted(p.iterdir()))})
                elif p.suffix.lower() in TEXT_EXT and p.stat().st_size < 2_000_000:
                    self.send(200, {"path": qs["path"][0],
                                    "content": p.read_text(encoding="utf-8", errors="replace")})
                else:
                    self.send(200, {"path": qs["path"][0], "binary": True,
                                    "content": f"[{p.suffix or 'binary'} file, {p.stat().st_size:,} bytes]"})
            elif url.path == "/api/search":
                self.send(200, search(qs.get("q", [""])[0]))
            elif url.path == "/api/git/status":
                self.send(200, git_status())
            elif url.path == "/api/download":
                p = safe(qs["path"][0])
                self.send(200, p.read_bytes(), "application/octet-stream",
                          {"Content-Disposition": f'attachment; filename="{p.name}"'})
            else:
                self.send(404, {"error": "not found"})
        except (PermissionError, KeyError, FileNotFoundError) as e:
            self.send(400, {"error": str(e)})

    def do_POST(self):
        try:
            d = {}
            if self.path != "/api/upload":
                d = self.body_json()
            if self.path == "/api/capture":
                if not d.get("body", "").strip():
                    self.send(400, {"error": "empty note"}); return
                self.send(200, save_note(d["body"], d.get("title") or None,
                                         [t.strip() for t in d.get("tags", "").split(",") if t.strip()],
                                         d.get("targets") or None))
            elif self.path == "/api/save":
                if not d.get("content", "").strip():
                    self.send(400, {"error": "refusing to save an empty page"}); return
                self.send(200, save_page(d["path"], d["content"]))
            elif self.path == "/api/rename":
                self.send(200, rename_page(d["path"], d["newName"]))
            elif self.path == "/api/upload":
                name = Path(urllib.parse.unquote(self.headers.get("X-Filename", "upload.bin"))).name
                n = int(self.headers.get("Content-Length", 0))
                if n > 500_000_000:
                    self.send(400, {"error": "file too large (500MB cap)"}); return
                INBOX.mkdir(exist_ok=True)
                dest = INBOX / f"{stamp()}_{name}"
                with open(dest, "wb") as f:
                    remaining = n
                    while remaining:
                        chunk = self.rfile.read(min(65536, remaining))
                        if not chunk: break
                        f.write(chunk); remaining -= len(chunk)
                self.send(200, {"saved": str(dest.relative_to(ROOT)), "bytes": n})
            elif self.path == "/api/export":
                self.send(200, export(d))
            elif self.path == "/api/ingest/pack":
                self.send(200, ingest_pack(d["item"]))
            elif self.path == "/api/ingest/apply":
                if not d.get("response", "").strip():
                    self.send(400, {"error": "empty response text"}); return
                self.send(200, ingest_apply(d["response"], bool(d.get("commit"))))
            elif self.path == "/api/git/sync":
                self.send(200, git_sync(d.get("message", "")))
            elif self.path == "/api/delete-inbox":
                p = safe(d["path"])
                if p.parent != INBOX:
                    self.send(400, {"error": "can only delete inbox items"}); return
                shutil.rmtree(p) if p.is_dir() else p.unlink()
                self.send(200, {"deleted": d["path"]})
            else:
                self.send(404, {"error": "not found"})
        except Exception as e:
            self.send(500, {"error": str(e)})


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Personal Wiki</title>
<style>
:root{
  --bg:#f6f4ef; --panel:#fffdf8; --ink:#26221c; --muted:#7a7263;
  --line:#e4dfd3; --accent:#7a5c2e; --accent-ink:#fff; --chip:#efe9db;
  --code:#f0ece1; --mark:#f3e4b5; --ok:#3d7a3d; --warn:#a33b3b;
}
@media (prefers-color-scheme: dark){
  :root{ --bg:#191713; --panel:#211e19; --ink:#e8e2d5; --muted:#968c78;
    --line:#37322a; --accent:#c9a25e; --accent-ink:#1a1610; --chip:#2c2820;
    --code:#2a261f; --mark:#5a4a1e; --ok:#7dbb7d; --warn:#e08585; }
}
*{box-sizing:border-box; margin:0}
body{font:15px/1.6 "Avenir Next","Segoe UI",system-ui,sans-serif;
  background:var(--bg); color:var(--ink); height:100vh; display:flex; flex-direction:column}
header{display:flex; align-items:center; gap:16px; padding:9px 16px;
  border-bottom:1px solid var(--line); background:var(--panel); flex-wrap:wrap}
header h1{font-size:15px; letter-spacing:.05em}
nav{display:flex; gap:2px}
nav button{border:0; background:none; color:var(--muted); font:inherit;
  padding:6px 13px; border-radius:8px; cursor:pointer}
nav button.on{background:var(--accent); color:var(--accent-ink)}
#gitBar{margin-left:auto; display:flex; align-items:center; gap:8px; font-size:12.5px; color:var(--muted)}
#gitPill{padding:3px 10px; border:1px solid var(--line); border-radius:20px; white-space:nowrap}
#gitPill b{color:var(--ink)}
#syncBtn{border:1px solid var(--line); background:var(--panel); color:var(--ink);
  font:inherit; font-size:12.5px; padding:4px 14px; border-radius:20px; cursor:pointer}
#syncBtn:hover{border-color:var(--accent); color:var(--accent)}
#pubWarn{width:100%; background:var(--warn); color:#fff; padding:6px 16px;
  font-size:13px; display:none; border-radius:8px}
main{flex:1; display:flex; min-height:0}
.hidden{display:none !important}
.tab{flex:1; display:flex; min-height:0}

/* sidebar */
#side{width:300px; border-right:1px solid var(--line); overflow-y:auto;
  background:var(--panel); padding:12px; flex-shrink:0}
#side input{width:100%; padding:7px 10px; border:1px solid var(--line);
  border-radius:8px; background:var(--bg); color:var(--ink); font:inherit; margin-bottom:10px}
#side details{margin-bottom:2px}
#side summary{font-size:11.5px; text-transform:uppercase; letter-spacing:.09em;
  color:var(--muted); cursor:pointer; padding:5px 4px; user-select:none; list-style:none}
#side summary::before{content:"▸ "; font-size:9px}
#side details[open] summary::before{content:"▾ "}
#side summary .n{float:right; font-size:10.5px; opacity:.7}
#side a{display:block; padding:2.5px 8px 2.5px 18px; border-radius:6px; color:var(--ink);
  text-decoration:none; font-size:13.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
#side a:hover{background:var(--chip)}
#side a.on{background:var(--accent); color:var(--accent-ink)}

/* content + toolbar */
#contentWrap{flex:1; display:flex; flex-direction:column; min-width:0}
#toolbar{display:flex; align-items:center; gap:8px; padding:8px 20px;
  border-bottom:1px solid var(--line); background:var(--panel); min-height:42px}
#crumb{font:12px ui-monospace,monospace; color:var(--muted); flex:1;
  overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.tbtn{border:1px solid var(--line); background:none; color:var(--muted); font:inherit;
  font-size:12.5px; padding:4px 13px; border-radius:7px; cursor:pointer}
.tbtn:hover{color:var(--accent); border-color:var(--accent)}
#content{flex:1; overflow-y:auto; padding:30px 44px; max-width:880px}
#content h1{font-size:25px; margin:0 0 14px}
#content h2{font-size:19px; margin:26px 0 8px}
#content h3{font-size:16px; margin:20px 0 6px}
#content p{margin:10px 0}
#content ul,#content ol{margin:10px 0 10px 26px}
#content table{border-collapse:collapse; margin:14px 0; width:100%}
#content th,#content td{border:1px solid var(--line); padding:6px 10px; text-align:left; font-size:14px}
#content th{background:var(--chip)}
#content blockquote{border-left:3px solid var(--accent); padding:4px 14px; margin:12px 0; color:var(--muted)}
#content code{background:var(--code); padding:1px 5px; border-radius:4px; font-size:13px}
#content pre{background:var(--code); padding:12px 14px; border-radius:8px; overflow-x:auto; margin:12px 0}
#content pre code{background:none; padding:0}
#content a{color:var(--accent)}
#content hr{border:0; border-top:1px solid var(--line); margin:20px 0}
#content mark{background:var(--mark); color:inherit; border-radius:3px; padding:0 2px}
.fm{background:var(--chip); border-radius:8px; padding:8px 12px; font-size:12px;
  color:var(--muted); margin-bottom:18px; white-space:pre-wrap; font-family:ui-monospace,monospace}
.hit{border:1px solid var(--line); border-radius:10px; padding:10px 14px; margin:10px 0;
  cursor:pointer; background:var(--panel)}
.hit:hover{border-color:var(--accent)}
.hit .p{font-weight:600; font-size:13.5px}
.hit .l{font-size:13px; color:var(--muted); margin-top:2px}

/* editor */
#editor{flex:1; display:none; flex-direction:column; padding:14px 20px; min-height:0}
#editor textarea{flex:1; width:100%; resize:none; padding:14px;
  border:1px solid var(--line); border-radius:10px; background:var(--panel);
  color:var(--ink); font:13px/1.5 ui-monospace,"SF Mono",Menlo,monospace}
.editbar{display:flex; gap:10px; margin-bottom:10px; align-items:center}

/* generic pane/card (capture, ingest, export) */
.pane{flex:1; overflow-y:auto; padding:30px; display:flex; justify-content:center; gap:26px}
.card{width:100%; max-width:660px}
.card h2{margin-bottom:4px}
.card .sub2{color:var(--muted); font-size:13.5px; margin-bottom:16px}
.card label{display:block; font-size:11.5px; text-transform:uppercase;
  letter-spacing:.08em; color:var(--muted); margin:13px 0 4px}
.card input[type=text], .card textarea, .card select{width:100%; padding:9px 12px;
  border:1px solid var(--line); border-radius:8px; background:var(--panel);
  color:var(--ink); font:inherit}
.card textarea{min-height:200px; resize:vertical; line-height:1.5}
.btn{margin-top:12px; padding:8px 20px; border:0; border-radius:8px;
  background:var(--accent); color:var(--accent-ink); font:inherit; font-weight:600; cursor:pointer}
.btn:disabled{opacity:.5}
.ghost{background:var(--chip); color:var(--ink)}
.msg{margin-top:10px; font-size:13px; color:var(--accent); white-space:pre-wrap}
#drop{margin-top:16px; border:2px dashed var(--line); border-radius:12px;
  padding:22px; text-align:center; color:var(--muted); cursor:pointer}
#drop.over{border-color:var(--accent); color:var(--accent)}
.acwrap{position:relative}
#ac{position:absolute; left:0; right:0; z-index:10; background:var(--panel);
  border:1px solid var(--line); border-radius:10px; box-shadow:0 8px 24px rgba(0,0,0,.15);
  max-height:220px; overflow-y:auto; display:none}
#ac div{padding:7px 12px; cursor:pointer; font-size:13.5px}
#ac div .d{color:var(--muted); font-size:11.5px; margin-left:8px}
#ac div.sel{background:var(--accent); color:var(--accent-ink)}
#ac div.sel .d{color:var(--accent-ink); opacity:.75}
#targets{display:flex; flex-wrap:wrap; gap:6px; margin-top:8px}
.tchip{display:inline-flex; align-items:center; gap:6px; background:var(--chip);
  border:1px solid var(--line); border-radius:20px; padding:3px 10px; font-size:12.5px}
.tchip button{border:0; background:none; color:var(--muted); cursor:pointer; padding:0}
.inb{display:flex; align-items:center; gap:10px; padding:9px 12px;
  border:1px solid var(--line); border-radius:9px; margin:6px 0; font-size:13.5px; cursor:pointer}
.inb.sel{border-color:var(--accent); background:var(--chip)}
.inb .nm{flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.inb .sz{color:var(--muted); font-size:12px}
.inb button{border:0; background:none; color:var(--muted); cursor:pointer; font-size:15px}
.inb button:hover{color:var(--warn)}
.step{border:1px solid var(--line); border-radius:12px; padding:16px 18px; margin:12px 0;
  background:var(--panel)}
.step h3{font-size:14px; margin-bottom:6px}
.step .hint{font-size:12.5px; color:var(--muted); margin-bottom:8px}
.note{background:var(--chip); border-radius:10px; padding:12px 16px; font-size:13px;
  color:var(--muted); margin-top:18px}
dialog{border:1px solid var(--line); border-radius:14px; background:var(--panel);
  color:var(--ink); padding:22px; max-width:430px; box-shadow:0 20px 60px rgba(0,0,0,.3)}
dialog::backdrop{background:rgba(0,0,0,.35)}
dialog input{width:100%; padding:9px 12px; border:1px solid var(--line); border-radius:8px;
  background:var(--bg); color:var(--ink); font:inherit; margin:10px 0}
</style>
</head>
<body>
<header>
  <h1>PERSONAL WIKI</h1>
  <nav>
    <button data-tab="wikiTab" class="on">Wiki</button>
    <button data-tab="captureTab">Capture</button>
    <button data-tab="ingestTab">Ingest <span id="inboxN"></span></button>
    <button data-tab="exportTab">Export</button>
  </nav>
  <div id="gitBar">
    <span id="gitPill">…</span>
    <button id="syncBtn">Sync</button>
  </div>
  <div id="pubWarn">⚠ Your GitHub repo is <b>PUBLIC</b> — anyone can read this wiki. Make it private: repo Settings → Danger Zone → Change visibility.</div>
</header>
<main>

<div id="wikiTab" class="tab">
  <div id="side">
    <input id="q" placeholder="Search the wiki…" autocomplete="off">
    <div id="nav"></div>
  </div>
  <div id="contentWrap">
    <div id="toolbar">
      <span id="crumb"></span>
      <button class="tbtn hidden" id="renameBtn">Rename</button>
      <button class="tbtn hidden" id="editBtn">✎ Edit</button>
    </div>
    <div id="content"><p style="color:var(--muted)">Loading…</p></div>
    <div id="editor">
      <div class="editbar">
        <button class="btn" id="editSave">Save</button>
        <button class="btn ghost" id="editCancel">Cancel</button>
        <span class="msg" id="editMsg" style="margin:0"></span>
      </div>
      <textarea id="editTa" spellcheck="false"></textarea>
    </div>
  </div>
</div>

<div id="captureTab" class="tab pane hidden"><div class="card">
  <h2>Capture</h2>
  <div class="sub2">Type a fact or story — it lands in the inbox for ingestion. Type <b>@</b> to target an existing page (correction/expansion). Square-bracket lines like <code>[RENAME PAGE TO x]</code> are executed as instructions at ingest time.</div>
  <label>Title (optional)</label>
  <input type="text" id="cTitle">
  <label>Text</label>
  <div class="acwrap">
    <textarea id="cBody" placeholder="A fact, a memory, a story… @ to target a page."></textarea>
    <div id="ac"></div>
  </div>
  <div id="targets"></div>
  <label>Tags (optional, comma-separated)</label>
  <input type="text" id="cTags">
  <button class="btn" id="cSave">Save to inbox</button>
  <div class="msg" id="cMsg"></div>
  <div id="drop">Drop files here or click to upload — any format</div>
  <input type="file" id="filePick" multiple style="display:none">
  <div class="msg" id="uMsg"></div>
</div></div>

<div id="ingestTab" class="tab pane hidden">
  <div class="card" style="max-width:380px">
    <h2>Inbox</h2>
    <div class="sub2">Select an item to ingest. Ingestion moves it to raw/ and writes wiki pages.</div>
    <div id="inboxList"></div>
    <div class="note">Prefer Claude Code? Open it in this folder and say "ingest the inbox" — same rules, fully automatic.</div>
  </div>
  <div class="card">
    <h2>Ingest with any LLM</h2>
    <div class="sub2">No subscription needed — works with any chat model.</div>
    <div class="step">
      <h3>1 · Generate the prompt</h3>
      <div class="hint">Bundles the item, the style guide, and the pages it touches.</div>
      <button class="btn" id="packBtn" disabled>Generate prompt</button>
      <span class="msg" id="packMsg"></span>
      <textarea id="packOut" class="hidden" readonly style="min-height:120px; margin-top:10px; font:12px ui-monospace,monospace"></textarea>
      <button class="btn ghost hidden" id="copyBtn">Copy prompt to clipboard</button>
    </div>
    <div class="step">
      <h3>2 · Paste the model's reply</h3>
      <div class="hint">Paste the full response (its FILE/MOVE/LOG blocks are extracted; extra prose is ignored).</div>
      <textarea id="applyIn" style="min-height:140px; font:12px ui-monospace,monospace" placeholder="===FILE: wiki/... ==="></textarea>
      <label style="text-transform:none; font-size:13px; margin-top:8px">
        <input type="checkbox" id="applyCommit" checked> commit automatically if lint passes</label>
      <button class="btn" id="applyBtn">Validate &amp; apply</button>
      <div class="msg" id="applyMsg"></div>
    </div>
  </div>
</div>

<div id="exportTab" class="tab pane hidden"><div class="card">
  <h2>Export corpus</h2>
  <div class="sub2">One Markdown file for LLM ingestion, with a token estimate.</div>
  <label>Scope</label>
  <select id="eDomain">
    <option value="">Whole wiki</option>
    <option>self</option><option>timeline</option><option>people</option>
    <option>mind</option><option>work</option><option>interests</option>
    <option>health</option><option>places</option><option>legal</option>
  </select>
  <label style="margin-top:12px; text-transform:none; font-size:13px"><input type="checkbox" id="eRaw"> include raw/ archive (big)</label>
  <label style="text-transform:none; font-size:13px"><input type="checkbox" id="eInbox"> include un-ingested inbox</label>
  <button class="btn" id="eGo">Export</button>
  <div class="msg" id="eMsg"></div>
</div></div>

</main>

<dialog id="renameDlg">
  <h3 style="margin-bottom:4px">Rename page</h3>
  <div style="font-size:13px; color:var(--muted)" id="renameFrom"></div>
  <input type="text" id="renameTo" placeholder="new name (will be slugified)">
  <div style="display:flex; gap:10px">
    <button class="btn" id="renameGo">Rename &amp; update links</button>
    <button class="btn ghost" id="renameCancel">Cancel</button>
  </div>
  <div class="msg" id="renameMsg"></div>
</dialog>

<script>
const $=s=>document.querySelector(s), api=async(p,o)=>(await fetch(p,o)).json();
let TREE=null, CUR=null, RAW=null, SEL_INBOX=null;

/* ---------- tabs ---------- */
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{
  document.querySelectorAll("nav button").forEach(x=>x.classList.toggle("on",x===b));
  document.querySelectorAll(".tab").forEach(t=>t.classList.toggle("hidden",t.id!==b.dataset.tab));
});

/* ---------- markdown ---------- */
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function inline(s){
  s=esc(s);
  s=s.replace(/`([^`]+)`/g,"<code>$1</code>");
  s=s.replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>").replace(/(^|\W)\*([^*]+)\*/g,"$1<i>$2</i>");
  s=s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,(m,t,u)=>
    /^https?:/.test(u)?`<a href="${u}" target="_blank">${t}</a>`:`<a href="#" data-wiki="${u}">${t}</a>`);
  s=s.replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g,`<a href="#" data-wiki="$1">$2</a>`);
  s=s.replace(/\[\[([^\]]+)\]\]/g,`<a href="#" data-wiki="$1">$1</a>`);
  return s;
}
function md(text){
  let fm="";
  if(text.startsWith("---")){
    const end=text.indexOf("\n---",3);
    if(end>0){ fm=text.slice(4,end).trim(); text=text.slice(end+4); } }
  const lines=text.split("\n"); let out=[],i=0;
  while(i<lines.length){
    let l=lines[i];
    if(/^```/.test(l)){ let buf=[]; i++;
      while(i<lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]);
      i++; out.push("<pre><code>"+esc(buf.join("\n"))+"</code></pre>"); continue; }
    if(/^#{1,4} /.test(l)){ const n=l.match(/^#+/)[0].length;
      out.push(`<h${n}>`+inline(l.replace(/^#+ /,""))+`</h${n}>`); i++; continue; }
    if(/^---+\s*$/.test(l)){ out.push("<hr>"); i++; continue; }
    if(/^\s*>/.test(l)){ let buf=[];
      while(i<lines.length && /^\s*>/.test(lines[i])) buf.push(lines[i++].replace(/^\s*> ?/,""));
      out.push("<blockquote>"+buf.map(inline).join("<br>")+"</blockquote>"); continue; }
    if(/^\|.*\|/.test(l) && /^\|[\s:|-]+\|/.test(lines[i+1]||"")){
      let rows=[]; while(i<lines.length && /^\|/.test(lines[i])) rows.push(lines[i++]);
      const cells=r=>r.replace(/^\||\|$/g,"").split("|").map(c=>inline(c.trim()));
      let h="<table><tr>"+cells(rows[0]).map(c=>`<th>${c}</th>`).join("")+"</tr>";
      for(const r of rows.slice(2)) h+="<tr>"+cells(r).map(c=>`<td>${c}</td>`).join("")+"</tr>";
      out.push(h+"</table>"); continue; }
    if(/^\s*[-*] /.test(l)){ let buf=[];
      while(i<lines.length && /^\s*[-*] /.test(lines[i])) buf.push("<li>"+inline(lines[i++].replace(/^\s*[-*] /,""))+"</li>");
      out.push("<ul>"+buf.join("")+"</ul>"); continue; }
    if(/^\s*\d+\. /.test(l)){ let buf=[];
      while(i<lines.length && /^\s*\d+\. /.test(lines[i])) buf.push("<li>"+inline(lines[i++].replace(/^\s*\d+\. /,""))+"</li>");
      out.push("<ol>"+buf.join("")+"</ol>"); continue; }
    if(l.trim()===""){ i++; continue; }
    let buf=[]; while(i<lines.length && lines[i].trim()!=="" &&
      !/^(#|```|>|\||\s*[-*] |\s*\d+\. |---)/.test(lines[i])) buf.push(lines[i++]);
    out.push("<p>"+buf.map(inline).join(" ")+"</p>");
  }
  return (fm?`<div class="fm">${esc(fm)}</div>`:"")+out.join("\n");
}

/* ---------- tree / sidebar ---------- */
async function refresh(keepOpen){
  const open={};
  document.querySelectorAll("#side details").forEach(d=>open[d.dataset.g]=d.open);
  TREE=await api("/api/tree");
  $("#inboxN").textContent=TREE.inbox.length?`(${TREE.inbox.length})`:"";
  const nav=$("#nav"); nav.innerHTML="";
  const groups={};
  for(const f of TREE.wiki){
    const parts=f.path.split("/");
    const g=parts[1]+(parts.length>3?" / "+parts[2]:"");
    (groups[g]=groups[g]||[]).push(f);
  }
  const mk=(gname,items,openDefault)=>{
    const d=document.createElement("details");
    d.dataset.g=gname;
    d.open=(gname in open)?open[gname]:openDefault;
    const s=document.createElement("summary");
    s.innerHTML=`${esc(gname)}<span class="n">${items.length}</span>`;
    d.appendChild(s);
    for(const f of items){
      const a=document.createElement("a");
      a.textContent=f.name.replace(/\.md$/,"");
      a.dataset.path=f.path;
      if(f.path===CUR)a.classList.add("on");
      a.onclick=e=>{e.preventDefault();openPage(f.path)};
      d.appendChild(a);
    }
    nav.appendChild(d);
  };
  const order=Object.keys(groups).sort();
  for(const g of order){
    const items=groups[g].sort((a,b)=>(a.name==="index.md"?-1:b.name==="index.md"?1:a.name<b.name?-1:1));
    mk(g, items, !g.includes("contacts"));
  }
  mk("meta", TREE.meta, false);
  renderInbox();
}
async function gitRefresh(){
  const g=await api("/api/git/status");
  const bits=[`<b>${esc(g.branch||"?")}</b>`];
  if(g.dirty)bits.push(`${g.dirty} uncommitted`);
  if(g.ahead)bits.push(`↑${g.ahead}`);
  if(g.behind)bits.push(`↓${g.behind}`);
  if(!g.dirty&&!g.ahead&&!g.behind)bits.push("in sync");
  $("#gitPill").innerHTML=bits.join(" · ");
  $("#pubWarn").style.display=(g.public===true)?"block":"none";
}
$("#syncBtn").onclick=async()=>{
  $("#syncBtn").disabled=true; $("#syncBtn").textContent="Syncing…";
  const g=await api("/api/git/status");
  if(g.public===true && !confirm("The GitHub repo is PUBLIC. Push anyway?")){
    $("#syncBtn").disabled=false; $("#syncBtn").textContent="Sync"; return; }
  const msg=g.dirty?prompt("Commit message for local changes:","edit: app sync"):"";
  if(g.dirty&&msg===null){ $("#syncBtn").disabled=false; $("#syncBtn").textContent="Sync"; return; }
  const r=await api("/api/git/sync",{method:"POST",body:JSON.stringify({message:msg})});
  alert(r.message);
  $("#syncBtn").disabled=false; $("#syncBtn").textContent="Sync";
  gitRefresh();
};

/* ---------- page view / edit / rename ---------- */
async function openPage(path, highlight){
  CUR=path; RAW=null;
  $("#editor").style.display="none"; $("#content").style.display="block";
  document.querySelectorAll("#side a").forEach(a=>a.classList.toggle("on",a.dataset.path===path));
  const r=await api("/api/file?path="+encodeURIComponent(path));
  $("#crumb").textContent=path;
  const editable=/^wiki\/.+\.md$/.test(path)&&!r.error&&!r.binary&&!r.dir;
  $("#editBtn").classList.toggle("hidden",!(editable||/^(queue|task|contact-review|LLM_HANDOFF)\.md$/.test(path)));
  $("#renameBtn").classList.toggle("hidden",!editable||path.endsWith("index.md"));
  let html="";
  if(r.error) html=`<p>${esc(r.error)}</p>`;
  else if(r.binary||r.dir||!/\.(md|txt)$/.test(path)) html=`<pre>${esc(r.content)}</pre>`;
  else html=md(r.content);
  if(!r.error&&!r.binary&&!r.dir) RAW=r.content;
  const c=$("#content"); c.innerHTML=html;
  if(highlight){ const rx=new RegExp(highlight.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"),"gi");
    c.querySelectorAll("p,li,td,h1,h2,h3,blockquote").forEach(el=>{
      if(rx.test(el.textContent)) el.innerHTML=el.innerHTML.replace(rx,m=>`<mark>${m}</mark>`); }); }
  c.scrollTop=0;
  c.querySelectorAll("a[data-wiki]").forEach(a=>a.onclick=e=>{
    e.preventDefault(); let t=a.dataset.wiki;
    if(!/\.md$/.test(t)) t+=".md";
    const hit=TREE.wiki.concat(TREE.meta).find(f=>f.path===t||f.path.endsWith("/"+t));
    openPage(hit?hit.path:t); });
  // ensure wiki tab visible
  document.querySelectorAll("nav button").forEach(x=>x.classList.toggle("on",x.dataset.tab==="wikiTab"));
  document.querySelectorAll(".tab").forEach(t=>t.classList.toggle("hidden",t.id!=="wikiTab"));
}
$("#editBtn").onclick=()=>{
  if(RAW===null)return;
  $("#editTa").value=RAW;
  $("#content").style.display="none"; $("#editor").style.display="flex";
  $("#editMsg").textContent=""; $("#editTa").focus(); };
$("#editCancel").onclick=()=>openPage(CUR);
$("#editSave").onclick=async()=>{
  const r=await api("/api/save",{method:"POST",body:JSON.stringify({path:CUR,content:$("#editTa").value})});
  if(r.error){$("#editMsg").textContent="⚠ "+r.error; return;}
  await refresh(); openPage(CUR); gitRefresh(); };

$("#renameBtn").onclick=()=>{
  $("#renameFrom").textContent=CUR;
  $("#renameTo").value=""; $("#renameMsg").textContent="";
  $("#renameDlg").showModal(); $("#renameTo").focus(); };
$("#renameCancel").onclick=()=>$("#renameDlg").close();
$("#renameGo").onclick=async()=>{
  const nn=$("#renameTo").value.trim();
  if(!nn){$("#renameMsg").textContent="enter a new name"; return;}
  const r=await api("/api/rename",{method:"POST",body:JSON.stringify({path:CUR,newName:nn})});
  if(r.error){$("#renameMsg").textContent="⚠ "+r.error; return;}
  $("#renameDlg").close();
  await refresh(); openPage(r.newPath); gitRefresh();
  setTimeout(()=>alert(`Renamed. ${r.linksUpdated} page(s) had links updated.`),50); };

/* ---------- search ---------- */
let debounce=null;
$("#q").oninput=()=>{ clearTimeout(debounce);
  const q=$("#q").value.trim();
  if(!q){ if(CUR)openPage(CUR); return; }
  debounce=setTimeout(async()=>{
    const hits=await api("/api/search?q="+encodeURIComponent(q));
    $("#crumb").textContent=`search: ${q}`;
    $("#editBtn").classList.add("hidden"); $("#renameBtn").classList.add("hidden");
    $("#editor").style.display="none"; $("#content").style.display="block";
    const c=$("#content");
    c.innerHTML=(hits.length?"":"<p style='color:var(--muted)'>No matches.</p>")+
      hits.map((h,i)=>`<div class="hit" data-i="${i}"><div class="p">${esc(h.path)}</div>`+
        h.matches.map(m=>`<div class="l">${m.line}: ${esc(m.text)}</div>`).join("")+
        (h.count>5?`<div class="l">…${h.count-5} more</div>`:"")+`</div>`).join("");
    c.querySelectorAll(".hit").forEach(el=>el.onclick=()=>openPage(hits[el.dataset.i].path,q));
  },250); };

/* ---------- capture (@-autocomplete + upload) ---------- */
let TGT=new Set(), acSel=0, acMatches=[], acStart=-1;
const body=$("#cBody"), ac=$("#ac");
function pageList(){ return TREE?TREE.wiki.map(f=>f.path.replace(/\.md$/,"")):[]; }
function renderTargets(){
  const el=$("#targets"); el.innerHTML="";
  for(const t of TGT){
    const c=document.createElement("span"); c.className="tchip";
    c.innerHTML=`<b>@${esc(t.split("/").pop().replace(/\.md$/,""))}</b> <span style="color:var(--muted)">${esc(t)}</span><button>✕</button>`;
    c.querySelector("button").onclick=()=>{TGT.delete(t);renderTargets()};
    el.appendChild(c); } }
function hideAc(){ ac.style.display="none"; acMatches=[]; acStart=-1; }
function showAc(q){
  const ql=q.toLowerCase();
  acMatches=pageList().filter(p=>p.toLowerCase().includes(ql))
    .sort((a,b)=>{
      const an=a.split("/").pop().toLowerCase().startsWith(ql)?0:1;
      const bn=b.split("/").pop().toLowerCase().startsWith(ql)?0:1;
      return an-bn||a.length-b.length; }).slice(0,8);
  if(!acMatches.length){ hideAc(); return; }
  acSel=0;
  ac.innerHTML=acMatches.map((p,i)=>
    `<div class="${i===0?"sel":""}" data-i="${i}"><b>${esc(p.split("/").pop())}</b><span class="d">${esc(p)}</span></div>`).join("");
  ac.style.display="block";
  ac.style.top=Math.min(body.offsetHeight,160)+"px";
  ac.querySelectorAll("div[data-i]").forEach(d=>{
    d.onmousedown=e=>{e.preventDefault();pickAc(+d.dataset.i)};
    d.onmouseover=()=>{acSel=+d.dataset.i;paintAc()}; }); }
function paintAc(){ ac.querySelectorAll("div[data-i]").forEach((d,i)=>d.classList.toggle("sel",i===acSel)); }
function pickAc(i){
  const p=acMatches[i]; if(!p)return;
  const short="@"+p.split("/").pop();
  body.value=body.value.slice(0,acStart)+short+body.value.slice(body.selectionStart);
  const pos=acStart+short.length;
  body.setSelectionRange(pos,pos); body.focus();
  TGT.add(p+".md"); renderTargets(); hideAc(); }
body.addEventListener("input",()=>{
  const caret=body.selectionStart, text=body.value;
  const at=text.lastIndexOf("@",caret-1);
  if(at<0||(at>0&&/[\w/]/.test(text[at-1]))){ hideAc(); return; }
  const q=text.slice(at+1,caret);
  if(/[\s@]/.test(q)||q.length>60){ hideAc(); return; }
  acStart=at; showAc(q); });
body.addEventListener("keydown",e=>{
  if(ac.style.display!=="block")return;
  if(e.key==="ArrowDown"){e.preventDefault();acSel=Math.min(acSel+1,acMatches.length-1);paintAc();}
  else if(e.key==="ArrowUp"){e.preventDefault();acSel=Math.max(acSel-1,0);paintAc();}
  else if(e.key==="Enter"||e.key==="Tab"){e.preventDefault();pickAc(acSel);}
  else if(e.key==="Escape"){hideAc();} });
body.addEventListener("blur",()=>setTimeout(hideAc,150));
$("#cSave").onclick=async()=>{
  const r=await api("/api/capture",{method:"POST",body:JSON.stringify(
    {title:$("#cTitle").value, body:$("#cBody").value, tags:$("#cTags").value, targets:[...TGT]})});
  $("#cMsg").textContent=r.error?("⚠ "+r.error):`✓ saved ${r.saved} (${r.words} words, ${r.kind})`;
  if(!r.error){ $("#cTitle").value=$("#cBody").value=$("#cTags").value=""; TGT.clear(); renderTargets(); refresh(); } };
const drop=$("#drop"), pick=$("#filePick");
drop.onclick=()=>pick.click();
drop.ondragover=e=>{e.preventDefault();drop.classList.add("over")};
drop.ondragleave=()=>drop.classList.remove("over");
drop.ondrop=e=>{e.preventDefault();drop.classList.remove("over");upload(e.dataTransfer.files)};
pick.onchange=()=>upload(pick.files);
async function upload(files){
  for(const f of files){
    $("#uMsg").textContent=`uploading ${f.name}…`;
    const r=await(await fetch("/api/upload",{method:"POST",
      headers:{"X-Filename":encodeURIComponent(f.name)},body:f})).json();
    $("#uMsg").textContent=r.error?("⚠ "+r.error):`✓ ${r.saved}`; }
  refresh(); }

/* ---------- ingest ---------- */
function renderInbox(){
  const el=$("#inboxList"); el.innerHTML="";
  if(!TREE.inbox.length){ el.innerHTML="<p style='color:var(--muted); font-size:13.5px'>Inbox is empty.</p>"; $("#packBtn").disabled=true; return; }
  for(const f of TREE.inbox){
    const d=document.createElement("div"); d.className="inb"+(f.path===SEL_INBOX?" sel":"");
    d.innerHTML=`<span class="nm">${esc(f.name)}</span><span class="sz">${f.size.toLocaleString()} B</span><button title="delete">✕</button>`;
    d.onclick=e=>{
      if(e.target.tagName==="BUTTON")return;
      SEL_INBOX=f.path; renderInbox(); $("#packBtn").disabled=false;
      $("#packMsg").textContent=""; $("#packOut").classList.add("hidden"); $("#copyBtn").classList.add("hidden"); };
    d.querySelector("button").onclick=async()=>{
      if(!confirm(`Delete ${f.name}? This cannot be undone.`))return;
      await api("/api/delete-inbox",{method:"POST",body:JSON.stringify({path:f.path})});
      if(SEL_INBOX===f.path)SEL_INBOX=null;
      refresh(); };
    el.appendChild(d); }
  $("#packBtn").disabled=!SEL_INBOX; }
$("#packBtn").onclick=async()=>{
  $("#packBtn").disabled=true; $("#packMsg").textContent="packing…";
  const r=await api("/api/ingest/pack",{method:"POST",body:JSON.stringify({item:SEL_INBOX.replace(/^inbox\//,"")})});
  $("#packBtn").disabled=false;
  $("#packMsg").textContent=r.ok?r.message.split("\n").slice(0,2).join(" · "):("⚠ "+r.message);
  if(r.ok){ $("#packOut").value=r.prompt; $("#packOut").classList.remove("hidden");
    $("#copyBtn").classList.remove("hidden"); } };
$("#copyBtn").onclick=async()=>{
  await navigator.clipboard.writeText($("#packOut").value);
  $("#copyBtn").textContent="✓ Copied"; setTimeout(()=>$("#copyBtn").textContent="Copy prompt to clipboard",1500); };
$("#applyBtn").onclick=async()=>{
  $("#applyBtn").disabled=true; $("#applyMsg").textContent="applying…";
  const r=await api("/api/ingest/apply",{method:"POST",body:JSON.stringify(
    {response:$("#applyIn").value, commit:$("#applyCommit").checked})});
  $("#applyBtn").disabled=false;
  $("#applyMsg").textContent=(r.ok?"✓\n":"⚠\n")+(r.message||r.error||"");
  if(r.ok){ $("#applyIn").value=""; SEL_INBOX=null; refresh(); gitRefresh(); } };

/* ---------- export ---------- */
$("#eGo").onclick=async()=>{
  $("#eGo").disabled=true; $("#eMsg").textContent="exporting…";
  const r=await api("/api/export",{method:"POST",body:JSON.stringify(
    {domain:$("#eDomain").value, raw:$("#eRaw").checked, inbox:$("#eInbox").checked})});
  $("#eGo").disabled=false;
  $("#eMsg").innerHTML=esc(r.message)+(r.file?
    `<br><a href="/api/download?path=${encodeURIComponent(r.file)}" style="color:var(--accent)">⬇ download</a>`:""); };

/* ---------- boot ---------- */
refresh().then(()=>openPage("index.md"));
gitRefresh(); setInterval(gitRefresh, 120000);
</script>
</body>
</html>"""


def main():
    import os
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}"
    print(f"Personal Wiki running at {url}  (Ctrl-C to stop)")
    if not os.environ.get("WIKI_APP_EXTERNAL_OPEN"):
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
