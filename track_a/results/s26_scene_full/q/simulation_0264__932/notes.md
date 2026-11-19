# Q932 — speed of the spacecraft (hover car) at t = 1.0 s

- 2D clip, 24 fps (file fps = question_fps, so there's no re-timing). The only object is the hover car. It moves left from rest with uniform acceleration.
- Prior: a = 4 m/s² (constant). Scale: metres per pixel = 4 / (pixel acceleration).
- `measure.py` re-measured the front edge x0 and the bbox centre using a background difference against the empty frame 71. Its values agree with scene/tracks to within 1–2 px.
- Quadratic fits:
  - x0, frames 4–52: a = 1.139 px/frame², residual sd 0.64 px. The fitted rest point is frame 0.14, i.e. the car starts at t ≈ 0.
  - Backward step at frame 24: 26.6 px/frame.
  - Speed = 4 · step / a / 24 = **3.89 m/s**.
- Checks:
  - Centre track: 3.92 m/s.
  - Local fit, frames 12–36: 3.90 m/s.
  - Cubic fits: 3.83–3.91 m/s.
  - Analytic: start from rest at t = 0, so the backward difference at frame 24 gives a·23.5/24 = 3.917 m/s. The instantaneous value a·t would be 4.0.
- Answer: 3.9 m/s. Confidence is high, within about 3%.
