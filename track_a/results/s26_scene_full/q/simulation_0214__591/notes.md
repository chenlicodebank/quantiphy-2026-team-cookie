# q_591 — width of the floor mirror (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scene
The camera looks straight down and is static. The "floor mirror" is the light-framed rectangle leaning on the top
wall, top-right. The scene record calls it "leaning_picture_frame" and gives only a rough bbox. Its face is parallel to the
image x axis: the bottom edge is horizontal at image y = 219.5 for every column from 1400 to 1550. So its width (the
horizontal extent across the face) is its image x extent. I measure it at the bottom edge, which rests on the floor.

## Measurements (scripts: edges.py, cat.py, crop.py)
- Mirror (edges.py, mean of all 50 frames, gradient edges):
  - Bottom edge: y = 219.5.
  - Outer left edge reaches the bottom at x = 1385.5. The outer right edge, extrapolated along its line, reaches it at x = 1549.
  - **Bottom width = 163.5 px (±2 px).**
  - Top edge (higher up, nearer the camera): x from 1465.5 to 1660.5, i.e. 195 px. The ratio of 1.19 to the bottom width is
    perspective magnification.
- Black cat (cat.py, dark-pixel mask): head edge slope 10.975 px/frame (rms 0.57 px), full-mask centroid 10.96, body
  centroid 10.97. Speed is constant within ±0.4 px/frame over 8-frame windows. This matches the record's 11.0.
  - 10.97 px/frame × 24 = 263.3 px/s.
  - Scale at the height of the cat's silhouette: 0.94 / 263.3 = 0.003570 m/px.

## Perspective correction
- The ratio of top to bottom mirror width gives ht/D = 1 − 1/1.19 ≈ 0.16 (ht = mirror height, D = camera height).
- With a leaning mirror about 1.5–1.6 m tall, D ≈ 9.5–10 m, f ≈ 2800 px and HFOV ≈ 38°.
- The cat's visible outline is about 0.2 m above the floor. So the floor-level scale is larger by D/(D − 0.2) ≈ 1.02:
  s_floor ≈ 0.00364 m/px.

## Result
- Uncorrected: 163.5 × 0.003570 = 0.584 m.
- Height-corrected: 0.596 m.
- **Answer: 0.594 m.**

## Check
- Visual reading of an enhanced 4× crop: bottom corners at about x = 1386 and 1547, i.e. 161 px, which gives 0.575–0.59 m.
- The cat's body length of 0.56 m at the same scale and the room width of about 5.6 m are plausible together with a mirror
  about 0.6 m wide (a typical floor mirror is about 0.6 m wide).

## Confidence
About ±4%. The main uncertainties are the soft bottom-right corner (±2 px) and the size of the perspective correction (1–2.5%).
