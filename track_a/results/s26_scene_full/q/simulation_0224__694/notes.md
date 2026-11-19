# q_694: speed of the moving chess piece at t = 1.5 s

- **Setup:** 2D simulation at 24 fps (the file and the question agree). The "chess" is the cream disc (a Chinese
  chess piece) lying flat in the board's channel and sliding down-left. Frame 36 corresponds to t = 1.5 s.
- **Scale:** the prior gives a diameter of 0.097 m. The piece's extent along the slope equals its diameter.
  - Half-max edge profiles on a background-difference image, frames 9-33 (`diam.py`): 80.0-81.2 px.
  - The record's mask gives a long axis of 81.5 px (range 80.2-82.7).
  - Adopted value: 81 px, so the scale is 0.097 / 81 = 1.198e-3 m/px.
- **Motion:** the centroid track from scene/tracks/block.csv, re-checked with my own masks (centroids agree to
  within a few px).
  - The video has duplicate and skipped frames. Frame 35 is a duplicate of 34 (source frame 35), and frame 36
    is source frame 36.
  - So the raw step from frame 35 to 36 is a true single-frame step: 34.67 px.
  - Route 2: a quadratic fit of the path length against the source frame index (rms 0.5-0.8 px) gives a
    backward difference at frame 36 of 34.9-35.2 px/frame, depending on the fit window.
  - Adopted value: 35.0 px/frame.
- **Speed:** 35.0 × 24 × 0.097 / 81 ≈ **1.005 m/s**.
  - Range across the choices: 0.99-1.04 m/s, coming from the 79.5-81.5 px diameter range and the raw vs.
    fitted step.
- **Confidence:** good, about ±3%.
