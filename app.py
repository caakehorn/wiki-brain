#!/usr/bin/env python3
"""Personal Wiki — single-file local app.

Run:  python3 app.py   (or double-click Wiki.command)
Then a browser opens at http://127.0.0.1:8477

One process, Python stdlib only, no network beyond localhost. It serves a UI
for: capturing facts/stories, uploading files, browsing and searching the
compiled wiki, viewing the inbox, and exporting the corpus for LLMs.
All data stays in the plain Markdown files of this repository.
"""
import datetime
import json
import re
import shutil
import subprocess
import sys
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = ROOT / "inbox"
WIKI = ROOT / "wiki"
PORT = 8477
TEXT_EXT = {".md", ".txt", ".csv", ".json", ".html", ".rtf", ".yaml", ".yml"}


# ---------------------------------------------------------------- helpers

def safe(path_str):
    """Resolve a repo-relative path, refusing anything outside ROOT."""
    p = (ROOT / path_str).resolve()
    if not str(p).startswith(str(ROOT) + "/") and p != ROOT:
        raise PermissionError(path_str)
    return p


def slugify(text, maxlen=40):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:maxlen].rstrip("-") or "note"


def stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")


def save_note(body, title=None, tags=None):
    INBOX.mkdir(exist_ok=True)
    title = (title or body.strip().splitlines()[0][:60]).strip()
    path = INBOX / f"{stamp()}_{slugify(title)}.md"
    words = len(body.split())
    kind = "story" if words > 150 else "fact"
    front = [
        "---",
        f"captured: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"title: {title}",
        f"type: {kind}",
        f"tags: [{', '.join(tags or [])}]",
        "source: wiki-app",
        "---",
        "",
    ]
    path.write_text("\n".join(front) + body.strip() + "\n", encoding="utf-8")
    return {"saved": str(path.relative_to(ROOT)), "words": words, "kind": kind}


def tree():
    def entry(p):
        return {"path": str(p.relative_to(ROOT)), "name": p.name,
                "size": p.stat().st_size}
    wiki_files = [entry(p) for p in sorted(WIKI.rglob("*.md"))]
    meta = [entry(ROOT / n) for n in ("index.md", "log.md", "queue.md", "README.md", "CLAUDE.md")
            if (ROOT / n).exists()]
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
    scopes = [WIKI] + [ROOT / n for n in ("index.md", "log.md", "queue.md")]
    files = []
    for s in scopes:
        if s.is_dir():
            files += sorted(s.rglob("*.md"))
        elif s.exists():
            files.append(s)
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lines = [(i + 1, l.strip()) for i, l in enumerate(text.splitlines())
                 if q in l.lower()]
        if lines:
            hits.append({"path": str(f.relative_to(ROOT)),
                         "matches": [{"line": n, "text": t[:200]} for n, t in lines[:5]],
                         "count": len(lines)})
        if len(hits) >= 50:
            break
    return hits


def export(opts):
    cmd = [sys.executable, str(ROOT / "bin" / "export-corpus")]
    if opts.get("raw"):
        cmd.append("--raw")
    if opts.get("inbox"):
        cmd.append("--inbox")
    if opts.get("domain"):
        cmd += ["--domain", opts["domain"]]
    out = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    result = (out.stdout + out.stderr).strip()
    m = re.search(r"-> (\S+)", result)
    return {"message": result, "file": m.group(1) if m else None}


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
                    listing = "\n".join(f.name for f in sorted(p.iterdir()))
                    self.send(200, {"path": qs["path"][0], "content": listing, "dir": True})
                elif p.suffix.lower() in TEXT_EXT and p.stat().st_size < 2_000_000:
                    self.send(200, {"path": qs["path"][0],
                                    "content": p.read_text(encoding="utf-8", errors="replace")})
                else:
                    self.send(200, {"path": qs["path"][0], "binary": True,
                                    "content": f"[{p.suffix or 'binary'} file, {p.stat().st_size:,} bytes — not viewable as text]"})
            elif url.path == "/api/search":
                self.send(200, search(qs.get("q", [""])[0]))
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
            if self.path == "/api/capture":
                d = self.body_json()
                if not d.get("body", "").strip():
                    self.send(400, {"error": "empty note"})
                    return
                self.send(200, save_note(d["body"], d.get("title") or None,
                                         [t.strip() for t in d.get("tags", "").split(",") if t.strip()]))
            elif self.path == "/api/upload":
                name = urllib.parse.unquote(self.headers.get("X-Filename", "upload.bin"))
                name = Path(name).name  # strip any path components
                n = int(self.headers.get("Content-Length", 0))
                if n > 500_000_000:
                    self.send(400, {"error": "file too large (500MB cap)"})
                    return
                INBOX.mkdir(exist_ok=True)
                dest = INBOX / f"{stamp()}_{name}"
                with open(dest, "wb") as f:
                    remaining = n
                    while remaining:
                        chunk = self.rfile.read(min(65536, remaining))
                        if not chunk:
                            break
                        f.write(chunk)
                        remaining -= len(chunk)
                self.send(200, {"saved": str(dest.relative_to(ROOT)), "bytes": n})
            elif self.path == "/api/export":
                self.send(200, export(self.body_json()))
            elif self.path == "/api/delete-inbox":
                d = self.body_json()
                p = safe(d["path"])
                if p.parent != INBOX:
                    self.send(400, {"error": "can only delete inbox items"})
                    return
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    p.unlink()
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
  --code:#f0ece1; --mark:#f3e4b5;
}
@media (prefers-color-scheme: dark){
  :root{ --bg:#191713; --panel:#211e19; --ink:#e8e2d5; --muted:#968c78;
    --line:#37322a; --accent:#c9a25e; --accent-ink:#1a1610; --chip:#2c2820;
    --code:#2a261f; --mark:#5a4a1e; }
}
*{box-sizing:border-box; margin:0}
body{font:15px/1.6 "Avenir Next", "Segoe UI", system-ui, sans-serif;
  background:var(--bg); color:var(--ink); height:100vh; display:flex; flex-direction:column}
header{display:flex; align-items:center; gap:18px; padding:10px 18px;
  border-bottom:1px solid var(--line); background:var(--panel)}
header h1{font-size:16px; letter-spacing:.04em}
nav{display:flex; gap:4px}
nav button{border:0; background:none; color:var(--muted); font:inherit;
  padding:6px 12px; border-radius:8px; cursor:pointer}
nav button.on{background:var(--accent); color:var(--accent-ink)}
#inboxBadge{margin-left:auto; font-size:12px; color:var(--muted)}
main{flex:1; display:flex; min-height:0}
.hidden{display:none !important}

/* browse */
#browse{flex:1; display:flex; min-height:0}
#side{width:290px; border-right:1px solid var(--line); overflow-y:auto;
  background:var(--panel); padding:12px}
#side input{width:100%; padding:7px 10px; border:1px solid var(--line);
  border-radius:8px; background:var(--bg); color:var(--ink); font:inherit; margin-bottom:10px}
#side h3{font-size:11px; text-transform:uppercase; letter-spacing:.1em;
  color:var(--muted); margin:14px 0 4px}
#side a{display:block; padding:3px 8px; border-radius:6px; color:var(--ink);
  text-decoration:none; font-size:13.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
#side a:hover{background:var(--chip)}
#side a.on{background:var(--accent); color:var(--accent-ink)}
#side .sub{padding-left:18px}
#content{flex:1; overflow-y:auto; padding:34px 44px; max-width:860px}
#content h1{font-size:26px; margin:0 0 14px}
#content h2{font-size:20px; margin:26px 0 8px}
#content h3{font-size:16.5px; margin:20px 0 6px}
#content p{margin:10px 0}
#content ul,#content ol{margin:10px 0 10px 26px}
#content table{border-collapse:collapse; margin:14px 0; width:100%}
#content th,#content td{border:1px solid var(--line); padding:6px 10px; text-align:left; font-size:14px}
#content th{background:var(--chip)}
#content blockquote{border-left:3px solid var(--accent); padding:4px 14px;
  margin:12px 0; color:var(--muted)}
#content code{background:var(--code); padding:1px 5px; border-radius:4px; font-size:13px}
#content pre{background:var(--code); padding:12px 14px; border-radius:8px;
  overflow-x:auto; margin:12px 0}
#content pre code{background:none; padding:0}
#content a{color:var(--accent)}
#content hr{border:0; border-top:1px solid var(--line); margin:20px 0}
#content mark{background:var(--mark); color:inherit; border-radius:3px; padding:0 2px}
.fm{background:var(--chip); border-radius:8px; padding:8px 12px; font-size:12.5px;
  color:var(--muted); margin-bottom:18px; white-space:pre-wrap; font-family:ui-monospace,monospace}
.crumb{font-size:12px; color:var(--muted); margin-bottom:14px; font-family:ui-monospace,monospace}
.hit{border:1px solid var(--line); border-radius:10px; padding:10px 14px; margin:10px 0;
  cursor:pointer; background:var(--panel)}
.hit:hover{border-color:var(--accent)}
.hit .p{font-weight:600; font-size:13.5px}
.hit .l{font-size:13px; color:var(--muted); margin-top:2px}

/* capture + export panes */
.pane{flex:1; overflow-y:auto; padding:34px; display:flex; justify-content:center}
.card{width:100%; max-width:680px}
.card h2{margin-bottom:4px}
.card .sub2{color:var(--muted); font-size:13.5px; margin-bottom:18px}
.card label{display:block; font-size:12px; text-transform:uppercase;
  letter-spacing:.08em; color:var(--muted); margin:14px 0 4px}
.card input[type=text], .card textarea, .card select{width:100%; padding:9px 12px;
  border:1px solid var(--line); border-radius:8px; background:var(--panel);
  color:var(--ink); font:inherit}
.card textarea{min-height:260px; resize:vertical; line-height:1.55}
.btn{margin-top:16px; padding:9px 22px; border:0; border-radius:8px;
  background:var(--accent); color:var(--accent-ink); font:inherit; font-weight:600; cursor:pointer}
.btn:disabled{opacity:.5}
.ghost{background:var(--chip); color:var(--ink)}
#drop{margin-top:18px; border:2px dashed var(--line); border-radius:12px;
  padding:26px; text-align:center; color:var(--muted); cursor:pointer}
#drop.over{border-color:var(--accent); color:var(--accent)}
.msg{margin-top:12px; font-size:13.5px; color:var(--accent); white-space:pre-wrap}
.inb{display:flex; align-items:center; gap:10px; padding:8px 12px;
  border:1px solid var(--line); border-radius:8px; margin:6px 0; font-size:13.5px}
.inb .nm{flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; cursor:pointer}
.inb .sz{color:var(--muted); font-size:12px}
.inb button{border:0; background:none; color:var(--muted); cursor:pointer; font-size:15px}
.inb button:hover{color:#c0392b}
.note{background:var(--chip); border-radius:10px; padding:12px 16px; font-size:13.5px;
  color:var(--muted); margin-top:22px}
</style>
</head>
<body>
<header>
  <h1>PERSONAL&nbsp;WIKI</h1>
  <nav>
    <button data-tab="browse" class="on">Browse</button>
    <button data-tab="capture">Capture</button>
    <button data-tab="inboxTab">Inbox</button>
    <button data-tab="export">Export</button>
  </nav>
  <span id="inboxBadge"></span>
</header>
<main>

<div id="browse" class="tab">
  <div id="side">
    <input id="q" placeholder="Search the wiki…" autocomplete="off">
    <div id="nav"></div>
  </div>
  <div id="content"><p style="color:var(--muted)">Loading…</p></div>
</div>

<div id="capture" class="tab pane hidden"><div class="card">
  <h2>Capture</h2>
  <div class="sub2">Type a fact or a full story. It lands in the inbox as plain text, ready for ingestion into the wiki.</div>
  <label>Title <span style="text-transform:none">(optional — auto-generated from first line)</span></label>
  <input type="text" id="cTitle">
  <label>Text</label>
  <textarea id="cBody" placeholder="A quick fact, a memory, a full story…"></textarea>
  <label>Tags <span style="text-transform:none">(optional, comma-separated)</span></label>
  <input type="text" id="cTags" placeholder="childhood, family">
  <button class="btn" id="cSave">Save to inbox</button>
  <div class="msg" id="cMsg"></div>
  <div id="drop">Drop files here or click to upload<br><span style="font-size:12px">any format — documents, exports, photos of letters…</span></div>
  <input type="file" id="filePick" multiple style="display:none">
  <div class="msg" id="uMsg"></div>
</div></div>

<div id="inboxTab" class="tab pane hidden"><div class="card">
  <h2>Inbox</h2>
  <div class="sub2">Captured material waiting to be ingested into the wiki. To process it, open Claude Code in this folder and say “ingest the inbox”.</div>
  <div id="inboxList"></div>
</div></div>

<div id="export" class="tab pane hidden"><div class="card">
  <h2>Export corpus</h2>
  <div class="sub2">Bundle everything into one Markdown file for LLM ingestion, with a table of contents and token estimate.</div>
  <label>Scope</label>
  <select id="eDomain">
    <option value="">Whole wiki</option>
    <option value="self">self</option><option value="timeline">timeline</option>
    <option value="people">people</option><option value="mind">mind</option>
    <option value="work">work</option><option value="interests">interests</option>
    <option value="health">health</option><option value="places">places</option>
  </select>
  <label style="margin-top:14px"><input type="checkbox" id="eRaw"> include raw/ source archive (big)</label>
  <label><input type="checkbox" id="eInbox"> include un-ingested inbox items</label>
  <button class="btn" id="eGo">Export</button>
  <div class="msg" id="eMsg"></div>
  <div class="note">Exports are written to <code>exports/</code> and are disposable — regenerate any time. The wiki itself is always plain Markdown, so this app is never a lock-in.</div>
</div></div>

</main>
<script>
const $=s=>document.querySelector(s), api=async(p,o)=>(await fetch(p,o)).json();
let TREE=null, CUR=null;

/* ---------- tabs ---------- */
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{
  document.querySelectorAll("nav button").forEach(x=>x.classList.toggle("on",x===b));
  document.querySelectorAll(".tab").forEach(t=>t.classList.toggle("hidden",t.id!==b.dataset.tab));
  if(b.dataset.tab==="inboxTab") refresh();
});

/* ---------- tiny markdown renderer ---------- */
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function inline(s){
  s=esc(s);
  s=s.replace(/`([^`]+)`/g,"<code>$1</code>");
  s=s.replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>").replace(/(^|\W)\*([^*]+)\*/g,"$1<i>$2</i>");
  s=s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,(m,t,u)=>
    /^https?:/.test(u)?`<a href="${u}" target="_blank">${t}</a>`
    :`<a href="#" data-wiki="${u}">${t}</a>`);
  s=s.replace(/\[\[([^\]]+)\]\]/g,`<a href="#" data-wiki="$1">$1</a>`);
  return s;
}
function md(text){
  let fm="";
  if(text.startsWith("---")){
    const end=text.indexOf("\n---",3);
    if(end>0){ fm=text.slice(4,end).trim(); text=text.slice(end+4); }
  }
  const lines=text.split("\n"); let out=[],i=0;
  const flush=()=>{};
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

/* ---------- browse ---------- */
async function refresh(){
  TREE=await api("/api/tree");
  const n=TREE.inbox.length;
  $("#inboxBadge").textContent=n?`${n} item${n>1?"s":""} in inbox`:"inbox empty";
  const nav=$("#nav"); nav.innerHTML="";
  const add=(label,items,cls)=>{ if(!items.length)return;
    const h=document.createElement("h3"); h.textContent=label; nav.appendChild(h);
    for(const f of items){ const a=document.createElement("a");
      a.textContent=f.name.replace(/\.md$/,""); a.dataset.path=f.path;
      if(cls)a.className=cls;
      if(f.path===CUR)a.classList.add("on");
      a.onclick=e=>{e.preventDefault();open(f.path)}; nav.appendChild(a); } };
  add("Start", TREE.meta.filter(f=>f.name==="index.md"));
  const domains={};
  for(const f of TREE.wiki){ const d=f.path.split("/")[1];(domains[d]=domains[d]||[]).push(f); }
  for(const d of Object.keys(domains)){
    const idx=domains[d].filter(f=>f.name==="index.md");
    const rest=domains[d].filter(f=>f.name!=="index.md");
    add(d, idx.map(f=>({...f,name:d+" index"})));
    for(const f of rest){ const a=document.createElement("a");
      a.textContent=f.name.replace(/\.md$/,""); a.className="sub"; a.dataset.path=f.path;
      if(f.path===CUR)a.classList.add("on");
      a.onclick=e=>{e.preventDefault();open(f.path)}; nav.appendChild(a); } }
  add("Meta", TREE.meta.filter(f=>f.name!=="index.md"));
  renderInbox();
}
async function open(path, highlight){
  CUR=path;
  document.querySelectorAll("#side a").forEach(a=>a.classList.toggle("on",a.dataset.path===path));
  const r=await api("/api/file?path="+encodeURIComponent(path));
  let html=`<div class="crumb">${esc(path)}</div>`;
  if(r.error) html+=`<p>${esc(r.error)}</p>`;
  else if(r.binary||r.dir||!/\.(md|txt)$/.test(path)) html+=`<pre>${esc(r.content)}</pre>`;
  else html+=md(r.content);
  const c=$("#content"); c.innerHTML=html;
  if(highlight){ const rx=new RegExp(highlight.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"),"gi");
    c.querySelectorAll("p,li,td,h1,h2,h3,blockquote").forEach(el=>{
      if(rx.test(el.textContent)) el.innerHTML=el.innerHTML.replace(rx,m=>`<mark>${m}</mark>`); }); }
  c.scrollTop=0;
  c.querySelectorAll("a[data-wiki]").forEach(a=>a.onclick=e=>{
    e.preventDefault(); let t=a.dataset.wiki;
    if(!/\.md$/.test(t)) t+=".md";
    const hit=TREE.wiki.concat(TREE.meta).find(f=>f.path===t||f.path.endsWith("/"+t));
    open(hit?hit.path:t); });
  // switch to browse tab
  document.querySelectorAll("nav button").forEach(x=>x.classList.toggle("on",x.dataset.tab==="browse"));
  document.querySelectorAll(".tab").forEach(t=>t.classList.toggle("hidden",t.id!=="browse"));
}

/* ---------- search ---------- */
let debounce=null;
$("#q").oninput=()=>{ clearTimeout(debounce);
  const q=$("#q").value.trim();
  if(!q){ if(CUR)open(CUR); return; }
  debounce=setTimeout(async()=>{
    const hits=await api("/api/search?q="+encodeURIComponent(q));
    const c=$("#content");
    c.innerHTML=`<div class="crumb">search: ${esc(q)} — ${hits.length} page${hits.length!==1?"s":""}</div>`+
      (hits.length?"":"<p style='color:var(--muted)'>No matches in the wiki yet.</p>")+
      hits.map((h,i)=>`<div class="hit" data-i="${i}"><div class="p">${esc(h.path)}</div>`+
        h.matches.map(m=>`<div class="l">${m.line}: ${esc(m.text)}</div>`).join("")+
        (h.count>5?`<div class="l">…${h.count-5} more</div>`:"")+`</div>`).join("");
    c.querySelectorAll(".hit").forEach(el=>el.onclick=()=>open(hits[el.dataset.i].path,q));
  },250); };

/* ---------- capture ---------- */
$("#cSave").onclick=async()=>{
  const r=await api("/api/capture",{method:"POST",body:JSON.stringify(
    {title:$("#cTitle").value, body:$("#cBody").value, tags:$("#cTags").value})});
  $("#cMsg").textContent=r.error?("⚠ "+r.error):`✓ saved ${r.saved} (${r.words} words, ${r.kind})`;
  if(!r.error){ $("#cTitle").value=$("#cBody").value=$("#cTags").value=""; refresh(); } };

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
    $("#uMsg").textContent=r.error?("⚠ "+r.error):`✓ ${r.saved} (${r.bytes.toLocaleString()} bytes)`; }
  refresh(); }

/* ---------- inbox ---------- */
function renderInbox(){
  const el=$("#inboxList");
  if(!TREE.inbox.length){ el.innerHTML="<p style='color:var(--muted)'>Inbox is empty — everything has been ingested.</p>"; return; }
  el.innerHTML="";
  for(const f of TREE.inbox){
    const d=document.createElement("div"); d.className="inb";
    d.innerHTML=`<span class="nm">${esc(f.name)}</span><span class="sz">${f.size.toLocaleString()} B${f.dir?" · folder":""}</span><button title="delete">✕</button>`;
    d.querySelector(".nm").onclick=()=>open(f.path);
    d.querySelector("button").onclick=async()=>{
      if(!confirm(`Delete ${f.name} from the inbox? This cannot be undone.`))return;
      await api("/api/delete-inbox",{method:"POST",body:JSON.stringify({path:f.path})});
      refresh(); };
    el.appendChild(d); } }

/* ---------- export ---------- */
$("#eGo").onclick=async()=>{
  $("#eGo").disabled=true; $("#eMsg").textContent="exporting…";
  const r=await api("/api/export",{method:"POST",body:JSON.stringify(
    {domain:$("#eDomain").value, raw:$("#eRaw").checked, inbox:$("#eInbox").checked})});
  $("#eGo").disabled=false;
  $("#eMsg").innerHTML=esc(r.message)+(r.file?
    `<br><a href="/api/download?path=${encodeURIComponent(r.file)}" style="color:var(--accent)">⬇ download ${esc(r.file)}</a>`:""); };

/* ---------- boot ---------- */
refresh().then(()=>open("index.md"));
</script>
</body>
</html>"""


def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}"
    print(f"Personal Wiki running at {url}  (Ctrl-C to stop)")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
