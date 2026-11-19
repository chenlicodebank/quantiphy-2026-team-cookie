# Context of question 1680 (organised record; every round adds to it)

## Question
- Text: What is the length of the rock in meters?
- Its own prior: speed of the boat = 4m/s
- Its own depth_info: t=1s, distance_boat_camera = 90.1103 m
t=2s, distance_boat_camera = 90.4360 m
- question_fps: 24
- Video: simulation_0024_segmented.mp4 (segmentation, V3MX)

## The answer currently submitted
20.5008 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 23 and an earlier DeepSeek median B = 15.675; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 23.0 | 1.122 |
| C2 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 2 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 16.4 | 0.800 |
| C3 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 3 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 16.4 | 0.800 |
| C4 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_9a D3 adjudication batch 1 (DeepSeek+SAM 3 differs >25 pct) | 21.0 | 1.024 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 16.0 | 0.780 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 15.35 | 0.749 |

DeepSeek median over its 2 runs: 15.6716.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v2; files in context/round1/)
- Answer: 21.8 (new, confidence medium, follows None)
- Where the answers part: rock depth: at the boat's 90 m (15.4-16.4) vs on the water plane behind it, where the camera pitch sets the depth (C1 15.25 deg -> 23.0, C4 20 deg -> 21.0)
- Fault proven: boat-depth candidates ignore that the rock's waterline is 343 px above the boat's under a down-looking camera (rock at ~120 m, not 90 m); C1's 15.25 deg pitch is biased low (sub-pixel vertical-VP fits on two dark verticals give 18.1 and 19.2 deg); submitted blend 20.5 inherits both and lies below the 21.3-21.5 m front-waterline lower bound
- Closure on the prior: 0.3 pct

# Round addendum for q1680 (rock length)

## Established
- **Focal length.** Boat track plus depth_info (frames 24 and 48 at question_fps 24) and the 4 m/s prior give f = 3501–3507 px.
  - Closure 0.2–0.4%.
  - Boat hull: 10.0 m.
- **Rock silhouette.** Frame 72, x 329–954 (626 px), not truncated. Tips at rows ~150–169. Top at row 25. Front waterline cut, a streaky band, at row 312, x ~600–750.
- **The rock is on the water behind the boat, not at the boat's depth.** Its waterline is 343 px above the boat's waterline, and the camera looks down (the deck is visible).
  - This rules out the 15.4–16.4 m answers (C2, C3, C5, C6).
- **Camera pitch from the vertical vanishing point** (vvp.py, sub-pixel darkness-weighted centroids, about 70 frames, u 265–777):
  - mast black stripe: 18.14° (bootstrap 17.8–18.5);
  - black post, thin-pole rows only: 19.15° (18.8–19.5).
  - Adopted θ = 18.6 ± 0.6°.
  - C1's 15.25° from the pale mast is biased low.
  - C4's post value of 21.6° is window-sensitive: a short window gave 26° and the thin-pole window gives 19.2°.
- **Water plane** anchored at the boat's near waterline (row 655.5, Zcam 88.5–89.5) gives a camera height of 32.6 m.
  - Front waterline depth Zb = 119–120 m, so L ≥ 21.3–21.5 m (lower bound).
  - Tips-on-water upper bound: 25 m. This is not reached, because the tips are about 4.5–5 m above the water.
- **Ellipsoid feature match** (ellfeat.py) for b/a 0.4–1.0 and θ 18.1–19.2: L = 21.3–22.6 m.

## New answer
21.8 m (medium confidence).

## Still open
- The rock's front-to-back extent is unknown. All readings take length = lateral (image-x) extent. A rock deeper than it is wide would change the answer; the silhouette cannot resolve that. The IoU ellipsoid fit (ellfit.py) is ill-conditioned.
- Pitch uncertainty of ±1° gives about ±2% in L.

### Round 3 (harness v3; files in context/round3/)
- Answer: 22.0 (new, confidence medium, follows round1 proposal (21.8))
- Where the answers part: rock depth: boat depth 90 m (15.4-16.4) vs water plane behind the boat with camera pitch from the vertical vanishing point (15.25 deg -> 23, 18.5 deg -> 22, 20 deg -> 21)
- Fault proven: rock is on the water ~30 m behind the boat (waterline 343 px higher, camera pitched down 18.2-18.8 deg by edge-based VVP), so boat-depth answers are wrong and C1's 15.25 deg pitch is biased low; submitted 20.5 lies below the 21.2-21.6 m front-waterline lower bound
- Closure on the prior: 0.1 pct

# Round 2 addendum for q1680 (rock length)

## Verified (own code, a different extraction from round 1)
- **Pitch from the vertical vanishing point** (vp_edges.py). Sub-pixel half-level edge crossings on two dark verticals, 70 frames, u 265–778:
  - mast stripe: 18.17° (17.8–18.5);
  - thin post: 18.80° (17.9–19.6).
  - This confirms θ ≈ 18.5 ± 0.5°. C1's 15.25° is biased low. The split halves of the post scatter (25° and 18°), so a short window is unreliable.
- **Focal length** (closure2.py). f = 3496–3503 px. The 4 m/s prior closes within 0.04–0.24%. Boat hull: 10.1 m.
- **Front-waterline lower bound.** L ≥ 21.2–21.6 m for θ 18.2–18.8° and Zwl 88.5–89.5 m. The submitted 20.5 is below it.
- **Round 1's ellfeat.py solutions are partly unphysical.** For example, at b/a = 1 it gives zc > c, an ellipsoid floating clear of the water.
- **New outline fit** (ellfit2.py). Ellipsoid touching the water, free yaw, full per-column outline. At θ 18.2–18.8° and b/a 0.5–1.0: lateral AABB extent 21.8–22.7 m, rms 12.5–14.6 px.
- **Adopted: 22.0 m** (round 1 had 21.8).

## Ruled out
- **Rock at the boat's depth** (15.4–16.4 m): its waterline is 343 px higher and the camera looks down.
- **θ = 15.25°** (23–24 m).

## Still open
- **Front-to-back extent.** Fits elongated in depth (b/a 1.6–2.0) are worse (rms 14.8–16.3 px against 12.5–13.7) and need a 3–4 m flat slab. That is weak evidence that length is the lateral extent, not proof.
- **Pitch.** ±0.5° gives about ±1.5% in L.
