# Q1630: average speed of the rabbit (m/s)

Prior: deer (the large horned quadruped) speed = 1.277 m/s. depth_info: rabbit 15.798 m at t=0 and 15.852 m at t=1 s.
fps = question_fps = 30. The camera is static, and both animals walk left to right on the same floor line (feet at y≈795–800), so they are at about the same depth.
Tracks come from scene/tracks (mask centroids, frames 0–74). I checked them on a frame sheet.

Measurements (measure.py):
- Rabbit: 7.69 px/frame net (7.71 mean per-frame, including hop jitter). Deer: 7.80 px/frame net (7.87 per-frame).
- Route 1 (scale from the prior): 1.277 / (7.804 × 30) = 0.005454 m/px, which gives a rabbit speed of 7.69 × 30 × 0.005454 ≈ 1.259 m/s.
- Route 2 (depth_info only): I solved for the focal length so that the rabbit's camera-z stays constant between t=0 and t=1 (motion parallel to the image plane). This gives f ≈ 2850–2910 px and z ≈ 15.75 m, so 0.00541–0.00553 m/px, a 3D displacement of 1.22–1.24 m over 0–1 s, and a speed of ≈ 1.25–1.28 m/s.
- The two routes agree to within about 1–2%.

Answer: 1.265 m/s. Confidence: high (within about 3%).
