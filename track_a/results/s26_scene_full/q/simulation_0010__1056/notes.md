# q_1056 – cart wheel diameter (m)

The file plays at 22.892 fps and question_fps is 24. Times are converted to frames with 24 fps (t = 1 s -> frame 24).

## Focal length from the bird (prior L = 1.19 m)
- Bird pixel length = bbox width from scene/tracks/bird.csv (frames 0–52, without heavy occlusion). Depth is
  interpolated linearly between d(f0) = 34.584 and d(f24) = 33.999 (measure.py).
- Lpx·d: median 5361, mean of the wings-level frames (bbox_h < 80, beak-to-tail clearest) 5507, 75th percentile 5637.
  I used about 5500. Converting to z-depth (the bird is off-axis, r²/f² ≤ 2 %) gives Lpx·Z ≈ 5475, so
  **f ≈ 4600 px** (HFOV ≈ 23.6°). Using the median instead gives f ≈ 4505 (−2 %).

## Wheel (frame 0, crops in frames/wheel.png, intensity profiles in measure.py)
- The near wheel is an almost face-on ellipse. Outer rim: top y ≈ 1061, bottom y ≈ 1268 (vertical ≈ 207 px);
  left x ≈ 1631, right x ≈ 1832 (≈ 201 px; slight yaw). Diameter = the vertical/major axis ≈ 207 px.
  Hub centre ≈ (1734, 1163).
- Cart distance 30.374 m. Off-axis factor sqrt(1 + r²/f²) = 1.015 at the wheel, so Z ≈ 29.9 m.
  D = 207 × 29.9 / 4600 = 1.346 m.
- The cart axle points almost along the line of sight, and the cart origin is probably between the wheels, so the
  near wheel is likely about 0.3–0.7 m closer than the origin. That gives D ≈ 1.32. **Answer 1.33 m** (range 1.30–1.37).

## Checks
- With the median bird length (f = 4505), D = 1.37. Each route stays within ±3 %.
- Sanity check: the cart is about 3.9 m long, and the barrels/door are about 1.4× real size. The scene looks
  uniformly scaled up by about 1.3–1.4 from real life, so a 1.33 m wheel is plausible (a real one is about 1 m).
- A second focal route from the bird's two depths, assuming it flies at constant altitude, was too noisy to use
  (the wingbeat makes the y position wobble by ±25 px).
Confidence: moderate. The main uncertainties are the bird's pixel length (±3 %) and the wheel's depth offset from
the cart origin (±2 %).
