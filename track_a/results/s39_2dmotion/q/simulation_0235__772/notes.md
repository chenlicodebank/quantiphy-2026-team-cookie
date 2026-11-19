# q_772 — speed of the basketball at t = 0.5 s

The file rate and question_fps are both 24, so t = 0.5 s is frame 12. Speed = |p(12) − p(11)| × 24 (backward difference).
This is a 2D scene. The scale comes from the prior: ball diameter = 0.282 m.

## Measurements (my scripts: measure.py, analyze.py)
- **Ball track:** measure.py uses an HSV mask of the ball blob with its convex hull and takes the centroid in each frame, frames 0–30. The ball falls straight down (x ≈ 907.3 constant) and bounces at frame 24.
- **Fall fit:** analyze.py fits a quadratic to cy over frames 0–23, giving a = 1.345 px/frame² (rms residual 0.17 px).
  - The fit's 11→12 displacement is 15.45 px. The result is the same for windows 3–20 and 6–18.
  - 15.45 / 1.345 = 11.49, which matches release from rest at frame 0 (agrees with scene notes).
- **Raw 11→12 displacements:**
  - My centroids: 15.79 px.
  - SAM 3 centroids: 569.9 → 585.8, 15.9 px.
  - Scene record circle fit: 14.93 px.
  - The fitted 15.45 px lies in the middle of these, so I use it.
- **Pixel diameter:**
  - Sub-pixel 50 % edge crossings on a horizontal profile through the centre, frames 0–23: median 107.1 px. The horizontal direction has no motion blur.
  - SAM 3 masks: horiz_px 107 at frames 11 and 12. Area-equivalent diameter 108.9.
  - My hull: 108 px wide. Scene record: circle fit 106.1, bbox 108.
  - All agree within 2 %, so I use 107.1 px. The circle fit (106) is slightly low because it leaves out the lower part of the contour. The SAM area-equivalent value (108.9) is slightly high because it includes the anti-aliased rim.
- **SAM 3 check (frames 11 and 12):** the overlay covers the whole ball and nothing else. Its centre and extents agree with mine to within 3 %.

## Result
- Scale: 0.282 / 107.1 = 0.002633 m/px.
- Speed = 15.45 px × 24 × 0.002633 = **0.976 m/s**.
- **Second route:** the raw SAM displacement (15.9 px) gives 1.005 m/s. The raw circle-fit displacement gives 0.943. A diameter of 106 or 108 px moves the result by ±1 %.

Confidence: high (about ±3 %).
