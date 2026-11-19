# q2421 — length of the slope (cm)

File fps 24 = question_fps 24.

Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
White ramp board segmented in frame 48 (book off the ramp) by HSV (S<40, V>200), `measure.py`.
- Far (top) edge: row 357, x 519–657 -> midpoint (588, 357).
- Near (bottom) edge: row 480, x 494–669 (row 478: 494–675) -> midpoint (~583, 480). Rows below 480 are the
  book's cream page block, excluded.
- Back-projected with depth_info: top edge midpoint at 1.2010 m, bottom edge midpoint at 0.9555 m.
- 3D distance = 29.91 cm (±0.5 px edge shifts: 29.83–29.99).

Checks:
- Board width from the same geometry: top 22.5 cm (1.201 m), bottom 22.7 cm (0.9555 m) — consistent, so
  the depths, f and edge rows agree (a rectangular board).
- Slope geometry: vertical drop ≈ 15 cm over 29.9 cm -> ≈30°; prior acceleration 2.8 m/s^2 = g(sin30 − μ cos30)
  gives μ ≈ 0.25, physically plausible.
- scene/ record corners (TL 519,357; TR 659,359; BR 673,479; BL 494,480) match my mask.

Answer: 29.9 cm. Confidence: good (±1 cm), main uncertainty is whether the given depths refer exactly to the
board's edge midpoints.
