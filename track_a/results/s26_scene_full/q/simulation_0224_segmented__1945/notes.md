# q_1945 — acceleration of the red general chess piece at t = 0.5 s

- Object: the scene record's "block" (cream rounded shape sliding down the ramp trough). It is the
  only moving object, so it is the chess piece (a disk seen obliquely). fps = question_fps = 24, so frame 12 is t = 0.5 s.
- Scale (2D): the prior gives a diameter of 0.097 m, which matches the piece's long silhouette axis (it lies along the
  motion direction). Record value: 81.3 px. My own mask (size.py, frames 0–30, extent along the path) gave 79–81.5 px,
  and I used 81 px, so 0.001198 m/px.
- Motion: the path is straight, and the piece speeds up steadily (uniform acceleration). The video has duplicated and
  skipped frames (record notes), so a raw one-frame difference at frame 12 is useless: frame 13 repeats frame 12.
  I re-mapped the frames to the true render index and fitted a quadratic to s_along_path (fit.py):
  a = 575–589 px/s² across fit windows (frames 3–20 / 3–30 / 3–36 / 3–39), with rms residual 0.3–0.7 px.
  I took 582 px/s².
- Second check: the per-true-frame steps grow linearly by about 1.0 px per frame (for example 11 → 38 px over
  frames 12–39), so a ≈ 1.0 × 24² ≈ 580 px/s², which agrees with the fit. A fit on the raw frame index gives the same
  a (577 px/s²) but with much larger residuals.
- a = 582 × 0.001198 ≈ 0.70 m/s².
- Confidence: about ±4%. The main uncertainty is the pixel diameter (±1.5%) and the spread between fit windows (±1.5%).
