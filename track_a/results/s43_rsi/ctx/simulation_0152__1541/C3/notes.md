# q_1541 – width of the blue car (the light-blue cart in scene/)

Answer: **0.73 m** (the cart's horizontal extent across its direction of travel, i.e. along the camera's depth axis).

## Setup
- 3D Blender scene, 24 fps (file fps = question_fps = 24). Camera static, level, principal point ≈ (960, 540)
  (vanishing point 959.3, 539.1 from scene/).
- The cart drives left→right parallel to the image plane at constant depth, so its width runs along the viewing
  direction. Width can only come from perspective: two points at the same along-track position X but different
  depths Z1 and Z2 project to u − 960 = f·X/Z. Tracking a feature against the near-side hub reference ref_x
  (scene track; it matches the Hough hubs with slope 1.000) over many frames gives
  slope = Zo / Z_feature, where Zo is the depth of the near-side hub plane.
- f and Zo: tyre diameter 0.369 m ↔ ~112–113 px. depth_info gives 9.312 m (Euclidean) to the right-front (near-side,
  camera-facing) tyre at frame 24, where the hub is at (623.5, 893.5). Solving those two together gives f ≈ 2780–2810 px
  and an on-axis depth Zn ≈ 9.17 m. Because the object is near the image centre, Zn barely depends on f (f = 2600
  gives 9.15). The hub plane sits a few cm nearer than the tyre's mid-plane: Zo ≈ 9.10 ± 0.05 m.

## Measurements (scripts in this folder)
| feature | method | Z/Zo |
|---|---|---|
| roof front, far silhouette corner (frames 13-30) | slopes.py / refit.py, rms 0.36 px | 1.0826 |
| roof front, near corner seen from right of centre (frames 33-41) | roof_right.py, rms 0.13 px | 1.0154 |
| roof corner chamfer (visible bevel, ~13 px at frame 38) | b ≈ 0.048 m → ±0.0053 | roof spans ≈1.010–1.088 → **0.078 Zo** |
| near headlight / far headlight (frames 13-27) | headlights.py, hl_fit.py, rms 0.3 px | 1.0134 / 1.0781 → centre line 1.0458 |
| far front tyre, far shoulder silhouette (frames 13-22) | tyres_lr.py, circle model with r0 = 55 px | ≈1.084 (±0.003) |
| near front tyre, near shoulder silhouette (frames 33-41) | tyres_lr.py, near_tyre_lr.py | ≈1.002–1.006 |

- Wheels, outer shoulder to outer shoulder: 1.084 − (1.002…1.006) ≈ 0.078–0.082 Zo. Their centre line (≈1.044) matches
  the headlight centre line (1.0458).
- Symmetric route: 2 × (far tyre shoulder 1.084 − centre line 1.0455) = 0.077 Zo.
- Roof: 0.078 Zo. The roof and the wheel track have about the same width.
- Combined: W ≈ 0.078–0.080 Zo ≈ 0.71–0.73 m. Silhouette shoulders lie a little inside the true sidewall planes
  (+0.01–0.03 m), so the bounding-box width is **≈0.73 m**.
- Second-route check: per-frame roof front ratios measured inside a single frame (independent of ref_x), corrected
  for the chamfer, give (Z2 − b)/Z1 ≈ 1.067–1.077, i.e. a roof width ≈ 0.07–0.08 Zo. This agrees.

## Caveats / confidence
- The width is only ~8 % of the camera distance, so a 0.003 error in a depth ratio moves the answer by ~4 %.
  Estimated uncertainty is ±8 %.
- Fits that rely on short baselines of the ref_x track (frames 33-41) carry ±0.005 errors.
- The scene record's tyre radius of ~56 px includes some contact shadow; silhouette-based r_eff is ≈ 55 px.
- The prior's yellow-car tyre (0.764 m, ~186 px) is ~6 % inconsistent with the floor geometry. It only matters
  through f, which hardly affects the answer.
- Named-size reading: width = shorter horizontal extent = side to side across the cart (the depth direction here).
  Length (for reference) ≈ 549 px ≈ 1.8 m.
