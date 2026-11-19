# q_2622 — basketball speed at t = 0.6 s (cm/s)

File fps = question fps = 24, so t = 0.6 s is frame 14. The basketball is in free flight over frames 12-18: the foot leaves it at frame 11/12 (frames are probably dropped between 11 and 12), and it hits the soccer ball between frames 19 and 20.

## Method (scripts: measure.py, velocity.py; visual check: view.py -> frames/sheet12_19.png)
- I re-measured the ball centre and diameter with an HSV orange mask and an ellipse fit. They agree with the scene/ record to within about 1 px.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depth: the camera distance is taken as K / pixel diameter, with K calibrated so that the distance at frame 14 is 2.27 m (depth_info). The last depth_info line ("t=1.6s, distance_soccer_ball_camera = 2.4120 m") is taken to be the basketball, mislabelled, because the line above it already gives the soccer ball at 1.6 s.
  - Check: K over the after-collision diameter (~69.5 px at frames 30-40) predicts 2.40-2.43 m at frame 38, against 2.412 given. So the depth-from-size model reproduces the second given distance.
- The ball shrinks from about 74.8 to 69.5 px between frames 12 and 18, so it moves away from the camera by about 0.19 m over 6 frames. Its pixel step is about 18.4 px per frame (up-left).
- 3D centre = unit ray(u, v) x distance. Velocity = linear fit of the 3D positions over a window around frame 14, inside the free flight only (frames 12-18).

## Results (|v| in cm/s)
| diameter used | smoothed depth, window 12-16 / 12-18 / 13-17 | raw depth, window 12-18 |
|---|---|---|
| minor axis | 152 / 154 / 154 | 155 |
| area-equivalent | 145 / 146 / 145 | 147 |
| scene fit_diam | 146 / 147 / 147 | 148 |

- Lateral (image-plane) part: about 108 cm/s.
- Depth part: about 95-110 cm/s. Its sign and size are confirmed by the change of the given distance from 2.27 to 2.41 m, which is already reached by frame 17-18.

## Answer
148 cm/s (range of routes 145-155).

## Confidence
Moderate. The depth part comes from the change in ball size; the reference probably used per-frame sensor depth. The routes spread by about 5%.
