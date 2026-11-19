# q_1951 — height of the black cat (incl. tail)

Prior: cat speed = 1.041 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

Method (planar: the cat walks parallel to the image plane; its pixel size stays constant and its vertical drift is
-0.04 px/frame, so one m/px scale applies):
- `measure.py`: median background over all 50 frames, |frame - bg| > 25, largest component plus nearby pieces
  (the white head and paws are included; mask overlay `frames/mask40.png` checked by eye).
- Pixel speed: linear fit of x against frame: centroid 5.414, bbox left 5.427, bbox right 5.418 px/frame,
  so about 5.42 px/frame = 130.0 px/s. The mean per-frame centroid step is 5.57, inflated by gait jitter of the
  mask centroid, so I used the fit.
- Scale = 1.041 / 130.0 = 0.00801 m/px.
- Height of the bbox including the raised tail: median 74 px, mean 75 px (range 67–83 over the gait). The scene
  record gives a median of 76 px. I used 75 px.
- Height = 75 × 0.00801 = 0.60 m.

Second route: the record's own track (centroid net displacement 265.8 px over 49 frames gives 5.42 px/frame, and
a 76 px median height) gives 0.61 m, which agrees.
If the reference speed were the mean of jittery per-frame steps (5.57 px/frame), the height would be 0.58 m.
Confidence: moderate-high (±5%). The main uncertainty is the tail pose, which changes the height by ±5 px.
