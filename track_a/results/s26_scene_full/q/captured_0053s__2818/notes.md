# q_2818 – basketball diameter (cm)

Question fps = file fps = 24. Prior (trashbin velocity) does not bear on the ball size; scale = depth_info
basketball distance 2.925 m at t=0.4 s (frame 10) with lab focal f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Measurement (measure_ball.py)
- Ball is static at (985.8, 369.8). Mask = residual > 20/30/45 from a quadratic background fitted to the ROI border.
  Frames 5–47 agree: bbox 68 x 62 px, fitted ellipse 67.3–68.2 (horizontal) x 61.0–62.2 (vertical), equivalent diameter 65.5 px.
  Frame 0 is contaminated by the nearby blue object, so it was not used. The overlay (frames/ball_mask.png) shows a tight outline.
- The ball is 346 px off-axis (θ = 24.4°, cos θ = 0.911). A sphere off-axis projects as an ellipse that is stretched radially by 1/cos θ:
  62 / 0.911 = 68.1, which matches the measured 68. So the extra width comes from perspective, not from the mask.

## Size
- The lab back-projection convention ((u-cx)/f, (v-cy)/f, 1) x depth treats depth as Z. The tangential (minor) extent is then
  f·D/Z, so D = 2.925 x 61.9 / 762.8 = **23.7 cm**.
- Second route: the major axis corrected by cos θ gives 2.925 x 67.9 x 0.911 / 762.8 = 23.7 cm, which agrees.
- Alternative readings: if depth is the Euclidean range, D = 21.7 cm. The naive card formula with the equivalent diameter
  (2.925 x 65.5 / f) gives 25.1 cm, but it ignores the off-axis stretch.
- Sanity check: a regulation size-7 ball is about 23.9 cm across (74.9 cm circumference), which is consistent.

Answer: 23.7 cm. Confidence: moderate-good. The main uncertainty is the depth convention (Z versus range, and whether it was read at the surface or the centre).
