# q_104: length of the black-and-white (dark) car

The scene is a 2D top-down view at 24 fps. The file rate and question_fps agree, so I used 24 fps throughout. I used one metres-per-pixel scale, taken from the prior (yellow car speed = 5.07 m/s).

## What I measured (measure.py, ext.csv)
- I segmented every frame with the same mask the record uses (gray<113 | gray>176 | sat>40), which keeps the shadows out. I took x extents from the body rows: yellow car rows 480-570, dark car rows 600-685.
- **Yellow car pixel speed:** the bumper-to-bumper centre moves -9.88 px/frame over frames 12-71, while the car is fully in view. The steps are -10 with an occasional -9. Cross-checks give front bumper over frames 1-71: -9.83, and rear bumper: -9.97. That gives 9.88 x 24 = 237.2 px/s.
- **Scale:** 5.07 / 237.2 = 0.02138 m/px.
- **Dark car length:** 274 px at the image edge, falling to 263 px near the centre, because the camera is perspective and the car has height. The clip-wide mean is about 268 px.
  - Second route, matching magnification: over the window used for the speed, the yellow car's mean length is about 272 px. Near the centre it is about 268, a factor of 1.015. Near the centre the dark car is 263-264 px, and 264 x 1.015 ≈ 268 px. Both routes give the same value.
- **Length:** 268 x 0.02138 = **5.73 m**. For comparison, the yellow car comes out at about 5.8 m.

## Confidence
About ±3%. The main uncertainty is the perspective-dependent pixel length, which varies ±2%.
