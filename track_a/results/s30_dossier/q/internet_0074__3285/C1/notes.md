# q3285: distance ball to net at 1.00 s

## Time base
The file runs at 23.976 fps and the question at 30 fps. The file was made from 30 fps footage by dropping every 5th
frame (scene notes: every 4th step is twice as long), so file frame i = source frame i + floor(i/4). t = 1.00 s at
30 fps is source frame 30, which is file frame 24. File time 1.00 s x 23.976 also gives frame 24, so both readings
agree.

## Measurements (measure.py, frames 23-25)
- Ball centroid (yellow mask) at frame 24: (818.5, 1801.1). This matches scene/tracks/ball.csv (818.6, 1800.6).
- Net tape (the bright row) next to the ball at x = 818: y = 1315.1. The tape is nearly level (1313 to 1317.5
  across the court), and in the frame image it sits at y about 1315.
- Pixel distance: ball to net, perpendicular, is 1801.1 - 1315.1 = 486 px. The ball's x is inside the court, so
  this equals the distance to the net line.
- Scale from the prior (court width 6.1 m = 20 ft, measured to the outer edges of the lines): at frame 24 the
  sideline centres are 904.4 px apart (court_lines_per_frame.csv). The lines are about 8.5 px wide, which makes
  ~913 px outer to outer; my own threshold gave 907 centre to centre and 916 outer. I used 910 px, which gives
  0.006703 m/px.
- Distance = 486 x 0.006703 = **3.26 m**. Across scale choices of 904-916 px the result is 3.24-3.28 m.

## Check
Same scale applied to the near kitchen depth (1628.5 - 1315 = 313.5 px) gives 2.10 m, against the regulation
2.13 m (7 ft). That supports the scale and the net position. The ball is about 1.1 m past the kitchen line on the
near side, after the serve. Frames 23 and 25 give 570 / 445 px (3.82 / 2.98 m), which shows the answer depends
on the frame chosen; both time bases point to frame 24.

## Caveat
The ball is in the air, and its image is the ball seen from almost straight above. Following the annotators'
planar convention, no correction for height is applied. Confidence: good (about ±3%).
