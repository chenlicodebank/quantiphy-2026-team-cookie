# Q419 – diameter of the rear (main) landing-gear wheels

Prior: airplane speed = 153.582 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scale (from the prior)
- The plane flies straight and level at constant pixel speed (no detectable acceleration).
- Pixel speed: scene track line fit gives 61.52 px/frame. My own fit to scene cx over frames 8–31 gives 61.63. An independent
  track of the wheel blob centroid gives 61.35. I used 61.52 px/frame = 1476.5 px/s.
- Scale = 153.582 / 1476.5 = 0.1040 m/px at the plane's depth. The wheels are at almost the same depth.

## Wheel size (fit_disks.py, sens.py)
- The nose gear is a small dot near the nose. The "rear wheels" are the main gear near x = 1087 at frame 18. They
  show as two dark tyre rings offset vertically by about 7.5 px, and their horizontal offset changes sign as the plane
  passes. These are the left and right main wheels, seen slightly from below in perspective.
- Each frame 8–31: crop, upscale ×8, threshold at half contrast between the background and the darkest tyre pixel,
  fill holes, then fit a union of two equal disks (frames/fit_18.png shows a good fit).
- D = 12.27 px (median; mean 12.25, std 0.36). In the central frames 17–21, where the wheels face the camera, D is
  11.6–12.0 px. The blob extents give a check: frame 20 has dx ≈ 0 and a blob width of 12.25 px, and the blob height
  minus the vertical offset is about 12.9 px.
- Threshold sensitivity: 0.65 gives 11.3 px; 0.35 gives 13.1 px, but it leaks into the strut and background. I adopted
  D ≈ 12.0 ± 0.7 px.

## Answer
D = 12.0 px × 0.1040 m/px ≈ 1.25 m. Sanity check: the plane's length of 459 px gives about 48 m, so the model is roughly
1.3× a regional jet, and 1.25 m wheels fit that size.
Confidence: moderate. The wheels are only about 12 px across, so the blurred edges give about ±6 %.
