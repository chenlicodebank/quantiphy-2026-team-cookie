# simulation_0030 – measurement record

3D Blender render, 960x960, 25 fps, 75 frames (t = frame/25). All values are in pixels and seconds. No metric scale is assumed.

## Scene
- The camera is **static**. Phase correlation of the island/beach band against frame 0 gives a shift of at most 0.04 px in x and 0.5 px in y (`scripts/cam_shift.json`). The water surface ripples, but the camera does not move.
- **bird**: the only moving object. It is a single dark-brown raptor (eagle/hawk-like) that flaps as it flies left-to-right across the sky above the island, at roughly the same image height (y 270–297). It is visible in frames 0–39 and fully inside the image in frames 0–36. In frames 37–39 it is cut off by the right edge (occluded=1), and from frame 40 to the end it is gone. Nothing in the scene looks like it, so it cannot be mistaken for another object.
- Static objects (extents from frame 74, `scripts/static_extents.py`):
  - **island**: a white snow-covered dome hill. x 230–812 (base), top y 380 (summit near x 380), base y ≈ 505, so about 582 x 125 px.
  - **beach**: a sand strip, x 0–870, y 472–530.
  - **water**: foreground, y 528–959, with pink reflections of the island.
  - **sky**: y < 500. The horizon is about y 500 and nearly level.

## Files
- `scene.json`: the inventory, camera, static extents and events.
- `tracks/bird.csv`: one row per frame from 0 to 39. Columns:
  - frame, t
  - cx, cy: mask centroid, used as the reference point (proxy for the bird's origin)
  - bbox_cx, bbox_cy: bounding-box centre
  - bbox_x0, bbox_y0, bbox_x1, bbox_y1, bbox_w, bbox_h
  - area_px
  - len_main_axis, width_across: PCA extents of the mask
  - main_axis_deg
  - occluded
- `scripts/track_bird.py`: tracking. The bird mask is the difference against a median background built from frames 45–74 (|diff| > 40 and gray < 175, then 3x3 closing), keeping the largest blob plus nearby fragments. The script also writes `frames/bird_overlay.png`, which I checked visually: the boxes cover the whole bird, including the wings.
- `scripts/static_extents.py`: extents of the island and beach (warm pixels where R − B > 8).

## Motion facts (raw only)
- The centroid moves from x 378.4 (frame 0) to 927.4 (frame 36), about 15.3 px per frame, at a nearly constant rate.
- The vertical motion is small and oscillates with the wing-beat: y ≈ 270 → 294 (frames 9–12) → 273 (frame 24) → 296 (frame 36).
- The apparent size shows no trend; the bird stays at roughly the same depth.
- The bbox changes strongly with wing phase:
  - wings up: about 25 x 33 px (frames 0–1, 22–27; tallest 34 px at frame 25)
  - wings flat: about 30 x 8–12 px (frames 5, 31–33)
  - maximum fully-visible bbox width: 36 px (frame 8)
- The wing-beat period is about 13–14 frames.
- For a "min/max wingspan" question, use bbox_w / len_main_axis over frames 0–36 together with the given depth.

## Reliability and ambiguity
- **Centroid**: about ±1–2 px, because it shifts with wing pose. The mask centroid is not the rig origin, so per-frame speed computed from cx/cy carries wing-flap jitter of about 1–3 px per frame. Smooth it, or use bbox_c, if needed.
- **Bbox**: about ±2 px. A looser threshold (diff > 25, gray < 200) changed the width by up to 6 px only when the wings are flat (frame 5) and by 0–3 px otherwise.
- **Edge frames**: frames 37–39 are truncated at the image edge, so their size and centroid are biased.
- **No shadows**: the bird casts no visible shadow.
- **Static extents**: about ±3 px. The island's right base merges with the rocky tail and beach, so x_right ≈ 812 is approximate.
