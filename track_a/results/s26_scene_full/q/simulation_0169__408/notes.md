# Q408 — astronaut acceleration at t = 3 s (frame 72), fps 24 (file = question fps)

- 2D scene, static camera, astronaut moves up the image along a nearly straight path with Blender ease-in/ease-out;
  body length along axis stable (~91.5 px) → no depth change.
- Scale: upright height at frame 0 = 91 px (head top y≈477 to feet y≈568, checked on a zoomed crop frames/f0.png;
  record bbox_h 90-91) → 2.2 m / 91 px = 0.02418 m/px.
- Track: scene/tracks/astronaut.csv centroids, projected on the net-motion direction (fit.py).
- Route 1: global smoothstep (Bezier auto-clamped ease) fit, frames -0.3 → 78.2, D = 274.8 px, rms 0.27 px.
  Discrete speed(72) - speed(71) = -0.218 px/frame²; analytic -0.225.
- Route 2: local quadratic/cubic fits around frame 72 (±6, ±8, ±10 frames): -0.199 … -0.209 px/frame².
- Adopted -0.212 px/frame² → ×576 = 122 px/s² → ×0.02418 = 2.95 m/s² (deceleration; magnitude reported).
- Confidence: moderate-good, routes span 2.77-3.13 m/s² (±6%).
