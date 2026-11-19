# Q38: speed of the walking pedestrian at 1.0 s (m/s)

The video is a 2D top-down Blender render with a static camera, so one m/px scale applies to the ground plane. fps = question_fps = 24, so t = 1.0 s is frame 24.

## Scale from the prior (the white car accelerates at 4 m/s^2)
- `measure.py` re-measures the car's front edge in every frame, using the white-pixel mask in columns 760–910.
- Quadratic fits of front-edge y(t) give an acceleration of 162.19, 162.08 and 162.12 px/s^2 for fits starting at frames 3, 5 and 10 (rms residual 0.3 px). A linear fit of the per-frame speeds gives 162.20 px/s^2.
- Scale = 4 / 162.15 = 0.02467 m/px.
- Sanity check: the car's length of 234 px works out to 5.8 m, which is plausible for a van.

## Pedestrian speed
- `measure.py` subtracts a background median in the strip y 800–900, x 1280–1520. It tracks two things: the centroid of the white top (torso), which is smooth, and the centroid of the full mask, which jitters with the limbs.
- `speed.py` fits a line to x around frame 24:
  - White-top centroid: 2.00, 2.02, 2.04 and 2.05 px/frame for half-windows of 4, 6, 8 and 12 frames. The whole-clip fit gives 2.04.
  - Full-mask centroid (second route): 2.01–2.11 px/frame.
- The raw one-frame back-difference at frame 24 is 1.92 px/frame (white top) or 1.52 (full mask). That is limb and pixel noise, so I used the smoothed value.
- Result: about 2.03 px/frame × 24 × 0.02467 = 1.20 m/s. All variants fall between 1.18 and 1.25 m/s.

Confidence: good. The scale is solid (fit residual 0.3 px). Most of the uncertainty is in the pedestrian's local speed, about ±3%.
