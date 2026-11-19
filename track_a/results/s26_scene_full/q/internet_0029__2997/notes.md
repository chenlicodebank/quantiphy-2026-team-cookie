# q_2997 — ball diameter (cm), prior g = 9.8 m/s^2

This is a 2D internet clip. The camera is static and the ball falls in a plane facing the camera. The scale comes from the ball's pixel acceleration matched to g.

## Measurements
- **Ball diameter in pixels:** 76 px. This is the horizontal width, which is not blurred; it is 74–77 px in frames 8–23. I checked it on a 4x zoom of frame 10 (about 519–594 px).
- **Ball track:** from scene/tracks/ball.csv, the mask centroid in frames 8–23.
- **Dropped frames:** one source frame is missing every 5th output frame (frames 12, 17 and 22; also 7 and 24). The doubled steps match in both x and y.
  - 5 output frames therefore span 6 source frames, so the source ran at 60 fps.
  - Normal steps are 1/60 s and doubled steps are 2/60 s.
- **Pixel acceleration:** I fitted a quadratic to y against the source-frame index (fit.py).
  - Frames 8–23 give 2.47 px per source frame², with rms 0.56 px.
  - The other windows give 2.40–2.50.
  - At 60 fps this is about 8,900 px/s².

## Result
- Scale = 9.8 / 8,900 m/px. Diameter = 76 × 9.8 / (2.47 × 3600) = **8.3–8.4 cm** (8.27–8.63 across the windows).
- **Other timing conventions:**
  - A naive quadratic over output frames at 50 fps (frames 8–23) gives about 9,470 px/s², or 7.9 cm.
  - Taking the doubled steps at 1/50 s gives 12 cm. That reading is implausible, because it contradicts the frame-drop pattern.
- **Sanity check:** the door knob is 61–64 px. A knob of about 6 cm suggests the ball is about 7–7.5 cm, or a little less because the ball is nearer the camera than the door. This agrees in magnitude.

## Answer
8.2 cm. This sits between the physical-timing value (8.3) and the naive-annotator value (7.9). Confidence is moderate.
