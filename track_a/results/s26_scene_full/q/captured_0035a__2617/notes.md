# q_2617 – soccer ball speed at t = 1.5 s (frame 36), cm/s

File fps = question_fps = 24, so t = 1.5 s is frame 36. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## depth_info
- The fourth line is labelled "soccer_ball" again, but it must be the basketball (2.412 m): the soccer ball rolls back
  toward person_A, who is far away (3.052 m), and the basketball rolls slowly away from the camera (2.27 -> 2.41 m).
  Pixel sizes agree: the basketball diameter goes from 74.4 px to 71.5 px, and the soccer ball shrinks with depth.
- Soccer: 2.758 m at frame 14 and 3.052 m at frame 38. Basketball: 2.270 m at frame 14 and 2.412 m at frame 38.

## Method
1. Track: the record's RANSAC centres, checked by my own re-track (track2.py: a bright-or-dark mask in a local crop,
   then the hull's ellipse or bbox centre). The two tracks agree to about 2-3 px. My mask includes a little of the
   shadow, which gives a constant offset of about +2.5 px in y. That offset does not affect the speed.
2. 3D positions: I back-projected the 4 depth points and fitted a floor-parallel plane through them. The residuals
   are at most 1.6 cm. Then I intersected each frame's ray with that plane, put through the soccer-ball points
   (vel.py, vel2.py). This reproduces the given distances: 2.737 m at frame 14 (given 2.758) and 3.076 m at frame 38
   (given 3.052).
   - I did not interpolate the depth linearly in time. The ball comes nearer before the collision at frame 20 and
     then goes back, so a straight line in time is wrong and gives too low a speed (about 55 cm/s).
3. Speed: frame-to-frame 3D displacement x 24, smoothed over 5 or more frames around frame 36. There is a known
   jump between frames 35 and 36 (a suspected dropped frame): one step is about 2x the others. It is left in, as in
   the reference convention.

## Results (cm/s)
| track | 5-frame centred mean (forward diff.) | 5-frame backward mean | 7-frame mean | quadratic fit, frames 30-42 | quadratic fit, frames 26-46 |
|---|---|---|---|---|---|
| my re-track, ellipse centre | 76.5 | 76.3 | 74.5 | 72.2 | 71.9 |
| my re-track, bbox centre | 79.7 | 76.6 | 75.2 | 72.9 | 71.6 |
| scene record | 83.2 | 80.9 | 76.1 | 73.8 | 72.3 |

## Second route
vel_line.py uses only the soccer ball. It puts a 3D line through the two soccer depth points and finds the closest
point on that line for each ray. The speeds are almost the same: 81 cm/s for the 5-frame window 34-38 and 69 cm/s
for frames 31-41.

## Answer
76.5 cm/s.

Confidence: moderate. The likely range is 72-83 cm/s, depending on the smoothing window and how the dropped-frame
jump is handled.
