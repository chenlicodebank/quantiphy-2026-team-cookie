# Q155: height of the car (prior: car length = 5.67 m)

This is a 2D side-view clip at 24 fps, and question_fps is also 24, so the time base doesn't matter for a size question.
Because the prior and the question are about the same object, the answer is the prior scaled by the car's height-to-length pixel ratio.

Script: `measure_car.py`. It segments the car against the background colour (80,81,88) in every frame,
using thresholds of 12, 25 and 40, plus a soft-coverage subpixel extent.
- Frames 0–5, where the car is near the image centre and perspective foreshortening is smallest:
  - Length: 91–92 px (threshold 25/40) and 91.0–91.7 px (soft).
  - Height: 30 px (threshold 25/40) and 29.1–29.5 px (soft).
  - Height/length ratio: 0.319–0.330.
- As the car moves off-centre, its apparent length grows to 97 px because more of the front/back shows.
  The height stays 30 px, so later frames would bias the ratio low (0.306–0.313).

Ratio used: 0.322 (the mean of the soft and thresholded values near the centre). Height = 5.67 × 0.322 ≈ 1.83 m.
Check: the binary threshold-25 extents at frame 0 (30/92) give 1.85 m, and the soft extents give 1.81–1.83 m.
The real Cybertruck's ratio (1.79/5.68) gives 1.79 m, which supports the result.
Confidence: about ±3%.
