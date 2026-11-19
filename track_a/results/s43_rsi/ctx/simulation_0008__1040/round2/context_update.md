# Round 2 addendum (q1040, width of the wooden stairs)

Round 2 verified round 1's proposed change with its own code. Its answer is **1.75 m**, against round 1's 1.76, and the
change stands.

## Established
**Focal length is about 1000 px** (`focal_check.py`):
- The depth pair at constant Z gives f = 1000 and Z_boat = 5.85 m.
- Varying the origin (0.45–0.55 of the length), the length (620–670 px) and the frame (23–25) gives f = 951–1048.
- C3's f = 1075 (from Z = 6.3 m) and C2's f = 1300 (Euclidean distance used as Z) are ruled out.

**Closure:** the stem post top-to-reflection span is about 250 px, so the post rises 126 px above the water. That is
0.737 m against the 0.75 m prior (−1.7 %).

**Stairs extent** (`stairs_profile.py`, mean of all frames):
- The outer edges are at x = 487.5 and 586.5, about 98 px, the same in every tread band. The treads alone span about
  490–585 (94 px).
- The pale posts (500–512.5 and 587–599) are centred at 549.5, against 537.5 for the stairs. They line up with the
  jetty's side lines (back corners at about 500 and 603), so they are not part of the stairs.

**Width:** 98 px × 17.6–18.1 m / 1000 = 1.72–1.77 m.

## Ruled out
- C1's 108–110 px, which includes the pale posts (that reading gives about 1.9 m).
- C4's 80 px tread span.
- C3's averaging of the width with the run.

## Open
- Whether the outer vertical members belong to the stairs model. They give 98 px; the treads alone give 94 px, which
  would mean −4 %.
- The members' depth: 17.6 m (the origin) or 18.1 m (deck front). This is about 3 %.
- The overall range is 1.65–1.77 m.
- A water-plane cross-check through the jetty failed: the jetty is stepped, not level.
