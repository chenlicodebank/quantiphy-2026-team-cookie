# q_1938: height of the TV stand (m)

Prior: black cat speed = 0.94 m/s. No depth_info was given. fps = question_fps = 24, so no re-timing.

## Scale
- Cat speed from scene/tracks/cat.csv (`measure.py`), using linear fits of x against t:
  cx 423.6, dark_cx 427.3, bbox_cx 421.4, bbox_x0 423.8 px/s. The walk is steady and there is no vertical drift.
  Adopted value: 425 px/s, giving 0.94 / 425 = 0.002212 m/px in the cat's plane.
- The record's TV stand box was checked on a zoomed crop (frame 48): top at y = 777, bottom of the metal base at
  y = 988, so the height is 212 px.
- With a single 2D scale: 212 × 0.002212 = 0.469 m.

## Perspective check
- The cat walks in front of the stand: it occludes the stand, its paws are at y ≈ 1021 and the stand base is at
  y ≈ 988.
- The camera is slightly above the furniture: the bench's top slats are visible from above.
- So the stand is somewhat farther from the camera than the cat, and its metres per pixel is larger.
- From the floor-contact rows, the depth ratio comes out between 1.03 (horizon above the frame, estimated from the
  bench's foreshortening) and 1.07 (horizon at the image centre, i.e. a horizontal camera). The corrected height is
  therefore 0.485 to 0.50 m.

## Answer
0.485 m. This applies a modest perspective correction (about 1.035) to the 0.469 m planar value.
Confidence: moderate. The answer is within about ±5% unless the reference ignores depth differences.
