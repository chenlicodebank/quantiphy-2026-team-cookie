# Q1130 – eagle wingspan (m) → 1.82

File is 25 fps; question_fps = 24 (t=1 s → frame 24, t=2 s → frame 48, used for all depth times).
Camera static (scene record). Principal point assumed at image centre (480,480).

## Geometry (geom.py, eagle3d.py)
- Camera pitch as a function of f: the boat moves on the water plane, so its 3D displacement between frames
  24 and 48 (depths 130.35 → 133.74 m, hull-centre track) must be horizontal → pitch(f) (12.7° at f=6000,
  12.0° at 6300). Check: the boat's apparent scale ratio 0.945/0.97 = 0.974 matches the depth ratio 0.9746.
- Independent check of that plane: the eagle's 3D path from its depths (139.76 → 130.25 m) comes out level
  (vertical speed ≈ −0.04 m/s) for every f, and the predicted image tilt of a horizontal wing axis
  perpendicular to its heading (−7°) matches the observed wing-line tilt (−3…−8°). Eagle speed ≈ 11.5 m/s.
- Focal length: the person's depth_info hardly changes (0.03 m/s) although the body walks down-left; on the
  ground plane the walk is mostly toward the camera (~85 % radial), so the origin is static and the prior
  speed is ill-conditioned for f (speed only falls from 1.43 to 1.34 m/s for f 6000 → 8000; f=8000+ would
  make the man 1.3 m tall). Taking the person's lateral-only motion (f≈3560) would make him 3 m tall –
  rejected. So the scale comes from the standard person: measured head-top→sole 76.5 ± 1 px at mid-stance
  (person.py, person_view.py), depth ≈ 139.3 m (origin 139.95, body somewhat nearer), standing height 1.78 m,
  walking factor 0.98, vertical foreshortening cos(13.5°) → f ≈ 6300 px (HFOV ≈ 8.7°). With this f the
  prior speed comes out 1.41 m/s (8 % high; a gentle beach slope toward the water would explain it).
  Boat stern-to-bow ≈ 15 m (plausible).

## Wingspan (span.py)
Eagle mask = |frame − clean plate| > thr, extent projected on the predicted image wing axis, converted with
the local px/m of a horizontal wing axis perpendicular to the heading at that frame's 3D position
(≈0.85 of the frontal scale f/depth).
Wings-flat frames (two wing-beat cycles): f=6300, thr 35 → frame 5: 1.81, 6: 1.81, 32: 1.82, 33: 1.82 m
(thr 20 halo: 1.87–1.94; thr 60 core: 1.67–1.76). Answer 1.82 m.
Sensitivity: f 6000 → ~1.94 m, f 6476 → 1.76 m (wingspan ∝ ~1/f). Person-height assumption 1.75–1.80 m
→ 1.79–1.84 m.

Confidence: moderate (±6 %), dominated by the focal length from the assumed person height.
