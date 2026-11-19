# Q163: height of the plane (m)

- This is a 2D side-view scene with a static camera. Prior: the car's speed is 30 m/s. fps = question_fps = 24.
- **Car speed in pixels** (measure.py): a linear fit of the bbox centre over unclipped frames 11–37 gives 28.39 px/frame. The rear edge gives 28.54 and the front edge 28.25, and they average to the centre value. 28.39 × 24 = 681.4 px/s.
- **Scale:** 30 / 681.4 = 0.04403 m/px.
- **Plane height in pixels** (measure2.py): I took the largest connected component above the car, with background differences at thresholds 20, 30 and 45. It runs from the fin top (y 300) to the engine-nacelle bottom (y 554). That is 255 px in every frame from 22 to 37 and at every threshold, so it is not affected by perspective.
- **Height** = 255 × 0.04403 = **11.23 m**.
- **Check by a second route:** at the same scale the car's length is 130 px → 5.72 m, which matches a real Cybertruck (5.68 m). The plane's length is 855 px → 37.6 m, which matches a real A320 (37.57 m). The plane's height is close to the real A320 height of about 11.8 m. So the single scale is consistent.
- **Confidence:** high. The answer is within about 2% of 11.2 m.
