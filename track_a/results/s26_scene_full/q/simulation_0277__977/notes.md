# q_977 — height of the raccoon (m)

- Video: a 2D side-view Blender render at 24 fps (question_fps is also 24). The camera is fixed and the raccoon gallops in a plane at constant depth. Its apparent size shows no trend over time.
- Prior: length including the tail = 1.51 m. This sets one metres-per-pixel scale. Height is the vertical extent of the bounding box (top of back/tail to lowest paw).
- Measurements: I used scene/tracks/raccoon.csv (shadow-free mask bounding box, all 72 frames). I checked it on zoomed, gridded crops at frames 0 and 24:
  - Frame 0: tail raised to y≈722, paws at y≈864, nose to tail 543–846.
  - Frame 24: back top ≈745, paws ≈862, x 1062–1379.
  - Both match the record within a few px.
- Over all frames, bbox_w has a median of 300.5 px and bbox_h a median of 122 px. The gallop changes both, so I used whole-clip statistics.
- Results (ratio.py):
  - Ratio of the medians: 1.51 × 122 / 300.5 = **0.613 m**.
  - Second route, median of the per-frame h/w ratios: 0.610 m (mean 0.613).
  - Extremes: max/max gives 0.666, and frame 0 (tail raised) gives 0.71.
- Sanity check: a height/length ratio of about 0.41 is plausible for a raccoon with its tail included.
- Confidence: moderate. The main uncertainty is which pose the reference bounding box used (gallop phase or rest), roughly ±10%.

Answer: 0.613 m
