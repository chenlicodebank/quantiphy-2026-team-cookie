# q_536: speed of the magnifying glass at t = 0.125 s

- 2D clip at 24 fps (file fps = question_fps = 24). t = 0.125 s is frame 3. Speed = (y3 - y2) x 24 x scale.
- I tracked frames 0-10 myself in `measure.py`. The mask is |frame - frame 29| > 40, and the reference point is the median per-column vertical centre of the ring (x 985-1075) and of the handle (x 1090-1130). I left out the bbox column because its bottom edge touched the crop limit at y = 949.
- Fitting a parabola to the ring y(t) over frames 0-10 gives a = 7391 px/s^2 (residual 0.22 px). Starting time t0 ≈ 0, so the glass falls from rest at frame 0. The scale is 9.8 / 7391 m/px.
- Route 1: the ring's backward difference at frame 3 is 1.050 m/s, and its fitted backward difference is 1.043 m/s.
- Route 2: on the handle, a = 7639 px/s^2, and the fitted backward difference at frame 3 is 1.060 m/s (direct value 1.047).
- Ideal check: free fall from rest at frame 0 gives 9.8 x 2.5/24 = 1.021 m/s.
- Answer: 1.04 m/s. Confidence: high (within about 3 pct).
- The record in scene/ agrees: its bbox-centre steps are 33 px at frame 3, with about 13 px/frame^2 (scale gives about 1.03 m/s).
