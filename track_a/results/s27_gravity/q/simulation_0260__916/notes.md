# Q916: long side of the bag (m)

The video is 30 fps, which is the same as question_fps. The view is frontal and planar: the mug falls in a plane parallel to the image, at about the bag's distance from the camera on the same table.

## Scale from the prior (mug falls at 9.8 m/s^2 before 0.5 s)
- `fit.py` fits a quadratic to the mug's free fall in frames 5-15 (scene/tracks/mug.csv), which is before impact at frame 16.
  - ref_y: 6.839 px/frame^2, giving 0.001592 m/px
  - top_y: 6.755 px/frame^2, giving 0.001612 m/px
  - bottom: 6.895 px/frame^2, giving 0.001579 m/px
- I used the ref_y fit: **0.001592 m/px**.
- Plausibility check: at rest the mug is 56 px tall (0.089 m) and 67 px wide with the handle (0.107 m). Both are realistic mug sizes, so the scale is consistent.

## Bag
- `bag.py` masks the bag in frame 36 using warm/light pixels against the blue wall.
- The horizontal extent is x = 1310-1535 (226 px including a strap tip). The body rows run from 1310-1312 to 1527-1533.
- scene.json gives 223 px, and the zoomed crop reading gives 1311-1532 (221 px). I used **223 px**.
- Long side = 223 x 0.001592 = **0.355 m**. With the range of the gravity fits and the pixel extent this falls between 0.35 and 0.36 m. That is a realistic size for a Nikon camera bag.

## Caveats
- The bag's front face is slightly nearer the camera than the mug's fall plane. Any depth difference is small, a few percent at most.
- Confidence: good (about ±5%).
