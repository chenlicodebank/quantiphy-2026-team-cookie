# q_2176 — basketball's initial height above the floor (cm)

File fps = question_fps = 24. Lab camera f = 763 px, principal point (640, 360). depth_info is the Euclidean distance (ray length).

Ball centre at t=0 (frame 0), from scene/tracks/ball.csv (circle fit, checked on frame): (482.5, 193.3) px, at 1.321 m
-> P0 = (-0.261, -0.276, 1.265) m. Floor distance at t=0: 2.0285 m, read as the floor point directly below the ball,
which is where the ball lands (bounce at frame 37, centre (547.5, 656.5), bottom y ~705).

Route 1 (solve.py): the ball falls vertically from P0. Unknowns: camera pitch, roll and height h. Constraints: the floor point
P0 + h*g lies 2.0285 m from the camera, and the centre P0 + (h - r)*g (r = 0.12 m) projects onto the frame-37 bounce centre.
Exact solution: pitch 28.5 deg, roll 2.6 deg, **h = 1.228 m**. The floor point projects to (552, 691), just above the ball's bottom
edge at the bounce, which fits.
Route 2 (fall.py): the prior is g = 9.8. Free-fall frames 32-37 are put on the vertical line through P0, with the scene record's
dropped capture frame between 35 and 36 included. The pitch that reproduces a = 9.8 is about 30 deg. That gives h = 1.27 m
(drop to the bounce centre plus r) or 1.20 m (from the floor depth). The two routes cross at about 28 deg, h = 1.23 m.
Without the dropped frame the fall gives a = 24 m/s^2, which is not physical. That supports the dropped frame.
Route 3: direct 3D distance from P0 to the back-projected bounce-contact pixel (547.5, 705) at 2.0285 m = 1.247 m.
Fall-time check: a 1.11 m drop takes 0.476 s = 11.4 frames. Release is at frame ~27 and contact at frame 37 + 1 dropped frame,
so this agrees.

Size-based depths do not fit the given depths well (the apparent diameters of 145 px held vs 112 px at the apex disagree by about 10%).
They were not used for scale.

Answer: ball centre height ≈ 1.23 m = **123 cm** (range of routes 120-127). Confidence: moderate (±4%).
If "distance" meant the ball's bottom surface, it would be about 111 cm.
