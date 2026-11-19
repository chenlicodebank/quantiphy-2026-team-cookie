# q_693 — acceleration of the moving chess piece at t = 1 s

The video and the question both run at 24 fps, so t = 1 s is frame 24. This is a 2D video: the piece slides down a
tilted board, and that motion lies in the image plane.

## Object
The scene record calls the moving object a "soap block". It is the Chinese chess piece: a cream disc that lies flat
on the tilted board. Seen from the side, its extent along the slope is its diameter. The prior is diameter = 0.097 m.

## Scale (prior)
- `length_rot.py` rotates crops so the slope is horizontal and measures the extent along the slope against a
  background frame. I did this on 10 frames between 0 and 36.
  - At thresholds 45 and 70, the row maximum is 79-81 px. The row median is about 79 px (78 px at threshold 70).
  - Checked by eye on a zoom (`frames/rot_16.png`): the edges are at x ≈ 21 and 100, so the length is about 80 px.
- I used **L = 80.5 px**, which gives a scale of 0.097 / 80.5 = 1.205e-3 m/px.
- The scene record gives 81.5 px, about 1.2 pct more. Its background mask probably takes in a little of the shadow
  at the lower edge.
- SAM 3 ("white disc") gives a length of 89-100 px, which is more than 3 pct too large. Its overlay and my zoom
  (`check_mask.py` -> `frames/chk_16.png`) show why: the mask includes the grey shadow below and to the lower left
  of the piece. So the SAM length is wrong, and my measurement of about 80 px is right. SAM's centroids sit about
  2 px lower than mine for the same reason, but they move the same way.

## Motion
- The scene record found duplicate and skipped frames, and I confirmed them: frames 6, 13, 25, 28, 35 and 38 are
  identical to the frame before. Single-frame differences of the file frames are therefore spiky (for example,
  frame 25 shows zero speed).
- The piece accelerates uniformly. I fitted a quadratic to the position along the slope against the corrected
  source-frame index (`source_frame_est` / 24), leaving out the duplicates.
  - Scene track, frames 3-38: 579.6 px/s², fit residual 0.8 px rms.
  - My centroid track (`measure2.py` -> `my_track.csv`), frames 3-38: 583.4 px/s², residual 0.4 px rms.
  - Sub-windows (3-20, 14-34, 18-30, 20-38) give 550-602 px/s². A linear fit to the speed gives 576 px/s².
- Second route: a quadratic through the SAM 3 mask centroids (`sam_fit.py`) gives 577.7 px/s², or 0.696 m/s².
- The fitted start time is t0 ≈ 0.3 frames, which is consistent with the piece being at rest in frames 0-1.
- Result: a ≈ 580 px/s² × 1.205e-3 m/px = **0.70 m/s²**. This is constant, so it is also the value at t = 1 s.

## Confidence
The uncertainty is about ±3 pct. It comes from the measured length (±1 px) and the spread of the fits (±2 pct). If
the length were 81.5 px, the answer would be 0.69.
