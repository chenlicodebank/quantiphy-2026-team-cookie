# q257 — length of the sofa (m)

2D top-down render. Prior: robot cleaner speed = 1 m/s, which gives a single metres-per-pixel scale.

- Vacuum pixel speed (scene track, checked in measure.py): linear fit over frames 0–32 gives 8.401 px/frame, over all
  frames 8.410, mean per-frame step 8.415. An independent bright-blob check (check_vac.py) gives 8.5 px/frame for
  centroids over frames 20–30 and 8.3 for the bbox right edge over frames 10–30, which agrees.
  The frame-0 blob check failed (threshold) and is not used.
  The rate is 8.41 px/frame × 24 fps = 201.8 px/s, so 201.8 px = 1 m. question_fps 24.0 and file fps 24.008 differ by
  0.03 %, which is negligible.
- Sofa (L-shaped sectional, right side): edges found from intensity profiles on frame 0 (measure.py).
  The top edge is y≈207 (back bolster block) or ≈218 (left back), and the bottom edge of the lower arm is y≈834.
  Left/right: x≈565 to 918.
  The longer horizontal extent is vertical in the image: 834−207 = 627 px, which gives **3.11 m**.
  The shorter extent is 353 px = 1.75 m (the width).
  If the bolster block were excluded, the length would be 616 px = 3.05 m.
- Answer: 627 / 201.8 = 3.11 m. Caveat: the sofa top is nearer the camera than the floor where the vacuum is, so the
  true value may be a few percent smaller. The one-scale convention is followed here.
  Confidence: moderate-high.
