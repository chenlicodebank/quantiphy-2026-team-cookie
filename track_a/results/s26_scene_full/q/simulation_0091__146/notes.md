# q146: speed of the big bird (eagle) at 0.3 s, prior: small bird (crow) speed = 11 m/s

2D scene, fps 24 (file and question agree). t = 0.3 s -> frame round(7.2) = 7; speed = |p7 - p6| x fps.

## Scale (from the prior)
The crow flies right at a constant speed. From frame 1 to frame 10 (9 steps, all frames uncut):
- scene record: body_cx 1154.0 -> 1859.0 = 78.33 px/frame; centroid 78.4 px/frame
- my own mask (measure.py, threshold 30): right edge 1199 -> 1904 = 78.33, left edge 1108 -> 1814 = 78.44
-> crow speed 78.4 px/frame, so 11 m/s = 78.4 px/frame, i.e. 11 / (78.4 x 24) = 0.005846 m/px.

## Eagle at frame 7
The beak (left edge) leaves the frame at frame 7, so I used the tail (right edge) as the moving reference instead:
817, 689, 560, 432, 304, 176, 48 (frames 1..7) -> steps of 128, 129, 128, 128, 128, 128 px/frame. The step from
frame 6 to 7 is 128 px/frame. The record's body_cx steps (128-128.5) agree. The dy is about 0.

## Answer
11 x 128 / 78.4 = 17.96 m/s.

Second route: the eagle's mean speed over frames 2-6 from body_cx is (742.5-105)/5 = 127.5 px/frame,
which gives 17.9 m/s. Confidence high (about 2%); both birds fly at a constant speed in the same plane.
