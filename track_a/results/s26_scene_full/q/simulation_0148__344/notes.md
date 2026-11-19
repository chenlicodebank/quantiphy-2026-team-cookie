# Q344: speed of the train at t = 0.5 s (m/s)

- fps 24 (file) = question_fps, so t = 0.5 s is frame 12. Speed = shift between frames 11 and 12 × 24.
- Prior: side window (not door window) width = 1.8 m. The side windows are on the train's near side wall, so I used
  the near layer for both the window width and the shift. The train's own scale is the same in every layer, so the
  ratio is not affected by perspective.
- Window width (glass opening, half-level crossings of the median row profile at y 560-680, `edges.py`):
  f7 348, f8 347, f13 353, f15 352 to 354, f17 354 px. I used about 351 px, so 1.8/351 = 5.13e-3 m/px.
- Near-layer shift (`shift.py`, NCC of |x-gradient| column profiles at y 580-680, with the pillar masked):
  f12 = 371.4 px. The scene record gives 371.6 measured and 372.5 from its line fit d(i) = 334.1 + 3.2 i.
  My own shifts for f7-f18 match the record to within about 1 px. I used 371.8 px.
- Speed = 371.8 × 24 × 1.8/351 ≈ 45.8 m/s. With 353 px it is 45.5, so the answer is 45.6 m/s.
- Second check: the window's left edge moves 1467 → 1090 px from f12 to f13 (377 px, the line gives 375.7). That is
  consistent with steady acceleration of about 3.2 px per frame.
- Uncertainty: if "window width" means the outer dark rim (about 367 px) rather than the glass, the speed would be
  about 4% lower (43.8 m/s). The glass opening was chosen. Overall confidence is about ±4%.
