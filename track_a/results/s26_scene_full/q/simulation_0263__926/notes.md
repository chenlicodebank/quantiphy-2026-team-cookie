# Q926: width of the spacecraft (m)

The "spacecraft" is the single futuristic car-like vehicle seen from above. It starts at rest and accelerates
uniformly to the left along y ≈ 718. The scene is 2D (top-down) and the camera is static. fps = question_fps = 24.

## Scale from the prior (a = 4 m/s² at t = 1.0 s)
- Track: scene/tracks/car.csv ref_x (template-matched, sub-pixel). Per-frame steps grow linearly.
- Linear fit of the step (speed) against frame number, frames 3-71: slope 0.8984 px/frame², which is 517.5 px/s².
- Second route: a quadratic fit of position over frames 2-71 gives 517.6 px/s². The local step differences
  around frame 24 are 0.82-0.95 px/frame², consistent with constant acceleration.
- Scale = 4 / 517.5 = 0.007730 m/px.

## Width
- Width is the shorter horizontal extent, across the direction of motion, which is the image y extent.
- Body mask y 536-901 gives 366 px in every untruncated frame (scene record, ±2 px).
- I checked this on a 3x crop: the mid-grey band from y ≈ 497 to 536 is the cast shadow (offset about 38 px
  upward). My own dark threshold gave about 402 px because it included that shadow, so I rejected that value.
- Width = 366 × 0.007730 = 2.83 m.
- Length for reference: about 776 px, or 6.0 m. Real-world check: a car-sized vehicle about 2.8 m wide is plausible.

Confidence: good (about ±3 %). The main uncertainty is the body edge versus the shadow, about ±5 px.
