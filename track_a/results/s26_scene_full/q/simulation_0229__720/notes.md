# Q720: paper airplane speed at t = 1 s

- I treated this as a 2D scene with a static camera and one metres-per-pixel scale. Frame rate is 24 fps (file and question agree), so t = 1 s is frame 24, and speed = |p24 − p23| × 24.
- **Scale:** the prior is chalkboard length = 5 m. I took that as the board's full bounding box including its wooden frame. measure.py re-measured the edges on the background median: outer frame x = 320 to 1692 (1372 px), green surface 342 to 1670 (1328 px). 5 / 1372 = 3.644 mm/px.
- **Plane position:** measure.py recomputed it with a sharp threshold mask (diff > 25) against the background.
  - Bbox-centre step 23→24: 70.0 px. Neighbouring steps: 69.5 (22→23) and 66.8 (24→25).
  - Centroid step 23→24: 68.5 px.
  - The record's nose–tail midpoint step 23→24: 69.0 px.
  - The motion is almost horizontal at the apex (dy ≈ 0.5 px).
  - Adopted: 69.5 ± 1 px/frame.
- **Speed:** 69.5 × 24 × 0.003644 = 6.08 m/s.
- **Second route:** the three independent reference points (bbox centre, centroid, record midpoint) agree to within ±1.5%.
- **Main uncertainty:** whether "length" means the outer frame or the green surface. Using the green surface (1327 px) would give 6.29 m/s, about 3.4% higher.
- **Confidence:** fairly high.
