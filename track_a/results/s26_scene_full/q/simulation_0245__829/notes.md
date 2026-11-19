# q_829 – rabbit height (m)

The prior says the antelope (the horned creature) moves at 1.277 m/s. The scene is 2D: the camera is static, both animals move parallel to the image plane, and their sizes stay constant. fps = question_fps = 30.

## Scale
I fitted the creature's x position against frame number (measure.py, scene tracks; the scene masks were checked in the frame sheet):
- centroid: 6.470 px/frame (6.465 from the endpoints)
- torso_cx: 6.473 px/frame
- bbox_x0: 6.540 px/frame
- bbox centre: 6.423 px/frame

Speed = 6.47 px/frame × 30 = 194.1 px/s, so the scale is 1.277 / 194.1 = 0.006579 m/px.

## Rabbit height
The rabbit's bbox height over frames 0–64 (before it reaches the image edge) follows the hop cycle:
- tall pose, ears up: 68–72 px
- crouched: 52–54 px
- median: 62 px

I checked this on 4× crops. In frame 0 the ears are at y≈1481 and the feet at y≈1550 (≈70 px). In frame 6 (crouched) the height is ≈54 px.

I don't know which pose the reference AABB uses. A rest pose with ears up gives ≈70 px → 0.46 m. The median gives 62 px → 0.41 m. I answer with 66 px × 0.006579 = **0.434 m**, which is within about 6% of both readings.

## Confidence
The scale is good to about 1%. The main uncertainty is which pose defines the height (0.34–0.47 m across the hop cycle).
