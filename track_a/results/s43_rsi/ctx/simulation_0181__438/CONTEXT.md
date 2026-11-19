# Context of question 438 (organised record; every round adds to it)

## Question
- Text: What is the speed of the box at time 1.5s in m/s?
- Its own prior: acceleration of the box after 0.75s = 2.338m/s^2
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0181.mp4 (simulation, A2MC)

## The answer currently submitted
3.83865 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 4.15 and an earlier DeepSeek median B = 3.2; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 4.15 | 1.081 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 2.94 | 0.766 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 3.2 | 0.834 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 3.64 | 0.948 |

DeepSeek median over its 3 runs: 3.2.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 3.6 (new, confidence medium, follows None)
- Where the answers part: pixel slide acceleration for the scale (594 vs 700-736 px/s2) and pixel centre speed at frame 36 (881-1133 px/s); both hinge on tracking the box centre while it changes yaw (frames 12-21 and 30-38)
- Fault proven: C1 extrapolated a constant acceleration to frame 36, but the silhouette-centre steps flatten to 35.8-38.3 px/frame after frame 29 when the box starts to yaw (C1 v36 1056 vs measured ~960 px/s); the DeepSeek runs took the scale from centroid quadratics inflated by the early yaw change (700-736 vs clean-window 616-642 px/s2)
- Closure on the prior: 4.0 pct

# Round 1 addendum — q438 (speed of box at 1.5 s)

Answer proposed: 3.6 m/s (decision "new"; submitted was 3.839 = blend of C1 4.15 and DeepSeek median 3.2). Confidence medium.

## Established (with measurement)
- Scale acceleration at frame 18. The clean window (frames 20–29, silhouette length stable at 281 ± 2 px) gives
  a = 616–642 px/s² from position quadratics of both the texture track (rms 0.15 px) and the silhouette midpoint.
  Adopted 625 → 3.74 mm/px.
- The DeepSeek scales (700–736) are inflated by a centroid bias in frames 12–21: the box's yaw settles there
  (length 311 → 280) and the centroid lags the texture by 16 → 0 px.
- Free fall (frames 0–7): the front-face top edge gives 2479 px/s² (rms 0.14) and the texture ECC 2560. At
  3.74 mm/px that is 9.3–9.6 m/s², closing to g within 2.5–5.4 %. The scene record's centroid fall value (≈2300) is
  biased by bottom-face foreshortening. The scene/ diff mask also misses the light top of the box; use an HSV mask
  (S>60, H 5–25, V<135).
- After frame 29 the box yaws: silhouette length 288 → 312 px over frames 30–34, and the left side face is 47.5 px
  wide at frame 36, 63 px at frame 38. From frame ~34 it also pitches by ~2.6°. The silhouette-centre steps are
  36.4, 35.8, 36.7, 36.8, 37.7, 38.3 px/frame for frames 29–34, so the acceleration falls to ~330 px/s².
  Texture (front-face) tracking runs ahead of the centre here; overlays show a ~20 px drift by frames 32–36.
- v36 ≈ 960 ± 30 px/s: midpoint quadratic over frames 29–34 extrapolated (944), and a side-face + trailing-edge
  geometry model (38–42 px/frame).
- Speed = 960 × 3.74e-3 = 3.59 m/s (range 3.41–3.80). The gravity-scale variant gives 3.68–3.80.

## Ruled out
- Constant acceleration through frame 36 (C1 4.15, C4's v36 = 1133 px/s).
- Centroid-quadratic scales of 700–736 px/s² (C2, C3, C4).
- C2's claim that the velocity is constant from frame 28: the centre is still accelerating mildly (~330 px/s²).

## Open
- The true centre speed exactly at frame 36, while the box yaws and pitches behind the crates and its leading
  corner is hidden (±3 %).
- Whether Blender's one-frame acceleration at frame 18 equals the mean slide acceleration. The gravity check
  suggests a mean of 2.4–2.5 m/s², which would raise the answer to ~3.75.

### Round 2 (harness v3; files in context/round2/)
- Answer: 3.68 (new, confidence medium, follows None)
- Where the answers part: pixel slide acceleration at frame 18 for the scale (594 vs 700-736 px/s2) and centre pixel speed at frame 36 (881-1133 px/s), both hinging on tracking the centre of a yawing box
- Fault proven: C1 extrapolated front-face texture at constant acceleration to v36=1056 px/s vs measured centre 963-979 px/s (trailing edge + half silhouette length); DeepSeek scales 700-736 px/s2 come from yaw-biased early windows (clean window 620-633, and 720 would make free fall 8.3 m/s2)
- Closure on the prior: 3.0 pct

# Round 2 addendum: q438 (speed of the box at 1.5 s = frame 36)

Answer: 3.68 m/s ("new"; verifies round 1's 3.6 within 2 %). Submitted was 3.839 (blend of C1 4.15 and DeepSeek median 3.2).

## Established (independent code: track.py, fit.py, fall.py)
- Free fall frames 0–7, from template tracking (rms 0.07 px): 2552 px/s². Taking this as g gives 3.844 mm/px.
- Slide acceleration over frames 20–29, where the silhouette length is constant at 281 ± 2 px: midpoint 633,
  trailing edge 618, leading edge 648 px/s². Trailing-edge fits over windows containing frame 18: 588–624.
  Adopted 620 → 3.77 mm/px. Closure with gravity: within 2–4 %.
- Early midpoint windows (14–22) give 730–810 px/s². These are biased by the side-face/yaw change in frames 12–20
  (length 312 → 281). At a 720 scale, g would come out at 8.3 m/s², so these windows are ruled out.
- From frame 30 the silhouette grows 6.5 px/frame (left side face, yaw). Trailing edge steps for frames 34/35/36 are
  35.5/36.2/36.9 px. Centre = trailing edge + half the length (extrapolated to 326 at frame 36). Centre step at
  frame 36 = 40.1–40.8 px → v36 = 970 ± 15 px/s (round 1: 960).
- Speed = 3.66 (prior scale) to 3.73 (gravity scale) m/s.

## Ruled out
- C1's v36 = 1056 px/s (constant-acceleration texture line).
- DeepSeek scales of 700–736 px/s².
- C2's constant v36 = 881 px/s.

## Open
- Whether a 2–3 % growth of the box height over frames 29–36 is approach to the camera (effect on the speed < 1 %).
- Residual ±3 % from the choice between prior scale and gravity scale.
