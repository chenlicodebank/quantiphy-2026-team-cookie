# q_588: length of the TV stand (m)

The prior is the black cat's speed, 0.94 m/s. depth_info is null. fps = question_fps = 24.
The camera is static and looks straight down. The corner edges of the room meet at the image centre (960, 540), so the principal point is there.

## Scale
- I fitted a line to the black cat's position over frames 0–49 in scene/tracks/black_cat.csv (`catspeed.py`). The head edge bbox_x1 gives 10.978 px/frame (residual 0.5 px), the body centroid 10.94 and the full centroid 10.96. Both halves of the clip give the same speed.
- I use 10.97 px/frame = 263.3 px/s, so the scale is 0.94 / 263.3 = 3.570 mm/px in the plane of the cat's origin.

## TV stand pixel length
I measured on frame 0 with `profile.py`, `enh*.py` and `rightedge.py`.
- **Left end:** the edge of the top surface is at x = 710.5. The step from about 90 to 60 grey level is sharp on rows 180–280.
- **Top surface:** it spans y 168 (back edge) to 283 (front edge). A front face about 8 px tall is visible (y 283→291). At the left end, the vertical edge runs from (710, 283) to (719, 291), pointing at the image centre.
  - The x shift and the y shift both give a ratio of 0.965. So the cabinet height is about 3.5 % of the camera height (h/H ≈ 0.035).
- **Right end:** it is hidden under the lamp shade, which is centred at (1190, 224) with a radius of about 73 px.
  - Right of the lamp's edge, every row is carpet (about 110 grey level), never cabinet (about 70). This holds on the front edge and front face rows (y 283–292), where the lamp's edge reaches only 1235→1220.
  - So the right end of the top surface is at most about 1229, after allowing for the front face's slant of about 9 px.
  - The lamp is a table lamp standing on the cabinet: its shade is centred on the cabinet's depth. So the cabinet reaches at least about 1205.
  - The decor looks symmetric: the vase is 44 px in from the left end, and the lamp base is at about 1183–1190 (correcting for the raised shade). That puts the right end at about 1227.
- **Result:** the length of the top surface is about 1227 − 710.5 = 516.5 px, with a range of 495–520.

## Perspective
- The cabinet's top is closer to the camera than the cat's origin (cat origin height ≈ 0.01–0.02 H).
- Correction factor: (1 − 0.035) / (1 − 0.015) ≈ 0.98.

## Answer
L = 516.5 px × 3.570 mm/px × 0.98 ≈ **1.80 m** (range 1.73–1.82 m).

## Check
I applied the same scale to the other objects:
- room/carpet width: 1561 px ≈ 5.6 m
- cabinet depth: 115 px ≈ 0.41 m, a typical TV stand depth
- bench: 289 px ≈ 1.03 m
- black cat body: 156 px ≈ 0.56 m

All are plausible, and 1.8 m is a typical TV stand length.

## Confidence
Moderate. The main uncertainty is the hidden right end, about ±3 %. If the stand were centred on the TV (centre ≈ 950), the right end would be at 1194 and the length 1.69 m. That is unlikely, because the lamp would then hang off the end of the cabinet.
