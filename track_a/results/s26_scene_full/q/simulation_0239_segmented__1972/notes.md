# q 1972 — length of the brown horse (m)

Prior: brown horse speed = 0.874 m/s. The clip is 2D, so I used one metres-per-pixel scale from the horse's own pixel speed.
fps = question_fps = 24, so no re-timing.

## Measurements (measure.py, my own segmentation, which agrees with the scene/ record within 1 px)
- The horse is seen from above with its head to the right. It walks horizontally at row ~776; cy drifts by less than 1.5 px.
  Frame 49 is a reset artifact and is excluded.
- Pixel speed in px/frame:
  - centroid linear fit over frames 0-48: 2.667
  - nose (bbox x1) fit: 2.650; nose net: 2.646
  - rump (x0) fit: 2.59
  - centroid over whole gait cycles (frames 8→30 and 18→40): 2.67 and 2.71
  - centroid net over frames 0-48: 2.555 (the gait phase differs at the two ends)
  
  Adopted value: 2.66 px/frame = 63.8 px/s. Scale = 0.874 / 63.8 = 0.01369 m/px.
- Horizontal bbox length in px: it changes with the gait (legs stretch fore and aft). Minimum 143-145 (legs under the body),
  median 149, maximum 168. Adopted length: 147-149 px. The rest-pose-like frames are about 145 and the median is 149.
- Length = 148 px × 0.01369 = 2.03 m.

## Check
- Scale from the nose track instead (2.646 px/frame): 0.01376 m/px, giving 2.04 m.
- Range over the readings: minimum-length frames give 1.98 m; mean length (151 px) gives 2.07 m. Both are within about 2.5% of the answer.
- 2.0 m is a plausible size for a horse.

Confidence: moderate-high. The main uncertainty is which gait pose the reference bbox used (±4%).
