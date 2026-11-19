# q_1482 – width (wingspan) of the plane

Answer: **18.0 m** (width of an aircraft = wingspan, the across-body horizontal extent).

File fps = question fps = 24; t=1 s -> frame 24, t=2 s -> frame 48. Camera static (scene record).

## Focal length (solve_f.py, fit_traj.py)
- Hull-centroid positions back-projected with the given distances (102.67 m @ f24, 121.83 m @ f48, principal
  point at image centre); f chosen so |P48 - P24| = 22.16 m (1 s at constant speed): **f = 3429 px** (HFOV 40.9°).
  bbox / raw centroid as reference point: f = 3369 / 3342.
- Constant-velocity check: a uniform straight-line 3D motion fits the whole hull track (frames 3–71) with
  rms 2.3 px; at f=3429 the fitted speed is 22.12 m/s (prior 22.16). Perspective alone does not fix f (flat
  residual), so f comes from the speed prior; depth part of the motion (19.2 m/s) is well-determined, the lateral
  ~11 m/s carries the f uncertainty.
- Velocity in camera coords (-10.6, -6.3, 18.4) m/s: plane flies away/left; if flight is level the camera
  pitch is 18.8° down.

## Wingspan (wing2.py, wing.py)
- The plane is seen from behind/above, yawed: wings run lower-left -> upper-right in the image. Level-flight
  model (wing = v × up, camera without roll) predicts a wing image direction of -9.2° at f24; the observed
  tip-to-tip line is -7.5° → consistent.
- Wingtip pixels read from zoomed crops (f24: ~(1005,665) and (1560,592); f48: ~(735,490) and (1235,455)),
  rays intersected with the horizontal plane through the origin: span 17.8–18.5 m (f24), 17.2–18.2 m (f48).
- Second route: bbox width × z / f = 573×102.6/3429 = 17.2 m (f24), 509×121.1/3429 = 18.0 m (f48)
  (bbox width is the near-horizontal projection, partly foreshortened, includes tip fins).
- Combined ≈ 17.9 m → 18.0 m.

Confidence: moderate (±7 %): main uncertainties are f from the ill-conditioned lateral-motion route and
the exact wingtip points / AABB convention.
