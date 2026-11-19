# The submissions this package reproduces (Track B, team Cookie)

| | entry | alternative |
|---|---|---|
| portal submission id | `d1ac996d-62e0-4988-b79a-571c28ec92af` | `bb9d428e-340a-47e0-b868-16e6797965b4` |
| uploaded (UTC) | 2026-10-26 00:05:57 | 2026-10-26 00:12:30 |
| file | `track_b_s37_b10mix.csv` | `track_b_s43_k3.csv` |
| sha256 | `30ba599f434987871261f7c457bbdea25bc75f8496bfc922bbea3a5c06898d25` | `605421dc24a6cae9984148b85d5aa0d1fb910945d9f2ab53d5a6f22fd7524e25` |
| portal MRA | .8269 (S2 .8265 / D2 .8745 / S3 .8031 / D3 .8037) | .8381 (S2 .8298 / D2 .8760 / S3 .8207 / D3 .8257) |
| per question | yes: every value comes from its own question's inputs | no for 499 rows: two lookup steps (`STATEMENT.md`) |

**Please rank us on the entry.** The alternative is the entry's per-question answers (with S3 from an earlier set of
the same runs) plus two lookup steps we are not sure the rules allow: a catalog of validation labels and priors, and
the prop sizes in the QuantiPhy paper's appendix B. If you rule that both are allowed, we ask to be ranked on the
alternative instead; otherwise on the entry.

Our best Track B upload on the leaderboard, `de61442b-affe-4a97-8d87-85addf79bfbb` (2026-10-25 15:49:00 UTC, .8470),
used other questions' information (answers pooled across renders and twins of one scene, sibling clips' priors) and
is not put forward.

`reproduce.sh` rebuilds both files from the per-question run records and checks their sha256 (`SUBMISSION.json`).
