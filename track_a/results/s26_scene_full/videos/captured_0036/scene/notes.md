# captured_0036 - measurement record

Lab video (real camera, 24 fps, 49 frames, 1280x720, f = 763 px per benchmark spec). The background has been
blurred/re-composited by "Segment Anything 2 Demo" (watermark bottom-right); only the table and the ball are sharp.
Camera is static (phase-correlation shift < 0.15 px over the clip).

Content: a white ball is held by a (blurred) hand at the back-left of a wooden table, pushed at frame 12 (t=0.50 s),
rolls diagonally toward the camera and to the right across the table top (frames 13-35), goes over the front-right
edge at frame 36 (t=1.50 s), falls (37-39) and leaves the image at the bottom at frame 40 (t=1.667 s).

## Files
- `scene.json` - inventory, table corners/extents, camera/perspective, events.
- `tracks/ball.csv` - final ball track, every frame (visible=0 for 41-48). Columns: frame, t, visible, occluded
  (1 = held by hand 0-12, partly cut/watermark 39-40), phase, cx, cy (ball centre px), bbox_x0..y1, diam_h_px
  (horizontal extent), diam_v_px (vertical extent), white_mask_y1, mask_cx/mask_cy (raw colour-mask centroid),
  len_major/width_minor/major_axis_deg (36-39 only, blurred streak), method.
- `tracks/ball_v2_bgdiff.csv` - alternative mask (median-background difference & low saturation); used for 36-39.
- `scripts/` - probe.py (first detection), track_ball.py (white core), track_ball2.py (bg diff), track_ball3.py
  (final), table.py/table2.py (table outline), crops.py, pts_check.py.

## How measured / reliability
- Ball, frames 0-35: the lower ~25% of the ball reflects the brown table and is lost by colour masks, so left/right/top
  edges come from the bright-white mask and the bottom edge is the dark contact-shadow line under the ball;
  centre = middle of these edges. Checked visually on overlays (frames/ball_overlay3.png). Centre +-1.5 px.
  diam_v_px is the blur-free diameter (motion is mostly horizontal); diam_h_px is inflated by motion blur
  (up to ~+13 px at frame 35). Apparent diameter: 24 px at frames 0-12, 27 at 15, 33 at 24, 39 at 30, 45 at 35
  -> the ball approaches the camera, depth roughly halves between release and the edge.
- Frames 0-12: hand covers the ball's left side (blurred), centre x +-2 px. Ball drifts left ~6 px (frames 4-10)
  while held, then moves right from frame 12.
- Frames 36-39: heavy motion blur on dark background; centre = centroid of the blurred streak (+-5 px), extents are
  blur streak lengths, not the ball size. Frame 39 bottom touches the watermark band. Frame 40: only a sliver at
  x~1078-1105, y>=683 (top tip), centre unknown (cx approximate, cy empty).
- Per-frame image step grows ~18 px (frame 14) to ~29 px (frame 35) on the table (perspective + approach);
  the 35->36 step is ~73 px - unusually large; may be a capture irregularity or the ball dropping off the edge
  between frames. Treat speeds across 35-36 with care.
- Table: outline from a saturation mask at frame 48; corners back-left (404,444), back-right (762,447),
  front-left (188,590), front-right (1000,593); front face 36 px thick (y 590-626). +-4 px. Side edges converge at
  (567,341) = vanishing point of the table's long axis; horizon y~341 if the table is level.
- Background objects (hand, chair, tripod, person's legs, TV screen) are blurred by the SAM compositing: positions
  only approximate, no sizes reliable.
