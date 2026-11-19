# Q1366 – width of the turning yellow car (taxi), simulation_0074

Answer: **2.0 m** (the body width; the car's shorter horizontal bounding-box extent). Confidence: moderate, about ±7%.

File fps = question fps = 24, so frame numbers and times agree. Object = `taxi` in scene/ (a yellow Crown-Victoria-type
sedan that turns about 90° left, from heading -90° at f0 to about -2° at f71).

## Camera (fixed)
- Two vanishing points from 8 kerb lines fitted on the sidewalk mask (`vp.py`): vA = (-1305,-260), vB = (2686,-260).
  The horizon is y = -260 (no roll). Assuming orthogonal roads, f = 1786 px.
- Independent check (`poles.py`): the vertical vanishing point from 7 lamp and signal poles gives f = 1792, with its
  x at 1073, close to cx. **So f ≈ 1790 px and pitch is 24.1°.**
- Camera height from depth_info (`cam.py`, `pedcheck.py`):
  - Taxi, van and cyclist centres at the given depths sit about 8.3–8.9 m below the camera. That fits origins at the
    object centres.
  - Feet-on-ground plus pelvis-at-depth for the pedestrian gives H ≈ 9.63–9.66 m.
  - The taxi silhouette fit gives 9.6 m and the rescaled van fit 9.65 m.
  - **I used H = 9.63 m.**
- Check against the prior: the van's wheelbase from its tire contacts at f71 is 3.74 m, lying along the road. That
  fits a van about 6 m long (the prior), so depth_info and the prior agree on the scale.

## Taxi measurements (metric via H = 9.63)
- Heading from the car's own body-line vanishing points on the horizon (`bodylines*.py`): f2 -91°, f10 -84°,
  f38 -24°, f54 -5°, f66 -3°. These agree with the silhouette-fit headings.
  - The roof-sign track with a turning correction (`heading.py`) disagreed and was rejected.
- Wheelbase from the near-side tire contacts at f34 (zoom picks): **2.98 ± 0.05 m**.
- Tire diameter is about 0.70–0.75 m.
- Convex-hull silhouette fits (box + cabin + wheels, `fit*.py`) match to 2–4 px, but width is degenerate there:
  - In this oblique top-down view, width trades almost freely against body heights and heading.
  - The fits gave W of only 1.39–1.43 m. On the overlays the model's front face is visibly narrower than the real
    one, so I rejected this value.
  - The same fits gave L ≈ 5.2 m (likely a little low; the van came out 5.6 m against 6 m).
- End-face corner pairs, back-projected (`facewidth.py`, `decomp.py`), solved under two assumptions:

  | Pair | Equal-height | Flat end face |
  |---|---|---|
  | Front body corners, f2 | 1.72 | 2.07 |
  | Front body corners, f10 | 1.47 | 2.16 |
  | Rear bumper corners, f66 | 1.86 | 2.29 |
  | Rear bumper corners, f70 | 1.93 | 2.34 |

  - The truth lies between the two columns, because the corners are rounded.
  - The front of this car tapers, so the front values are below the full width.
  - Bracket: about 1.85–2.2 m.

## Answer and second route
- Route 1 (direct): the rear-bumper corners at equal height give 1.86–1.93 m, a lower bound near full width.
- Route 2 (proportions): the taxi is clearly a Crown Victoria (real wheelbase 2.91 m, body width 1.99 m).
  - The measured wheelbase of 2.98 m means a scale of 1.02, so W ≈ 2.03 m.
  - L ≈ 5.2–5.4 m combined with the model's W/L of 0.37 gives 1.92–2.0 m.
- Final: **W = 2.0 m**.
- If the mesh bounding box includes the side mirrors, the true value could be about 2.1–2.2 m. The mirrors here look
  small and could not be measured: the near one is barely visible and the far one is poorly conditioned in height.
