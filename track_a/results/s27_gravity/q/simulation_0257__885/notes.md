# q 885 – table width (longer side), simulation_0257

The question asks for the table's longer side (its length). File fps = 24, question_fps = 30. All time conversions use 30.
The scene is 2D: a fronto-parallel wall and a static camera.

## Scale from the prior (plant accelerates at 9.8 m/s^2 before 0.5 s)
- I fitted a quadratic to the pot track in scene/tracks (frames 0–14, before the impact at frame 15). See fit.py.
  - mask centroid: a = 6.93 px/frame^2 (resid 0.29 px)
  - bbox bottom: a = 7.00 px/frame^2. Using frames 7–14 gives 6.95, and frames 3–14 give 7.12.
  - Adopted value: a = 6.95 px/frame^2.
- At 30 fps that is 6255 px/s^2, so the scale is 9.8 / 6255 = 0.001567 m/px.

## Table
- On frame 0 the table runs from x 518 to x 1539, which is 1021 px. I drew this line on frames/table_check.png and it matches both ends.
- Length = 1021 × 0.001567 = **1.60 m**. Across the different fits the result ranges from 1.56 to 1.70 m.

## Sanity check
- At 30 fps the AC unit is 505 px = 0.79 m wide (a real outdoor unit is about 0.8 m) and the pot is 7.4 cm wide. Both are plausible.
- At 24 fps the same objects would be 1.23 m and 11.5 cm, and the table 2.5 m. That is less plausible, so the 30 fps time base is consistent.

Confidence: good, about ±4%.
