# q_695: acceleration of the moving chess piece at t = 1.5 s

The "chess" is the cream Chinese-chess disc that slides down the tilted board, seen almost edge-on. The track in
scene/tracks/block.csv follows it. It is a 2D scene and the camera does not move. I used fps = 24, which matches
question_fps, so t = 1.5 s is frame 36. The piece is still sliding then; it reaches the lip at frame 39.

## Scale
- Prior: the disc diameter is 0.097 m. The diameter is the disc's length along the slope.
- diam.py measures it by background difference against frame 44, when the piece has left the ramp.
  - Low threshold: 81.5 px (80.7–82.2) on frames 0–36. This includes some anti-aliasing.
  - Higher threshold, or 0.5–99.5 percentile extents: 78–80 px.
- I used 80.5 px, giving 0.097 / 80.5 = 1.205e-3 m/px.
- The length stays the same along the path, so there is no visible perspective change.

## Acceleration
- The video has duplicated and skipped frames, so I used the record's `source_frame_est` re-index. I checked it
  myself: the fit residual is about 0.6 px, against about 10 px with the raw frame index.
- A sliding piece on a constant slope should have constant acceleration, so I fitted a quadratic in time to the
  along-ramp distance (measure.py, local.py):
  - frames 3–38: 580 px/s²
  - frames 8–38: 573 px/s²
  - frames 2–30: 590 px/s²
  - frames 15–38: 564 px/s²
  - a linear fit to the per-step velocities gives 576 px/s²
- Fits restricted to late windows (frames 26–38) give 520–530 px/s². They are noisier because the duplicated and
  skipped frames sit close together there.
- I took a ≈ 575 px/s² × 1.205e-3 m/px = **0.69 m/s²**.
  - Using 81.5 px for the diameter gives 0.684.
  - Using the late-window fit gives about 0.63.

## Checks
- The straight-line image distance from the start, instead of the along-ramp coordinate, gives the same 580 px/s².
- Physical sanity check: the slope is about 26°, where frictionless sliding would give 4.3 m/s². The measured
  0.69 m/s² implies a friction coefficient of about 0.41, which is plausible.
- Confidence: moderate, roughly ±7%. The main uncertainties are which fit window to use and the exact edge of the
  diameter.
