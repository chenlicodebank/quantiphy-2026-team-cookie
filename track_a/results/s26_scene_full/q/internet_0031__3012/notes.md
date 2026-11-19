# q_3012 — width of the football pitch (m)

Prior: length of goal frame = 7.32 m. Internet video, near-nadir static drone view (drift < 3 px), so one planar scale is used.
The question is about sizes only, so the frame rate doesn't matter.

Measurements (measure.py, median of frames 0/40/80/120/170, sub-pixel brightness centroids):
- Pitch width = touchline-to-touchline (top y≈47, bottom y≈883), measured at 9 columns x=20..340: 833.6–838.3 px, mean **835.7 px**
  (it varies slightly because the image is rotated about 0.5°).
- Goal frame along the goal line: post-bar centroids 415.3 → 511.8 = 96.5 px (the scene record gives 97.9 px). The outer white frame
  runs from about 412.5 to 513.8, about 101 px. Annotator-style pixel length ≈ 97–101 px.
- Check from other markings (standard dimensions): goal area 238.3 px / 18.32 m = 13.01 px/m; penalty area 525.1 px / 40.32 m
  = 13.02 px/m. These imply a goal of 95.3 px and a pitch width of 64.2 m.

Results:
- Goal 96.5 px: 63.4 m. Goal 97.9 px: 62.5 m. Goal 101 px (outer): 60.6 m. Box-based scale: 64.2 m.
- Answer: 835.7 × 7.32 / 98.2 ≈ **62.3 m**, the middle of the plausible readings of the goal pixel length (60.6–64.2 m).

Confidence: moderate. The touchline measurement is solid (±0.3%); the uncertainty comes from how the goal frame's pixel length was taken (±3%).
