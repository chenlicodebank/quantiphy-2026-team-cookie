# q_1002 – displacement of the plane, 0.5 s to 1.0 s

Prior: plane speed = 22.16 m/s (exact). 2D simulation; the jet flies in a straight horizontal line, right to left, at constant image y (417 ± 1 px).

## Constant speed check (measure.py, scene/tracks/jet.csv)
- Mask centroid steps: 42.30 px/frame (frames 13-25), 41.62 (25-40), 42.94 (40-55), 42.28 overall (13-55).
  The speed is constant. The bbox-centre steps (40.8 then 42.4) drift only because the view angle changes the
  nose/tail extents; the centroid shows no such drift. The fin-to-gear height stays at 224 px, so the depth is constant.
- No dropped or doubled frames in the fully visible range. Frames 0 and 1 are duplicates, which doesn't affect 0.5-1.0 s.

## Answer
With constant velocity, displacement = v x Δt = 22.16 x 0.5 = **11.08 m** (24 fps: frames 12 to 24).
Pixel route check: centroid moves 508.3 px over frames 12-24; scale = 22.16 / (42.28 x 24) m/px gives 11.10 m.

## Time base (file 24 fps vs question_fps 25)
Every frame is a distinct rendered frame, so the frame rate can't be told apart physically: the jet length comes out
at 15.6 m (24 fps) or 15.0 m (25 fps), and both are plausible.
- 25 fps, round-half-even: frames 12 to 25 give 11.52 m.
- 25 fps, round-half-up: frames 13 to 25 give 10.64 m.

11.08 m (24 fps) sits between those two and is within about 4% of each, so it is the robust choice.

Confidence: high that the motion is constant speed. The only uncertainty is the frame-rate convention (±4%).
