# Q1225 – average walking speed of the person, 1.0–2.0 s (frames 30–60, question_fps = file fps = 30)

Scripts: `fit.py`, `fit2.py` (they read scene/tracks/man.csv and car.csv).

## Pixel motion
Man pelvis_x (head centre + 3 px, smooth) goes from 981.0 (frame 30) to 873.5 (frame 60): mean per-frame step 3.583 px,
always in the same direction and roughly steady. His apparent height (~370 px) stays constant, so his depth is constant.

## Focal length (pinhole, principal point at the image centre 540,540)
1. **Man, two depths**: d = Z·sqrt(1 + r²/f²) with constant Z. Using d(0) = 8.313 at u = 1071 and d(1) = 8.189 at u = 981
   (v ≈ 748) gives **f ≈ 1630 px, Z_man ≈ 7.85 m**.
2. **Car, acceleration prior**: a quadratic fit to the clean rear-edge part of the car track (frames 49–77, rms
   0.15 px) gives a = −438 px/s², so the scale is 2.86/438 = 0.00653 m/px. Combining that with d(1 s) = 11.671 gives Z_car ≈ 10.73 m and
   **f ≈ 1645 px**. Check: the predicted d(0) = 15.94 vs the given 16.059 (0.7 %), and the car length comes out at 4.83 m
   (plausible). The front-edge part of the track (frames 28–48: blurred nose, noisy steps) gives an inconsistent
   value (f ≈ 1130, car 6.5 m long, d0 17.7), so I rejected it.
The two independent routes agree within 1 %, so I used f ≈ 1638.
(Hydrant/streetlight distances: their origin heights are unknown. If both origins are at the object centres, f ≈ 1465;
other origin choices give inconsistent values. I did not use them.)

## Answer
Scale at the man's depth: Z/f = 7.85/1638 ≈ 0.00479 m/px, giving speed = 3.583 px/frame × 30 × 0.00479 ≈ 0.515 m/s (0.509–0.526
for f between 1600 and 1660). Adding the small vertical pelvis bob, which the per-frame speed convention counts, gives
≈ 0.52–0.53. Sanity check: the man is 370 px × 0.00479 ≈ 1.77 m tall, which is plausible.
**Answer: 0.52 m/s.** Confidence: fairly good (about ±5 %).
