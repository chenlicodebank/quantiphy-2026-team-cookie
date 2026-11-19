# Q503 – speed of the bubble at t = 0.8 s (m/s)

2D simulation, 2560x2560, file fps = question_fps = 30 → t = 0.8 s is frame 24. Static camera.

## Scale (prior: horizontal width of the "skynova" text on the bottle = 0.00188 m)
- The brand word runs vertically along the bottle's left side. Only "NOVA" is visible; "SKY" is cut off by the
  bottom of the frame. Because the word is rotated 90°, its horizontal width in the image is the letter (cap)
  height, which is the same for every letter.
- `measure_text.py`: white-letter threshold mask at frame 24 (`frames/text_mask.png`, which fits the letters well)
  gives x = 1106–1185, a width of **80 px**.
- `check_text_edges.py`: half-max edges of the column brightness profile give 78.0 / 78.3 / 79.7 px for three letter
  rows. The "O" is slightly wider than the others, as letters of that shape usually are.
- SAM 3 "white text" (box prompt): horiz_px 89 (x 1102–1190), about 11 % wider. On the 3x zoom with the SAM outline
  drawn (`frames/text_sam_edges.png`), the SAM contour sits a few px outside the letter edges all round.
  The threshold and half-max edge measurement is correct, so SAM is not used for the scale.
- Width used: **79.5 px** → scale = 0.00188 / 79.5 = 2.365e-5 m/px.

## Bubble speed (`bubble_speed.py`)
Speed = |p(24) − p(23)| × 30.
- scene/ track (hull centroid): 12.68 px/frame; mean over frames 22–26: 12.41.
- My own measurement (template match of the frame-24 bubble patch, subpixel): 12.91 px/frame; mean over 22–26: 12.76.
- SAM 3 "bubble" track (box at frame 24; the overlay follows the bubble): steps of 11.2, 12.9 and 12.9 px for frames
  24–26. Its centres agree with the scene/ track to within about 2 px.
- The bubble moves at a steady ~12–13 px/frame from frame 17 to frame 31, so frame 24 is in the steady part of the
  motion. Value used: 12.7 px/frame = 381 px/s.

Speed = 381 × 2.365e-5 = **0.0090 m/s** (routes give 0.0088–0.0092).

Confidence: fairly high. The main uncertainty is the text width (78–80 px, ±1.5 %) and per-frame centroid noise
(±2 %).
