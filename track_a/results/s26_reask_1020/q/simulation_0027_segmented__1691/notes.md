# Q1691 — height of the rock (m)

File: 960x960, 25 fps (question_fps 24; irrelevant here, rock is static). Prior: person 1.75 m; depth_info: human
origin 100.56 m (t=1 s), 100.60 m (t=2 s).

## Measurements (measure_h.py, fit_size.py)
- Person pixel height (mask, min RGB < 248): median 60 px (58 at <240, 63 at <252; pale head). Walking, ~0.97 x 1.75.
- Rock (static): mask rows 25..310 -> 285 px tall; cols 328..959 (touches right edge).
- Person moves down-right in image: feet 0.605 px/frame down, 0.469 px/frame right; seen front-on (walking
  along the line of sight). Given distances barely change (0.036 m/s) -> origin stays put, body walks toward camera.

## Geometry (rock_model.py)
- Naive same-depth scale: 285 x 1.75 / 60 = 8.3 m (upper-ish bound: ignores downward camera pitch, which makes the
  rock's top surface add to its image height).
- Camera pitch from the walk: lateral motion only ~0.33 m/s, so for a 1.0-1.6 m/s walk the down-image motion is a
  foreshortened approach -> LOS depression 15-23 deg, f ~3700 px (HFOV ~15 deg), camera height ~25-40 m.
- Rock modelled as an ellipsoid on the same ground, solved so its tangent rays hit image rows 25 and 310; rock
  slant distance ~105-108 m, length >= 18 m. H = 7.6 / 7.15 m for front-back depth 12 / 16 m at 1.3 m/s walk;
  full range over walk 1.0-1.6 m/s and depth 8-20 m: 4.1-8.2 m, most plausible cases 6.8-8.0.

## Answer
7.5 m (between ellipsoid model central value ~7.4 and naive 8.3 upper estimate).
Confidence: low-moderate — rock depth and front-back extent are not given; scale relies on the person.
