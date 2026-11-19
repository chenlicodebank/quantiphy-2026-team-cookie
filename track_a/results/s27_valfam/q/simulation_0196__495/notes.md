# q_495: horizontal length of the "SKYNOVA" text (m)

The file is 30 fps and question_fps is 30, so the two rates match. The scene is 2D, so one m/px scale applies.

## Scale (from the prior: bubble speed = 0.00144 m/s)
- The sphere/bubble in the drop sinks at a constant velocity. In scene/tracks/sphere.csv, a linear fit of cy over
  frames 0–49 gives 109.0 px/s.
- Re-checked independently from the raw integer top edge of the mask: 108.6 px/s for frames 0–39.
- Scale = 0.00144 / 109.0 = 1.321e-5 m/px.

## Text (measure_text2.py, frame 24)
- Text mask: the "whiteness" ratio B/R minus its 151 px median background, thresholded. The mask is checked in
  frames/textmask2.png and covers all 7 letters cleanly. The result is stable across thresholds 0.08–0.16.
- The word runs **vertically** in the image, reading bottom to top:
  - y 1092–2357, so 1266 px long.
  - x 1856–2007, so 152 px wide. The word is slanted by about 26 px over its length (about 1.2°).
  - The letter cap height across the word axis is about 118–122 px.
- Interpretation: "horizontal length" is taken as the world-AABB horizontal extent of the text object, i.e. its
  extent across the image horizontal. That is about 120 px if the slant comes from camera roll, or 152 px if the
  bottle is really tilted. I used a compromise of about 136 px.
- 136 px × 1.321e-5 = 0.0018 m.
- Alternative reading (the length along the word): 1266 px gives 0.0167 m. I rejected it because the question says
  "horizontal" and the word is vertical in the scene.

## Confidence
- The scale is good (about 1%).
- The main risk is the interpretation: a factor of 10 if the asker meant the reading-direction length.
- Within the chosen interpretation, the pixel value is uncertain by ±12% (120–152 px).
