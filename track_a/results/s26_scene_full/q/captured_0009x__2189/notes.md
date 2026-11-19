# Q2189 – basketball velocity at t = 1.8 s (frame 43, 24 fps; file fps = question fps = 24)

Phase: ball rebounding upward after floor bounce (f37), apex at f46 (t=1.917 s, matches depth_info "1.92 s max rebounce").

## Measurements (measure.py, route2.py)
- Re-measured centres/diameters f36-48 (circle fit on SAM mask): agree with scene/tracks within ~1 px (centre).
  f43: (529.3, 504.0), diameter ~103-108 px; apex image-y vertex at frame 46.02 (t = 1.9176 s).
- Route A (lab method card, depth_info only, depth ~1.58 m nearly constant on rebound): image-plane-only speeds
  give fwd 0.63 / bwd 0.87 / 5-frame smoothed 0.60 m/s, but the implied acceleration is only ~4.9 m/s^2 – half the
  prior's 9.8. The ball's apparent diameter grows 3.5 % from f43 to f46, i.e. the camera looks down and much of the
  vertical motion is along the line of sight; the two depth_info values (1.5835 / 1.5795) don't capture it. Route A
  therefore underestimates and is rejected.
- Route B (physics with prior): v = g * (t_apex - 1.8) = 9.8 * 0.1176 = 1.15 m/s (1.176 with the stated 1.92 s);
  horizontal drift adds <0.1 m/s in quadrature (negligible).
- Route C (3D from apparent size, scale fixed so |a| = 9.8): v(1.8) = 1.14-1.46 depending on window/diameter
  measure; bbox_w diameters (more reliable) give 1.14-1.26.
- A forward-difference convention (v at t=43.5 frames) would give ~1.02.

Answer: 1.15 m/s. Confidence: moderate (reference pipeline depth treatment unknown; physics routes agree ~1.15-1.25).
