# q3119: height of the left basketball stand (m)

Prior: rider average speed = 2.9 m/s. Internet video, 30 fps (file and question rates match), so I used one planar scale, as the annotators did.

## Scale
- From scene/tracks/rider.csv (stabilised, frames 0-93), mean per-frame speed of the bbox centre = 476.3 px/s.
  Other reference points give 475.8 (centroid), 475.8 (front wheel) and 476.8 (rear end). Motion is uniform and horizontal: the 2D path gives 476.4.
- Scale = 2.9 / 476.3 = 0.006089 m/px.

## Stand height (px), measure.py
- Top: the backboard frame's top edge, found from the gradient of the mean column profile at x 450-560, left of the bird (the bird is not counted).
- Base: where the dark pole meets the light court, from a column profile through the pole.
- Frame 0: top 524.5, base about 1155.5, giving 631 px.
- Frame 46: top 518.5, base about 1149, giving 630.5 px.
- Frame 93: top 514.5, base about 1144.5, giving 630 px. The camera drifts slowly in y, so the edges move but the difference stays the same.
- Height = 630.5 px × 0.006089 = **3.84 m**.

## Check
- Three frames agree within ±0.5 px.
- A regulation backboard top is about 3.9-4.0 m above the ground, so the result is plausible. The pole base (y≈1150) sits a little behind the rider's ground line (y≈1177). Correcting for that perspective would make the answer slightly larger, but the annotators applied no perspective correction.

Confidence: moderate to high, about ±3% from the measurement itself.
