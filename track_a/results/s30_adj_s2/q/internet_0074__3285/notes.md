# q3285: ball-to-net distance at 1.00 s

## Where the earlier answers split
- C1 (3.26 m) used file frame 24. Its reasoning was that the file is 30 fps footage with every 5th frame dropped,
  so source frame 30 = file frame 24.
- C2 (1.47 m) used frame 30 = round(1.00 x question_fps 30). It measured the straight-line distance to the
  net's *centre point* (789.9, 1305.5) and then averaged that with the distance to the net line.
- The rules give the time base: time t means frame round(t x question_fps) = **frame 30**, also when the file's
  rate is different. The file runs at 23.976 fps, and frame 30 is file time 1.25 s. So C1 used the wrong frame.
- The net is a line across the court, so "distance to the net" is the perpendicular distance from the ball to the
  net line. A distance to the net's midpoint (C2) adds the sideways offset, which does not belong in it.

## Measurement (measure.py, frames 29-31)
- Ball centroid at frame 30: (875.0, 1510.6). This matches scene/tracks/ball.csv, and a crop with the point drawn
  on it (frames/f30_crop.png) confirms it.
- Net tape (the bright row) at x = 875: y = 1315.9. The tape is nearly level, y 1313 to 1318 across the court.
- Perpendicular pixel distance: 1510.6 - 1315.9 = 194.7 px.
- Scale (one factor from the prior, the court width 6.1 m = 20 ft): sideline outer edges at row 1510 are
  x = 333 and 1249, which is 916 px apart. Line centres are 908 px apart. I used 912 px, which gives
  0.006689 m/px.
- Distance = 194.7 x 0.006689 = **1.30 m**. The 908-916 px scale range gives 1.297-1.308 m.

## Checks
- The same scale on the near kitchen depth (1628.9 - 1316 = 313 px) gives 2.09 m, against the regulation 2.13 m.
- Frames 29 and 31 give 235.6 and 154.6 px (1.58 and 1.03 m), so the answer depends on the frame chosen.
- The ball is in the air. Following the annotators' planar convention, no height correction is applied.

I agree with C2 on the frame and disagree with its net reference point. Confidence: good, provided that
"frame 30" is the reference's frame.
