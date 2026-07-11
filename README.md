# Personal Wiki (v2) — second brain

A lifelong personal wiki: complete biographical history, psychological and
ideological profile, and everything else about your personhood, stored as
plain Markdown files. No apps, no databases, no APIs — just text files, two
small scripts, and git for history. Claude (or any LLM agent) does the
compilation; you just feed it material.

## The app

**To pin it in your Dock:** drag **Personal Wiki.app** onto the Dock. Click
it any time to launch (or refocus) the wiki in your browser — clicking it
again while it's already running just opens/reuses the tab, it never starts
a second server.

Alternatively, double-click **Wiki.command** (or run `python3 app.py`).
Either way, your browser opens
at `http://127.0.0.1:8477` with everything in one place:

- **Browse** — read the whole wiki with rendered pages, clickable links,
  and full-text search; every page has an **✎ Edit** button at the bottom
  for direct fixes (edits are logged in log.md)
- **Capture** — type facts or full stories; drag-and-drop any file to upload.
  Type **@** to autocomplete a wiki page reference — the note is then saved
  as a *correction/expansion targeting that page*, and ingestion applies it
  there first
- **Inbox** — see and manage what's waiting for ingestion
- **Export** — one click bundles the corpus for LLMs, with a download link

It's a single Python file using only the standard library — nothing to
install, runs entirely on your machine, touches only this folder.

## Adding material from the terminal (optional)

The same three ways also work as CLI commands, all landing in `inbox/`:

```bash
bin/capture                     # type or paste a story; end with a "." line
bin/capture "quick fact here"   # one-liner, no prompts
bin/capture -f ~/some-file.pdf  # upload any file (or a whole folder)
bin/capture status              # see what's waiting
```

Or double-click `Capture.command` in Finder to open a capture window.
You can also just drag files into `inbox/` yourself — same thing.

## Getting it into the wiki

Open Claude Code in this folder and say **"ingest the inbox"**. It processes
one item at a time: files the original into `raw/` (kept forever, never
edited), then writes/updates the relevant wiki pages and commits. The rules
it follows are in `CLAUDE.md`.

## Reading it

Start at `index.md` — it links to the eight domain indexes (self, timeline,
people, mind, work, interests, health, places). Everything is plain Markdown;
it also opens cleanly in Obsidian if you ever want a nicer reader.

## Exporting for LLMs

```bash
bin/export-corpus                 # the whole compiled wiki -> exports/
bin/export-corpus --domain mind   # one domain only
bin/export-corpus --raw           # include the raw source archive (big)
```

Produces a single Markdown file with a table of contents and a token count,
ready to paste or upload into any LLM.

## Layout

```
app.py     the app: capture + browse + search + export in one window
inbox/     what you've added but hasn't been processed yet
raw/       original sources, immutable archive
wiki/      the compiled knowledge (the actual second brain)
exports/   generated LLM bundles (disposable, not in git)
bin/       capture + export-corpus
CLAUDE.md  the agent's operating rules
index.md   master navigation
log.md     history of every operation
queue.md   what's pending ingestion
```
