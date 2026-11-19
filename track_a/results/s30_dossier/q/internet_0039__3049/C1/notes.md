# q_3049 – acceleration of the swimmer, 0–2.33 s

- Scale: prior height 1.68 m = body length from cap top to feet, median 1041 px (scene record; frame 0 checked by eye at about 990–1010 px). That gives 1.614e-3 m/px. As a sanity check, the lane width of 1364 px comes to about 2.2 m, which is plausible.
- Camera is static (scene record). The swimmer moves in -y.
- Time base: question_fps = 25 (file 18.54 fps, with duplicate frames 1, 11, 20, ...). At 25 fps the swimmer moves at 0.75 m/s with a stroke cycle of 2.24 s. At 18.54 fps it would be 0.56 m/s with a 3.0 s cycle. 25 fps is the more natural fit, so 2.33 s = frame 58.
- Measurements (acc.py; duplicate frames replaced by the mean of their neighbours for differencing):
  - Speed at start vs. end, slope over 7 frames: head 0.81→0.88 m/s (+0.03 m/s²), hip 0.72→0.97 (+0.11), mask centroid 0.63→0.82 (+0.085).
  - One-frame forward-difference endpoints: head +0.15, hip +0.097, centroid +0.057 m/s².
  - Quadratic fit over frames 0–58: about 0 (−0.01 to +0.03). The speed is essentially constant, with an oscillation within each stroke.
- Answer: about 0.1 m/s² (the median of the endpoint estimates). Confidence is low: the true mean acceleration is close to zero, and the reference value depends on how the annotator picked the endpoints. If the file's duplicate frame 1 had been used (v0 = 0), the value would be about 0.35.
