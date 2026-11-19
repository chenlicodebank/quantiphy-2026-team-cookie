# Q1306: speed of the yellow car (taxi) at t = 2.5 s, in m/s. Answer: 4.2

The file rate and question_fps are both 24, so t = 2.5 s is frame 60. Speed = backward difference at frame 60 ≈ the derivative at frame 59.5.

## Focal length (3D scene, static camera; principal point taken as the image centre (1080, 540))
- The prior (van acceleration 4 m/s²) can't fix f, because the van drives almost straight at the camera.
- **Route A: vanishing points** (`poles.py`, `curbs.py`).
  - Horizon: I fitted the far-left curb (rms 1.1 px) and the near-right curb (rms 0.4 px). Their vanishing point is (1084, −122.4), so cy − horizon = 662.4 px.
  - Vertical vanishing point: the near signal poles tilt by dx/dy = +0.093 (left) and −0.115 (right). The two lines meet at (1085, 7537), so the vertical VP is 6997 px below cy.
  - f² = 662.4 × 6997, giving **f = 2153 px**. Both VPs have x ≈ 1085, which fits zero roll.
- **Route B: pedestrian** (`ped.py`). They walk along the cross street, which is parallel to the camera X axis, so Zcam stays constant (feet row is constant). Their x position at f14 is extrapolated from a linear fit to the walk (3.08 px/frame). The given range ratio 38.722 / 38.347 then gives **f = 2190 px**.
- I used f ≈ 2170 (the two routes agree within 1.7%).

## Taxi depth
- Ground normal comes from the horizon. The taxi root is the ground point under the car's centre. At f38 that is the midpoint of the near-wheel contacts (657, 362.5), shifted ~11 px into the scene for half the track width, giving (657, 351.5).
- With range 33.0077 m, Zcam38 = 32.28 m and camera height H ≈ 6.74 m.
- Check: van anchors (ground centre estimated) give H = 6.74 m (f14) and 6.58 m (f38). Consistent.
- At f60 the near wheels touch the ground at row ≈ 372, so the root row is ≈ 360. That gives Zcam60 ≈ 31.71 m.

## Taxi pixel motion (`taxi_track.py`)
- Background difference against frame 0. I took the body rows y 318–350 (above the ground shadow) and the largest run across the pole. The front and rear extents were checked on an overlay at f60.
- The midpoint moves 11.76–12.14 px/frame at f59.5, depending on the fit window (quadratic fit over f52–71: 11.91). Front edge: 12.2; rear edge: 11.6.
- The ground row drifts down by about 0.3 px/frame, a small approach component (<1% of the speed).

## Result (`speed.py`)
Lateral speed = du × Z / f × 24 = 4.14–4.21 m/s across f = 2190–2153. Adding the depth component gives **4.17–4.23 m/s**. Across the different fit windows the range is 4.15–4.28 m/s.

**Answer: 4.2 m/s.** Confidence: moderate-good (±4%). The main uncertainties are f (±1.7%), the taxi root's ground row (±1%) and the pixel rate (±2%).
