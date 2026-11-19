# q_896 — speed of the pen at t = 0.4 s

- The file runs at 24 fps, but question_fps is 30, so every time is converted at 30 fps: t = 0.4 s → frame 12. The speed is (cy12 − cy11) × 30 × scale.
- This is a 2D scene: the pen falls straight down, cx stays at about 1025, and the camera is static.
- The scale comes from the prior (g = 9.8 m/s² before 0.5 s, i.e. frames 0–15 at 30 fps).

## Measurement (`measure.py`)
- I re-measured the pen centre in frames 3–15 myself. Method: difference against frame 0 inside columns 970–1080, keep rows with at least 15 changed pixels, then take the bbox centre and the pixel-weighted centre. The results match `scene/tracks/pen.csv` within 1 px.
- A quadratic fit over frames 3–15 gives a = 6.85 px/frame² (both centre definitions agree). Residuals are ≤ 0.6 px.
  - The velocity extrapolates to zero at frame −0.12, consistent with release at t = 0 under the 30 fps time base.
- Scale = 9.8 / (6.85 × 30²) = 1.589e-3 m/px.
  - Sanity check: the pen's length (65.3 px) then comes out at 0.104 m, which is plausible for a pen.
- Speed at frame 12:
  - Raw backward difference: 79.0–79.7 px/frame → 3.77–3.80 m/s.
  - Fitted backward difference: 3.797–3.799 m/s.
- Second route: physics alone gives g × (12 − 0.5 + 0.12)/30 = 3.80 m/s, which agrees.

**Answer: 3.80 m/s.** Confidence is high, provided the 30 fps time base is right. Under 24 fps the answer would instead be about 9.8 × 11.6/24 ≈ 4.75 m/s, but the rules say to use question_fps.
