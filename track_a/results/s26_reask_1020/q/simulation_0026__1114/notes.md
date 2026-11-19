# Q1114 – length of the boat (simulation_0026)

File fps 25, question_fps 24: t=1 s -> frame 24, t=2 s -> frame 48 (frame indices used, scene/ seconds ignored).

## Scale (focal length)
- Person (prior 1.75 m) head-to-feet height measured at 53-55 px around t=1 s (scene/tracks/person.csv, checked on
  zoomed frames: head top y~530, feet y~583.5 at frame 24). Depth 114.83 m (constant, and the body's apparent size
  does not change much, so the body stays near that depth). f = 54 x 114.83 / 1.75 = 3543 px (range 3478-3609
  for 53-55 px). HFOV about 15.5 deg.

## Boat orientation (key point)
- The boat is NOT side-on. 3D positions of the hull centre from the given depths (103.157 m at t=1, 106.091 m
  at t=2) + rays give a velocity of (-2.85, -0.03, +2.77) m/s: it moves left AND away, 44 deg from the image plane
  (geom.py, vp.py). Its apparent scale falls exactly as the depth ratio does (0.971 vs 0.972).
- Checks that the heading equals this motion direction (bow first, bow pointing away):
  * the wheelhouse shows a lit side face (39 px) AND a shaded aft face with a door (37 px), and the stern transom
    is visible. With theta=44 deg both wheelhouse faces come out about 1.55 m (a squarish house); with a small yaw
    the aft face would be an impossible 4 m wide.
  * vanishing point: the boot-stripe line on the hull has slope 0.052 (rms 0.23 px, lines.py). With the horizon at
    v~448 (the row the boat's points converge to as it recedes, vp.py) that puts the hull's vanishing point at a
    yaw of about 51 deg (sheer probably biases it high). The motion's vanishing point is at u=-3165, v=444.
    Both routes give a large yaw, so I used 44 deg from the motion.

## Length
- Bow tip and stern extremes from a background-difference mask (ends.py), plus the transom's near edge, at frames
  24, 36, 48 and 60. I solved for the points on the boat's centreline in the X-Z plane, with heading theta and the
  centre at the hull-centre pixel and its depth (length.py, length2.py).
- f=3543, theta=44.2: L = 10.06 / 10.09 / 10.09 / 10.14 m (frames 24/36/48/60), with a transom width of about 1.2 m.
- Sensitivity: f 3478 -> 10.3, f 3609 -> 9.9; theta 48 deg -> 10.9; theta 40 deg -> ~9.3.
- Naive side-on reading (no foreshortening): 249 px x 103.16 / 3543 = 7.25 m. This is rejected because of the
  visible yaw.

Answer: 10.1 m. Confidence is moderate: the result mostly depends on the yaw angle, which I estimate at ±4 deg
(about ±8 % in the length).
