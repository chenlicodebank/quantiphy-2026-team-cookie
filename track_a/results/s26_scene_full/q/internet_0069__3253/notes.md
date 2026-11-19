# q3253 – velocity of the cup at 2.10 s (prior: a = 0.32 m/s^2 over 2.00–2.30 s)

Time base: file 30.013 fps vs question 30.0 fps. The difference is negligible, so I used 30 fps. 2.00 s is frame 60, 2.10 s is frame 63 and 2.30 s is frame 69.
Camera: static to within a few px (scene/tracks/camera.csv). The mug moves 65–80 px/frame.

## Method (internet convention: one scale from the prior)
- track.py: the mug's frame-to-frame displacement comes from template matching. I took the body region of frame i (rows 700–1000, edges from
  a background-difference mask) and matched it in frame i+1, with sub-pixel peak and NCC > 0.99. I also found sub-pixel body
  edges from the background difference in three bands.
- Forward-difference velocity (px/frame): f60 65.25, 61 66.91, 62 67.42, 63 68.53, 64 70.15, 65 71.94, 66 73.05,
  67 75.28, 68 76.87, 69 79.14.
- Pixel acceleration over frames 60–69 (linear fit of v): 1360 px/s^2. The endpoint difference (v69 − v60)/9 frames gives 1389.
- Scale = 0.32 / 1360 m/px/s^2 → 2.35e-4 m/px.
- v(2.10 s) = v63 = 68.53 px/frame = 2056 px/s → **0.484 m/s**.

## Second route
I used edge tracks instead of template matching:
- Left-edge forward differences: a = 1220–1414, v63 = 2160 → 0.49–0.57 m/s.
- Right-edge forward differences: a = 1360–1450, v63 = 2028 → 0.45–0.48 m/s.
- Endpoint-acceleration convention with template matching: 0.474 m/s.

Template matching is the least noisy route, so I kept 0.484. The answer depends on the ratio v/a, which is noisy because
the acceleration is small over only 9 frames. Confidence: moderate (about ±8%).
