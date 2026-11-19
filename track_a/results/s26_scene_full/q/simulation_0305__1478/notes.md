# q_1478 – displacement of the plane, 0.5 s → 1.0 s

File fps = question_fps = 24, so 0.5 s = frame 12 and 1.0 s = frame 24 (12 frames apart).
Prior: speed of the plane = 22.16 m/s, given as a single value for the whole clip, so the speed is constant.
depth_info: 102.6664 m at frame 24 and 121.8263 m at frame 48.

## Method
- I checked the track in scene/tracks/aircraft.csv. It follows the single aircraft smoothly up-left and away from
  the camera. Frames 0 and 1 are duplicates, and the motion starts at frame 1→2. Both of these frames come
  before frame 12, so they don't affect this interval.
- If the plane moves in a straight line at constant velocity, displacement = 22.16 × 0.5 = **11.08 m**.

## Check (fit3d.py, fit_fixedf.py)
- I fitted a 3D straight-line, constant-velocity trajectory to the pixel centroid track, constrained by both
  depth_info distances, for a range of focal lengths:
  - The focal length that reproduces the prior speed of 22.16 m/s is about 2900 px.
  - Solving the frame 24→48 chord directly for the 22.16 m/s prior gives f ≈ 3390 px (HFOV ≈ 41°).
  - At these focal lengths the fitted 12→24 displacement is 10.9–11.3 m. The reprojection RMS is about 2 px.
- A free fit with constant acceleration lowers the RMS a little, from 2.0 to 1.4 px. That gain is consistent with
  the mask centroid drifting against the true origin as the silhouette changes. The prior's single
  speed value implies constant speed.
- Sanity check: the plane's length comes out at about 577 px × 102.7 m / 3000 px ≈ 20 m, which is plausible for a
  fighter jet.

Answer: 11.08 m. Confidence: high, assuming constant velocity, which the prior implies.
