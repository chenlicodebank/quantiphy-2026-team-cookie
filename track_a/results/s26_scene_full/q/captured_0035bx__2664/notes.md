# q 2664 — soccer ball velocity at t = 1.3 s (cm/s)

Time base: question_fps = 24, same as the file's rate. t = 1.3 s → frame 31. Depth times: 0.9 s → frame 22, 1.4 s → frame 34.

## Depth labels
The depth_info labels both 1.4 s values as the soccer ball (2.6020 and 2.373). One of them must be the basketball.
- Ground-plane test (plane.py). Fitting a plane through the four ball centres:
  - soccer = 2.602: the plane needs about 40° of camera roll. The frame shows the far person standing upright, so this is not plausible.
  - soccer = 2.373, basketball = 2.602: the plane has about 7° roll, a 56° downward tilt and a 1.66 m camera height. Plausible.
- Size check. Basketball (23.2 cm) at 2.602 m should be 68 px across. I measured about 71 px. At frame 22 it is 68 px measured against 63.7 px expected, so the halo ratio is about the same. 2.373 m would need 74.6 px.

→ Used: soccer 2.477 m (frame 22) and 2.373 m (frame 34).

## Measurement
- measure.py: I re-measured the soccer ball centres for frames 18–47. Method: foreground below 248 with orange excluded, then convex hull, then a least-squares circle centre plus the bbox centre. Overlay at frames/chk31.png. My centres agree with scene/ to within about 1–2 px.
- velocity.py: back-projection with f = 763, c = (640, 360). Depth per frame comes from two routes:
  - (a) linear interpolation of the given soccer depths between frames 22 and 34
  - (b) ray intersection with the ball-centre plane, which reproduces 2.460 and 2.389 m
- Per-frame differences are noisy (±2 px), so I smoothed over 5–7 frames around frame 31:
  - chord 29→33: 52.3 (a) / 54.6 (b)
  - chord 28→34: 51.3 / 53.9
  - linear fit 28–34: 52.0 / 54.4
  - with bbox centres: 49–53
- Second route: pixel speed after the collision is a steady ~6.2 px/frame over frames 28–47, allowing for the dropped frame at 35→36. At about 2.41 m that is ≈ 47 cm/s laterally, plus the depth component, giving ≈ 50–55 cm/s.
- Frames 35→36 (likely dropped capture frame) and the collision at frames 24–27 are outside the window.

Answer: 53 cm/s. Confidence: moderate (±10%). The main uncertainties are centre noise and the per-frame depth.
