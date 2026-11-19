# q_1987 — average speed of the rabbit (m/s)

Prior: speed of the deer (the large horned quadruped, "creature" in scene/) = 1.277 m/s. No depth_info.
question_fps = file fps = 30.

## Method
Both animals walk/hop left→right parallel to the image plane. Their ground contact rows match (deer hooves y≈790–800,
rabbit feet y≈792–803), so they are at about the same depth. I used one pixel scale for both:
v_rabbit = 1.277 × (rabbit px speed / deer px speed). Tracks come from scene/tracks (mask centroids), which I checked
on frame 36. Script: ratio.py.

## Measurements (px/frame)
- Deer: net dx/74 = 7.93, linear fit = 7.90, whole gait cycles 0–40 / 30–70 / 34–74 = 7.86 / 7.88 / 7.89.
- Rabbit: net = 7.73, fit = 7.66, whole hop cycles 3–68 / 9–74 = 7.64 / 7.66. The mean 2D per-frame step is 7.74,
  so vertical motion adds almost nothing.
- Ratio: 0.970 (fits and whole cycles) to 0.975 (net displacement).

## Result
v = 1.277 × 0.972 ≈ 1.24 m/s (range 1.238–1.245).
Second route: net-displacement ratio 7.731/7.930 × 1.277 = 1.245. This agrees with the fit-based 1.238.
Confidence: good. The main risk is a small depth difference between the two animals, which would be a few percent.
