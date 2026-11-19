# q243 – width of the door (simulation_0117, 2D)

The file runs at 24.020228 fps. All times use question_fps = 24, and frame indices come from the frame column.

## Scale from the prior (g = 9.8 m/s^2)
- `measure.py`: quadratic fit of the ball centre y(frame/24) from scene/tracks/ball.csv, unclipped frames 2-18:
  a = 6289 px/s^2 (rms residual 0.19 px). Frames 4-18 give 6292. The mean of the second differences is 6267.
- Scale = 9.8 / 6290 = 1.558e-3 m/px.
- Check: the ball is 45 px, which gives 0.070 m, consistent with a tennis ball (6.7 cm). The scale is plausible.

## Door width (`edges.py`, frame 18, row profiles averaged over y 500-1700, with zoomed crops)
- Left: the outer frame edge is at x≈697 and the leaf/inner jamb edge at x≈713.
- Right: the leaf/inner edge is at x≈1410 and the outer frame edge at x≈1429.
- Outer frame (door object including casing): 732 px, which gives **1.14 m**.
- Leaf/opening: 697 px, which gives **1.09 m**.
- The scene record's value is 697-1412 = 715 px, which gives 1.114 m. That is between the two readings and within about 2.6 pct of each.
- Height for reference: about 1474-1490 px, which gives 2.30-2.32 m. A 1.1 x 2.3 m door is plausible.

## Answer
1.114 m. I chose this compromise because it is within 3 pct of both readings (leaf and frame bbox).
The second-route check is that the ball size gives a consistent scale. Confidence: moderate to high (the reading of "door" is the main uncertainty, ±3 pct).
