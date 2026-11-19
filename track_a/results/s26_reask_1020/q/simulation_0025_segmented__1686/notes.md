# q_1686 — height of the person (m)

File fps 25, question_fps 24 (frame = round(t*24)); 75 frames. Segmented 3D render, white background.

## Measurements
- Person pixel height (head top to sole, faint white head included, threshold >5; scene/tracks/human.csv bh,
  checked on row profiles in headprof.py: frame 0 head top y=527, sole y=583): median ~54-55 px, walking.
  Stricter thresholds (measure.py) lose the white head (~47-49 px), so they were not used.
- Person depth (origin) 114.83 m at t=1 and t=2: constant, so the origin stays put while the body walks.
- Person image motion: x -12.5 px/s, feet +3.4 px/s down. Crops (crops.py) show the body seen from the front,
  legs side by side, so it walks mostly TOWARD the camera, with a small sideways part.

## Focal length (the hard part)
- Speed prior route: f = 12.5 px/s * 114.8 / (1.3 sin theta) = 1104/sin(theta), where theta is the walking
  direction measured from the optical axis. If the walk were all sideways (theta = 90 deg) you get f ~ 1100 and a
  5.6 m person, which is impossible. The body faces the camera, so theta is small, but the image doesn't pin it
  down: the change in apparent size over 3 s (~3 %) is buried in gait noise (height trend -1 %/s, area
  +2.8 %/s, contradictory). So this route is ill-conditioned.
- Eagle route (birdcrops.py): the bird's spread-wing span times its depth is about constant at 5600 px*m
  (spans 46/48/52/55 px at Z = 119/114/110/105 m). Its 3D velocity between t=1 and t=2 comes from the pixel
  positions plus the given depths (dZ = -7.77 m/s). Correcting the wing foreshortening (wings perpendicular to
  the flight path) gives these pairs: f=3500 -> span 2.36 m; f=3700 -> 2.16 m; f=3900 -> 2.00 m. Bird speeds of
  11-11.4 m/s are plausible. An eagle span of 2.0-2.2 m gives f ~ 3700-3900, so the person's walking bbox is
  1.60-1.69 m (rest height ~2-3 % more).
- Standard-person check: a 1.75 m person would need f = 3580 (horizontal FOV 15 deg), theta ~18 deg, and an
  eagle span of 2.3 m. All of these are consistent.

## Answer
1.72 m: the eagle-scale value (~1.67 walking, ~1.71 rest), kept within the adult-person range. The speed prior
alone can't set the scale here because the walk direction is mostly in depth and the given human distance
belongs to the static origin, so the scale rests on the eagle's assumed wingspan and the standard adult height.
Confidence: moderate (about ±8 %).
