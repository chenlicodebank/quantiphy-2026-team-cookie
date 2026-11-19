# q3197: velocity of the acorn at 1.40 s (prior: g = 9.8 m/s^2)

## Interpretation
- The phone video is rotated: gravity points along image **+x**. Evidence: after release (frame 39) the toy speeds up in +x at a
  steady ~35-45 px/frame^2 until it hits the backrest at frame 45 (here the backrest is the "floor"). The rebound (46-57) is a parabola
  in x (it reverses at frame 52) with the same ~37 px/frame^2, while its y velocity stays roughly constant.
- Time base: question_fps is 30 and the file runs at 30.013 fps. Either way, t = 1.40 s is frame 42, and the 0.04% difference doesn't matter.
  Frame 42 falls inside the free-flight window, frames 39-44.

## Measurement (`capedge.py`, `fit.py`)
- Reference point: the sharp vertical boundary between the black cap and the white dome. For each frame it is the strongest
  dark-to-bright step, taken as the median over about 60 rows (IQR ±2 to ±8 px). x for frames 38-44 = 256, 290, 374, 500, 669, 873, 1108.5.
- Per-frame steps: 34, 84, 126, 169, **204 (42→43)**, 235.5 px. The y drift is about 5 px/frame, which is negligible.
- Second differences: 50 (includes the hand push), 42, 43, 35, 31.5. The pixel acceleration falls slowly because the toy moves away
  from the camera; its apparent size shrinks about 4% per frame.
- Pixel g estimates: mean of the 2nd differences for frames 40-43 = 37.9; quadratic fit over 39-44 = 38.2; fit over 40-44 = 36.3.
  The rebound parabola gives 37.9 (dome centroid, frames 48-56).
  Adopted value: a = 37.5 px/frame^2, i.e. 37.5 × 900 = 33750 px/s^2.
- Single scale: 9.8 / 33750 = 2.90e-4 m/px.
- Velocity at frame 42 (forward difference): about 205 px/frame. The cap edge gives 204; the record centre gives 208.5 (2D).
  205 px/frame × 30 = 6150 px/s, and 6150 × 2.90e-4 = **1.79 m/s**.

## Checks
- The rebound gives an independent pixel g (37.9) that matches the flight value, which supports the scale.
- The scene record's centre track (cx) gives 1.75-1.97 m/s depending on the fit window. The cap-edge track gives 1.71-1.90 m/s.
- Sanity check: the toy is 279 px ≈ 8 cm long, and the drop height is about 0.3 m. Both are plausible.
- Confidence: moderate, about ±7%. The main uncertainty is which pixel acceleration the annotators used, because perspective
  makes it vary from 31 to 43 px/frame^2.
