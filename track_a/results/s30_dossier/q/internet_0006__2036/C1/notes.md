# q2036 – length of the white car (prior: lane width = 3.66 m)

Top-down static drone shot, 2D/planar convention: one m/px scale from the lane width.

- Lane width (measure.py; column intensity profiles of a 4-frame median, half-intensity asphalt edges):
  rows 1250-1340: 525 → 598 (73 px), centre line x≈559; rows 1450-1600: 520 → 597 (77 px), centre 558.5
  (lanes 38 / 38.5 px); rows 900-1000: 72.5 px; rows 600-700: 75.5 px. Road ≈ 75 px → lane ≈ 37.5 px.
  Scale = 3.66 / 37.5 = 0.0976 m/px.
- White car length, bumper to bumper (carlen.py over scene tracks, clean masks): 79 px near y 1200-1500,
  77 at 800-1200, 76 at 400-800 (82 near top edge = lens stretch, ignored); visual check on frame 0
  ≈ 75-79 px. Used 77 px.
- Length = 77 × 0.0976 = 7.5 m.
- Second route (mid-frame, y 500-1000): car 76 px, local road ≈ 74 px → lane 37 px → 76 × 3.66/37 = 7.52 m.
- Sanity: real car ~4.7 m; this narrow road's lanes are really ~2.3 m, so the prior inflates the scale.
  Following the benchmark convention (prior is exact), answer 7.5 m. Confidence moderate (±5 % from
  edge definitions).
