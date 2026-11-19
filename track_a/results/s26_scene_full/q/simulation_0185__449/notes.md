# Q449: length of the gift box (m)

The prior is the gift box's acceleration after 1 s, 3.18 m/s². At t = 1 s (frame 24) the box is sliding down the ramp.
The scene is 2D and the camera is static, so one m/px scale is taken from the slide acceleration.

## Measurements (fit.py, size.py)
- Track: scene/tracks/gift_box.csv (body centroid, using the dupfix value at frame 38). I checked it against the frames.
- Slide acceleration: quadratic fit of path length against time over frames 10–37 gives 745 px/s² (rms 0.7 px).
  Sub-windows give 10–24: 749, 15–30: 773, 20–37: 718. The motion is close to uniform acceleration.
- Scale: 3.18 / 745 = 0.00427 m/px.
- Box size on the unoccluded falling frames 0–8 (min-area rectangle of the body): 111–112 × 108–109 px, so the box
  is almost a cube. The longer side is 111.5 px. A second mask of my own (size.py) also gives 112 / 110.5 / 111.2 px
  along the long side.
- Length = 111.5 × 0.00427 = **0.476 m**.

## Second-route check
- Free fall over frames 0–8 gives 2277 px/s². With g = 9.81, that is 0.00431 m/px, within 1% of the prior-based
  scale. This supports both the planar scale and the 24 fps time base (question_fps = fps = 24).
  With this scale the length would be 0.480 m.

## Ambiguity
- I used the box's own edge length (about 111 px). If the reference instead used the world AABB of the tilted box
  (tilted ~29°), the answer would be about 133–150 px × 0.00427, which is 0.57–0.64 m. I did not use that reading.

Confidence: moderate-high for the edge-length reading (scale ±3%, size ±3 px).
