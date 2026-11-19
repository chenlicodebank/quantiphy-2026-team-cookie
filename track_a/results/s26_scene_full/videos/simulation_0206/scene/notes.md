# simulation_0206 — measurement record

Video: Blender render, 3D scene, 2124x1080, 24 fps, 30 frames (t = frame/24, 0 … 1.208 s).
Content: an old manual typewriter drops from the top of the frame onto a cluttered desk, lands, tips/rocks and comes to rest.
**The typewriter is the only moving object.** Camera is static (frame 0 vs 29: no pixel change outside the typewriter regions).

## Files
- `scene.json` — inventory (all objects with description, pixel bboxes [x0,y0,x1,y1] at frame 0), camera, perspective cues, events.
- `tracks/typewriter.csv` — one row per frame 0-29: `ref_x, ref_y` (reference point = bbox centre, proxy for the object origin),
  raw mask bbox, `bbox_x1_clean / bbox_y1_clean` (corrected edges), bbox w/h, bbox centre, mask centroid, mask area,
  principal-axis length/width (`major_len`, `minor_len`, angle), `clipped_top`, `occluded`, `clean_box` (1 = trustworthy box), `phase`, `note`.
- `scripts/` — `track.py` (segmentation + track), `finalize.py` (corrections, scene.json), `view.py`/`closeup.py`/`montage.py`/`shadowtest.py` (inspection).

## How measured
Background = last frame with the typewriter's resting region replaced by frame 0 pixels (typewriter was in the air then).
Mask = |frame − background| > 22 (max over BGR), morphological cleanup, largest component plus nearby parts. The overlays
(frames 0,4,6,8-14,16,18,20,22,28, plus close-ups of 9-23) were inspected: the masks cover the whole typewriter during the fall and at rest.

## Typewriter motion (pixels)
- Falls almost straight down at x ≈ 1236-1243. ref_y: 49, 55, 73.5, 104, 139, 194, 249.5, 324, 397, 495, 586 (frames 0-10).
  Bottom edge: 107, 113, 131, 162, 204, 255, 317, 389, 470, 579, 668. Frame-to-frame steps grow by about +11 px/frame each frame (roughly constant pixel acceleration;
  perspective/rotation adds noise). Velocity extrapolates to zero at frame ≈ 0, so the drop starts at frame 0 (t = 0).
- Apparent width stays ~290-297 px through the fall, so depth is roughly constant; the box height grows from 116 to 168 px because it rotates a little
  (major-axis angle changes from 180° to −167°) and is seen more from above as it drops.
- Frames 0-1: the top of the typewriter is cut off by the image edge. There, ref_y = bottom edge − 58 px (half the frame-2 height). This is approximate (±5 px).
- Frame 10: still in the air (gap and cast shadow visible under it). The raw mask included the shadow, so the bottom/right edges were corrected by eye (668/1385).
- Impact on the desk is between frames 10 and 11 (t ≈ 0.42-0.46 s); frame 11 is the first contact frame.
- Frames 11-18: it tips (rear rises, box top 532→483 at f15), falls back and rocks. The raw boxes here may include some cast shadow
  (bottom-right) and the darkened edge of the clock (±10 px). `clean_box = 0` marks these frames.
- At rest from frame ~23 (box constant to 1 px for frames 24-29): bbox x 1095-1371, y 524-695 (277 x 172 px), ref (1233, 609.5),
  mask principal axes 286 x 161 px at −167°.

## Static objects
All are listed with bboxes in scene.json, read by eye on gridded zooms of frame 0 (±5 px): the desk (top corners), green banker's lamp (333 px tall),
book stack, standing letter, ashtray, front paper sheet, back paper with keys/glasses (covered by the typewriter after landing),
red alarm clock (partly hidden by the typewriter after landing), picture frame, rotary telephone, brass stand, revolver on a paper slip, left chair,
back chair, wall/floor.

## Reliability and ambiguities
- Fall track frames 2-9 are good (±2 px): clean wall background, no shadow. Frames 0-1 are partly outside the image. Frames 10-18 are affected by shadow and tumbling.
- The reference point is the bbox centre, not the true 3D origin. The origin of a rigid typewriter is near its geometric centre, but projection can shift it a few px.
- Focal length is unknown. Use the given depth_info plus a known size to set the scale (e.g. the typewriter's 277-297 px width).
- No motion blur large enough to matter. Only one typewriter, so nothing can be mixed up with it.
