# q_2599 – speed of the right tennis ball at t = 1.2 s (cm/s)

t = 1.2 s -> frame round(1.2 x 24) = 29. The file and the question both run at 24 fps.

## Track (pixels)
- scene/tracks/tennis_ball_right.csv (circle fit). I checked it with my own yellow-mask centroid (measure.py).
  Per-frame steps (record / mine), in px/frame:
  27->28 14.2/12.6, 28->29 12.2/11.7, 29->30 10.6/10.7, 30->31 10.5/10.6, 31->32 10.0/9.8, 32->33 9.9/10.5.
  The ball slows down after the push (~frame 25-27).
- I smoothed over 5 frames centred on frame 29. Mean of the forward differences 27..31: 11.5 (record), 11.1 (mine).
  Regression slope of positions 27..31: 11.8. A forward-only window 29..33 gives 10.4.
  Value used: 11.2 px/frame = 269 px/s (spread 10.4-11.8).

## Scale – conflict between the prior and depth_info
- Apparent ball diameter is ~30.7 px: record circle fits are 30.0 (static) and 30.6-31.1 (frames 40-48). A zoomed crop
  at frame 44 reads ~30 px.
- Method card (f = 763 px, Z = 0.776 m) gives 0.776 x 30.7 / 763 = 3.1 cm for the ball diameter. That is about half
  the exact prior of 6.7 cm. The soccer ball also comes out at 12.3 cm instead of a real ~22 cm. With the prior's
  scale the soccer ball is 105/30.7 x 6.7 = 22.9 cm, which is realistic.
- So this background-replaced video looks shrunk by ~0.47 relative to the camera's intrinsics: the "Segment
  Anything 2 Demo" output padded and scaled down the content. depth_info + f = 763 + 6.7 cm are consistent with each
  other at the original resolution (the ball would be ~66 px there). The reference, measured in the main camera,
  therefore corresponds to the prior's scale. The question kind is "SD" (size prior -> dynamics question).
- Scale used: 6.7 cm / 30.7 px = 0.2182 cm/px. This equals Z / f_eff with f_eff = 30.7 x 77.6 / 6.7 = 356 px.
- Depth (z) component, from table-top perspective (front/back edge ratio 1.24 over 170 px): ~0.17 cm/frame against
  2.5 cm/frame lateral. That adds +0.2%, which is negligible.

## Answer
269 px/s x 0.2182 cm/px = **58.7 cm/s** (the spread of smoothing choices gives 54-62).
Second route, a literal method card (0.776/763 m/px): 27.3-28.7 cm/s. I rejected it because it contradicts the exact
6.7 cm prior by a factor of ~2.1.
Confidence: moderate. The scale choice is the main risk; within the prior route, about ±5%.
