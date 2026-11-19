# q_2675 — length of the table (m)

Lab video, 24 fps (file fps = question fps = 24), 1280x720, f = 0.5959*1280 = 762.8 px, c = (640,360).
Prior: ball diameter 4 cm. Depths: t=0.9 s (frame 22) 1.010 m; t=1.4 s (frame 34) 0.716 m (camera to ball centre).

## Method (table_lines.py, recon.py)
1. Frame 48 (no ball): segmented the wood and fitted four lines: left side, right side, back edge, and the front top
   edge (the light top meets the dark band; robust refit). RMS residuals are 0.7–1.1 px. The extrapolated corners
   are BL (418.5,439.8), BR (756.9,447.0), FL (187.2,586.2), FR (993.0,591.2). The real corners are rounded, so the
   extrapolated corners give the bounding-box extents.
2. Vanishing points: sides L×R and front/back B×F, back-projected with K. The two table directions come out at
   89.88° apart, which confirms both the rectangle and the focal length. The plane normal comes from their cross
   product (camera pitch ≈1.5°, grazing view).
3. Scale: each ball centre from tracks/ball.csv is back-projected with its given depth. The centre sits 2 cm above
   the top, so camera height above the top = 0.02 − n·P. Frame 22 gives 0.1710 m and frame 34 gives 0.1684 m. These
   are two independent references, and they agree to 1.5%.
4. The four corners are back-projected onto that plane:
   - h = 0.1697 m (mean): front/back (left–right) edge 0.547 m, front-to-back sides 0.720 m.
   - Per depth: sides 0.725 m (frame 22) and 0.714 m (frame 34).
   - Ball moves 0.417 m between frames 22 and 34.

## Answer
Length is the longer horizontal extent, here front-to-back: **0.72 m**. The other reading, the edge facing the
camera (the wide edge in the image), measures 0.547 m and is the width.

## Checks
- Moving the frame-22 ball centre 2 px lower (the track may lose the ball's underside) gives h = 0.1735, so the
  length rises 2%.
- Second route, independent of depth_info: the resting ball (frames 0–11, ≈28 px including halo) gives a depth of
  ≈1.09 m and a length of ≈0.65 m. This route is less reliable. The ball's apparent size disagrees with the given
  depths in both directions (25.8 px at frame 22 against the 30 px expected; 48.5 px at frame 34 against 42.6),
  because of segmentation halo and blur. The answer therefore uses the given depths.
- Confidence: moderate to good, about ±4%.
