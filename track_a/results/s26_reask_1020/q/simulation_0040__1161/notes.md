# Q1161 — eagle speed at t = 1.0 s (frame 24, question_fps = file fps = 24)

Prior: eagle length = 0.8 m. depth_info: eagle 179.2691 m (t=1), 177.1009 m (t=2); man 182.92 / 183.02 m.

## Scale (focal length)
- `measure.py`: per-frame bird mask (darkness fraction > 0.5 vs median background), extent of the mask projected on
  the flight heading (= tail tip to beak tip; crops in frames/crops.png show tail fan left, beak right).
  Frames 8-48 on sand (excl. 23-24, merged with man's shadow): median 28.35 px, sd 0.63, n = 39.
  Over water (49-66) contrast is lower → ~26 px, not used.
- f = 28.35 px x 179.27 m / 0.8 m ≈ 6350 px (bird is near the image centre, off-axis < 2°).
- Checks: max projected wingspan 62.8 px → 1.77 m (eagle, plausible); man at 183 m walks ~1.5 px/frame → ~1.04 m/s
  (slow walk, plausible).

## Speed
- `speed.py`: 3D origin positions = depth (linear interpolation/extrapolation of the two given eagle distances) x unit
  ray through the scene-record mask centroid (cx, cy), principal point at the image centre.
- Raw one-frame speeds around frame 24 are noisy (centroid wobbles with wing beat; frames 23-24 merged with shadow):
  10.6-12.5 m/s. Linear fits of position over ±4…±12 frames about frame 24: 11.64-11.58 m/s; quadratic fit 11.58;
  1-s chord 24→48: 11.63 m/s; chord 4→24: 11.36 m/s. Radial component -2.17 m/s is included.
- Answer 11.6 m/s. Sensitivity: ±1 px in body length → ±0.4 m/s (±3.5 %).

Confidence: moderate-high; main uncertainty is the pixel body length (prior object) used for f.
