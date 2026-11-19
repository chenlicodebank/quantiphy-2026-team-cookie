# Q446: acceleration of the box from 0 s to 0.3 s

The question's fps (24) matches the file's fps, so every time and frame below uses 24 fps. Frames 0–7 (0–0.29 s) are the free fall from rest. The box lands on the ramp between frames 8 and 9.

## Scale
The prior is the slide acceleration at 1 s: 3.18 m/s². The box slides down the ramp at a steady acceleration.
- Slide acceleration in pixels: a quadratic fit of path length to time over frames 10–37 (from scene/tracks/gift_box.csv) gives 745 px/s². Sub-windows give 10–24: 749, 12–30: 768 and 24–37: 692. The late window is a little lower, probably because of perspective near the image edge.
- The scale is therefore 3.18 / 745 = 0.00427 m/px.

## Fall acceleration
- From the record's centroid y (fit.py): fitting frames 0–7 gives 2335 px/s², frames 0–6 gives 2325 and frames 1–7 gives 2345.
- Independent check (check_fall.py): I took my own difference mask against frame 39 and tracked the top edge of the box. Over frames 0–7 this gives 2318 px/s².
- 2330 px/s² × 0.00427 m/px ≈ 9.9 m/s². Using the early-slide value of 749 px/s² gives about 9.85 m/s².

These numbers sit within about 1% of Blender's gravity, 9.81 m/s². The box falls from rest, so the fall phase should be pure gravity. The answer is 9.81 m/s²; the measured range is 9.7–10.0.

Confidence: high. The answer depends on the ratio of the two accelerations, and that ratio is stable to within about 3%.
