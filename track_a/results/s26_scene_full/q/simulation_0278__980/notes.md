# q_980: whale length (m)

The prior is whale speed = 1.67 m/s. This is a 2D top-down view (orthographic-looking) with a static camera, at 24 fps (file fps and question_fps agree).

## Scale
- I refit the blowhole track (body-fixed mark, scene/tracks/whale.csv) in check.py. For frames 1–71, x = 1060.91 − 5.8709·frame. That is 140.90 px/s; the mean per-frame step speed is 140.87 px/s. Motion is horizontal with constant speed (frames 0 and 1 are identical).
- Scale = 1.67 / 140.90 = 0.011853 m/px.

## Length (snout tip to fluke tip, horizontal x extent)
- I checked the bbox on frames 0, 26 and 58, viewed at half scale. The snout is at about 373 px and the fluke at about 1157 px at frame 0 (half scale), which matches bbox_w = 1568 px at full scale.
- The extent changes with the tail beat:
  - Frame 0 (start pose): 1568 px, giving **18.59 m**.
  - Minimum: 1422 px (frame 27), giving 16.9 m.
  - Maximum: 1599 px (frames 57–60), giving 18.95 m.
  - Mean over the clip: 1519 px, giving 18.0 m.
- Answer: frame 0, the static start pose, which is the usual reference for an object's dimensions. It is also within about 3% of both the clip mean and the maximum.

## Check
The second route is the mean bbox_w over the clip, giving 18.0 m, and the maximum straight-pose extent, giving 18.95 m. Both are within 3–4% of the answer. Speed is very reliable (residual ≤ 0.14 px), and the edges are accurate to ±3 px (0.2%).

Confidence: fairly high. The main uncertainty is which tail-beat pose the reference used (about ±3%).
