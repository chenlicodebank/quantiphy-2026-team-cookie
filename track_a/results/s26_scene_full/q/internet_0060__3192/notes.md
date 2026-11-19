# q3192 — velocity of the box (pink packet) at 2.00 s

- Prior: g = 9.8 m/s^2. The packet falls freely along image +x (clip rotated 90°) for frames 52–64, then hits the floor strip at frame 65.
- Time base: question_fps = 30 and file fps = 30.014 are effectively the same. t = 2.00 s → frame 60 (checked visually: packet bbox ~564–675 px in x, matching the track).
- Track: scene/tracks/packet.csv (checked on frame 60). I fitted a quadratic x(t) over the free-fall frames (53/54/55 to 63/64) for the centroid, the background-corrected centroid, the bbox centre and both bbox edges. This gives a_px ≈ 9500–10250 px/s², so scale = 9.8/a_px ≈ 0.00096–0.00103 m/px. That fits the ~100 px packet being about 10 cm.
- Velocity at frame 60, background-corrected centroid with the 54–64 fit (scale 0.000975 m/px):
  - forward difference (x61 − x60), the annotators' convention: 3.44 m/s
  - backward difference: 3.17 m/s
  - derivative of the quadratic fit at t = 2.00 s: 3.27 m/s
- Second route: the bbox edges and bbox centre give forward differences of 3.41–3.65 and fitted values of 3.23–3.57, which agree within about 5%.
- Answer: 3.43 m/s (the forward-difference convention). Confidence: moderate. The range across methods is about ±5%.
