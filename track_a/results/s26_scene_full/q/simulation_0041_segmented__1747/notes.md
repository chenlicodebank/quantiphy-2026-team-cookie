# q_1747 — average speed of the boat (m/s)

Prior: person height 1.75 m. No depth_info. fps = question_fps = 24 (no re-timing issue).

## Observations
- Camera is fixed and looks steeply down on a ground/water plane (crops `frames/persons.png`, `frames/boat_clean.png`):
  the person's head overlaps the shoulders, the boat deck is widely visible. So a naive 2D scale
  (1.75 m / 46.5 px bbox height) would overstate metres per pixel; I corrected for camera elevation e.
- Boat motion (scene tm track, rigid template match, checked): linear fit (-5.666, -1.591) px/frame, uniform,
  frames 1-71 (frame 0->1 nearly zero motion). Net (-396.1, -111.1) px.
- Template-scale test: the boat shrinks ~0.9 % from frame 5 to 60 (moving ~87 px up) -> ~1 % per 100 px of image y;
  the person sits ~445 px above the boat -> boat's scale ~4 % larger than the person's.

## Scale and elevation (from the person, scripts boat.py/crops.py + scene/tracks/person.csv)
- Gait: bbox height minima every 17 frames (40.25 px average at mid-stance); front-foot (bbox bottom) plateaus
  429.5 -> 455 -> 479 -> 505.5 px => 25.3 px per step in image y (ground step foreshortened by sin e).
- Width 19-20 px (arms included, ~0.5 m) -> s ~ 39 px/m.
- Model: s(1.72 cos e + 0.2 sin e) = 40.25 (mid-stance height), s*L*sin e = 25.3 with step L = 0.70-0.75 m
  -> e = 60-62 deg, s_person = 39-41 px/m; agrees with the width route. Took e = 61 deg, s_person = 40 px/m,
  s_boat = 41.6 px/m (perspective +4 %).

## Speed
- Ground-plane px/frame = hypot(5.666, 1.591/sin61) = 5.95 px/frame = 142.8 px/s -> 3.43 m/s.
- Including the zero-motion first step (mean of 71 backward differences) gives 3.38; answer 3.42 m/s.
- Sanity: boat length ~360 px / 41.6 = ~8.7 m (plausible small fishing boat), ~7 knots.
- Contrast: naive single 2D scale from the 46.5 px median person height would give ~5.3 m/s; rejected because the
  view is clearly steep top-down (foreshortened person height).

Confidence: moderate (±10 %); the main uncertainty is the person's pixel scale under the steep view angle.
