# q_189 — length of the shark (prior: boat length = 10 m)

2D side-view simulation, 24 fps (file and question rates agree). I used one metres-per-pixel scale taken from the boat.

## Boat (prior object)
- Frame 57 (whole boat visible). `measure.py` thresholds the difference from the per-row sky colour above the
  waterline. Results: x 664–1523 → 860 px (th 30), 858 (th 60), 854 (th 100). The scene record gives 859 px.
- Boat length used: 859 ± 3 px → 0.01164 m/px.

## Shark
- `measure.py` and `snout2.py` use a clean-plate difference: frames 25 and 57 against each other, since the shark
  positions in those frames don't overlap. The tail tip is sharp: x 1539–1541 in frame 25 and 1195–1197 in frame 57.
- The snout is hard to see because the dark-blue top of the head blends into the water. At thresholds of 45 or
  more, the extent stops at the lighter underside (261 px). At thresholds of 20–30 it includes the head (278–282 px).
  The row profiles show the head begins with a clear outline spike at x≈1264 (frame 25).
  - Consistency check: the shark moves 32 × 10.746 px between frames 25 and 57, so the snout should be at ≈919 in
    frame 57. The low-contrast head edge is indeed at 918–919 there.
  - The snout→tail tip length is the same in frames 25, 40 and 57 (278, 280, 280 px at th 30). The scene record's
    median of 274 px agrees.
- Shark length used: 277 ± 4 px.

## Answer
277 / 859 × 10 m = **3.22 m**.
- Second route: the record's median of 274 px gives 3.19 m.
- Lower bound: counting only the high-contrast body (261 px) gives 3.04 m.

Confidence: good, roughly ±3%. The main uncertainty is where the low-contrast snout ends.
