# q_2416 — velocity of the book at t = 1.2 s (cm/s)

Time base: question_fps = file fps = 24 → t = 1.2 s is frame round(28.8) = 29. The book is still sliding down the
ramp (it reaches the bottom edge at f30 and drops onto the table at f31–33).

Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360). Track: scene/tracks/book.csv ref_x/ref_y
(bbox centre). I checked it by eye on f27 and f29 at 3× zoom: the box encloses the book (f29 y ≈ 405–462).

## Route C (main), measure_c.py
I built the ramp plane from depth_info: the far edge centre (589, 358) is at 1.201 m and the near edge centre
(583.5, 479.5) at 0.9555 m, and the edge direction comes from the corners. Checks: the top and bottom widths come
out equal (0.220 / 0.221 m), so the geometry is consistent; the slope is about 30°. The book-centre ray hits this
plane at 1.0275 m at f29, against 1.02 m given. I calibrated the offset so f29 = 1.02 m (book centre 4 mm above the
board) and back-projected f18–30 onto that plane.
Per-frame 3D speeds (backward difference, m/s): f25 0.49, f26 0.54, f27 0.64, f28 0.70, f29 0.77, f30 0.81.
- Forward difference at f29: 0.810 m/s. Central difference: 0.792. Backward difference: 0.774.
- A quadratic fit of position along the ramp over f21–30 gives a = 1.90 m/s² and v(f29) = 0.815 m/s. A linear fit
  of speed gives a = 1.87 m/s² and v = 0.81 at the forward-difference midpoint.
- I left out frames from f31 on: the book is leaving the ramp there, so the plane constraint stops holding.

## Route A/B checks, measure.py
- A: book moves on a line parallel to the ramp through the f29 point. Same speeds (forward 0.814, central 0.794).
- B: depth from apparent length (L × D = const, calibrated at f29: 146.9; given depths imply 143 at f34 and 150 at
  f38). This route is noisier: backward 0.83, forward 0.70, linear fit 0.82–0.87.

The prior (a = 2.8 m/s² at 1.4 s) is in the landing/table phase, so it cannot be checked against the ramp slide
(a ≈ 1.9 m/s²).

## Answer
v(1.2 s) ≈ 0.80 m/s = **80 cm/s**. This sits between the forward (81), central (79) and fitted (81) values. I'd put
the uncertainty at about ±5%.
