# q_2039 – average speed of the black (dark) car

Prior: lane width = 3.66 m. Top-down static drone shot (record: background drift < 2 px), planar convention.

## Pixel speed (speed.py, scene/tracks/dark_car.csv, template-match centre)
- Tracked f0–f171, y 1836.5 → ~405 px, x 529.5 → 538.5 (along the road).
- Mean per-frame displacement 8.37 px/frame (all frames); 8.38 for f0–150 (clean part); net 8.38 (f0–150),
  8.43 (f20–140), linear-fit slope 8.39 px/frame. Nearly constant speed.

## Scale (road.py, column profiles at 5 road strips, frame 171)
- Asphalt edges x ≈ 521 and ≈ 598 → road width ≈ 77 px; centre line at x ≈ 559–560 → each half ≈ 38 px.
- Reading A (used): the 3.66 m "lane" = the whole asphalt width (77 px) → 0.0475 m/px.
  Sanity: car width 36 px → 1.7 m, car length 69–78 px → 3.3–3.7 m, i.e. realistic; the road is a narrow country
  road whose total width is about one standard lane.
- Reading B: half the road (38 px) → 0.0963 m/px → car 3.5 m wide, 6.6 m long (implausible), speed 24.2 m/s.

## Time base
question_fps 30 vs file 29.68 (1 % difference); used 30 (rate stated with the question).

## Answer
8.38 px/frame × 30 fps × 3.66/77 m/px = 11.95 m/s (11.8 m/s with 29.68 fps). Answer 11.9 m/s (~43 km/h).
Confidence: moderate – main uncertainty is which pixel span the annotator took as the lane (reading B would double it).
