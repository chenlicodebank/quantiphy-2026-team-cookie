# q_239: width of the middle yellow door (m)

The file runs at 24.006 fps; question_fps = 24.0 is used for all timing (frame index from the track CSV).

## Scale from the prior (gravity 9.8 m/s^2), 2D scene
- fit.py: quadratic fit to the football centroid y(frame) from scene/tracks/football.csv (frame 17 excluded).
  a = 3.123 px/frame^2 (fits starting at frame 0, 3 or 6 give 3.123 to 3.125; bbox_cy gives 3.115 to 3.125; rms residual 0.4 to 0.6 px).
  a = 3.123 x 24^2 = 1799 px/s^2, so the scale is 9.8 / 1799 = 0.005447 m/px.
- Route check: the per-frame second differences scatter around 3.1 px (from 1.2 to 4.5, noisy), with no trend and no bounce.

## Door width
- door.py: yellow HSV mask on frame 0, rows 840-1030 of the middle door. The outer yellow door frame runs from x = 647.5 to 807.5, so it is 160 px wide. The value is constant over every row, and the bottom and top doors give the same result.
  The door leaf inside the frame (x = 659-797) is 139 px wide.
- The zoomed crop (frames/door.png) confirms the edges.
- Door assembly including the frame: 160 x 0.005447 = **0.87 m**. This is the answer, read as the bounding box of the door object.
- Alternative reading (leaf only): 139 x 0.005447 = 0.76 m.

## Caveats
- The football appears about 0.33 x 0.21 m at this scale, compared with about 0.28 x 0.17 m for a regulation ball. The ball probably sits in front of the wall, or is a composited or scaled model. Following the 2D convention, one scale from the prior is used.
- Confidence: moderate. The scale is solid to about 1%. The main uncertainty is whether the door frame should be included (0.87 vs 0.76 m).
