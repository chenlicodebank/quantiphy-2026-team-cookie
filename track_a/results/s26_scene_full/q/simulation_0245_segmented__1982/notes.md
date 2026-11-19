# q_1982 — average speed of the rabbit (m/s)

Prior: deer speed = 1.277 m/s. The "deer" is the large horned quadruped (called "ibex" in scene/). It walks
left to right next to the small rabbit. This is a 2D scene: the camera is static, both animals walk on the same
ground line (y ≈ 1551) and keep a constant size, so one m/px scale covers both animals.
fps = question_fps = 30, so no re-timing.

Method (m.py, using scene/tracks): I compared the pixel speeds of the two animals over the same frame windows,
then multiplied the deer prior by the ratio rabbit/deer. Frames 69-74 are left out for the rabbit because it is
cut off by the right image edge there.
- Linear fit over frames 0-68: deer centroid 6.516 px/frame (torso centre 6.523); rabbit centroid 6.732 px/frame.
  Ratio 1.033 (1.032 against the torso centre). Speed = 1.277 × 1.032 = 1.318 m/s.
- Second route: net displacement over several windows (0-68, 0-60, 5-55, 10-64, 0-50, 8-58), with the rabbit
  measured by its centroid, rear edge (x0) and front edge (x1). The ratios range from 1.014 to 1.040, which gives
  1.30-1.33 m/s.
- I used the smooth net speed rather than the summed per-frame centroid path. The centroid path includes gait
  jitter from the legs moving, which the root origin does not have.

Answer: 1.318 m/s. Confidence: high (about ±2%), because the answer depends only on the ratio of the two
speeds, and that ratio is about 1.03 and steady across all the windows.
