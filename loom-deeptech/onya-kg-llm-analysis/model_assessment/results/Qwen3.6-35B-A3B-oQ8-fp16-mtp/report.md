# Model assessment — `Qwen3.6-35B-A3B-oQ8-fp16-mtp`

*2026-07-27 18:42 UTC*  ·  endpoint `http://acholonu:8080/v1`  ·  prompt `extract.loom.toml`  ·  thinking `off`  ·  chunk 48,000 chars  ·  max_tokens 8000

## Headline

| metric | value |
|---|---|
| wall-clock | 486s (8.1 min) |
| chunks skipped | 0 / 10 |
| **relationship recall (reachable)** | **10 / 14** |
| relationship recall (all gold) | 10 / 14 |
| nodes / people | 414 / 142 |
| edges (all / person-person) | 309 / 100 |
| largest connected people-cluster | 41 |

## Relationship recall (gold set)

`in text?`: ✓ both parties appear within the processed span · `·` a party appears only later in the book (unreachable here) · `?` a party's name was not located.

| A | B | A found? | B found? | in text? | edge? | relationship |
|---|---|:--:|:--:|:--:|:--:|---|
| equiano | pascal | ✓ | ✓ | ✓ | **✓** | Pascal bought Equiano, renamed him Gustavus Vassa, took him to sea |
| equiano | robert_king | ✓ | ✓ | ✓ | **✓** | King bought Equiano; Equiano later bought his freedom from him |
| equiano | richard_baker | ✓ | ✓ | ✓ | · | shipboard companion and close friend |
| equiano | daniel_queen | ✓ | ✓ | ✓ | **✓** | Queen taught Equiano to read, shave and dress hair aboard the Aetna |
| equiano | guerin | ✓ | ✓ | ✓ | **✓** | Pascal's cousins; had Equiano baptised and showed him kindness |
| equiano | thomas_farmer | ✓ | ✓ | ✓ | **✓** | Equiano sailed under Farmer, a trading captain for King |
| equiano | charles_irving | ✓ | ✓ | ✓ | **✓** | joined Irving on the Arctic voyage and the Mosquito Coast plantation |
| equiano | phipps | ✓ | ✓ | ✓ | · | joined Phipps 1773 expedition toward the North Pole |
| equiano | granville_sharp | ✓ | ✓ | ✓ | **✓** | appealed to Sharp over the John Annis case and the Zong massacre |
| equiano | john_annis | ✓ | ✓ | ✓ | **✓** | friend kidnapped back into slavery; Equiano sought Sharp's help |
| equiano | thomas_clarkson | ✓ | ✓ | ✓ | · | fellow abolitionist |
| equiano | doran | ✓ | ✓ | ✓ | **✓** | Captain Doran carried Equiano to Montserrat and sold him to King |
| robert_king | thomas_farmer | ✓ | ✓ | ✓ | **✓** | King employed Farmer as a vessel captain |
| phipps | lutwidge | ✓ | ✓ | ✓ | · | Lutwidge commanded the Carcass alongside Phipps’s Racehorse |

## Per-chunk

| chunk | chars | attempts | status | nodes after | time |
|---|---|---|---|---|---|
| 0 | 48,000 | 1 | ok | 41 | 57s |
| 1 | 48,000 | 1 | ok | 63 | 23s |
| 2 | 48,000 | 1 | ok | 140 | 69s |
| 3 | 48,000 | 1 | ok | 164 | 31s |
| 4 | 48,000 | 1 | ok | 282 | 151s |
| 5 | 48,000 | 1 | ok | 293 | 29s |
| 6 | 48,000 | 1 | ok | 339 | 46s |
| 7 | 48,000 | 1 | ok | 364 | 31s |
| 8 | 48,000 | 1 | ok | 406 | 40s |
| 9 | 6,758 | 1 | ok | 414 | 8s |
