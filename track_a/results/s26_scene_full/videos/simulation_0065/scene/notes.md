# simulation_0065 – measurement record

3D Blender render, 2160x1080, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). All values are in full-resolution
pixels (x right, y down) and seconds. No metric scale was assumed.

## Scene
Elevated **static** camera looking down a straight road across a 4-way intersection (grey asphalt, no lane markings,
beige sidewalks). Four moving objects, all visible for the whole clip (frames 0-71):

| name | what | motion |
|---|---|---|
| white_van | white cargo van seen from behind, left lane | drives straight away (up the image), speeds up from almost rest |
| taxi | yellow taxi with TAXI roof sign, starts right of the cyclist | turns RIGHT into the cross street, side-on driving right from ~f57-60 |
| cyclist | man in a dark suit on a bicycle, between the van and the taxi | rides straight away, steady |
| pedestrian | man in a white T-shirt and jeans on the near-right sidewalk, starts beside the green trash can | walks right ~4.3 px/frame, nearly constant depth; touches the right image edge from f68 |

Static objects (pixel extents and positions in `scene.json → static_objects`): 4 traffic lights (near-right corner one
457 px tall, with a pedestrian-crossing triangle sign; far-left; far-centre; near-left one cut by the left edge),
3 lamp posts (the near double-lantern one right of the trash can, a far one directly behind it, a far-centre one),
the green trash can (49 x 80 px), 3 brick-bordered tree grates, and the sidewalk corners/curbs.

## Files
- `scene.json`: inventory, static objects, events, camera/perspective, apparent size at frames 0/12/24/36/48/60/71.
- `tracks/<object>.csv`: one row per frame (0-71). Columns:
  `ref_x, ref_y` (reference point, see below), `ref_kind`, `bbox_cx/cy` (bbox centre), `mask_cx/cy` (mask centroid),
  `ground_x/ground_y` (bottom-centre of bbox = lowest mask pixel), `bbox_x0..y1, bbox_w, bbox_h`,
  `mask_len_major / mask_wid_minor / major_axis_deg` (PCA extents of the mask in the image), `mask_area_px`,
  `occluded` (taxi overlaps the near-right traffic-light pole), `truncated` (touches the image border).
- `camera_shift.json`: per-frame [frame, dx, dy] background shift against frame 0 (all < 0.01 px, so the camera is static).
- `bg_small.jpg`: half-resolution median background.
- `scripts/`: `bg.py` (median background, camera check) → `track.py` (segmentation/tracking, writes *_raw.csv and
  overlays in ../frames) → `finalize.py` (reference points, final csv) → `make_scene.py` (scene.json, removes raw csv);
  `crop_bg.py` (grid crops for reading static extents), `check_refs.py` (draws the final points), `summarize.py`.

## How it was measured
Background = median of every 3rd frame, patched where the slow van/cyclist left a ghost (rows < 440 taken from frame 0,
rows >= 440 from frame 71, x 480-930). Foreground = |frame - bg| > 28 (vehicles, with cast-shadow suppression:
uniformly darker pixels with no colour change are removed) or > 14 (humans, only mild shadows removed so that dark
clothing and thin wheels stay). Each object takes the connected components that touch its previous bbox
(vehicles +-25 px; humans inside a +-15/30 px window so the van's shadow cannot join the cyclist). The masks and
points were drawn on frames 0, 20, 24, 30, 36, 40, 46, 56, 60, 71 and inspected: they cover the right objects and their
full extent.

Reference points (the Blender origin is not visible, so these are image proxies):
- vehicles: `ref` = bbox centre; `ground_y` = lowest pixel (rear tyres/bumper while seen from behind; tyre bottoms when side-on).
- pedestrian: pelvis estimate, x = mask centroid, y = bbox_y0 + 0.47*bbox_h.
- cyclist: hips/saddle estimate, x = mask centroid, y = bbox_y0 + 0.53*bbox_h (ratio read on frame 0).
For a 3D distance, combine an image point with the given depth_info and a focal length you estimate.

## Reliability and caveats
- Camera: static (sub-0.01 px). Perspective: the far-road curbs meet at a vanishing point near (800, -208), so the
  ground-plane horizon is ~208 px above the top edge; cross-street curbs are almost horizontal (roll ~0). Focal length unknown.
- white_van: very clean (+-2 px). The bbox width includes both side mirrors (mirror-to-mirror). Its top/bottom move
  ~1-2 px/frame for f0-6 and ~8 px/frame of ground_y from ~f36: it pulls away from almost rest and keeps accelerating
  in the image. Size shrinks from bbox 279x333 (f0) to 138x162 (f71), i.e. it ends about 2x farther away.
- taxi: frames ~22-58 its body passes behind the near-right traffic-light pole and its two pedestrian signal heads
  (x 1335-1420, y 365-440). The mask is split there; the bbox is still mostly right, but `bbox_x0` (rear end) is
  hidden by about 10-25 px around f53-59 (jumps of 18-24 px in x0 at f56-57), so the bbox centre jumps ~10 px there.
  The front (`bbox_x1`) and top (`bbox_y0`) stay smooth all through. `bbox_y1` jitters +-5-10 px from leftover
  shadow under the car (e.g. f47, f50). The image major-axis angle goes from ~50 deg (rear view, mask nearly square,
  angle meaningless) through -63 at f12 down to 0 at f60. Side-on length (f60-71) is 413-423 px (median 422). The front reaches
  the near double lamp pole (x~1960) only at the last frame.
- cyclist: head top (`bbox_y0`) is reliable. The thin bicycle wheels are low-contrast, so the lowest pixel varies
  between the wheel and the foot/pedal: the height is ±10-20 px noisy (168 px at f0 → 88 px at f71) and the
  ref_y point jitters as a result. The rider's width is 50 → 29 px.
- pedestrian: clean. The walking height (head to lowest foot) is 148-162 px (median 154) depending on gait phase (min/max in
  scene.json); the width swings 44-95 px with the stride. Height and position barely change, so the depth is nearly
  constant (y of feet 585 → 566, slightly farther). Truncated by the right image edge at f68-71 (x extents unreliable there).
- Events: all four move from frame 0 to frame 71; nothing starts or stops inside the clip; no contacts or collisions.
  Taxi turn: f0 to ~f57-60, then straight. Van: straight and accelerating (image speed rises until ~f36).
- Shadows: soft cast shadows under the vehicles are removed by the shadow test. Some dark window pixels are also
  removed (holes in the mask), so `mask_cx/cy` is a little biased; for vehicles use the bbox centre.
