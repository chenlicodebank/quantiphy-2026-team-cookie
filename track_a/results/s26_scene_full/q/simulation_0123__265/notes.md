# Q265: length of the blue rolling cup (m)

The camera looks straight down and is static, so this is a 2D scene. The "blue rolling cup" is the teal object that the scene record calls `teal_box`. It is a cup lying on its side and rolling in +x. Its axis lies along image y, so seen from above it is a rectangle: 78 px along y (the cup's length along its axis) by about 44 px along x (its diameter).

fps = question_fps = 24, so the clip has not been re-timed.

## Measurements (measure.py, HSV teal mask with y < 450 excluded, overlays in frames/mask_*.png)
- Per-frame step over frames 2–71: 14.536 ± 0.22 px/frame. A linear fit of x gives a slope of 14.537 px/frame, so the speed is 348.9 px/s.
- Scale: 0.338 / 348.9 = 9.688e-4 m/px.
- Length along y: 78.0 px in every frame, measured both as the bbox height and as the median column count.
- Length = 78 × 9.688e-4 = **0.0756 m**.
- For reference, the diameter is about 43–44 px, or roughly 0.042 m. "Length" is read as the longer horizontal extent, which is the cup's axis (78 px).

## Check
- Second route for the speed: net displacement from frame 1 to frame 71 is about 1017 px over 70 frames, or 14.53 px/frame. This matches the first route.
- The scene record's numbers (78 px; 14.54 px/frame) agree with my measurements.
- A cup 7.6 cm long and 4.3 cm across is a plausible size.

Confidence: high. The remaining uncertainty is about ±1 px of soft edge on 78 px, so about ±1.5%.
