# Q1011 – displacement of the fish from 0.5 s to 1.0 s (m)

- 2D top-down render, 24 fps (file fps = question_fps, so no re-timing). t=0.5 s -> frame 12, t=1.0 s -> frame 24.
- Prior: fish speed 0.67 m/s (constant swim: per-frame shift from the template-match track is 23.5–24.0 px/frame,
  mean 23.80 px/frame over frames 2–70).
- Script `disp.py` (reads scene/tracks/koi_fish.csv, match_x/match_y column = subpixel template-match path).
  - Scale: 0.67 m/s / 24 fps / 23.80 px/frame = 1.173e-3 m/px (using the frames 13–24 mean of 23.77 px/frame: 1.175e-3).
  - Net displacement frames 12→24: 285.04 px (path length 285.21 px, i.e. nearly straight).
  - Displacement = 285.04 × 1.173e-3 = 0.334 m (0.335 with local speed; 0.332–0.338 using the instantaneous speed at
    frame 12 or 24 as the scale).
- Second route: because the speed is constant and the path is almost straight (net/path = 0.9994), displacement ≈
  0.67 m/s × 0.5 s × 0.9994 = 0.335 m. Body-mask centroid (noisier, ±3 px/frame jitter) gives 276 px → 0.324 m.
- Answer: 0.335 m. Confidence high (±2 %).
