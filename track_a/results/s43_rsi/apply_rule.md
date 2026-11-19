# Series 43 apply rule (pre-registered 2026-10-26 ~01:35 UTC, before any round-2 verdict was read)

A question's RSI answer is the verdict of its newest round. It replaces the incumbent (#223 C1 for the gray file; the
strict splice for the strict file) when all hold:
1. decision is `switch` or `new`;
2. confidence is `high` or `medium`;
3. |ln(answer / incumbent)| >= 0.02;
4. the question is not on a physical-scale / Series 30 S2-adjudication clip (`excluded_physscale.json`);
5. a round-1 proposal counts only after a round-2 session re-checked it: the newest verdict decides, so a proposal
   that round 2 rejected (`keep`) is not applied, and one it confirmed is applied at round 2's value;
6. a proposal made in the first investigation of a question under harness v2 (the D3 rows round 1 never reached)
   needs `high` confidence unless a later round verifies it.
Strict file: the same rows, except the human-check rows (s43_strict_a.py HUMAN), whose contexts showed the human value
as the submitted answer.
Read: slot 4 = C1 + these rows, per category against #223 (S2 has no RSI row unless round 2 adds one, so it is the
control). Slot 5 = strict file + the rows of the categories that slot 4 shows did not lose.

Addendum (2026-10-26 ~02:20 UTC, after the D3 v2 verdicts, before any board read of RSI rows): class 2 exclusion -
a proposal that moves a row back toward its pre-re-ask E2 value (E2 combine steps `gravity` / `u1`) is not applied,
for the same reason as the physical-scale clips: it undoes a convention the board validated for the population
(6 D3 rows: 1063, 1071, 1072, 1715, 1561, 1569). Harness v3 = v2 + lesson 15 (the same point, as procedure).
Round 3 verifies the 7 proposals that are still open (S3 1039 / 1883 from round 2; D3 1680 / 1314 / 1583 / 1481 / 1486).
