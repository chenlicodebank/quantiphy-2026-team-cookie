# captured_0022x – measurement record

**Scene.** This is a lab capture (3D, 24 fps, 49 frames, 1280x720). Segment Anything 2 replaced the background with black, and the watermark sits at the bottom right. The camera is static: phase-correlation shift is ≤0.2 px on every frame. It looks obliquely down at a light-brown wooden rectangular table top that stands on one grey post leg. One **white ball** (ping-pong size) sits at rest on the far/back edge of the table for frames 0–11. It starts rolling at frame 12 (t = 0.500 s) and rolls straight toward the camera, so it moves mostly in depth: in the image it goes down and slightly left. It reaches the front edge around frame 46 (t = 1.917 s) and falls off, appearing below the edge in frames 47–48. There are no other moving objects.

**Files.**
- `scene.json`: inventory, static extents, events, camera.
- `tracks/ball.csv`: one row per frame with these columns:
  - `frame`, `time_s`
  - `cx`, `cy`: centroid of the filled mask. This is the visible centre and the recommended reference point.
  - bbox, `mask_area_px`, `equiv_diam_px`
  - `len_major_px`, `wid_minor_px`, `major_axis_deg`: PCA extents
  - `height_px`: vertical extent
  - `occluded`: always 0
  - `cx_box`, `cy_box`: an alternative centre, x = bbox mid and y = top + bbox width/2. This is less sensitive to the shaded bottom of the ball. For frames ≥46 it is the bbox centre.
  - `phase`: rest / rolling / falling
  - `motion_blur`
- `scripts/`: `make_bg.py` (median background of frames 12–48), `track_ball.py`, `refine_and_overlay.py`, `static_and_camera.py`, `crops.py`, `probe.py`, and `_masks.npz` (small packed mask crops).

**Method.** Ball mask = pixels inside a ROI around the previous position that are either (saturation <28 and value >140) or bright pixels that differ from the background. The ball has saturation ≤~25 and the table ≥33. The mask is morphologically cleaned and hole-filled. I checked the overlays visually on crops of frames 0–48 and on a full-path overlay.

**Reliability.**
- Centre: about ±1 px while rolling on the table.
- Shaded lower rim: during frames 20–30 the bottom 1–2 px of the ball can be missed, which biases `cy` up by about 0.5–1 px. In frames 34–35 and 43–44 a little of the contact shadow may be included.
- Apparent diameter (horizontal bbox width): about 18–19 px at the back edge and mid-table, about 21–22 px near the front edge (frames 40–45). It grows because the ball comes closer.
- `equiv_diam_px` is noisier, ±1.5 px.
- Frames 46–48: the ball is falling with strong vertical motion blur (vertical extent 27→39 px), so only the horizontal width (~20–24 px) means a size. The centre is the blur centre.
- Frame 36: the 35→36 step is about 12 px, roughly twice its neighbours. This is most likely a dropped capture frame. Treat it carefully when differencing; if smoothing, perhaps interpolate over it.

**Static objects.**
- Table top-surface corners (px): back-left (285,418), back-right (597,362), front-right (671,514), front-left (227,618).
  - Edge lengths: back 317 px, front 456 px, left 210 px, right 168 px.
  - The front slab thickness is about 10–12 px.
  - The ball rolls across the table's short (depth) axis, from about (438,380) to the front edge at about (393,575).
  - Edges are measured from the colour median background; accuracy is about ±3 px, and corners are rounded.
- Leg: a grey post, bbox (464,572)–(510,689), about 120 px of it visible below the table top, about 31 px wide.

**For 3D questions.**
- Use fx = 763 px and the principal point (640,360), back-projecting the ball centre with the given depth_info.
- The motion is mainly toward the camera, so image-plane displacement greatly under-represents the 3D motion. The change in apparent diameter (about 18.5→21.5 px) and the depths are needed.
- Whether the table is tilted is unknown. The ball accelerates from rest: the step grows from ~4 to ~8 px/frame, partly through perspective.
