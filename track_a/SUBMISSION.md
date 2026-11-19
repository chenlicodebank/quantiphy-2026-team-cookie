# The submissions this package reproduces (Track A, team Cookie)

| | entry | alternative |
|---|---|---|
| portal submission id | `9de2b974-6be8-4c1a-938d-c9acc93ccc47` | `5978cdf6-3fcf-4594-8f1f-2d1867bd8f4b` |
| uploaded (UTC) | 2026-10-26 02:29:09 | 2026-10-26 07:51:34 |
| file | `track_a_s43_strict_rsi.csv` | `track_a_s43_gray_rsi.csv` |
| sha256 | `5e73fc704f79848ae6aab025bfaf0a743cbfa1207859bdfdd017c9690c822f92` | `2c4b1273948dfc67f355a0f237f500ee318d9d0a046b144359414b15453459bd` |
| portal MRA | .8499 (S2 .8527 / D2 .8918 / S3 .8148 / D3 .8404) | .8606 (S2 .8591 / D2 .8964 / S3 .8265 / D3 .8605) |

**Please rank us on the entry.** The alternative adds steps we are not sure the rules allow: a catalog of validation
labels and priors, the prop sizes in the QuantiPhy paper's appendix B, and seven answers changed after a review of
individual answers, six to a value from that question's own session notes and one (q1668) to a typical walking speed
(`STATEMENT.md`). If you rule that these are allowed, we ask to be ranked on the alternative instead; otherwise on the
entry. The entry itself carries the one exception listed in `STATEMENT.md`.

Our highest Track A uploads on the leaderboard (the best: `ffd54f88-cebb-49ee-91e3-74e901e32752`, 2026-10-25 11:44:30
UTC, .8697) used other questions' information (answers pooled across renders and twins of one scene, sibling clips'
priors, a line from sessions that held all questions of a video). We made them to measure what such information is
worth and do not put them forward.

`reproduce.sh` rebuilds both files from the answer lines and checks their sha256 (`SUBMISSION.json`), then traces every
value of the answer lines to its per-question record.
