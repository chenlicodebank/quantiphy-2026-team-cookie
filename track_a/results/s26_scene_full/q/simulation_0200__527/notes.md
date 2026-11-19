# q_527 — vertical height of the "SKYNOVA" lettering (m)

The video is 2D, 60 fps (the file's rate and question_fps are the same). The camera is static. I used one m/px scale, taken from the drop's acceleration prior (9.7 m/s²).

## Scale (accel.py)
- I fitted a quadratic to the drop track in scene/tracks/drop.csv, using two independent reference points:
  - the centre: a = 28.87 px/frame² (frames 2–11), 28.93 (frames 1–11), 28.78 (frames 3–11);
  - the sharp tip (mask_y0, which does not depend on the centroid offset): 28.87 / 28.92 / 28.77.
- I used a = 28.87 px/frame² = 103,930 px/s². That gives a scale of 9.7 / 103,930 = 9.33e-5 m/px.

## Lettering (measure.py, frame 13)
- The white text runs vertically along the right edge of the amber liquid, in columns x ≈ 1059–1069.
- I took the row profile of the brightest pixels in the bands x 1050–1075 and 1052–1072. The text is bright (≈180–195) against ≈130–140.
  - The top of the first letter crosses half-maximum at y ≈ 682.
  - The bottom of the last letter crosses at y ≈ 949.
  - Height ≈ 267 px (±3).
- Result: 267 × 9.33e-5 = **0.0249 m**.

## Checks
- The centre and tip tracks give the same acceleration to within 0.1%. The two column bands give the same text extents.
- Sanity check: at this scale the whole bottle with its cap (≈943 px) is ≈ 0.088 m, which is a plausible dropper bottle.
- Confidence: good (about ±3%). The main uncertainty is the soft text edges (±3 px) and how the reference defines the lettering box.
