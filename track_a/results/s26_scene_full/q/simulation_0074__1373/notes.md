# q_1373 – diameter of the bicycle wheel (simulation_0074)

Answer: **0.635 m**. Prior: white car (the van) length = 6 m. File fps = question fps = 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Camera (3D scene, static camera)
- Focal length from vanishing points (`beige.py`, `vp.py`). I fitted the kerb edges in code: 8 segments, line rms about 0.3 px.
  The segments form 2 collinear pairs per road direction. VP_A = (-1319, -266) and VP_B = (2698, -267), so both sit on a
  level horizon at y = -266. With the principal point at the image centre and the two roads perpendicular,
  f = sqrt(-(vA-c)·(vB-c)) = **1797 px** (horizontal FOV 62°). The camera looks down at 24.2°.
- Independent check of f (`fcheck2.py`): I back-projected the given depths at frames 14 and 38. Only near f ≈ 1800–1850
  do the 3D displacements of the cyclist and the van come out parallel to road direction B (89.8° and 87.7° from road A).
  Other values of f make them skew.
- Camera height above the origins (`cam.py`) is about 8.6–8.9 m for every object at both times. That makes the ground about
  9.65 m below the camera (±0.15 m, depending on how high each origin sits).
- Prior check (`vanlen.py`, `vanlen2.py`): at frame 71 I projected the van's silhouette bottom onto the ground plane along
  road B. Bumper to bumper it measures 5.8–6.1 m, against the 6 m prior, so the camera and scale agree with the prior.

## Wheel
- I read 7–11 outer-tyre contour points per wheel by hand on 10× contrast-stretched crops (`crop2.py`). This was done for
  the front and rear wheels at frames 30, 38 and 50, followed by an ellipse fit (`wheel_ell.py`), with overlays in
  `frames/overlay.png` to confirm the fits. The ellipse's major axis equals the projected wheel diameter.
- Each wheel's distance comes from intersecting the ray through its hub with the hub-height plane (ground minus r).
  Diameter = distance × major axis / f.

| frame | wheel | major (px) | distance (m) | D (m) |
|---|---|---|---|---|
| 30 | front | 41.6 | 25.64 | 0.593 (hand fit looked slightly small; automatic edge fit gave 45.9 px → 0.654) |
| 30 | rear | 43.4 | 26.38 | 0.636 |
| 38 | front | 45.9 | 24.29 | 0.620 |
| 38 | rear | 46.8 | 25.03 | 0.651 |
| 50 | front | 48.8 | 22.47 | 0.609 |
| 50 | rear | 51.2 | 23.13 | 0.659 |

The six fits average 0.628 m (sd 0.023). The points sit on the dark tyre outline, not its outermost edge, so they read about
1 px small; correcting for that gives roughly 0.635–0.64.
- Second route (`wheel38.py`): at frame 38 I scaled directly from the bike's given depth (24.51 m) instead of the ground
  plane, under several guesses for where the bike's origin sits. This gives 0.62–0.65 m.
- Sanity check (`wheelbase.py`): the front-to-rear hub distance comes out 1.06–1.08 m in all three frames, a consistent and
  realistic wheelbase.
- The automatic ellipse refinement (`wheelfit.py`, `refine.py`) was unreliable because the rider's leg and the bike frame
  get in the way. I did not use it except as the frame-30 front cross-check.

## Confidence
About ±5%. The main uncertainties are the tyre-edge pixel readings (±1 px out of about 47) and the ground height (±1.5%).
The rear wheels read about 6% larger than the front ones, probably because the leg hides part of the rear tyre.
