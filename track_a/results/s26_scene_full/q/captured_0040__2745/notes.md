# q2745 – distance travelled by the white ball, 1.5 s → 1.9 s (cm)

- question_fps = file fps = 24 → frames 36 → 46 (round(1.9×24)=46). The interval includes the 2nd bounce (frame 41).
- Ball centres: scene/tracks/ball.csv (mask centroids), checked on zoomed crops of frames 36, 38, 41, 44, 46
  (view.py → frames/check.png); every one sits on the ball. Frame 36 overlaps the cup rim, so its centroid may be about 2 px high (negligible).
- Camera: f = 0.5959×1280 = 762.8 px, principal point (640,360).
- Depth: given 0.7045 m at t=1.5 (f36) and 0.627 m at t=2.0 (f48), linearly interpolated per frame (the ball's
  horizontal image speed is nearly constant, so depth is roughly linear in time). Depth changes by only about 0.65 cm per frame,
  so this assumption has little effect.
- Back-projected 3D centres → per-frame displacements (cm): 2.94 3.67 4.53 5.78 3.70 5.29 4.39 3.25 2.86 2.92.
- **Path length (raw sum) = 39.3 cm** (measure.py).
- Checks: Savitzky-Golay (5 frames) smoothing within each bounce segment (not across the bounce) gives 40.0 cm;
  constant depth 0.67 m with image motion only gives 40.5 cm; a 5-frame moving average across the bounce
  gives 33.2 cm, but it cuts the bounce corner, so I rejected it. Net displacement = 29.4 cm.
- Answer 39.3 cm. Confidence: moderate-good (±5%).
