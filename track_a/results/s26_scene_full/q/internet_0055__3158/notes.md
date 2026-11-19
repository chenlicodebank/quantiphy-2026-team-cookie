# q3158 – width of the YIELD sign (m)

Prior: average speed of the "person riding scooter" = 1.95 m/s. Nobody in the clip rides a scooter. The only person
moving is the woman walking right to left across the far end of the path, so the prior must refer to her (most
likely a labelling slip). fps = question_fps = 30, so no re-timing.

Method (internet convention: one scale = prior world value / prior pixel value, planar):
- Walker's pixel speed, taken from scene/tracks/pedestrian.csv (mean of per-frame forward differences over all 75 frames):
  bbox centre 8.36 px/frame (net 8.29), head top 8.18, stabilised bbox centre 8.39 (5-frame smoothed), stabilised
  head-top x 8.19–8.23. The centroid's raw per-frame value (9.0) is inflated by mask jitter, so I left it out.
  Adopted 8.3 px/frame = 249 px/s. Camera drift is tiny (~1%).
- Scale = 1.95 / 249 = 0.00783 m/px.
- YIELD sign (measure: edges2.py, overlay frames/yield_outer.png): red triangle filled plus its white outer border,
  widest row near the top edge, every 5th frame. The red part alone is 113.5 px wide. Including the white border it is
  118–120 px (mean 118.9), which matches the scene record's 120. Adopted 119 px.
- Width = 119 × 0.00783 = **0.93 m**.

Second check: the extreme combinations (120 px with 8.18 px/frame, 118.9 px with 8.39 px/frame) give 0.954 and 0.921 m,
so the answer lies within about ±2.5%. A real US yield sign is 0.76–0.91 m (30–36 in), so 0.93 m is plausible.
Confidence: moderate. The main uncertainty is which reference point the annotators used for the speed, and the scooter mislabel.
