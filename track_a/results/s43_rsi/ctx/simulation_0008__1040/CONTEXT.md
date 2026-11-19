# Context of question 1040 (organised record; every round adds to it)

## Question
- Text: What is the width of the wooden stairs in meters?
- Its own prior: height of boat = 0.75m
- Its own depth_info: t=0s, distance_boat_camera = 7.452 m
t=1s, distance_boat_camera = 6.655m
distance_pier_camera = 11.579m
distance_stairs_camera = 17.623m
- question_fps: 24
- Video: simulation_0008.mp4 (simulation, S3MC)

## The answer currently submitted
1.65982 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 1.9 and an earlier DeepSeek median B = 1.45; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 1.9 | 1.145 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 1.37 | 0.825 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 1.45 | 0.874 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 1.56 | 0.940 |

DeepSeek median over its 3 runs: 1.45.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 1.76 (new, confidence medium, follows None)
- Where the answers part: focal length from the off-axis boat (Z = 5.86 m, not the 7.45 m Euclidean distance) and whether the stairs' pixel width includes the two pale posts in front (98 px stairs frame vs 110 px with posts)
- Fault proven: the submitted blend's B input (C3; C2 likewise) took f from the boat height with a depth larger than the boat's perpendicular Z (f 1075/1300 vs about 1000), and C3 then averaged in the run; C1 counted pale posts that are aligned with the jetty axis, not the stairs
- Closure on the prior: -1.7 pct

# Round 1 addendum (q1040, width of the wooden stairs)

## Established
- **Focal length is about 1000 px (973–1005)**, shown by two routes:
  - The depth pair (7.452 m at frame 0, 6.655 m at frame 24, boat at constant Z) gives f = 1002 and Z = 5.86 m.
  - The prior bound gives f ≥ 973 px. At frame 0 the bow post spans 126 px from its top (row 620) to the waterline
    (row 746), half of the 252 px span to its reflection. The 0.75 m box must contain that height, so f/Z ≥ 168.
- **Closure:** the prior comes back as at least 0.737 m (−1.7 %).
- **Plausibility:** door 1.85 m, railing 1.06 m, boat length 3.8 m.
- **Stairs pixel extent (frame 0):** the dark side members span x 489.5–587.5, about 98 px, with the treads between them
  (x 494–584). The pale posts at x 500–512.5 and 587.5–599 are centred on the jetty axis (x ≈ 549), not on the stairs
  axis (x ≈ 538).
- **Width:** 98 px × 17.6–18.1 m / 1000 = 1.72–1.77 m. Answer: 1.76 m.

## Ruled out
- **f = 1300 (C2):** it used the Euclidean distance as Z for a boat 774 px off-axis.
- **f = 1075 (C3):** it used Z ≈ 6.3 m instead of 5.86 m.
- **C4's 80 px tread span:** it starts inside the left member.

## Open
- **Depth drift of the boat between frames 0 and 24.** The pixel speed falls 6.5 % over the clip; receding and
  decelerating models fit equally well. A 1 % recession would lower f to 950 and raise W by 5 %, though the prior bound
  limits f to at least 973.
- **Whether the pale posts belong to the stairs model.** If they do, W is about 1.9 m.
- **Whether "width" means the run** (about 1.0–1.2 m) under the shorter-horizontal-extent reading.

### Round 2 (harness v3; files in context/round2/)
- Answer: 1.75 (new, confidence medium, follows None)
- Where the answers part: focal length (1000 px from the constant-Z depth pair vs 1075/1300 from treating Euclidean distance as Z) and stairs pixel extent (98 px members vs 108-110 px including jetty-aligned pale posts)
- Fault proven: the blend's B input (C3) used f=1075 from Z=6.3 m (depth pair gives Z=5.85 m, f=1000) and averaged in the run; the A input (C1) counted pale posts centred on the jetty axis, 12 px off the stairs axis
- Closure on the prior: -1.7 pct

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
