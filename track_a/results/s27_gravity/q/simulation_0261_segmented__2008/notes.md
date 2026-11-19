# q_2008: mug speed at t = 0.4 s

- This is a 2D video at 24 fps (file rate and question_fps are the same). t = 0.4 s → frame round(9.6) = 10.
- In `measure.py` I re-segmented frames 0–18, from the start of the free fall up to just before impact (f18/19).
  I tracked the bbox centre, the mask centroid, the top edge and the bottom edge.
- **Scale from the prior (g = 9.8 m/s²):** I fitted a quadratic to cy_bbox over f0–18 and got a = 8.85 px/frame²
  (rms 0.57 px). That gives 9.8 / (8.85 × 576) = 1.923e-3 m/px. Over other windows (0–12, 4–18, 6–14) and with the
  centroid, a is 8.81–8.90 px/frame².
- **Speed:** backward difference of the centre between f9 and f10: 528.5 − 443.5 = 85 px/frame → 85 × 24 × 1.923e-3
  = **3.92 m/s**. The centroid gives 3.93. The fitted parabola's velocity at f9.5 (the same quantity, from the fit)
  is 3.90–3.93 across windows.
- **Second route:** the top and bottom edges over the 0–12 and 6–14 windows give 3.89–3.94 m/s. Full free fall from
  the fitted release time (frame ≈ −0.1) is the same thing as the fit itself, so it is not a separate check.
- **Sanity check of the scale:** the mug body is 77 px wide = 0.148 m (0.21 m with the handle). That is a large mug
  but plausible, and the prior is exact.
- Answer: 3.92 m/s. Confidence: high (±2%).
