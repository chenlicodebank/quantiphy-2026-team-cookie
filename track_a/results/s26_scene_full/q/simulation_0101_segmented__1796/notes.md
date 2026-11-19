# q_1796 — initial speed of the shark (prior: shark acceleration = 1 m/s^2)

2D segmentation clip, 24 fps (file fps = question_fps, no re-timing). The shark swims left at constant y and speeds up.

Method (measure.py, fit.py): segmented the shark in every frame (non-white mask, rows 760+), and tracked four
reference points: snout x, mask centroid, head-region centroid, and sub-pixel template match of the head. Then I fit
x(t) = x0 + v0 t + a t^2 / 2 with t = frame/24 over frames 1–72, 2–72 and 5–72. The cubic terms are negligible
(|c3| < 0.35) and the rms is 0.3–0.9 px, so the acceleration is uniform.

Scale: one m/px scale from the prior, m/px = 1 / a_px. So initial speed = |v0_px / a_px| (in seconds) x 1 m/s^2.

| reference | a (px/s^2) | v(t=0) (px/s) | v0/a (s) |
|---|---|---|---|
| snout | -86.0 | -171.8 | 1.997–2.000 |
| centroid | -86.0 | -172.1 | 2.001 |
| head centroid | -86.1 | -172.0 | 1.996 |
| head template | -87.5 | -173.4 | 1.981 |
| tail tip | -85.9 | -172.1 | 2.003 |

Second route: fits that start at frame 5 (leaving out the first frames) and fits from different body points agree
within 1 %. The values at frame 1 (t = 1/24) are about 2.04 instead. Under the benchmark's uniform-acceleration
convention, the initial speed is the t=0 value, v0/a = 2.00 s.
The scene px/s^2 ≈ 86, so 1 m ≈ 86 px and the shark is about 279/86 ≈ 3.2 m long. That is plausible.

Answer: 2.0 m/s. Confidence: high (about ±2 %).
