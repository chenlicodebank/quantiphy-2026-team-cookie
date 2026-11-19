# q_508: bottle body diameter (m)

Prior: the droplet accelerates at 9.7 m/s². The video is treated as 2D, so one metres-per-pixel scale comes from the drop's pixel acceleration. fps = question_fps = 60, so no re-timing.

## Drop acceleration (measure.py, using the centroids in scene/tracks/drop.csv)
- Quadratic fit to raw frames 0–6, before the duplicated frame 7: a_y = 31.67 px/frame² (residual 0.29 px).
- Quadratic fit to frames 1–10 with the record's render-step mapping (frame 7 is a duplicate, render step 8 is missing):
  31.69 px/frame² (residual 0.38 px).
- Second differences of frames 0–6: 31.98, 31.75, 31.02, 31.90, 32.30.
- I used a = 31.69 px/frame² × 3600 = 114,085 px/s².
- Scale = 9.7 / 114,085 = 8.50e-5 m/px.

## Bottle body width (measure.py and profile.py, frame 12)
- Horizontal edge positions in 10 bands from y = 750 to 1200: left edge 1702–1706, right edge 2125–2133. The width is 419–426 px,
  median about 425.
- The colour profiles at y = 950 and y = 1100 put the glass/background transitions at x ≈ 1703–1704 and x ≈ 2128–2129,
  which gives 425 px. The record's 431 px was read by eye and is slightly too large.

## Answer
425 px × 8.50e-5 m/px = 0.0361 m (about 36 mm, which is reasonable for a 30 mL serum bottle).

## Second-route check
- The two acceleration fits (raw frames 0–6, and the mapped frames 1–10) agree to within 0.1%.
- The width from the edge gradient and the width from the colour profile agree to within 1 px.

## Confidence
The measurement is moderately high, about ±3%. The main risk is that the bottle and the drop are at different depths, which a
single 2D scale cannot correct for. The benchmark convention for 2D videos uses one scale, so I followed it.
