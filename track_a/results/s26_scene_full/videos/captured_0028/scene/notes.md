# captured_0028 – measurement record

Lab video, 3D, 1280x720, 24 fps, 49 frames (t = 0 … 2.000 s). Camera static. Background (person, walls, tripod)
blurred by a Segment-Anything edit; only the **white ball** and the **wooden tabletop** are sharp.

## Scene
A person stands behind a small single-post wooden table. Their right hand holds a white ping-pong-type ball still
(frames 0-11), raises it slowly (12-20), releases it at ~frame 21 (from rest; drop, no throw — the fall is a clean
parabola with ~6-10 px/frame² increments), and the ball bounces on the tabletop three times (frames 26, ~36.3, 47) with
apexes at frames 32 and 42. The ball drifts right (x 720 -> 766) and **toward the camera**: its apparent diameter grows
from 17 px to ~24-25 px, and its bounce points move down in the image (bottom y 420 -> 428 -> 454), i.e. forward on
the tabletop. Only one moving object of interest; nothing occludes the ball.

## Files
- `scene.json` – inventory (ball, table, person, tripod, walls), camera, table geometry, events.
- `tracks/ball.csv` – every frame 0-48: `center_x, center_y` (recommended reference point = visible ball centre),
  `cx/cy_mask_centroid` (raw centroid of the bright mask), bbox (x0,y0,x1,y1 exclusive, w,h), mask length along main
  axis / width across, mask area, `diameter_est_px` (= bbox_w), `motion_blurred` flag, `occluded` (always 0).
- `scripts/` – `probe.py` (blob search), `track_ball.py` (track + overlay), `crops.py` (zoomed montage), `table.py`
  (tabletop segmentation).

## How measured / reliability
- Ball mask: local window around previous position, threshold halfway between local background median and ball
  peak brightness, low saturation. Overlays checked visually for all 49 frames (frames/ball_overlay.png, scratch).
- When sharp (frames 0-21, apexes), the lower shaded half of the ball falls below the threshold, so the mask is
  only ~12 px tall; there `center_y = bbox_y0 + bbox_w/2` (top edge + radius). When vertically motion-blurred
  (bbox_h >= bbox_w; frames 22-30, 34-39, 43-48) the mask is a streak and `center_y` = streak midpoint (mid-exposure
  position). Accuracy ~±1 px in x, ±1.5 px in y (sharp), ±3 px in y (blurred). Bounce frames 26, 36, 37, 46, 47
  are long streaks that may contain the descent and rebound in one exposure.
- Apparent diameter = horizontal bbox width (not affected by vertical blur): 17 px (frames 0-21), 20-22 (28-34),
  24-25 (38-42), ~24-27 (43-48, slight horizontal blur inflates). For a back-projection: depth ≈ f·D/width_px with
  f = 763 px (benchmark camera, HFOV 80°) and D the real ball diameter if given; principal point ≈ (640, 360). Width
  is ±1 px, i.e. ±4-6 % in depth — prefer given depth_info when available.
- Table (frame 0, static): top surface corners front-left (464,484), front-right ≈(965,497), back-left (564,430),
  back-right ≈(850,425) (right side partly hidden by the person's hand, ±5 px). Front edge ≈501 px long, back edge
  ≈286 px; front-edge board thickness ≈20 px; post x≈710-750 below y≈515. Strong perspective (table close to camera).

## Ambiguities
- Release frame: ball reaches its highest held position at frames 20-21 and is clearly falling from 22; take
  release ≈ 21 (±1). The hand is near the ball during 22-24 but appears not to push it.
- Exact bounce contact is within the blurred frame (26; between 36 and 37; 47).
- Person is too blurred to track; their size/pose not recorded beyond an approximate bbox.
