# Model assessment — `gemma-4-26B-A4B-it-oQ8`

*2026-07-19 05:05 UTC*  ·  endpoint `http://acholonu:8080/v1`  ·  chunk 48,000 chars  ·  max_tokens 8000  ·  thinking-control on

## Headline

| metric | value |
|---|---|
| wall-clock | 584s (9.7 min) |
| chunks skipped | 2 / 10 |
| **relationship recall (reachable)** | **6 / 14** |
| relationship recall (all gold) | 6 / 14 |
| nodes / people | 245 / 107 |
| edges (all / person-person) | 58 / 23 |
| largest connected people-cluster | 10 |

## Relationship recall (gold set)

`in text?`: ✓ both parties appear within the processed span · `·` a party appears only later in the book (unreachable here) · `?` a party's name was not located.

| A | B | A found? | B found? | in text? | edge? | relationship |
|---|---|:--:|:--:|:--:|:--:|---|
| equiano | pascal | ✓ | ✓ | ✓ | **✓** | Pascal bought Equiano, renamed him Gustavus Vassa, took him to sea |
| equiano | robert_king | ✓ | ✓ | ✓ | **✓** | King bought Equiano; Equiano later bought his freedom from him |
| equiano | richard_baker | ✓ | ✓ | ✓ | **✓** | shipboard companion and close friend |
| equiano | daniel_queen | ✓ | ✓ | ✓ | · | Queen taught Equiano to read, shave and dress hair aboard the Aetna |
| equiano | guerin | ✓ | ✓ | ✓ | **✓** | Pascal's cousins; had Equiano baptised and showed him kindness |
| equiano | thomas_farmer | ✓ | ✓ | ✓ | **✓** | Equiano sailed under Farmer, a trading captain for King |
| equiano | charles_irving | ✓ | ✓ | ✓ | **✓** | joined Irving on the Arctic voyage and the Mosquito Coast plantation |
| equiano | phipps | ✓ | ✓ | ✓ | · | joined Phipps 1773 expedition toward the North Pole |
| equiano | granville_sharp | ✓ | ✓ | ✓ | · | appealed to Sharp over the John Annis case and the Zong massacre |
| equiano | john_annis | ✓ | ✓ | ✓ | · | friend kidnapped back into slavery; Equiano sought Sharp's help |
| equiano | thomas_clarkson | ✓ | ✓ | ✓ | · | fellow abolitionist |
| equiano | doran | ✓ | ✓ | ✓ | · | Captain Doran carried Equiano to Montserrat and sold him to King |
| robert_king | thomas_farmer | ✓ | ✓ | ✓ | · | King employed Farmer as a vessel captain |
| phipps | lutwidge | ✓ | ✓ | ✓ | · | Lutwidge commanded the Carcass alongside Phipps’s Racehorse |

## Per-chunk

| chunk | chars | attempts | status | nodes after | time |
|---|---|---|---|---|---|
| 0 | 48,000 | 2 | ok | 38 | 55s |
| 1 | 48,000 | 2 | ok | 71 | 57s |
| 2 | 48,000 | 3 | ok | 118 | 96s |
| 3 | 48,000 | 1 | ok | 142 | 23s |
| 4 | 48,000 | 5 | SKIPPED | 142 | 125s |
| 5 | 48,000 | 5 | SKIPPED | 142 | 111s |
| 6 | 48,000 | 1 | ok | 183 | 25s |
| 7 | 48,000 | 1 | ok | 203 | 23s |
| 8 | 48,000 | 2 | ok | 240 | 66s |
| 9 | 6,758 | 1 | ok | 245 | 4s |
