# q_224 – length of the boat (prior: boat speed = 2 m/s)

2D top-down render, 24 fps (file fps = question_fps, no re-timing). Static camera (per scene/notes.md).
One metres-per-pixel scale from the prior speed.

## Speed in pixels (measure.py)
Background-difference mask of the boat (bg = frame 200 for early frames, frame 40 for late frames).
Linear fit of the stern-tip row over frames 3–69 and 203–210: 5.4977 px/frame (rms residual 0.38 px);
pre-bridge-only fit 5.490. scene/ record gives 5.4961 – agrees. Motion is purely vertical.
=> 131.94 px/s, scale = 2 / 131.94 = 0.015158 m/px.

## Length in pixels (tips.py, row-by-row diff profile at the tips)
- Frame 36: thin stem post rows 339–349, hull (two gunwale lines converging) starts at ~350, stern tip 590.
  Hull ~240 px; including post ~252 px.
- Frame 209: post 1289–1304, hull from ~1303–1305, stern tip 1542. Hull ~238–240 px; with post ~254 px.
- Boat axis tilted ~3.5 deg (tip x 639 vs 622): along-axis length differs from vertical extent by <0.3 px.
- (scene/ record said 233 px hull and ~250 with post; my tip profile puts the hull at ~240.)

## Answer
- Hull only: 240 px x 0.015158 = 3.64 m
- Including stem post (full object extent): 252 px x 0.015158 = 3.82 m
Ambiguity is whether the reference bounding box includes the thin bow post. Answer the midpoint
246 px -> **3.73 m**, within ~2.5 pct of either reading.

Second route: the post-bridge window (frames 203–210) gives the same pixel length (238–240 hull, 254 with post)
and the same speed, so the scale and size are consistent before and after the bridge.
Confidence: moderate-high (main uncertainty = post inclusion, ±2.5 pct).
