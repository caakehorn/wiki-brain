# Ingest Queue

_Items waiting for or in the middle of ingestion. `bin/capture status` lists the inbox._

## Inbox — pending ingestion

| Item | Priority | Notes |
|------|----------|-------|
| 2026-07-11_013210_the-house-at-337-saratoga-drive… | HIGH | First capture through the app — likely a places/timeline page seed |
| 2026-07-11_140000_ANCESTRY_DNA.txt | MEDIUM | Ancestry narrative (Frank/Harris, Gillingham/Van Voorhis lines) — expand wiki/self/ancestry.md; not previously in raw/ |
| 2026-07-11_140001_google-takeout-manifest.html | LOW | Google Takeout archive manifest — file to raw/self/, useful as export inventory |

## Carried over from old repo (raw/ present, synthesis pending)

| File | Priority | Notes |
|------|----------|-------|
| raw/self/dox-md/tom_kristin_master_dossier.md | MEDIUM | Expand wiki/people/tom.md; add Kristin people page |
| raw/self/dox-md/MAX_PRIME.md | MEDIUM | Populate wiki/work/tech/max-framework/overview.md |
| raw/self/dox-md/ulmer_dui_megadoc.md | LOW | Annie DUI detail — check for gaps vs existing pages |
| raw/self/dox-md/The-Eli-incident-investigation.md | LOW | Check against wiki/timeline/events/ |
| raw/self/dox-md/DAN_COMP.md | LOW | Unknown — read and route |
| raw/self/dox-md/Annie 10-Year… Forensic Report.md | LOW | Supplement wiki/mind/synthesis/attachment-trauma-bond if gaps |
| raw/self/message-csv/MASTER_DUMP_PART_1_ARCHAIC.csv | MEDIUM | Pre-2015 coverage — fills timeline gaps |
| raw/self/message-csv/ (remaining CSVs) | LOW | Thread-specific slices |

## Re-synthesis queue (lint 2026-07-11: 22 oversized pages)

All pages over the 8 KB budget, mostly mind/synthesis and self/chats — see lint-report.md.
Worst offenders: ai-collaborative-analysis (21 KB, still contains v1 agent chatter in
frontmatter), forensic-methodology (20 KB), context-core (14 KB), youtube-watch-history (14 KB).

## External acquisitions

- Twitter @danfrank: only sampled — full archive via X Settings → Download archive → drop in inbox/
- iMessage chat.db: bin/export-imessage-template.sh existed in old repo but never ran (needs Full Disk Access)

## Completed

- **2026-07-11 migration:** 562 MB raw/ archive (3,166 files), 261 wiki pages remapped
  into 9 domains, indexes rebuilt, lint clean (0 errors). Old repo at `~/wiki project`
  untouched, now safe to archive.
