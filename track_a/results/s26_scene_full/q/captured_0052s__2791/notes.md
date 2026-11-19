# q_2791 — initial distance yoga ball ↔ shoe (captured_0052s)

The file rate is 24 fps, and question_fps is also 24. "Initial" means frame 0, when the ball is held at rest (frames 0–17).
Lab camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360). Back-projection uses ((u-cx)/f, (v-cy)/f, 1)·depth.

## Measurements
- Ball centre at frame 0: (615.5, 506). This is the widest-chord centre from scene/ and matches the mask at frame 0: left edge 552, right edge ≈680, top 442.
  Apparent diameter ≈128.5 px (frames 0–13).
- Ball at t = 1.0 s (frame 24): centre (571.5, 540), diameter ≈148–151 px (148 measured, local trend ≈150); I used 149.5.
- Shoe (static): centre (285.5, 657.2), from the mean of the bbox centre and the centroid. Depth 2.231 m.
- depth_info gives the ball's depth only at t = 1.0 s (2.612 m). The ball has moved by then, so I had to estimate the depth at frame 0:
  1. Size route: Z0 = 2.612 × (149.5·cos θ24)/(128.5·cos θ0) = 3.00 m. The cos θ factors correct for off-axis widening.
  2. Floor route: the ball's centre stays at constant height above the floor. The camera pitch (6.8°) comes from the shoe
     (centre about 5 cm high) and the ball at frame 24 (radius 0.256 m). This gives Z0 = 2.99 m. The pitch can vary between 4° and 10°, which gives a Z0 range of 2.93–3.06 m.
  I used Z0 = 2.994 m, the mean of the two routes.
- Distance from the ball at frame 0 to the shoe: 1.251 m (size route) and 1.243 m (floor route). **Answer 1.247 m.**
- If the depth at t = 1.0 s (2.612 m) were wrongly used for frame 0, the result would be 1.09 m. I rejected this because the ball is not there at frame 0.

## Caveats
- The velocity prior (2.19 m/s at 1.0 s) is higher than the speed estimated from the change in apparent size (about 1.3 m/s).
  The prior probably comes from noisy per-frame depth. It does not enter this distance.
- Confidence: moderate. The main uncertainty is Z0 (±0.07 m), which moves the answer by about ±4%.
