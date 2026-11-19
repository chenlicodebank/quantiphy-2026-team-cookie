# Q118 – length of the car (m); prior: car acceleration = 4.03 m/s^2

2D top-down Blender render at 24 fps. question_fps is also 24, so no re-timing is involved. The scale comes from the car's pixel acceleration.

## Measurements (scripts: edge.py, fit*.py, steps.py)
- **Edge tracking.** `edge.py` compares each frame with the empty frame 71 (|diff| > 30). It takes the column-coverage profile of the car's core rows (y 592–712) and finds the front (left) and rear (right) edges with subpixel precision. The results are in `edges.csv`.
- **Blur correction.** The car's midpoint, (front + rear)/2, cancels the symmetric motion-blur smear of the two edges.
- **Quadratic fits of the midpoint** (acceleration in px/frame^2):
  - frames 2–20: 0.540
  - frames 20–40: 0.533 (rms 0.12 px)
  - frames 2–30: 0.527
  - frames 15–45: 0.533
  - frames 2–57: 0.539
  - Frames 40–57 give a higher value (0.64), but the fit is poor (rms 0.7 px). There are edge glitches there (for example, the rear-edge step at frame 49) and the front edge is close to the image border. The rear edge alone over frames 56–68 gives 0.54 again, so I treat 40–57 as a measurement artifact rather than a real change in acceleration.
- **Adopted value:** a ≈ 0.536 px/frame^2 = 0.536 × 24² = 308.8 px/s^2.
- **Scale:** 4.03 / 308.8 = 0.01305 m/px.
- **Car pixel length** at rest (frame 0, sharp): front bumper x ≈ 874 to tailgate x ≈ 1311.5, so 437.5 px (bbox 438 px).
- **Length** = 437.5 × 0.01305 = **5.71–5.74 m**. Answer: 5.72 m.

## Checks
- **Range of fits.** The acceleration fits span 0.527–0.540 px/f^2, which gives lengths of 5.67–5.81 m.
- **Second route: the cyclist** at the same scale. Bicycle length 129 px gives 1.69 m and its speed 16 px/frame gives 5.0 m/s. Both are plausible.
- **Real-world sanity check.** The car is a Cybertruck-style pickup, and the real one is about 5.68 m long, which is consistent.

Confidence: good (about ±3%).
