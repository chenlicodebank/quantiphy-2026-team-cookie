# q1319 – width of the lane (main road, curb to curb)

Answer: **11.64 m**

The file and the question are both 24 fps. Frame 14 is t=0.58 s and frame 38 is t=1.58 s.

## Geometry (static camera, roll ≈ 0, principal point (1080,540))
- **Curbs** (`curbs.py`, frame 71, grey-asphalt boundary): left curb x = 653.4 − 0.799·y, right curb x = 920.9 + 0.582·y.
  The near and far curb segments lie on one line (fit residuals < 3 px). They meet at the road VP (808, −194), which
  gives the horizon at y = −194. The scene record's −208 was slightly off. With −194 the two back-projected curbs come
  out parallel on the ground (0.01°; with −208 they are 0.5° apart).
- **Focal length** (`poles.py`): 6 vertical poles converge at (1075, 6899), with x close to the image centre.
  f² = (cy − y_horizon)(vy − cy) gives **f ≈ 2160 px** (HFOV 53°). This route does not use any depth.
- **Camera height from the prior** (`refine.py`): I projected the van's rear tyre contact point onto the ground plane
  (in units of camera height). A quadratic fit over all 72 frames gives a = 0.4975 h/s², so a = 4 m/s² means **h = 8.04 m**.
  The roof-top track is cleaner: its speed increments every 8 frames are constant, so the acceleration really is uniform.
  It gives a van height of 2.10 m, which is realistic.
- **Width** (`width.py`): back-project both curb lines onto the ground and take the perpendicular distance.
  W/h = 1.448, so **W = 11.64 m**.

## Checks (`check.py`, f = 2160, h = 8.04)
- Pedestrian: height from head to lowest foot is 1.71 / 1.74 m. The pelvis (0.95 m above the foot) is 25.22 / 25.70 m
  from the camera; the given distances are 25.36 / 25.92 m (within 1%).
- Taxi side-on (frames 62–71): 5.45–5.51 m long, about a real Crown Victoria (5.4 m). Scaling to the taxi instead gives about 11.4 m.
- Cyclist ground point: 25.81 / 31.17 m vs the given 25.34 / 30.43 m (2% far; the bike's origin is probably above the
  ground). Speed is 5.6 m/s.
- Van: the depth-matched origin sits 1.6–2.1 m ahead of the rear contact point and stays consistent over time.
  The rear body is about 2.2 m wide.
- Sensitivity (`sens.py`): W changes roughly as 1/f, giving 12.03 m at f = 2080 and 11.28 m at f = 2240. The pole
  estimates span f ≈ 2105–2180, so W ≈ 11.5–11.9 m.

Confidence: good, ±4%.
