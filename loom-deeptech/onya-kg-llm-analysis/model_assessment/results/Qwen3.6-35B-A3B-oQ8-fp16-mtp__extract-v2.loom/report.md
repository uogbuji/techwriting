# Model assessment — `Qwen3.6-35B-A3B-oQ8-fp16-mtp`

*2026-07-27 21:54 UTC*  ·  endpoint `http://acholonu:8080/v1`  ·  prompt `extract-v2.loom.toml`  ·  thinking `off`  ·  chunk 48,000 chars  ·  max_tokens 8000

## Headline

| metric | value |
|---|---|
| wall-clock | 1439s (24.0 min) |
| chunks skipped | 0 / 10 |
| **relationship recall (reachable)** | **7 / 14** |
| relationship recall (all gold) | 7 / 14 |
| nodes / people | 291 / 124 |
| edges (all / person-person) | 135 / 64 |
| largest connected people-cluster | 21 |

## Relationship recall (gold set)

`in text?`: ✓ both parties appear within the processed span · `·` a party appears only later in the book (unreachable here) · `?` a party's name was not located.

| A | B | A found? | B found? | in text? | edge? | relationship |
|---|---|:--:|:--:|:--:|:--:|---|
| equiano | pascal | ✓ | ✓ | ✓ | **✓** | Pascal bought Equiano, renamed him Gustavus Vassa, took him to sea |
| equiano | robert_king | ✓ | ✓ | ✓ | **✓** | King bought Equiano; Equiano later bought his freedom from him |
| equiano | richard_baker | ✓ | ✓ | ✓ | **✓** | shipboard companion and close friend |
| equiano | daniel_queen | ✓ | ✓ | ✓ | · | Queen taught Equiano to read, shave and dress hair aboard the Aetna |
| equiano | guerin | ✓ | ✓ | ✓ | **✓** | Pascal's cousins; had Equiano baptised and showed him kindness |
| equiano | thomas_farmer | ✓ | ✓ | ✓ | · | Equiano sailed under Farmer, a trading captain for King |
| equiano | charles_irving | ✓ | ✓ | ✓ | **✓** | joined Irving on the Arctic voyage and the Mosquito Coast plantation |
| equiano | phipps | ✓ | ✓ | ✓ | **✓** | joined Phipps 1773 expedition toward the North Pole |
| equiano | granville_sharp | ✓ | ✓ | ✓ | · | appealed to Sharp over the John Annis case and the Zong massacre |
| equiano | john_annis | ✓ | ✓ | ✓ | · | friend kidnapped back into slavery; Equiano sought Sharp's help |
| equiano | thomas_clarkson | ✓ | ✓ | ✓ | · | fellow abolitionist |
| equiano | doran | ✓ | ✓ | ✓ | **✓** | Captain Doran carried Equiano to Montserrat and sold him to King |
| robert_king | thomas_farmer | ✓ | ✓ | ✓ | · | King employed Farmer as a vessel captain |
| phipps | lutwidge | ✓ | ✓ | ✓ | · | Lutwidge commanded the Carcass alongside Phipps’s Racehorse |

## Per-chunk

| chunk | chars | attempts | status | nodes after | time |
|---|---|---|---|---|---|
| 0 | 48,000 | 1 | ok | 22 | 148s |
| 1 | 48,000 | 2 | ok | 78 | 426s |
| 2 | 48,000 | 3 | ok | 155 | 339s |
| 3 | 48,000 | 2 | ok | 187 | 120s |
| 4 | 48,000 | 2 | ok | 197 | 96s |
| 5 | 48,000 | 1 | ok | 206 | 39s |
| 6 | 48,000 | 1 | ok | 223 | 58s |
| 7 | 48,000 | 2 | ok | 264 | 119s |
| 8 | 48,000 | 1 | ok | 286 | 61s |
| 9 | 6,758 | 2 | ok | 291 | 33s |
