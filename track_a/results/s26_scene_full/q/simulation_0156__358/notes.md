# Q358 – displacement of the shark (m)

Prior: shark speed = 7 m/s (exact). fps = question_fps = 24, 48 frames (t = 0 … 47/24 = 1.958 s).

Method: displacement over the whole clip = straight-line distance between origin at frame 0 and frame 47.
The shark moves in a straight horizontal line (cy constant ≈ 322 px, leftward only), so displacement = path length
= speed × elapsed time if the speed is constant.

Uniformity check (measure.py, from scene/tracks/shark.csv, using only untruncated edges):
- nose x0, frames 0–30: linear fit −57.49 px/frame, quadratic coef −0.046 px/frame² (negligible), rms residual 9 px (snout jitter).
- tail x1, frames 14–46: −57.32 px/frame, quadratic coef +0.097 (negligible, opposite sign), rms 8.5 px.
Two independent edges agree on a constant ≈ 57.4 px/frame → uniform motion, no acceleration.

Answer: 7 m/s × 47/24 s = 13.71 m. (Second route: scale 7/(57.4×24) m/px = 0.00508 m/px; pixel travel
57.4 × 47 = 2698 px → 13.71 m, the same since the speed is uniform.)
If the clip's duration were taken as 2.0 s, the answer would be 14.0 m (2 % higher); the frame convention gives 13.71.

Confidence: high.
