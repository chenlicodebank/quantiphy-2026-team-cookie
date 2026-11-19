# q_3130 — distance between the two closest tall trees (m)

Prior: average speed of the scooter rider = 2.91 m/s. 2D internet clip, 30 fps (file fps = question_fps, so no re-timing).

## Scale (from prior)
The scene/ track (front-wheel leading edge, checked on frames 0 and 55) moves 1262 -> 244 px raw (1262 -> 235 px
when stabilised) over 55 frames. That gives 555 px/s raw and 560 px/s stabilised; bbox centre gives 555/561. I used 557 px/s.
Scale = 2.91 / 557 = 0.005224 m/px.
Sanity check: the scooter's 203 px works out to 1.06 m, which is realistic.

## Trees
The two big foreground palms are on the planting strip (the left trunk is near x≈400 and the right near x≈1418).
Trunk edges were read from 2x gridded crops of frame 30 (trunks.py -> frames/crop_L.png, crop_R.png):
- y=500: L 361–441 (c 401), R 1365–1460 (c 1412)
- y=600: L 360–442 (c 401), R ~1366–1462 (c 1414)
- y=700: L 354–444 (c 399), R 1370–1467 (c 1419)
- y=800: L 340–445 (c 392), R 1375–1480 (c 1427) (flared base)
Centre-to-centre distance is 1011–1035 px. I took 1020 px.

Distance = 1020 × 0.005224 = **5.33 m**. Using the 560 or 555 px/s speed estimates gives 5.30 or 5.35 m.

Second route: the edge-to-edge spacing (L right edge to R right edge, 442 -> 1462) is also about 1020 px, which agrees.
The trees stand slightly behind the rider's plane, but I kept the annotators' single-scale convention.
Confidence: moderate-high (±3%).
