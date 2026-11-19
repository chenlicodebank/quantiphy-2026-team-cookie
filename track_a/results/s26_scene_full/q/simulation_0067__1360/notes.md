# Q1360 — height of the purple car (m)

Answer: **1.46 m**. The file is 24 fps and question_fps is 24, so no time conversion was needed.

## Object
The purple car is the parked classic sedan (W123-like) on the far side of the intersection, facing left. It is
static. Measured on frames 0 and 70:
- near-side tyre bottoms: front (1332,334), rear (1417,311)
- roof top silhouette at y = 240.7 (x ≈ 1365)
- near roof edge (top of the side windows) at y ≈ 258
- bumper extremes at x 1253 and 1451

## Camera (3D, static)
- Vertical vanishing point from 9 poles, fitted in code (`vvp.py`): (1072, 2645), stable to ±15 px when any one pole is left out.
- Ground vanishing points (east-west road (2697,-43), diagonal road (110,-47)) give the horizon y ≈ -45.
- Principal point at the image centre. The orthogonality relations give f = 1114 / 1108 / 1110 → **f = 1110 px**.
- Ground normal from the horizon. Camera height h = 7.07 m, from the pedestrian: pelvis = bbox centre at the given
  depths (t = 0.58 s and 1.58 s), feet = bbox bottom (`geom.py`).
- **Check against the prior:** I tracked the van's rear tyre–ground contact frame by frame (frames 14-60, template
  matching, `wheeltrack.py`) and projected it onto the ground plane (`wheel_accel.py`). Its fitted acceleration is
  **4.00 m/s²** (3.99-4.04 over different frame windows). The prior is 4 m/s², so the metric scale is confirmed
  within about 1 %.
- The van's given depths could not be reproduced with an origin at the van's box centre: the fitted origin
  comes out below the ground. So the van's origin is probably not at its geometric centre. This does not affect the
  ground-plane scale, which the acceleration check confirms.

## Height
- The purple car's near-side tyre contacts are projected onto the ground plane, which fixes the car's axis.
  Wheelbase = 2.835 m.
- Route 1 (`purple_h2.py`): the near roof edge (y = 258) lies in the vertical side plane, 0.1-0.2 m inboard of the
  tyre line. Its height is 1.41-1.45 m. The roof crown adds about 0.03-0.06 m, giving H ≈ 1.45-1.50.
- The top silhouette (y = 240.7) is consistent with a roof about 1 m wide at the same height.
- Sensitivity: about 47 px per vertical metre at the car. One metre of lateral offset moves the image only 9 px
  vertically. f ± 30 px changes the result by about ±2 %.
- Route 2 (proportions): the measured wheelbase is 2.835 m and the length 4.4-4.6 m (`purple_len.py`). A W123 is
  2.795 m wheelbase, 4.725 m long and 1.438 m high, so scale 0.96-1.01 gives H ≈ 1.39-1.46.
- Final answer 1.46 m. Confidence: moderate (about ±5 %). The main uncertainties are the roof crown and the exact
  roof edge and contact pixels.
