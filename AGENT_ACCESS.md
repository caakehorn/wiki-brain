# Agent / LLM access to wiki-brain

How to give models and agents the **current compiled wiki** from GitHub.

## What you already have

| Layer | URL | Notes |
|-------|-----|--------|
| GitHub source of truth | https://github.com/caakehorn/wiki-brain | `main` is authoritative after merge |
| GitHub raw file | `https://raw.githubusercontent.com/caakehorn/wiki-brain/main/wiki/…` | Always tracks `main`; good for one page |
| GitHub Pages (agent feed) | https://caakehorn.github.io/wiki-brain/ | Rebuilt on every push to `main` by Actions |

The local app (`app.py` on `localhost:8477`) is for **you** (capture, edit, ingest). Agents should use the online feed, not your laptop.

## Agent entrypoints (after deploy)

Once [`.github/workflows/deploy-site.yml`](.github/workflows/deploy-site.yml) has run on `main`:

| Resource | URL |
|----------|-----|
| **Discovery** | https://caakehorn.github.io/wiki-brain/llms.txt |
| **Machine index** | https://caakehorn.github.io/wiki-brain/agent/manifest.json |
| **Critical spine** | https://caakehorn.github.io/wiki-brain/agent/critical.md |
| **Full corpus** | https://caakehorn.github.io/wiki-brain/agent/corpus.md |
| **Domain corpora** | https://caakehorn.github.io/wiki-brain/agent/domains/&lt;domain&gt;.md |
| **One page** | https://caakehorn.github.io/wiki-brain/wiki/self/overview.md |

Domains: `self` · `timeline` · `people` · `mind` · `work` · `interests` · `health` · `places` · `legal`

### Recommended agent strategy

1. Fetch `llms.txt` or `agent/manifest.json`.
2. Check `git_sha` / `generated_at` if you care about freshness.
3. Load by context budget:
   - **Small:** `agent/critical.md`
   - **Medium:** one or more `agent/domains/*.md` (people is large; mind/self first for identity)
   - **Large:** `agent/corpus.md` (~300k+ tokens — often multi-pass)
4. Deep-dive individual `wiki/…/*.md` URLs from the manifest.

### Prompt snippet you can paste into any agent

```
You have online access to my personal wiki (compiled second brain).

Discovery: https://caakehorn.github.io/wiki-brain/llms.txt
Manifest:  https://caakehorn.github.io/wiki-brain/agent/manifest.json
Spine:     https://caakehorn.github.io/wiki-brain/agent/critical.md

Rules:
- Prefer the compiled wiki over inventing facts.
- Start with critical.md or domain corpora; fetch individual pages as needed.
- Honor CONTRADICTION / REVISED blockquotes on pages.
- Cite page paths (e.g. wiki/people/annie-ulmer.md) in answers.
```

## Keep the feed current

1. Work on a branch → merge to **`main`** (PRs as you already do).
2. Push to `main` triggers **Deploy agent site**.
3. Pages updates in ~1–2 minutes. Manifest `git_sha` should match `main`.

Local preview of the same site:

```bash
bin/build-site
# open site/llms.txt  or  python3 -m http.server -d site 8787
```

## Privacy warning (important)

This repository is currently **public**, including a large `raw/` archive (messages, dossiers, etc.). The agent **Pages** feed deliberately publishes only the compiled `wiki/` tree — not `raw/` or `inbox/`.

That does **not** hide `raw/` from the internet: anyone can still clone the GitHub repo.

If you want agents online but the public web **off** your life archive:

1. Make the GitHub repo **private**.
2. Keep Pages only if your plan supports private Pages + auth, **or**
3. Put a token-gated proxy in front (Cloudflare Worker, Fly.io, etc.) that clones with a deploy key and serves `site/` only.

Until then, treat everything in this repo as world-readable.

## Optional next upgrades

| Upgrade | When you need it |
|---------|------------------|
| **Private + token API** | Secrets must not be public; agents use `Authorization: Bearer …` |
| **MCP server** | Claude/Cursor tools: `search_wiki`, `get_page`, `list_domain` over the same feed |
| **Search endpoint** | Full-text search without downloading corpora (small Worker over `manifest` + page bodies) |
| **Disable old Jekyll workflow** | Jekyll is removed; deploy is `deploy-site.yml` (stdlib-only `bin/build-site`) |

The agent site uses `.nojekyll` and replaces the human Jekyll theme with raw Markdown + JSON optimized for models.
