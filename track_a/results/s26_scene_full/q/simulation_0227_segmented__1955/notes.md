# q_1955 — black cat height (incl. tail)

2D convention, fps 24 (file and question agree). Cat walks right in profile at constant depth (apparent size constant).

Scale from prior (cat speed 1.041 m/s):
- centroid x 567.4 -> 836.0 over 49 frames = 5.48 px/frame; nose edge 621 -> 888 = 5.45; tail-end edge 514 -> 779 = 5.41.
  Mean ~5.46 px/frame = 131.0 px/s -> 0.00795 m/px.

Height (measure.py, background-difference mask, per frame top-of-tail to bottom of paws):
- Frames where chair pixels contaminated the top (top ~824) were excluded. Clean frames: tail tip y 842-852, paw
  bottom ~919-921 (early frames 925-927 include the faint shadow). Height 68-83 px, median 74 px; visual checks
  at frames 0, 6, 24, 45 give 75-80 px.
- 74-75 px x 0.00795 = 0.59 m (range 0.56-0.63 depending on where the tail is in its sway).

Second route: the nose and tail edge speeds agree with the centroid speed to within 1%, and the frame-by-frame visual
reads agree with the code median. Confidence: moderate. The main uncertainty is which tail pose the reference AABB used (±5%).

Answer: 0.59 m
