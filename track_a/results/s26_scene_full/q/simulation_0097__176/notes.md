# Q176 – height of the car (prior: car acceleration = 10 m/s²)

2D simulation, 24 fps (file fps = question_fps, so no re-timing). Car (Cybertruck-like) moves left along a straight line, starting from rest at frame 1.

## Scale from the prior
- Car centroid x(frame): quadratic fits from frames 1, 2 and 5 onward give 2c = 0.3706–0.3708 px/frame²,
  which is **213.1–213.5 px/s²** (my own mask in measure.py gives 213.0). The mean of the backward-difference speed changes
  over frames 2–40 is 216 px/s², which is noisier and agrees.
- Scale = 10 / 213.3 = 0.04688 m/px.

## Car height
- Car mask (difference from the background colour > 4, 6 or 10) gives y = 587–627, so **41 px** in every frame (once 42).
  A 5x zoomed crop of frame 0 confirms the roof top at about 587 and the wheel bottoms at about 627.
- Height = 41 × 0.04688 = **1.92 m**.

## Check
- Car length is about 122 px, which gives 5.7 m. Both the height (1.92 m) and the length match a real Cybertruck (about 1.9 m × 5.7 m), so the scale is plausible.
- Uncertainty: ±0.5 px from anti-aliasing at the edges (±1.2%), ±1% from the acceleration fit, so about ±2% overall.
