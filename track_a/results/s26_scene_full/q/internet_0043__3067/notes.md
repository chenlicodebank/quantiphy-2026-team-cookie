# q_3067: height of the kettle (cm)

Prior: the white ball is moving at 33.38 cm/s at t = 1.0 s. fps = question_fps = 30, so this is frame 30.
The "white ball" is the one the scene record calls the "egg". It is actually a ping-pong ball rolling right to left
along the desk. The camera is almost static (drift ≤0.3 px/frame, ignored).

## Ball pixel speed at frame 30 (forward difference, the annotators' convention)
- From scene/tracks/egg.csv, ref_x: x30 − x31 = 1211.5 − 1166.3 = 45.2 px/frame. Drift-corrected: 44.8. Backward difference: 45.9.
- My own white-mask centroid (measure.py): forward difference 44.5. Neighbouring differences are 45.8, 46.2 and 46.5. The
  ball travels at a steady ~45-46 px/frame over frames 28-32.
- Adopted value: 45.3 px/frame = 1359 px/s, so scale = 33.38 / 1359 = 0.02456 cm/px.

## Kettle pixel height
I made a red HSV mask of the kettle (measure.py; overlay in frames/kettle_mask.png) and took the top of the lid to
the base on frames 0, 10 and 60: y 476→762, 477→763 and 474→759. That gives H = 287, 287 and 286 px. The
record's bbox gives 292 px, which includes some slack. Adopted value: 287.5 px.

## Answer
287.5 px × 0.02456 cm/px ≈ **7.06 cm**.

Check: the forward-difference range 44.5-45.9 px/frame gives 6.97-7.19 cm. This is far from the real size: a 0.8 L
Tefal kettle is about 18-20 cm tall, and a ping-pong ball's 79 px would give about 4 cm, which implies 70+ cm/s.
So the prior's scale is about 2.5x off from reality. The benchmark rule is to use one scale from the prior, so I answer
with the prior-derived value. Confidence that this reproduces the reference convention: moderate-high.
