# simulation_0150 – measurement record

Blender render, 3D, 24 fps, 42 frames (t = frame/24), 1920x1080. Underground parking garage ("B1"),
**static camera** looking straight down the aisle (vanishing point of the ceiling light tubes ≈ (960, 540),
i.e. image centre → level camera, optical axis parallel to the aisle). One moving object: a **yellow sports
coupe** that pulls out of the right parking bay and drives right→left across the image, side-on, at roughly
constant depth. No metric scale is assumed anywhere.

## Files
- `scene.json` – inventory, static-object pixel extents, camera, events, car side-on pixel dimensions.
- `tracks/car_track.csv` – **main car track**, every frame 0-41. Columns:
  - `visible`, `occluded` (`right_pillar` = rear hidden behind right near pillar x≥1831, frames 0-21;
    `left_pillar` = front hidden behind left near pillar x≤95, frames 28-40; frame 41 fully hidden), `pose`.
  - Mask extents: `front_x` (left end, blank if hidden), `rear_x` (right end, blank if hidden), `top_y`,
    `contact_y` (ground contact / bottom), `bbox_*`, `len_px_visible`, `height_px`.
  - Wheels: `front_wheel_x/y`, `rear_wheel_x/y` (rim-centroid of white rim pixels), `rim_diam_px`.
  - `step_dx_px` = x shift of the car from frame i-1 to i (negative = leftward); `step_dx_upper` (body
    y 540-700) and `step_dx_lower` (y 700-860) separately.
  - **Origin estimates** (frames 12-40): `x_wheelmid` (midpoint between wheel centres) and `x_bodyc`
    (bbox centre, bumper..rear; = x_wheelmid + 26), y: `y_wheel_axle` 793.5, `y_bodyc` 705, `y_contact` 882.
    Built by cumulating the template-match shifts, anchored at frame 24 (fully visible).
    Frames 0-11: no origin (car yawed and mostly hidden) – only the front edge and visible bbox.
- `tracks/car.csv` – mask-only version (with edge-extrapolated centres `center_x_body` using L=1154 px,
  `center_x_wheels` using wheelbase 711 px); superseded by car_track.csv for positions.
- `tracks/car_auto.csv` / `car_raw.csv` – intermediate segmentation output (raw includes floor reflection; ignore).
- `tracks/car_ref_dims.json` – side-on length / wheelbase samples from frames 22-27.
- `scripts/` – `track_car2.py` (segmentation + wheels), `finalize_car.py` (extents, occlusion),
  `build_track.py` (template-match track → car_track.csv), `shift_tm.py`, `tail_tm.py`, `check_track.py`,
  `crops.py`, `explore*.py`.

## Method
Background = frame 41 (car gone; camera static). Mask = max-channel |frame − bg| > 45, morphological
open/close, largest component. The glossy floor reflects the car and ceiling lights: the mask is cut at the
contact row (last row whose width ≥ 40 % of the widest row), and front/rear ends are measured only on rows
above contact−45 px so the contact shadow ahead/behind the car is excluded. Overlays (frames/ov2_sheet.png,
frames/check_track.png) confirmed the mask covers the whole car and that wheel circles predicted from
`x_wheelmid ± 355.6` land on the real wheels in frames 14-34.

## Car pixel dimensions (side-on, frames 16-37, constant to ~1 %)
length 1154 px (bumper→rear), height 355 px (roof y 528 → ground y ~882), wheelbase 711 px, rim
diameter ~125 px, tyre outer diameter ~175 px (approx.), wheel axle y ≈ 793. The car is at constant depth
while side-on (contact y 876-884, wheel y 789-798), so one px/m scale applies to its motion in frames ~14-40.
Width (across the car) is never seen side-on; at frames 0-6 only the front fascia is visible (partially).

## Motion (for answering sessions; pixel units)
Per-frame shift (px/frame, f i-1→i): 13: 67, 14: 72, 15: 75, 16: 78, 17: 81, 18: 85, 19: 87, 20: 90,
21: 92, 22: 93, 23: 95, 24: 97, 25: 98, 26: 99, 27: 100, 28-31: ~101, 32: 100, 33: 99, 34: 99, 35: 98,
36: 97, 37: 94, 38: 91, 39: 80, 40: 78. I.e. accelerating until ~f28-31, then slowing.
Lower-body patches move ~1.5 px/frame faster than upper-body patches (body parts at slightly different
depths / perspective); `step_dx_px` is the mean of both — ~1.5 % uncertainty in speeds.
Frames 0-13 the car is turning out of the bay (yaw ~90°, approaching the camera: contact y 809→877), so
image motion there is not a pure translation; frames 12-13 have slight residual yaw.

## Reliability / ambiguities
- Positions frames 14-37: ±3 px (cumulative drift over the track ≲ 10 px). Frames 38-40: the renderer draws
  the visible tail as a smeared blob; shifts from a small tail patch, low reliability (±5 px/frame).
- Frames 0-11: only partial car, yawed; bbox only.
- Fully visible only frames 22-27 – the only frames where length is measured directly.
- Contact/bottom y is from the shadow line (±4 px); floor reflection of the yellow car lies below it.
- Static object extents read by eye from grid crops (±5 px).
- For 3D questions: depth along the optical axis is roughly constant during the side-on pass; if depth_info
  is given, focal length f ≈ pixel_size × depth / world_size (car length 1154 px or wheelbase 711 px), and
  lateral world displacement ≈ pixel displacement × depth / f (depth to the origin, small x-offset from centre
  makes depth vary slightly: d = sqrt(Z² + X²)).
