# q 2870 – white ball diameter (cm)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 762.75 px.
Scale: depth_info t=1.0 s (frame 24) white ball distance = 1.235 m. D = 1.235 * w_px / 762.75.

## Pixel diameter of the white ball at frame 24 (heavily motion-blurred, streak along ~-35 deg)
- Across-streak intensity profiles (prof2.py, frames/prof24.png): top edge half-level at t~-16.5, bottom edge
  (shaded lower limb ending at the dark segmentation rim) at t~+23..+25 -> 39.5-41 px.
- Scene record mask minor width: 40.8 px (includes a little of the overlapping yellow streak).
- Circle fit to the leading cap of the blur streak (capfit.py, frames/cap_24.png; the cap of a motion-blurred disc
  is a semicircle of the true radius): 38.3-38.8 px (thr 25-35). Frame 25 (clean cap against wall): 36.0-37.2 px,
  consistent with the ball receding (widths drop 38.5 -> 36.6 -> 33.9 -> 30 -> 26.4 over frames 24-28).
- Half-contrast thresholds (ballistic.py) cut off the shaded lower half of the ball (~29 px) – rejected after visual
  check (frames/half_24.png).
- Adopted w = 39.3 +/- 1.5 px.

## Result
D = 1.235 * 39.3 / 762.75 = 0.0636 m -> **6.4 cm** (range 6.2-6.5 cm for 38.3-40.8 px).

## Checks
- Green (yellow-green) ball at the same time: ~40-42 px at 1.331 m -> ~7 cm, so the two thrown balls are of similar
  size, as they look in the video.
- An attempted ballistic (|g| = 9.81) scale fit was too sensitive to width noise (gravity direction came out wrong),
  so it is not used.
- Note: the orange-ball depths (2.24 m at 0.5 s, 1.81 m at 1.0 s) conflict with its shrinking apparent size;
  irrelevant to this answer, which uses only the white-ball depth.
Confidence: moderate (about +/-5 %), limited by motion blur at the only frame with a given depth.
