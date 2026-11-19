# Q565: lampshade height (m). Prior: black cat speed = 0.94 m/s. No depth_info.

Time base: the file and the question both use 24 fps, so no re-timing.

## Scale from the prior
- The cat walks at a steady speed. I fitted a line to x(t) for scene/tracks/cat.csv: mask centroid 427.7 px/s, nose 426.4,
  bbox centre 426.1. The mean |dx|·fps of the centroid is 429.7 px/s. I used 428 px/s, so
  s_cat = 0.94/428 = 0.002196 m/px. This holds only at the cat's depth.

## Lampshade pixel height (shade.py, rim.py; frames 0/25/49 averaged, since the lamp doesn't move)
- Bright-mask bbox: y 513–619 (106–107 px), width 211–213 px.
- The bottom rim is seen slightly from above. Its silhouette sags about 4 px in the middle (quadratic fit across the rim):
  the ends are at y≈616 and the front point is at y≈620. The world AABB height runs from rim centre to rim centre: 513 → 616,
  about 103–104 px. I used 104 ± 2 px.

## Depth correction (the 2D single-scale assumption breaks here)
- The floor shows clear perspective. Cat paws touch at y≈1030. The table's front feet are at y≈997 and its back feet at
  y≈975. The lamp base sits near the back of the table top, so its floor-equivalent contact is y≈980.
- The rim sag (b/a ≈ 0.038) puts the horizon above y=619, which fits a level camera (horizon ≈ 540, hFOV ≈ 49°).
  Ground-plane ratio Z_lamp/Z_cat = (1030−y_h)/(980−y_h): 1.114 for y_h=540, and 1.10–1.14 for y_h between 450 and 600.
  I used 1.11.

## Result
104 px × 0.002196 m/px × 1.11 = 0.254 m.
- Second-route check: the plain single-scale 2D estimate is 0.228–0.235 m. The answer with the perspective correction
  is 0.25–0.26 m.
- Sanity check: 0.25 m is a normal lampshade height.

Confidence: moderate, ±8%. The main uncertainties are the horizon/lamp depth and the cat-origin speed.
