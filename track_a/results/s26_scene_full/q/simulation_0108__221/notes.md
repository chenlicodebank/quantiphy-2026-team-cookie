# q_221 – velocity of the left virus at 1.0 s

Prior: speed of the left virus = 1.7393 m/s (no time given, so it is the speed of the motion). The file fps and question_fps are both 24, so t = 1.0 s is frame 24.

## Measurements (scene/tracks/virus_A.csv, checked with fit3d.py)
- Pixel speed rises roughly linearly, from 11.48 px/frame at frame 2 to 12.29 at frame 24 and 12.40 at frame 27 (+8%).
- The apparent size grows too: sqrt(mask area) rises 4.4% over frames 1–27, and 1/size falls linearly (Z shrinks by about 0.16% per frame).
  So the virus is coming toward the camera, not just accelerating in the image plane.
- Perspective check: assume a constant 3D velocity and a principal point at y = 540. Two effects then raise the image speed:
  (a) the 1/Z growth adds about 4.4% of 11.4, roughly 0.5 px/frame;
  (b) the radial term (v − cy)·|Vz|/Z adds about 0.0016 × 282, roughly 0.45 px/frame, by frame 27.
  Together they predict about 0.95 px/frame of growth. The measured growth is 0.92 px/frame. The speed-up is therefore explained
  by perspective, with the 3D speed constant.

## Answer
The 3D speed is constant, so the speed at 1.0 s equals the prior: **1.7393 m/s**.
Other reading: if the speed-up were real 2D acceleration and the prior were the initial speed, the answer would be
1.7393 × 12.286 / 11.476 = 1.862 m/s. The size growth argues against this reading.
Confidence: moderate to high.
