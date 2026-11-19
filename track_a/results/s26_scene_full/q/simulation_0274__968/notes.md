# q968 – width of the raccoon (m)

Prior: the raccoon's length is 1.51 m. This is a 2D top-down render, 24 fps (same as question_fps), with a static camera.
In a top view, length is the x extent (nose to tail tip) and width is the y extent (flank to flank).

## Measurements (width.py, measure.py)
- Length: x extent of the bbox (raccoon only), median 296 px over frames 2–71 (range 282–304, because of tail swing). Frame 0 gives 300.
- Width: for each column, I scanned from the body midline (y = 729) up to the shadow (grey < 80) or the background (> 195),
  and down to the background.
  - Walking frames 12–60: the maximum column width is 62–65 and the 95th percentile is 61–63. The overall y extent is 695–759,
    which is 63 px. The median over frames is 63 for the maximum and 61 for the p95.
  - Rest/start frames 0–6: the width is only 53–56. The top edge there (≈705) is close to the dark shadow, and the legs are not splayed.
  - Frames 66–71: the width is inflated by the shadow's light face patch, so I ignored them.
- I used 62 px (between the p95 and the maximum).

## Answer
Width = 1.51 × 62 / 296 = 0.316 m.
Range of readings: 0.311 (61 px) to 0.321 (63 px). Using only frame 0 (56/300) gives 0.282.

Second-route check: the record's PCA mask_width_across is 60–64 px and its length is 296 px, which gives 0.31–0.33 m.
This agrees with the column-scan result.

Confidence: moderate-good (±5%). The main uncertainty is whether the reference bounding box is the rest pose or a walking pose.
