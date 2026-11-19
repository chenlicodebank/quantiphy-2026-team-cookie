# Q895 — speed of the pen at t = 0.2 s

- 2D falling pen, static camera. The file is 24 fps, but the question says question_fps = 30, so all time↔frame conversions use 30 fps: t = 0.2 s → frame 6.
- I re-measured the pen myself (`measure.py`): the mask is |frame − frame0| > 20 in columns 960–1090, frames 3–15 (free fall). The centre is the bbox centre. My values match scene/tracks/pen.csv within 0.5 px.
- Quadratic fit of cy(frame): a = 6.852 px/frame² (the centroid route gives 6.850), residuals < 0.65 px, and velocity is zero at frame −0.12.
- Scale from the prior (g = 9.8 m/s²) at 30 fps: m/px = 9.8 / (6.852 × 900) = 1.589e-3. Check: the 65 px pen comes out at 0.104 m long, which is plausible.
- Speed at frame 6 is the backward difference (p6 − p5) × 30:
  - from the fit: 23.11 px/frame → 1.837 m/s
  - from the raw cy difference: 38.0 px → 1.81 m/s
  - These agree with the physics check g·(5.5 + 0.12)/30 = 1.836 m/s.
- If 24 fps were used instead (frame 5), the answer would be about 1.89 m/s, so it depends little on this choice.
- Answer: 1.84 m/s. Confidence: high.
