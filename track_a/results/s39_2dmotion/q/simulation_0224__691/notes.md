# q_691: acceleration of the moving chess piece at t = 0.5 s (m/s^2)

The prior is a Chinese chess piece diameter of 0.097 m. This is a 2D video at 24 fps, and the file fps equals
question_fps, so t = 0.5 s is frame 12.

## Object
The "soap-bar" block in the scene record is the Chinese chess piece: a disc lying flat on a tilted board and seen
nearly edge-on. It slides down-left along the board's channel at 25.9 deg in the image, and it is the only moving
object. Its extent along the slope is its diameter, because the slope direction lies in the image plane.

## Scale (diameter in pixels)
- `edges.py`: I rotated frames 0-33 so the slope is horizontal and took the position of the largest gradient at each
  end of the piece. Median 80 px (79-80 on every frame).
- `measure2.py`: a mask from the median background (with the shadow excluded) gives an along-slope extent of 79-80 px.
  It slightly misses the darker lower side (checked in `frames/m2_12.png` and `frames/m3_12.png`).
- Scene record: a principal-axis extent of 81.5 px (mean).
- SAM 3:
  - Frame 12, "white chess piece": 99.5 px.
  - Frame 20, "chess piece", tight box: 86.5 px.
  - Both differ from my measurement by more than 3 pct. The zoomed overlay `frames/samov_20.png` shows the SAM mask
    takes in the contact shadow at the lower left and a rim of background, so SAM is too large there. The visible
    piece runs about 1023 -> 1099 px, about 80 px along the slope.
- Adopted D = 80.5 px, so the scale is 0.097 / 80.5 = 1.205e-3 m/px.

## Motion
- The video has duplicate frames (6, 13, 25, 28, 35, 38) and skipped source frames (see scene notes). I checked the
  scene's `source_frame_est` re-indexing: against it the along-slope position is a clean quadratic, with an rms
  residual of 0.4-0.7 px, compared with 10 px against the raw frame index.
- `fit_accel.py` fits the along-slope position of the centroid (my track and the scene track) against
  source_frame_est / 24:
  - Quadratic fits over different windows give 578-605 px/s^2, which is 0.696-0.729 m/s^2.
  - A cubic fit evaluated at 0.5 s gives 0.68-0.72 m/s^2.
- Second route: a linear fit to the per-source-frame speeds over the whole slide gives 0.709 m/s^2. A local window of
  0.25-0.8 s gives 0.75 m/s^2, but it is noisier.
- The acceleration is essentially constant, as expected for sliding down an incline. I adopted a = 590 px/s^2, which
  gives **0.71 m/s^2**.

## Confidence
About ±3-4 pct. The spread comes from the fit window (±2 pct) and the pixel diameter (80-81.5 px, ±1 pct).
