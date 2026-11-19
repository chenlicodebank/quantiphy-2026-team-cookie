# q_1729: average speed of the person (m/s)

Prior: the boat is 10 m long. Depths: boat 133.96 m at t=1 s and 131.26 m at t=2 s; person 139.103 / 139.104 m.
The file and the question both run at 24 fps, 72 frames.

## Focal length (from the boat), `focal.py`
- The boat moves left and toward the camera. Its radial speed is -2.70 m/s, from the two depths.
  Its mast-to-keel height grows 6.5% over the clip, which matches the depth ratio of 6.3%. So the depths fit the image.
- Its bbox width grows 12%, which is more than the depth change explains. The boat is therefore seen obliquely, and the
  view becomes more broadside as it moves left.
- Model: the boat's heading equals its 3D velocity direction (from the pixel track plus depth, which depends on f). Its
  lateral image extent is f·(L·sinφ + c·cosφ)/Z, with L = 10 m.
- Fitting f and c to the bbox width over all 72 frames gives **f = 3078 px** and c = 0.7 m (rms 0.65 px).
  The heading is about 41° off the image plane and the boat's speed is about 4.2 m/s, which is realistic.
- Sensitivity: c from 1.0 to 0.5 m gives f from 2970 to 3160 px. A broadside reading with no foreshortening would give
  f ≈ 2450-2510 px, but that contradicts the extra width growth and the person check below.

## Check with a standard object
- The person's bbox height is 40.5 px (mean over frames) at 139.1 m. With f = 3078 that gives **1.83 m**, a plausible
  adult. With f = 2500 the person would be 2.25 m, which rules that value out.

## Person motion, `person.py`
- The person is seen in side profile, walking to image-right. The given distance to the person's origin barely changes
  (+0.001 m in 1 s) even though the body moves about 75 px. So the origin stays put; I did not use that distance for
  the body's motion.
- The direction of motion comes from the profile view and the near-constant apparent size: I took it as perpendicular to
  the line of sight.
- Linear fit of the soft-mask centroid over frames 1-71: du = 1.062 px/frame, dv = 0.049 px/frame.
  The raw per-frame centroid steps average 1.36 px, but that is inflated by gait and mask jitter, so I used the trend.
- Z = 139.10/1.0093 = 137.8 m. Speed = 1.063 px × 24 × 137.8 / 3078 = **1.14 m/s**. Treating the motion as perpendicular
  to the ray instead of parallel to the image plane gives 1.136 m/s.
- Pelvis bob and sway add roughly 1-2% to the mean of the per-frame speeds, so the answer is **1.15 m/s**.

## Confidence
- The f range of 2970-3160 px gives 1.10-1.18 m/s. If the person were exactly 1.75 m tall instead, f would be 3217 px and
  the speed 1.09 m/s.
- Any small motion toward or away from the camera, which can't be resolved here, would add a little.
- Overall confidence: moderate, roughly ±7%.
