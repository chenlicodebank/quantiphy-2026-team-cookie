# Q1800 — height of the shark (prior: shark acceleration = 1 m/s^2)

2D segmentation clip, 24 fps (file fps = question_fps, so no re-timing). The shark swims left at constant y and speeds up smoothly.

## Method (measure.py)
- Shark mask per frame: non-white pixels (255 - min RGB > 30) below y=760 (the boat is entirely above y≈645), components > 40 px.
- Pixel acceleration: quadratic fit of x(frame) over frames 1–72 (motion starts at frame 1):
  - snout -0.1497, bbox centre -0.1490, mask centroid -0.1494 px/frame^2 (rms residual about 0.5 px).
  - Halves (1–36, 36–72): -0.145 to -0.151. Cubic fits give a nearly constant acceleration, so it is uniform.
  - I use a = 0.1494 px/frame^2 = 86.1 px/s^2.
- Scale: 1 m/s^2 / 86.1 px/s^2 = 0.01162 m/px.
- Shark height (bbox from dorsal fin top to pectoral fin bottom): 104 px (median; range 103–106) at threshold 30, and 105 px in
  the scene record (threshold 12). I use 104.5 px.

## Answer
height = 104.5 x 0.01162 = **1.217 m**

## Checks
- The three reference points (snout, bbox centre, centroid) and both half-windows agree on the acceleration within ±2 %.
- Sanity check: length 278 px gives 3.2 m, which is a plausible shark, and height/length ≈ 0.38 with fins.
- Confidence: high (±3 %).
