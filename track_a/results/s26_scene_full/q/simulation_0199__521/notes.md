# Q521: droplet speed at t = 0.05 s (2D video, prior a = 9.7 m/s^2)

Time base: fps = question_fps = 60, so t = 0.05 s is frame 3. The speed is the backward difference p(3) - p(2), times fps.

Scale: a single metres-per-pixel factor from the prior acceleration. A pixel acceleration a_px (px/frame^2) corresponds
to 9.7 m/s^2, so speed = step_px * 60 * 9.7 / (a_px * 3600) = (step_px / a_px) * 9.7 / 60.

Measurements (`fit.py` uses scene/tracks/droplet.csv; I checked that the record's mask is clean, with area about 3200 px
in every frame, and that it is the falling drop):
- The top edge y0 steps by 18, 48, 80, 112, 144, 176, 207, 240, 271 and 304 px per frame. That is 16·(2k-1), uniform
  acceleration from rest at t = 0, with a_px of about 31.9 px/f^2. So step(2→3) / a_px = 2.51.
- The centroid cy: a quadratic fit over frames 2–10 gives a_px = 31.3 and a step of 81.35, ratio 2.60. Over frames 0–7
  the ratio is 2.53. The bottom edge gives 2.55–2.61 and the bbox centre 2.54–2.57.
- The horizontal drift is about 1.5 px/frame, which is negligible (it adds 0.01 px to the 81 px step).
- Ratios lie in 2.51–2.60 (the ideal model gives 2.5), so speed = 0.404–0.420 m/s. Raw centroid step / fitted
  2D acceleration gives 0.418.
- My own re-segmentation (`measure.py`, which has no hole filling for the transparent drop) is noisier, but its top-edge
  fit agrees: a = 31.8 px/f², v(3) ≈ 96 px/f, so a·t ≈ 3.0·a.

Answer: 0.41 m/s (backward-difference convention). Note that the instantaneous speed a·t = 9.7 × 0.05 = 0.485 m/s would be
the answer under a continuous-time convention. I used the paper's backward-difference definition.
Confidence: high for the backward-difference value (±2%).
