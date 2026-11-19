# Q1149 – height of the boat (m); prior: boat length = 10 m
File fps = question_fps = 24. 3D Blender scene, static camera, 1080x1080, principal point taken as (540,540).

## Measurements (pixels)
- Boat full vertical extent (mast/antenna tip to keel bottom), scene/tracks/boat.csv checked on 3x crops at t=1 s and 2 s:
  225.8 px (frames 22-26 mean) at d = 133.957 m, 229.2 px (frames 46-50) at d = 131.256 m.
  Height ∝ 1/depth holds (1.5 % vs 2.1 % growth, within ±1 px).
- Height in metres = H_px · d / f, so everything hinges on the focal length f.

## Focal length
Route A – person (person_h.py): pixel height 41-42 px (median 42 from a difference mask, 40-41 by eye at t=1 s),
human depth 139.10 m (constant; apparent height also constant, so body depth ≈ 139 m). Adult 1.75 m ⇒ f ≈ 3300 px
(1.70-1.80 m ⇒ 3200-3400).
Route B – boat length (boat_geom.py): heading taken from 3D motion between t=1 and t=2 (Δu = -73.5 px, Δd = -2.70 m),
10 m along that heading plus the stern half-beam projected, matched to the 182.6 px hull width. Ill-conditioned:
half-beam 0 ⇒ f = 3378; 1.0 m ⇒ 2927; 1.5 m ⇒ 2773. Realistic beams give f ≈ 2700-2900, which would make the
person 2.0-2.1 m tall – fails the plausibility check, so route B (heading = motion direction, length exactly along
the hull, possible AABB rotation of the "length") is unreliable; it only bounds f to ≲ 3380.

## Result
f ≈ 3300 ⇒ height = 225.8·133.957/3300 = 9.17 m (t=1), 229.2·131.256/3300 = 9.12 m (t=2).
Route B with realistic beams would give 10.3-11 m; the answer is nudged slightly toward it: **9.4 m**
(person 1.80 m reading). Confidence moderate (±10 %), limited by the focal length.
