# Q338: height from the floor to the ceiling (m). Prior: walking speed = 1.693 m/s

fps = question_fps = 24, so there is no re-timing.

## Geometry (from the video)
- Floor tile joints converge at VP (960, 538) (`vp.py`, Hough fit, 26 lines, median residual 1.9 px). That is the image centre, so the camera is level and the horizon is y = 538.
- Transverse tile joints sit at y = 800 (wall base), 816, 837, (862), 891, 925, 967, 1019. 1/(y-538) steps by a constant 0.000252 per tile, which confirms the horizon (`tiles.py`).
- Measured edges (`edges.py`): wall base / floor line at y = 800.3. The ceiling meets the back wall (bottom of the planks, top of the black beam) at y = 287.8.
- The man walks at constant depth with his soles at y ≈ 905. The back wall is farther away, so the scale differs between the two depths:
  Z_wall / Z_man = (905-538)/(800.3-538) = 1.399.

## Scale
- Speed: the man moves 18.85 px/frame (same-phase pairs of head and mask centroid: 18.78–18.95; pelvis track 18.78), i.e. 452.4 px/s.
  s_man = 1.693/452.4 = 0.003742 m/px. This gives him a height of 492 px × s_man = 1.84 m, which is plausible.
- s_wall = 0.003742 × 1.399 = 0.005236 m/px. This is equivalent to a camera height of 367 × s_man = 1.373 m.

## Answer
- H = (800.3 - 287.8) × s_wall = 512.5 × 0.005236 = **2.68 m**. Equivalently, H = h_cam × 512.5/262.3.

## Check
- The longitudinal tile joints along the wall base are 116.4 px apart, so a tile is 116.4 × s_wall = 0.61 m. That is a standard 0.6 m tile.
- If the tiles are exactly 0.60 m, then H = 2.64 m (1.5 % lower). This route is independent of the speed prior.
- With f = 1766 px from square tiles, the wall is Z ≈ 9.3 m from the camera and the man ≈ 6.6 m.

## Ambiguity
The ceiling is not flat. Its wooden planks are straight and share a vanishing point at (942, ~955), well below the horizon. So the ceiling plane rises toward the camera at about 13°. Because of that, "ceiling height" can be read three ways:
- At the back wall (the visible floor-to-ceiling junction): 2.68 m. **This is the answer given.**
- At the top edge of the frame (Z ≈ 6.5 m): about 3.35 m.
- Extrapolated over the camera: about 4.9 m. This depends on the tile-based focal length and on the slope continuing that far.

Confidence: the measurement at the wall is good (about ±3 %). Which reading the reference used is the main uncertainty.
