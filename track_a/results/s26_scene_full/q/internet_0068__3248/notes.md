# q3248 – acorn displacement 2.10 s → 2.20 s (cm)

Prior: acceleration of the acorn 2.00–2.30 s = 0.77 m/s². 2D internet clip, 30 fps (file = question_fps; no retiming).
Frames: 2.00 s = 60, 2.10 s = 63, 2.20 s = 66, 2.30 s = 69. The acorn is fully visible in frames 59–72 and moves horizontally (y constant), so one scale applies.

## Method
Scale = 0.77 m/s² / pixel acceleration over frames 60–69. Displacement = x(66) − x(63) in pixels × scale.

Three position tracks were used (camera drift corrected; it is only ~4–6 px and nearly constant):
- record `ref_bbox_cx` (bbox centre),
- my own blur-invariant centroid of the background-subtracted cap darkness (`centroid.py`); motion blur is a convolution, so it keeps the centroid,
- record `ref_stem_x` (stem knob), plus my own re-measurement of it (`measure.py`).

Frame 61 is an edited/anomalous frame: its position differs by about 15 px between trackers and makes the step sequence zigzag. I excluded it and fit quadratics to the positions (`fit_ex61.py`), instead of using the raw second difference (v69 − v60), which depends heavily on frame 61.

## Key numbers
- Displacement 63→66: 318 px (stem), 320 px (bbox), 321.4 px (centroid). These are consistent.
- Pixel acceleration, quadratic fit without frame 61:
  - bbox: 4337–4414 px/s² (windows 59–72, 60–69, 60–70, 59–70)
  - centroid: 4279–4397 px/s²
  - stem: 3278–3938 px/s²
- A second route agrees: the per-frame steps grow from 84.6 px (59→60) to 143.7 px (71→72). That is 4.9 px/frame², or about 4400 px/s².
- With a ≈ 4360 px/s²: scale = 1.77e-4 m/px, and the displacement = 320 px → 5.65 cm.

## Confidence
Bbox and centroid agree within about 2% (5.58–5.78 cm). The stem marker gives lower accelerations (6.2–7.5 cm). The knob probably wobbles relative to the body, or its narrow band is blurred, so I gave it less weight. If annotators used a stem-like point and the raw v69 − v60, the answer could be about 6.4–6.7 cm. Overall uncertainty is about ±10%.
