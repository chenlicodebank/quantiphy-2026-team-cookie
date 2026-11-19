# Context of question 258 (organised record; every round adds to it)

## Question
- Text: What is the length of the TV in meters?
- Its own prior: speed of the robot cleaner = 1m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0120.mp4 (simulation, V2MC)

## The answer currently submitted
1.46974 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 1.57 and an earlier DeepSeek median B = 1.26; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 1.57 | 1.068 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 1.25 | 0.850 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 1.95 | 1.327 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 1.26 | 0.857 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 1.21 | 0.823 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 0.8 | 0.544 |

DeepSeek median over its 5 runs: 1.25.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 1.57 (switch, confidence medium, follows C1)
- Where the answers part: distance of the TV's wall plane from the camera axis: the plinth front edge (x~296, X=1.21 m) versus the marble wall behind the plinth (junction on plinth top x=219, X~1.51-1.54 m); L = 1.048 x X_face
- Fault proven: The B component (DeepSeek 1.25/1.26/1.21) took the floor edge of the plinth's front face at x=295.6 as the wall base, but the wall meets the plinth top at x=219 (texture edge), 0.31 m further back; this gives 1.27 instead of 1.58
- Closure on the prior: 0.5 pct

# Round 1 addendum (Q258, TV length)

## Established (by my own code, frame 0, static scene)
- The TV is the black clock panel on the LEFT wall. The panel on the right wall is contour-line art (C6 measured the wrong object).
- Nadir pinhole: the TV side edges meet at (539.1, 539.3). The ratio Δv/u is 1.048 in every column (sd 0.0001), so L = 1.048 × X_face.
- Vacuum scale: 8.36–8.41 px/frame → about 201 px/m at the vacuum top. With a 1.4 % height correction, the floor scale is about 198.4 px/m.
- White plinth front face: top edge at x = 284.68, floor edge at x = 295.64 (sub-pixel, about 145 rows).
  The marble wall meets the plinth top at x = 219.0 ± 0.5 (texture edge).
- From these: X_front = 1.228 m and X_wall = 1.545 m.
- The TV's top face (grey strip, x 145.5–151.2) shows a TV about 2 cm thick. X_wall/X_face lies between 1.015 and 1.035.
- **L = 1.56–1.60 m (central 1.58).** This matches C1's 1.57 within 1 %.
- Checks: a 16:9 TV gives f ≈ 1180 px and a camera ≈ 5.9 m up; the plinth is 0.26 m high and the TV sits 0.47–1.36 m above the floor; the fireplace is about 1.6 m long. All are plausible.

## Ruled out
- X = 1.20 m (C2, C4, C5): x ≈ 296 is the floor edge of the plinth's front face, not the wall. That reading would put the TV floating 1.5–2.2 m up and 0.31 m in front of the wall.
- Planar single scale, 2.0 m (C3): ignores perspective.
- 0.80 m (C6): wrong object.

## Decision
Switched to C1 = 1.57 (the submitted 1.47 is a blend that includes the faulty 1.26).

## Open
- The TV's stand-off from the wall (±1.2 %).
- The height of the tracked vacuum feature (±0.4 %).

### Round 2 (harness v3; files in context/round2/)
- Answer: 1.57 (switch, confidence high, follows C1)
- Where the answers part: horizontal distance of the TV's wall plane from the nadir: plinth-front floor edge x=295.6 (X=1.21 m) vs marble wall meeting the horizontal plinth top at x=219.0 (X=1.54 m); L = 1.0457 x X_face
- Fault proven: DeepSeek runs (and blend component B=1.26) used the plinth front-face floor edge as the wall; marble texture and wall joint lines end at x=219 and the plinth top is horizontal (fireplace end edge constant y), so the wall is 0.31 m further out; their geometry reproduces 1.27, the correct one gives 1.58
- Closure on the prior: 0.2 pct

# Round 2 addendum (Q258, TV length): round 1's switch to 1.57 is verified

## Established (with my own code, frame 0)
- **Nadir camera, principal point at the image centre.** Four vertical marble-wall joint lines meet at (539.49, 539.46) (m_joints.py, rms 0.15 px).
  This is independent of the TV edges, whose own intersection along x is ill-conditioned (535–539).
- **TV ratio.** Δv/(cx − x) = 1.0457 ± 0.0007 at cx = 539.5 (dark-mask sub-pixel edges in columns 154–211, m_tv2.py). Round 1 had 1.048 and C1 had 1.045.
- **Vacuum.** 8.397 px/frame from two routes (circle centre 8.4035, edge midpoint 8.3904) → 201.5 px/m at the top disc and 198.8 px/m at floor level (8 cm top, H ≈ 5.9 m).
- **Plinth edges.** Front-face top x = 284.77, floor edge x = 295.64.
- **Wall junction x = 219.0.** The marble texture energy drops from about 3 to 0.08 at x = 218.5–219, and the wall joint lines end there.
- **The plinth top x 219–284 is horizontal.** The fireplace frame's end edge sits at a constant y = 408.4–408.5 over x 232–264; on a vertical surface it would be radial and drift about 15 px.
- From these: X_wall = 1.544 m. With the TV's thickness / stand-off k = 1.015–1.035, **L = 1.56–1.59 (central 1.58)**. It would be 1.61 if the face were flush with the wall.
- **Fault reproduced.** Using x = 295.6 as the wall gives X = 1.211 and L = 1.27, which matches the DeepSeek 1.21–1.26.

## Decision
Switch to C1 = **1.57** (high confidence). My value is within 1 % of it.

## Still open (small)
- The TV's stand-off from the wall (±1.5 %).
- The vacuum feature height and camera height correction (±0.5 %).
