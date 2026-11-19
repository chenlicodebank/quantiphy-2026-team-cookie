# q_2433 — book displacement 1.0 s → 1.6 s (cm)

File fps = question fps = 24. Frames: t=1.0 → frame 24 (book sliding down the white-board ramp), t=1.6 → frame 38 (book at rest on table).
Lab camera: f = 0.5959*1280 = 763 px, principal point (640,360).

Track (scene/tracks/blue_book.csv) checked on zoomed frames 24 and 38 — mask centroid matches the book:
f24 centroid (590.9, 384.0), f38 (563.1, 494.9); bbox centres within 4 px.

Depth at f38 = 0.851 m (given, t=1.6). Depth at f24 not given → estimated:
- Route B (geometry, measure.py / check_slope.py): slope endpoints back-projected from depth_info (top edge centre (588,356) @1.201 m,
  bottom (585,481) @0.9555 m) give the ramp direction; line parallel to it through the book centre at f29 (t=1.2, 1.02 m).
  Intersecting the f24 ray → depth 1.123 m. (Surface line w/o anchor → 1.133 m.) Uniform acceleration along the ramp fits with 0.7 mm rms.
- Route A (apparent length ∝ 1/depth): L*d/f across slope frames 25–29 ≈ 0.191 m → d24 = 0.191*763/129.3 ≈ 1.13 m.
  Calibrating on the table rest length gives 1.17 m, but there the visible length is the front edge (nearer than centre), so it is biased high.
- Adopted d24 ≈ 1.127 m.

Displacement = |bp(f38, 0.851) − bp(f24, d24)|: 30.7 cm (d=1.123), 31.2 (1.13), 33.2 (1.15), 35.2 (1.17).
Answer: 31.0 cm. Confidence moderate: answer is sensitive to the unknown depth at t=1.0 (~2.3 cm per 0.01 m of depth).
The prior (acceleration 2.8 m/s² at t=1.4) is during the tip/landing and was not usable for scale.
