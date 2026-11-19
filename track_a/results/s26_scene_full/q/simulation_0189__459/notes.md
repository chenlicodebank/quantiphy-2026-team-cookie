# Q459 — height of the truck at t = 0 s (prior: box speed 0.094 m/s)

2D side view, fps 120 = question_fps (no re-timing). Camera static.

Scale: box centre track (scene/tracks/cardboard_box.csv, re-fitted in speed.py) rises at a constant
19.19 px/s (linear fits over frames 0-100, 100-200, 200-300, 300-400 give 19.20, 19.19, 19.22, 19.18 px/s;
quadratic term ~0, total shift 63.95 px / 400 frames = 19.19 px/s as a second check).
=> 0.094 / 19.19 = 0.004897 m/px.

Truck vertical extent at frame 0 (extent.py, intensity column profiles):
- top: top of the white front post / railing platform, edge at y ≈ 305.5 (x 1462-1500); nothing on the truck higher.
- bottom: tyre ground contact, dark→floor transition at y ≈ 1025.5 (both wheels, x 705 and 1582).
  (Stabilizer foot pads reach y ≈ 1029.)
Height ≈ 720 px → 720 × 0.004897 = 3.53 m (3.54 m if the stabilizer pads are included).

Confidence: medium-high; scale is very clean, edges ±2 px (~0.3%). Main uncertainty is whether the
reference bbox differs (e.g. perspective/depth of box vs truck side), not the measurement.
