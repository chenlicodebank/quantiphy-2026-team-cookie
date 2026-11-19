# q_2171 — basketball's initial distance from the desk (cm)

The file rate and question_fps are both 24 fps. f = 0.5959 x 1280 = 763 px, principal point (640, 360). The camera is static.

## Method
- I used the ball track from scene/tracks/ball.csv (circle-fit centre), checked against frames 0 and 30. The ball is held
  still in frames 0-20 at pixel (519.7, 96.9), r = 57.0 px. It is released at about frame 20.5 and first hits the desk at frame 30.
- I back-projected the depth_info points as 3D points: frame 24 (t = 1.0, 1.401 m), frame 29 (t = 1.2, 1.564 m) and frame 36 (apex, 1.5225 m).
- The initial ball depth is not given, so I estimated it in two ways:
  1. Line route: the ray at the rest pixel meets the fall line (the direction from P24 to P29) at d = 1.3855 m.
     The two lines pass within 2 mm of each other. On this line the ball has fallen 10.3 cm by frame 24, which matches free fall
     with g = 9.8 (the prior) from a release at frame 20.5 (10.4 cm expected).
  2. Size route: d is proportional to 1/r. This gives 1.378-1.43 m.
  Both routes agree, and using 1.401 m instead changes the distance by only 2 mm.
- Desk centre: I clicked the centre of the tabletop and back-projected it with 1.725 m. The 1.725 m depth puts the point
  about 0.2 m below the tabletop plane, so the desk origin is below the top surface. The answer depends on which pixel
  is clicked:
  diagonal intersection (589, 469) -> 0.808 m; tabletop centroid (597, 489) -> 0.844 m;
  visible desk centroid including leg (593, 508) -> 0.876 m.
- Vertical-only distance (along the fall direction) is almost the same as the 3D distance (0.806 m for the diagonal click).
- Another reading would place the ball at t = 1.0 (the time the depths are given), when it is already falling. That gives 0.705-0.772 m.
  I treated "initial" as the ball at rest at t = 0.

## Answer
The 3D distance from the ball centre at t = 0 to the desk centre is 0.81-0.88 m. I answer 82 cm,
leaning slightly toward the lower values to allow for the t = 1.0 reading.
Confidence: moderate. The main uncertainties are which pixel was clicked as the desk centre and which time "initial" refers to.
Scripts: geom.py, geom2.py, geom3.py, geom4.py.
