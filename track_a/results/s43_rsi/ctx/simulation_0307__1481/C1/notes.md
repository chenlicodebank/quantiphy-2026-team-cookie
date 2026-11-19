# Q1481 – length of the plane (m)

Prior: speed 22.16 m/s. depth_info: 102.6664 m at t=1 s (frame 24), 121.8263 m at t=2 s (frame 48).
question_fps = file fps = 24. 3D Blender scene with a static camera. A single VTOL aircraft flies away from the camera, up-left in the image.

## Focal length / trajectory (focal.py, fit3d.py)
- The angle between the origin rays at frames 24 and 48 follows from d1, d2 and |Δp| = 22.16 m (constant speed): θ = 5.706°.
  Hull-centroid pixels (scene track) give f = 3429 px; bbox centre gives 3369; raw centroid gives 3342.
- Full constant-velocity 3D fit over frames 2..71 (hull centroid, both depths, |V| = 22.16): f = 3409 px (HFOV 41°),
  pixel rms 2.3 px, V_cam = (-10.55, -6.31, 18.44) m/s. A constant velocity fits well. If the flight is level, the camera pitch is 18.9°,
  and a rough ground-plane check from the three tank sizes gives about 16°, which is consistent.
- Sensitivity (origin_sens.py): f moves about 1.6 %/m with the origin's position along the fuselage. If the origin is the 3D
  bbox centre (1.6 m aft of the hull centroid), f = 3508. I adopted f ≈ 3460 ± 2 %.

## Body dimensions by triangulation (tri_manual.py, tri_tips.py)
The aircraft keeps a constant attitude, so each feature is a fixed offset D from the origin in camera axes.
I clicked features on zoomed, gridded crops at frames 0/24/48/71 (crop.py), solved D by least squares
(residuals of a few px), and expressed D in body axes h (heading), s (span) and u (up):
- Fin tops: right s = -9.16, left s = +8.22 (both h ≈ 1.9, u ≈ 1.6; the symmetry checks out). Fin-top span = 17.38 m.
  Lower right fin tip s = -9.41, so the maximum span extent is about 17.4–17.9 m.
- Fore/aft: antenna and wing leading corner h ≈ +4.9; canopy front +3.85; fuselage end -7.1; ventral fin bottom -8.2.
  The nose-to-tail extent is about 13.2 m.
- Second route: at frame 24, the fin-top pixel separation (506 px) decomposed on the projected axes gives 17.1 m,
  which agrees with the triangulated value within 1.5 %.

## Answer
Named-size rule: length = the longer horizontal extent. The span (about 17.4–17.9 m at f = 3409, scaled to f ≈ 3460, gives
about 17.3–17.6 m) is longer than nose-to-tail (about 13.2 m), so length = span direction, which assumes the AABB is aligned with the aircraft's axes.
**Answer 17.4 m.** Alternative reading (nose-to-tail along the flight direction): about 13.0 m.
Confidence: moderate. Scale is ±3 % (origin location); feature picks are ±2 %; the main risk is which reading of "length" was meant.
