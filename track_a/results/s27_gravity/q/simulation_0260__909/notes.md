# Q909: plant diameter (width)

2D clip; file fps = question_fps = 30.

## Scale, from the prior (mug falls at 9.8 m/s^2 before 0.5 s)
- `fit.py`: a quadratic fit of the mug's vertical position from scene/tracks/mug.csv over frames 5-15 (free fall, before the impact at frame 16).
  - ref_y (mid-silhouette): 6.84 px/frame^2.
  - y1_true (bottom): 6.89 px/frame^2.
  - Other windows (6-15, 5-12): 6.79-6.94 px/frame^2.
  - Fit residuals are under 1 px.
- I used a = 6.86 px/frame^2 = 6174 px/s^2. Scale = 9.8 / 6174 = 1.587e-3 m/px.
- Sanity check: at rest the mug is 56 px tall and 48 px wide, which gives 8.9 cm x 7.6 cm. That is a realistic mug, so the scene is at real scale. The mug rests at the back of the table, at the same depth as the plant (bottoms at y = 869 and 868).

## Plant width (`plant.py`, `plant2.py`; frame 36, zoomed crop frames/plant_big.png)
- The colour difference from the wall, with half-maximum edges per row, gives:
  - foliage: about 1083.6 to 1131.5 px across the rows, 46-48 px (row 820: 46.3 px);
  - pot rim (lavender band): about 1082.5 to 1128.5 = 46 px;
  - pot body: 42-44 px (scene.json gives 44).
- Overall horizontal extent (bounding box) is about 47 px (±1).
- Width = 47 x 1.587e-3 = 0.0746 m.
- Second route: the pot rim alone (46 px) gives 0.073 m. The pot body alone (44 px) gives 0.070 m.

Answer: 0.0746 m. Confidence is moderate to good: about ±3% in pixels and ±1% in the scale.
