# Context of question 556 (organised record; every round adds to it)

## Question
- Text: What is the height of the typewriter in meters?
- Its own prior: acceleration of the typewriter before 0.45s = 9.8m/s^2
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0208.mp4 (simulation, A2MS)

## The answer currently submitted
0.193233 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 0.179 and an earlier DeepSeek median B = 0.231; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.172 | 0.890 |
| C2 | Claude Opus 5.5 (Claude Code agent), 27_9 gravity-prior re-ask | 0.179 | 0.926 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.231 | 1.195 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.2 | 1.035 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 0.231 | 1.195 |

DeepSeek median over its 3 runs: 0.231.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 0.176 (switch, confidence high, follows C2)
- Where the answers part: flat 2D rest-silhouette pixel height (includes top deck seen from above, 0.231) vs perspective-corrected world height (0.172-0.179)
- Fault proven: the 0.231 component of the blend scaled the 173 px rest silhouette, taken well below eye level so it includes the foreshortened top face; the focal-length-free horizon-crossing timing route gives 0.176 m (true height ~136 px at front-face scale)
- Closure on the prior: 0.0 pct

# Round 1 addendum: Q556 (typewriter height)

## Established
- The scene is a 3D perspective render with a level camera. The horizon (eye level) is at row ≈539.5, where the mat
  side edges meet at the image centre (C2 found this; the right mat edge extrapolates to y ≈ 542 at x = 1062).
- The free fall is a clean parabola. Top edge, frames 0-7: 6801 px/s², rms 0.09 px. Bottom-back edge, frames 0-5:
  6894 px/s². Vertex (release) at frame -0.20.
- Focal-length-free timing route (edges.py, timing.py): the lowest point reaches eye level at frame 5.96 and the
  highest at frame 7.46. h = g/2·[(t_t−t0)² − (t_b−t0)²] = **0.176 m** (0.175-0.176 across fit windows; horizon ±1.5 px
  has no effect). The bottom-front branch gives 0.179. The pixel-gap route gives 0.176. The rough rest-pose route
  gives 0.18.
- Plausibility: width 0.38-0.42 m, depth ≈ 0.37 m, camera 0.63 m above the mat. Realistic.

## Ruled out
- 0.231 (C3, C5, and the 0.3 weight of the submitted blend): this is the rest silhouette, 173 px × the fall scale,
  measured while the object is far below eye level. The silhouette includes the top deck. The true height is ≈136 px
  at the front-face scale.
- C4's 0.20 is a hedge toward that flat value. Its own corrected routes gave 0.188-0.194.

## Decision
Switch to the C2 reading. Answer 0.176 (my value, within 2 % of C2's 0.179 and 2.5 % of C1's 0.172).
Confidence: high.

## Open
Only small risks remain: a slight roll in frames 7-8, and possible protrusions (feet, levers) at the extremes outside
the central columns I measured. None are visible on the zoomed frames 0 and 29.

### Round 2 (harness v3; files in context/round2/)
- Answer: 0.177 (switch, confidence high, follows C2)
- Where the answers part: flat 2D rest-silhouette pixel height (includes top deck seen from above, 0.231) vs perspective-corrected world height from eye-level crossing times (0.172-0.179)
- Fault proven: the 0.231 component of the blend scaled the 173 px rest silhouette taken far below eye level (top deck included); the focal-length-free horizon-crossing timing route gives 0.1776 m (front-face height ~134 px, not 173 px)
- Closure on the prior: 0.0 pct

# Round 2 addendum: Q556 (typewriter height)

## Established (independently re-measured with new code: edges3.py, fit3.py)
- Round 1's switch is verified. The timing route (horizon row 539.5, bottom crossing at frame 5.95, top crossing at
  frame 7.465, vertex at frame −0.2) gives h = 0.1763-0.1795 m (median 0.1776) over 20 fit windows × 3 choices of t0.
  The pixel-gap route gives 0.1765-0.1795 m.
- Accelerations: top (paper-rest plate edge) 6730-6795 px/s²; bottom-back 6880-7020; bottom-front 7415 px/s².
  All fits have rms ≤ 0.15 px. The top parabola predicts frame 8 within 1 px, so the top is a single thin edge.
- In-flight roll reaches about 3° at the crossings and 3.8° by frame 9. Its effect on the centre-column extent is
  0.1 %, which is negligible.
- Consistency: at 757 px/m (front-face scale) the parabola puts the bottom at row ≈ 982 in frame 10 (the scene record
  says 975-982) and contact at frame 10.4, which matches what the clip shows.
- Answer 0.177 m (switch, follows C2). Confidence: high.

## Ruled out
- 0.231 (C3, C5) is the flat rest silhouette (173 px), which includes the top deck. The front-face height is ≈ 134 px.
- The submitted blend, 0.193, is ≈ 9 % high because it carries 30 % weight on 0.231.

## Open
- Nothing material. The top-edge detector needs a threshold relative to the plateau because the plate's contrast is
  only ≈ 23 levels; a fixed threshold mis-tracks it.
