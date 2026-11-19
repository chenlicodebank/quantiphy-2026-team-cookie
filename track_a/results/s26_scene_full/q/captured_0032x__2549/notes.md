# q_2549 — diameter of the white (ping-pong) ball, cm

File fps = question_fps = 24; t = 1.5 s -> frame 36. Lab camera f = 0.5959 x 1280 = 763 px.
depth_info at t=1.5: tennis ball 1.183 m, ping-pong (white) ball 1.353 m.

## Measurement (profile.py, yellow.py, measure.py; grid crops in frames/)
At frame 36 the white ball rolls right (about 5-14 px/frame in x, 2-4 px/frame in y), so the horizontal extent is inflated by motion blur.
I took grey-level profiles through the ball centre. Edges: the half-max crossing at the top, where the ball meets the black segmented background, and the start of the dark segmentation fringe at the other sides.
- White ball, frame 36: vertical extent about 22 px (37-38: 22-22.5), horizontal about 24-24.5 px (blurred).
  -> vertical: 22 x 1.353 / 763 = 3.90 cm; 22.5 px -> 3.99 cm; horizontal 24.3 px -> 4.31 cm (blur-inflated).
- Check against the prior (tennis ball, frame 36, same edge convention): vertical about 44 px -> 44 x 1.183 / 763 = 6.82 cm vs the prior 6.7 (+1.8 %).
  This confirms that the vertical-extent method with f = 763 and the given depths is accurate to about 2 %. Horizontal is about 46 px (blurred, like the white ball).
- Second route (ratio to the tennis ball, which cancels any edge bias): 6.7 x (22/44) x (1.353/1.183) = 3.83 cm.
  The direct method card gives 3.90-3.99 cm. The scene notes say the segmentation fringe makes extents 1-2 px small.

Answer: 3.95 cm (the routes span 3.83-3.99; a real ping-pong ball is 4.0 cm, which agrees). Confidence: good, about ±3 %.
