# q_309 – height of the hot air balloon (prior: speed = 4 m/s)

2D scene: one balloon rising straight up against a uniform sky, camera static. File fps 24.004 and question_fps 24 are
effectively the same, so I used 24.

Measurement (`measure.py`): the mask is the pixels that differ from the sky RGB (137,168,196) by more than 30, summed
over channels, measured on all 97 frames.
- Vertical pixel speed, from linear fits: basket bottom 4.000 px/frame, mask centroid 4.020 px/frame, envelope top
  4.070 px/frame. I used 4.01 px/frame, which is 96.2 px/s.
- Scale = 4 m/s / 96.2 px/s = 0.04156 m/px.
- Full height (envelope top to basket bottom) is 472–479 px, 475.0 px on average. The width stays at 358 px.

Height = 475 px x 0.04156 = 19.74 m.

Second route: taking the extremes (472 px with 4.07 px/frame, and 479 px with 4.00 px/frame) gives 19.3–20.0 m. So the
answer is about 19.7 m, ±2%.

Confidence: good. The main uncertainty is the slight growth of the apparent height (about 1.5%) and which point the
speed refers to.
