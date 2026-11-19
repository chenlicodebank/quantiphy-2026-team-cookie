# Q1218 – length of the green car (m)

The green car is the "black_car" in scene/ (a very dark green vintage coupe in the near lane, visible f24-53, moving at
a constant speed). File fps is 30.0033 and question_fps is 30; frames are used directly (t=1 s -> f30, t=2 s -> f60).
At f60 the green car is off-screen, so its position there comes from its constant-speed motion.

## Focal length from the orange car (solve.py, solve2.py)
- Orange wheelbase-centre track (scene/): u(f0)=1343.7, u(f30)=621.3. Its pixel acceleration from a quadratic fit
  over f6-79 is 0.3345 px/frame² = 301.0 px/s².
- Two depths only: f=1584, Zo=15.29 -> acceleration 2.906 m/s² (prior 2.86, 1.6% off).
- Two depths plus the exact prior, with a free origin offset: f=1609, Zo=15.29, offset 14 px. So **f ≈ 1585-1610 px**.
  Sanity check: orange wheelbase 323.2 px at near-side depth (~14.5 m) = 2.91 m, which is Kia-Stinger-like.

## Green-car ends (edges.py, final.py)
- I tracked the chrome bumper extremes frame by frame. The front leading edge (rows 790-806, f29-39) moves at
  67.7 px/frame. The rear trailing edge (rows 762-782, f38-46) moves at 65.8 px/frame. The wheel hubs move at
  69.84 px/frame, so the bumper tips are at the car's centre-line depth, behind the near-side wheels.
- Motion blur: the edge ramp is ~32 px, so the shutter is ~0.5 frame (Blender default). Each edge is corrected by
  0.25 frame.
- When an end crosses the image-centre column, its lateral X is 0 whatever its depth. The front crosses at f32.47
  and the rear at f45.19, so the car takes **Δ = 12.73 frames** to pass the centre column.

## Speed and length
- Route 1 (no focal length): I take the origin as the bbox centre, which crosses at tc = 38.83. Then
  d30² − d60² gives V = 0.3956 m/frame (11.9 m/s), and **L = V·Δ = 5.035 m**. The implied focal length is
  f = 1617-1626, which agrees with the orange car's 1585-1610 (independent check).
- Route 2: I fix f from the orange car (1584 / 1610) and solve Zg and the crossing time from the two depths.
  This gives Zg ≈ 9.57-9.61 and tc = 38.9-39.1 (matches the bbox-centre crossing), with L = 5.05-5.13 m.
  The pixel-length route (≈850 px mid-blur at f39 × Zg / f) gives the same values.
- If the origin were the wheelbase centre (tc 38.18), L = 4.79. That case is less consistent: it implies f ≈ 1740,
  which disagrees with the orange car's value.
- Shutter sensitivity: with no blur correction, L would be 5.23.

Answer: **5.05 m** (range ~4.95-5.13). Confidence: moderate-good, about ±4%.
