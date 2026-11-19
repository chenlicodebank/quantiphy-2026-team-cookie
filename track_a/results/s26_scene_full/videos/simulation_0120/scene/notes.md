# simulation_0120 — measurement record

Blender render, 2D scene, 1080x1080, 24.007839 fps, 49 frames (0–48, t = frame/fps, last frame t = 1.999 s).
Top-down view of a living room: L-shaped dark grey sofa (right), blue-grey rug, square light-grey coffee table
with chessboard, left wall with black clock/TV panel and fireplace strip, white plush toy, white curtains at bottom.
**Camera is static** (frame differencing shows no background change).

## The only moving object: robot_vacuum
White round robot vacuum (top disc, diameter **68.8 px**, sd 0.3 px over 33 unoccluded frames; visible bbox ~70x70 px).
It moves in a straight line to the right along image row y ≈ 811.5 px (constant to ±0.3 px), from centre
x = 353.4 (frame 0) to x = 757.2 (frame 48): net 403.8 px, mean 8.41 px/frame (per-frame steps 7.75–9.25 px are fit noise, path length 403.9 px;
no visible acceleration). It is already moving at frame 0 and still moving at frame 48 (no start/stop, bounce or turn).
From frame 33 it slides under the sofa's lower-left arm (sofa edge x ≈ 666, bottom edge y ≈ 834); by frames 42–48 only
a ~15 px sliver of its lower edge is visible below the sofa.

`tracks/robot_vacuum.csv` columns: frame, t_s, cx_px, cy_px (circle-fit centre = origin), bbox of the visible mask
(x0,y0,x1,y1), visible_w/h, diameter_fit_px, visible_area_px, occluded (1 from frame 33), method.
Method (`scripts/track_vacuum.py`): temporal-median background in a ROI, |frame−bg|>40 mask, largest blob, contour.
Frames 0–32: free circle fit to contour (very reliable, ±0.3 px). Frames 33–48: contour points touching the sofa
occluder removed, centre fitted with fixed radius 34.39 px (reliable ±0.5 px through f41; f42–48 rely on a short
bottom arc, ±1–2 px in x, but the y stays 811.5 and steps stay ~8.4 px, so consistent). Bboxes in occluded frames are
of the visible part only; frame 33 bbox reaches x=674 because of a sofa-edge artefact. Overlay check: `scripts/overlay_check.py`
(circles land on the vacuum in all checked frames).

## Static objects
Pixel bboxes at frame 0 in scene.json (`static_objects_px_frame0`), read from gridded zooms, ±3 px. Key ones:
coffee table 167x165 px (centre 515,541), chessboard 85x85 px (8x8, ~10.6 px squares), sofa overall 353x628 px,
seat cushions ~180x178 px, rug visible 338x560 px (continues under sofa), wall art 117x206 px, plush toy ~68x60 px.

## Caveats
- Perspective: walls lean outwards; objects on walls or tall objects (sofa top, table top) are nearer the camera than
  the floor, so their pixel/metre scale is slightly larger than the vacuum's (floor level). For 2D questions use one
  scale from the prior object, as the convention says.
- Vacuum height is not observable (top view). Its two small grey marks (front/back indicators) are on the y-axis.
- Tiny 1–3 frame flicker at TV corner (x 152–167, y 777–790) is compression noise, not an object.
- `scripts/diff_scan.py` = motion scan; `scripts/overlay_check.py` = visual check.
