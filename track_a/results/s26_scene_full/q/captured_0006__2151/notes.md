# q_2151 — height of the toy (cm)

Prior: a = 9.8 m/s^2 (not needed for a size). depth_info: toy ("ball") at 1.402 m at t=1.0 s (frame 24),
1.065 m at t=1.2 s (frame 29). question_fps = file fps = 24.
Lab camera: f = 0.5959 x 1280 = 762.8 px.

The toy is a yellow plush ring (pineapple-like, its face blurred out by the anonymiser). It is in flight at both depth times.

## Measurement (edges.py)
Toy yellowness = Lab b* minus background median; mask at half the peak; largest blob; bounding box.
(A 30 % threshold also picks up the skin of the hand below the toy, so the height comes out too big; the scene/ csv's
HSV mask, 61x46 at f24, misses the faint upper-left rim.)
- f24 (sharp, near the apex): 55 w x 53 h px -> height = 1.402 x 53 / 762.8 = **9.74 cm** (width 10.1 cm)
- f29 (second route, other depth): 71 px tall (some vertical motion blur) -> 1.065 x 71 / 762.8 = **9.91 cm**
- Check: the toy's apparent size from f24 to f29 grows ~1.3x, which matches the depth ratio 1.402/1.065 = 1.32.
  So the two depths agree with each other.

Answer: about 9.8 cm (the toy looks roughly round, ~10 cm across). Confidence: moderate-good (±5 %). The toy is
slightly tilted in flight and its edges are soft.
