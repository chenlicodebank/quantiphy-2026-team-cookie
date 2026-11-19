# q1680: length of the rock (m). Answer 22.0 m (decision: new; verifies the round-1 proposal of 21.8)

- Video: 960x960, 75 frames. The file runs at 25 fps; question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48. I used frame indices throughout.
- 3D Blender scene, segmentation clip. The boat moves right to left. The rock is static, above and behind the boat in the image.

## What the answer depends on
L = rock pixel width × camera depth of the rock's widest points / f.
- **Rock pixel width.** 626 px, from the frame-72 mask (x 329–954, not truncated). My outline.py reproduces the record.
- **f.** From the boat, the prior and depth_info.
- **Rock depth.** No depth is given for the rock. It comes from the water plane: camera pitch θ, plus a camera height anchored at the boat's near waterline (row 655.5, Z ≈ 88.5–89.5 m).

## Crux
Where the answers part is the rock's depth.
- The 15.4–16.4 m answers (C2, C3, C5, C6) put the rock at the boat's 90 m.
- C1 (23.0, θ = 15.25°) and C4 (21.0, θ = 20°) put it on the water plane behind the boat. Between them, the pitch is what differs.

## Verification of round 1 (it proposed 21.8, "new")
- **Pitch: reproduced with my own extraction** (vp_edges.py). Round 1 used darkness-weighted centroids. I used sub-pixel half-level crossings of the left and right edges of the dark feature, then took the per-frame line slope against u over 70 frames.
  - Mast black stripe: θ = 18.17° (bootstrap 17.8–18.5), rms 0.07 px.
  - Thin black post: θ = 18.80° (17.9–19.6).
  - Upper post: 18.0° (noisy).
  - The overlay is frames/vp_ov40.png.
  - This confirms θ ≈ 18.5 ± 0.5° and that C1's 15.25° is biased low. The split-half values of the post scatter (25° and 18°), which explains the window sensitivity seen in C4.
- **Front-waterline lower bound: reproduced** (ellfit_theta.py). The bound is L ≥ 21.2–21.6 m for θ = 18.2–18.8° and Zwl = 88.5–89.5 m.
- **Round 1's ellfeat.py five-feature fits are partly unphysical.** For example, at b/a = 1 its solution has zc 6.0 > c 4.05, so the ellipsoid floats clear of the water. So I re-fitted (ellfit2.py):
  - Model: an ellipsoid with a vertical axis and free yaw, constrained to touch the water (zc < c).
  - Data: the full per-column outline (top and bottom rows) plus the extreme columns.
  - Fit residuals are 12.3–14.6 px rms.

| θ | b/a 0.5 | b/a 0.7 | b/a 1.0 |
|---|---|---|---|
| 18.2° | 22.33 | 22.67 | 22.66 |
| 18.6° | 21.76 | 22.30 | 22.49 |
| 18.8° | 21.81 | 22.30 | 22.30 |
| 15.25° (C1) | 23.7 | 24.2 | 24.4 |
| 20° (C4) | 21.45 | 21.59 | 21.98 |

- **Length versus depth extent (the round-1 open point).** The fits prefer b/a ≤ 1.3 (rms 12.5–13.7 px). Shapes elongated front-to-back fit worse (b/a 1.6: 14.8 px; b/a 2.0: 16.3 px) and would need a 3–4 m flat slab. This is weak evidence, but it supports taking length = lateral extent.
- **Adopted value: 22.0 m.** That is θ = 18.5°, b/a 0.5–1.0, range 21.8–22.6, sitting above the lower bound of 21.4. It agrees with round 1's 21.8 within 1%.

## Rechecks
- **a. Closure** (closure2.py). Linear boat tracks at frames 24 and 48 with the given distances give f = 3496–3503. At f = 3495, the boat speed comes out at 4.002–4.009 m/s against the 4 m/s prior: 0.04–0.24%.
- **b. Plausibility.**
  - Boat hull: 390 px → 10.1 m, a small fishing boat.
  - Camera height is about 32 m and the horizontal FOV 15.6°.
  - The rock comes out about 22 × 11–22 m in plan and 7–8 m above the water, a plausible sea rock.
- **c. Units and time base.** The answer is in metres. Frames 24 and 48 come from question_fps 24.
- **d. Fault proof.**
  - C2, C3, C5, C6 (15.35–16.4) used the boat's depth for the rock. The rock's waterline is 343 px above the boat's, and the camera looks down at 18.5°, so the rock sits at about 119–124 m, not 90 m.
  - C1 (23.0) used θ = 15.25°. My edge-based vertical vanishing point gives 18.2–18.8°.
  - C4 (21.0) used θ = 20°. That is about 4% low and within the uncertainty, not a clear fault.
  - The submitted 20.5 is a blend of 23 (pitch fault) and 15.7 (depth fault). It lies below the 21.2–21.6 lower bound that holds at the measured pitch.

## Decision
I adopt my own value, 22.0, which verifies round 1's 21.8. Confidence: medium. The rock's true shape is not an ellipsoid, and its front-to-back extent is only weakly constrained.
