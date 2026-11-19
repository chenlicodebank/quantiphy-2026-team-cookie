# q_247 — length of the toy car (m)

Prior: speed of the toy car = 0.05 m/s. 2D top-down scene, static camera (scene/ record confirmed).
fps 24.003175 (question_fps 24.0 — difference 0.01 %, irrelevant).

## Measurements (measure.py, own mask: |frame − median bg| > 30 AND HSV sat > thr, every 5th frame 0–120)
- Speed: uniform straight motion along +x. Linear fit slopes: centroid 2.607–2.616 px/frame, rear edge 2.615–2.618 px/frame
  (scene record 2.617). Use 2.614 px/frame → 62.74 px/s.
- Scale: 0.05 / 62.74 = 7.97e-4 m/px.
- Length along motion: mask bbox median 130 px (sat>85; p25–p75 129–132), 135 px with looser sat>60 (includes shadow edge);
  zoomed grid crop at frame 60 reads the body from x≈247 to ≈373–378 → 126–131 px. Adopt 129 px.

## Answer
L = 129 px × 7.97e-4 m/px = 0.103 m.

## Check
Second route: rear-edge slope (2.615 px/frame) with the frame-60 visual extent (126–131 px) → 0.100–0.104 m. Same as the main route.
Confidence: about ±3 % (comes mostly from the edge blur and shadow at the car's ends).
