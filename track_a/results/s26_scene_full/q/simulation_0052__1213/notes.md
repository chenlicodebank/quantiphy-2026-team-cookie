# Q1213 – speed of the green car at t = 1.0 s (frame 30)

The green car is the very dark green vintage coupe that the scene record calls `black_car`. It is in the near lane and
moves at a constant pixel speed. The file is at 30.0033 fps. I used question_fps = 30 for every conversion (t = 1 s is
frame 30, t = 2 s is frame 60).

## Pixel measurements (from the scene/ tracks, checked on frames 30 and 39)
- Green car: hub-midpoint linear fit over the measured frames 28-49 gives -69.84 px/frame (rms 0.8 px). A quadratic
  fit gives at most ~0.3 % speed change at frame 30, which I ignored. u(f30) = 1110.9, u(f60) = -984.3 (constant-speed
  extrapolation, off-screen).
- Orange car: a quadratic fit of the hub midpoint gives 0.3346 px/frame² (sub-windows give 0.3307-0.3375).
  u(f0) = 1345.0 (fit), u(f30) = 621.3.

## Scale (pinhole, principal point at the image centre)
- From the prior: Zo/f = 2.86 / (0.3346 x 30²) = 0.009497 m/px at the orange car's depth.
- Orange depths: with 17.260 m at t=0 and 15.436 m at t=1, each depth gives its own Zo: 15.35 m and 15.29 m.
  So f ≈ 1610-1616 px. The two depths agree, which checks that the prior and depth_info are consistent.
- Joint solve with 5 equations and 5 unknowns: f, Zo, Zg and the two cars' origin offsets along x. The equations are
  the two orange depths, the two green depths and the prior scale. It gives f = 1609 px, Zg = 9.37 m and a
  green-origin offset of ~+68 px toward the rear. Speed = 69.84 x 30 x 9.37 / 1609 = **12.20 m/s**.
  - Varying the origin row (hub, ground or body-centre) gives 12.19-12.26 m/s.
  - Varying the orange acceleration window gives 12.13-12.30 m/s.
- Second route: use only the green depth at t=1 (no extrapolation to f60, origin offset 0) with f from the orange car.
  This gives Zg = 9.45-9.51 m and a speed of 12.31-12.36 m/s.
- Route that does not hold up: a green-only solution (both green depths, offset 0, no orange information) gives
  11.29 m/s. It implies f ≈ 1790 px, which contradicts the orange data (it would predict an orange depth of 18.7 m
  instead of 17.26 m). The likely cause is the green rig origin sitting ~65 px (≈0.4 m) behind the wheelbase centre,
  so I rejected this route.

## Answer
12.25 m/s, the middle of the 12.13-12.36 range. Confidence: good, about ±3 %.
