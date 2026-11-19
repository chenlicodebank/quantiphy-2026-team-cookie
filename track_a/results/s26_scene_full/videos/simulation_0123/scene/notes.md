# simulation_0123 — measurement record

**Video:** Blender render, 2D scene, 1920x1080, 24 fps, 72 frames (t = frame/24, so the last frame is 71 at t = 2.958 s).
**View:** a static top-down camera over a double bathroom vanity. Image x runs along the counter from left to right. Image y is the counter depth, with the wall at the top and the counter's front edge at y ≈ 665.
**Camera:** static. Frames 0 and 1 are pixel-identical, and every frame-to-frame change lies on the moving box, so no background-shift correction is needed.

## Files
- `scene.json`: inventory, static-object pixel geometry, events, camera, and a pixel-only motion summary for the moving box.
- `tracks/teal_box.csv`: one row per frame (0–71). Columns:
  - frame, time_s
  - centroid cx, cy (the reference point)
  - bbox x0/y0/x1/y1/w/h
  - minAreaRect length and width (mask_len_px, mask_wid_px) and its angle
  - mask area
  - occluded flag (always 0)
- `scripts/`:
  - `diff.py`: frame differencing, used to find what moves.
  - `track.py`: teal colour mask → largest component → centroid/bbox. Also writes the check overlays `frames/check_{0,36,71}.png`.
  - `static.py`: colour/dark masks for static items.
  - `build_json.py`: builds `scene.json`.

## Moving object (the only one)
**teal_box:** a small teal rectangular box, possibly a soap box or soap bar. It starts on the counter just below the left basin.

- **Size and orientation:** its top face measures 44 px along x (the motion direction) and 78 px along y. Its long axis is perpendicular to the motion. It never rotates, and its height cannot be seen in this view.
- **Path:** it is at rest at (412.1, 586.9) in frames 0–1. From frame 2 it slides straight right (+x) at constant speed. y stays at 587.0 ± 0.3.
- **Speed in pixels:** the per-frame step is 14.54 ± 0.24 px/frame. A linear fit over frames 2–71 gives a slope of 14.538 px/frame. That line extrapolates to x = 412.4 at frame 1, so the box effectively starts moving at frame 1 at full speed, with no visible acceleration phase.
- **Distance travelled:** at frame 71 the centroid is at (1429.7, 587.3). Net displacement from frame 0 is 1017.6 px and path length is 1017.8 px.
- **End of clip:** the box is still moving at the last frame. There is no contact, bounce or direction change.

**Reliability:**
- Centroids: about ±0.3 px.
- Box length: exactly 78 px in every frame.
- Box width: 44 px. Some frames read 45–46 px because of motion blur or antialiasing. Use 44 px.

If a prior gives the box's size or speed:
- scale = prior / 78 px for the long side, or prior / 44 px for the side along the motion.
- For a speed prior, scale = prior / (14.54 px/frame × 24 = 349 px/s).

Positions are the visual centroid of the top face, which is the object's origin as seen from straight above.

## Static objects (frame 0, pixels; full list in scene.json)
- **Basins:** left basin about x 170–652, y 200–515; right basin about x 1210–1690, same y. Edges are soft (±5 px).
- **Drains (dark discs, Ø 35.5 px):**
  - left at (465.1, 366.3)
  - right at (1501.8, 366.2)
  - the two are 1036.7 px apart
- **Gold faucets:**
  - spouts at x ≈ 409 and 1453, each about 178 px long in y
  - handles (Ø 40 px) at (308, 108), (512, 108), (1350, 108) and (1556, 108)
- **Gold bars along the wall:** x 163–709 and 1160–1707, each about 546 px long and 20 px high.
- **Folded white towel:** rotated about 25°, centre about (908, 198), sides about 365 × 183 px (±10 px).
- **Teal toothbrush cup:** centre (830.2, 415.4), Ø 46.5 px. It is a different object from the moving box: round, higher up, and static.
- **Loose toothbrush:** yellow-green with a white head, lying diagonally from (752, 404) to (835, 486). Total length about 116 px; the yellow handle is 89 px.
- **Front-edge hardware:** a long gold drawer pull at x 764–1097 (333 px), plus small gold knobs at x ≈ 354, 430, 1431 and 1507 (y ≈ 675).
- **Floor:** a woven rug covers y ≳ 885.

## Ambiguities
- **Two teal objects:** the moving box and the static cup in the centre. The tracker excludes y < 450 so it only picks up the box.
- **Faint ghost around the box:** a pale, semi-transparent region shows above and below the box (about y 515–545 and 625–650). It is a shadow or reflection and is not part of the mask.
- **No perspective information:** the scene is top-down and 2D, so one metres-per-pixel scale applies to everything on the counter plane. Objects at other heights, such as the wall bars and faucets, may differ slightly from that scale.
