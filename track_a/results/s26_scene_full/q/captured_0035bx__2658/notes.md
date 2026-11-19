# q_2658: basketball velocity at 0.9 s (cm/s)

The file runs at 24 fps and question_fps is also 24, so t = 0.9 s is frame round(21.6) = 22.

## Method (lab method card)
- Focal length f = 0.5959 x 1280 = 762.8 px. Principal point (640, 360).
- Ball centre: my own HSV orange mask, filled to its convex hull, centroid taken (`measure.py`). It matches scene/tracks/basketball_orange.csv to within about 1 px in frames 12-35.
- Depth: 2.7777 m at frame 22 (given). The two 1.4 s lines in depth_info are both labelled "soccer_ball". The basketball's apparent size grows from 63.2 px to about 67.5 px between frames 22 and 34. That predicts Z(f34) = 2.574 m, so the 2.602 m value belongs to the basketball, and I used it as the basketball's depth at frame 34.
- Size check: the area-equivalent diameter at frame 22 is 63.2 px. With Z = 2.7777 m this gives 23.0 cm, against the 23.2 cm prior.
- Back-projection: P = ((u-cx)/f, (v-cy)/f, 1) x Z(t). The velocity is a linear fit of P over a window centred on frame 22 (`velocity.py`).

## Results
- Depth model 1, Z linear between 2.7777 and 2.602 m:
  - Fit windows 17-27, 18-26, 19-25 and 20-24 give |v| = 126.3, 126.2, 125.2 and 125.5 cm/s.
  - Mean of the forward differences over frames 20-24 is 125.3 cm/s.
- Depth model 2 (second route), Z from the ball's apparent size: 125.8 to 127.7 cm/s.
- The velocity vector is about (-100, +67, -35) cm/s in camera coordinates.
- The ball-to-ball contact at frame 25 is at the edge of the windows. The windows that stop before it (20-24) agree.

Answer: **125.5 cm/s**. Confidence: high, within about ±5%.
