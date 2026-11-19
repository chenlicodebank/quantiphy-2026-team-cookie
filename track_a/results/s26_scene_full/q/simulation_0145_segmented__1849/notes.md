# q_1849: tire diameter (prior: rocket length = 2.9 m)

This is a 2D side view with a static camera, 24 fps (the file rate matches question_fps). The scale is one metres-per-pixel value, taken from the rocket's length.

## Rocket length in pixels
- I measured it with `measure.py`: the difference mask against frame 28, then the PCA extent along the axis, on frames 15-20.
- The results per frame were 224.4, 220.5, 227.5, 226.6, 226.0 and 222.2 px. The mask includes a small bluish nozzle/plume blob at the tail.
- The scene record gives 221.9 px (median nose to tail). A visual check on frame 18 gives about (587,139) to (763,281), which is roughly 226 px.
- Adopted value: L ≈ 222.5 px (±3). Scale = 2.9 / 222.5 = 0.01303 m/px.

## Tire diameter in pixels
- I measured it with `circ.py`: circle fits to the lower outline and bottom edge of each wheel on frame 28 (the truck alone). The upper part of each tire is hidden by the body.
  - Front: 104.0 px. This may be inflated by the mudflap or fender.
  - Middle: 101.3 px.
  - Rear: 99.8 px.
- Second route: the horizontal widths at the wheel-centre rows (`measure.py`) are about 100 px (middle, 983-1083) and about 101 px (rear). All wheels touch y = 867.
- Adopted value: D ≈ 101 px.

## Answer
D = 101 × 0.01303 ≈ 1.32 m. Using L = 226 instead would give 1.30 m. A real tire of about 1.2-1.3 m on a military truck is plausible.

Confidence: moderate-high, with an uncertainty of about ±3%.
