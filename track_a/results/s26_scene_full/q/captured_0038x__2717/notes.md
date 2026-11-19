# q_2717 – displacement of the white ball, 0.9 s to 1.4 s (cm)

The file rate and question_fps are both 24, so the frames are round(0.9*24) = 22 and round(1.4*24) = 34.
Camera: f = 0.5959*1280 = 763 px, principal point (640,360).

## Ball centres (scene/tracks/ball.csv, checked)
- Frame 22: (527.7, 497.0), template-match score 0.985.
- Frame 34: (722.7, 504.0). The ball is over the white cards here, so the edges are less reliable. The x value
  fits the steady ~16.3 px/frame steps between frames 29 and 35, and y fits the trend (503 to 505).
- I checked frame 34 by eye (frames/f34.png).

## Depth
- At 1.4 s, depth_info gives 0.716 m, so Z1 = 0.6996 m.
- No depth is given at 0.9 s. To get one, I used the table as a ground plane.
  - The camera is about level, with the horizon near cy. Under this model, v - cy = f*h/Z.
  - The given depths of three objects resting on the table give a consistent camera height above the table:
    bottle h = 0.154, cup h = 0.154, credit card h = 0.159 m.
  - The ball centre at 1.4 s comes out 0.132 m below the camera. That is about 2.2 cm above the table, which
    matches a 4 cm ball, so the model holds together.
- From this, Z0 = Z1*(504-360)/(497-360) = 0.735 m, and the camera distance at 0.9 s is about 0.755 m.

## Result
- Ground-plane model, horizon offset 0 to 20 px: 18.61 to 18.76 cm.
- Second route, assuming constant depth (same Z or same distance at both times): 17.87 to 17.90 cm. This is a
  lower bound, because it ignores the ~3.5 cm approach toward the camera.
- A free 4-point plane fit (1/Z linear in u, v) was poorly conditioned (residuals 1-2.5 cm) and gave 20.8 cm,
  so I rejected it.
- Answer: **18.6 cm**. Confidence is moderate: the spread between routes is about ±4 %, and it comes mainly
  from the depth at 0.9 s.

Scripts: measure.py, level.py.
