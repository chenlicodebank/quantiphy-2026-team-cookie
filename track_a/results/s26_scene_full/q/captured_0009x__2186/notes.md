# Q2186 – basketball's initial distance from the floor (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640,360).
Prior: a = 9.8 m/s^2. depth_info: ball 1.3210 m at t=0, floor 2.0285 m at t=0, ball 1.5835 m at f43, 1.5795 m at f46 (apex).

## Record check
scene/tracks/basketball.csv checked against a contact sheet: right object, held f0-26, release ~f27, bounce ~f37, apex f46.
Track centres used as is. Step f35->f36 is ~2x neighbours -> dropped frame in recording (confirmed: the fit with one
missing frame has rms ~2 px; without it 10 px).

## Method
- P0 = back-projection of ball centre at f0 (483.1,186.4) with depth 1.321 m -> (-0.260,-0.287,1.263) m.
- Camera is tilted strongly down (ball shrinks 136 -> 93 px while falling). Joint 3D fit (jointfit.py / jointfit2.py):
  fall from rest from the held position (release time free, dropped frame after f35) + rebound parabola f38-48
  constrained by the given depths at f43/f46, shared gravity vector |g| = 9.8 with unknown tilt/roll, fitted to pixel
  centres. Tilt ~32-36 deg, roll ~1 deg, rms 2-3 px. Bounce = where fall and rebound parabolas meet (~f37).
- Ball radius from depths + pixel diameters (f0, f43, f46): D ~ 0.221 m, R ~ 0.111 m.

## Results (centre height above floor)
- Route 1 (dynamics): (bounce centre - P0)·g_hat + R = 1.204 - 1.285 m over fit variants.
- Route 2 (floor depth): floor contact point = model contact pixel (~553,704) back-projected at the given floor depth
  2.0285 m; |P0 - C| = 1.225 - 1.261 m (vertical component 1.216 - 1.256). Model |C| = 2.01-2.08 m vs given 2.0285: consistent.
- Route 3 (floor point straight below P0 at 2.0285 m): 1.11-1.18 m (sensitive to tilt; the contact point is slightly
  offset horizontally, so this is a lower bound-ish variant).
Answer: centre of ball ~1.24 m above floor -> **124 cm**. (If "distance" meant the ball's bottom: ~113 cm.)
Confidence: moderate (±5 %); main uncertainty is the camera tilt and the floor reference point.
