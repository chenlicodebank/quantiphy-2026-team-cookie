# q_1947 — acceleration of the red general chess piece at t = 1 s

- Object: the record's "block" (scene/tracks/block.csv) is the chess piece — the only moving object, a disc
  sliding down the ramp trough (checked on a zoomed crop at frame 24). fps = question_fps = 24, so no re-timing.
- Scale (2D video): diameter 0.097 m = silhouette long axis along the ramp, median 81.4 px (range 79.6–83.6, constant
  along the path) -> 1.192e-3 m/px. The ellipse major axis lies along the motion direction, so the motion direction is
  not foreshortened relative to the diameter.
- Motion: the file has dropped/duplicated frames (see scene notes). I mapped frames to true render indices
  (5→6, 10→11, 11→12, 12→13, 23→24, 24→25, 27→28, 34→35, 37→38; dropped the repeats) and fitted
  s(t) = quadratic along the path (fit_acc.py). The motion is uniformly accelerated (rms residual 0.3–0.6 px).
  - frames 4–39: a = 576 px/s² → 0.687 m/s²
  - 4–24: 584 → 0.696; 20–39: 556 → 0.663; 10–36: 577 → 0.688; 14–30 (around t = 1 s): 586 → 0.698
- Second route: per-render-frame speed differences (backward differences) are noisy, median 537 px/s² → 0.64 m/s²;
  the step sizes grow linearly (~4.6 → 38 px per frame over ~34 frames ≈ 0.99 px/frame² ≈ 570 px/s²), consistent.
- Answer: 0.69 m/s² (constant acceleration, so the value at 1 s). Confidence: moderate-good; main uncertainty is the
  pixel diameter (±2.5 %) and the frame-timing mapping (±3 %).
