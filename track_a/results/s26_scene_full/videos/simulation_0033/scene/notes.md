# simulation_0033 – measurement record

Blender render, 3D scene, 1080x1080, fps 30.005455, 54 frames (t = frame/fps, last frame 53 = 1.766 s).
All values are pixels (x right, y down) and seconds. No metric scale was assumed.

## Scene
A street seen side-on: a white brick building facade (fronto-parallel), with a wet sidewalk, curb and a two-lane wet road in front of it.
The **camera is static** (phase correlation of the wall vs frame 0 is under 0.02 px in every frame). It is level, and its image plane is parallel to the facade and the street:
facade verticals are vertical, both window rows have the same pixel width and all ground lines are horizontal. There is no visible horizon. For a level camera
it is at the principal-point row (assumed y = 540).

Moving objects (all motion is horizontal in the image, parallel to the image plane):
1. **orange_car**: orange fastback sports sedan with dark wheels and red calipers, in the far lane. It drives right to left and **decelerates throughout**, without stopping.
   Its apparent size is constant: roof y = 742, tyre/ground y = 982, wheel radius ~53 px in every frame, so it stays at a constant depth.
2. **grey_car**: dark grey/silver car in the near lane, very close to the camera, with strong motion blur. It drives right to left much faster (~115-130 px/frame) and passes in front of the orange car in frames 26-37.
   It is never entirely in frame.
3. **pedestrian**: a man in a navy jacket and grey trousers with a blank white face. He walks slowly left to right on the sidewalk near the wall,
   behind the hydrant and the lamp post (so he is farther from the camera than both cars).

Static objects: lamp_post, fire_hydrant, graffiti "NEOM", 4 windows (upper row cut by the top edge), wall, sidewalk, curb, lane line, road.
Their pixel extents are in scene.json (measured on the clean background plate, thresholded with the dark/teal/white masks in s9_static.py and checked visually on gridded frames).

## Files
- `scene.json`: inventory, camera, apparent sizes, static extents, events.
- `tracks/orange_car.csv`: one row per frame.
  - `ref_x, ref_y` = axle midpoint (wheel centres from Hough circles; when only one wheel is found, ±wheelbase/2 with wheelbase = 509 px), y = axle height 929.
    `ref_method` says how each row was obtained. Frames 1-9 use front bumper + 147.5 + 254.5, with the front overhang measured at f10-11.
    Frames 12, 28 and 32 are interpolated. Frames 1-11 give x > 1080 (the centre is still off-screen).
  - `x_min/x_max` = extents of the orange mask (largest component of orange & changed-vs-background, closed with 25 px).
  - `front_x` / `rear_x` are filled only where that bumper is truly visible: front f1-30, rear f26 and f33-53.
  - `y_top` = 742 (roof), `y_ground` = 982 (tyre contact), `height_px` = 240.
  - `bbox_cx` is filled only when both ends are visible (f26).
  - Also: wheel centres and radius, edge-clip flags, and `occluded_by_grey_car` (f26-37).
- `tracks/pedestrian.csv`: `ref_x` = head centre x (proxy for pelvis x; the body is upright), with raw head blob values and the correction method.
  - f25-33: left head edge + 12.5. f37-41: right head edge - 12.5, because the lamp pole (x 186-199) hides part of the head.
  - f34-36 are interpolated (head fully hidden).
  - `feet_y` is given where the soles are visible (f5-24, ~871). `est_pelvis_y` = 765 is a rough estimate (≈ 53% down from the head top).
- `tracks/grey_car.csv`: manual readings of the grey car's leading (front, left) edge for f20-28 and trailing (rear) edge for f33-40, from gridded crops (s7_gridcrops.py).
  Uncertainty is ±20-40 px because of motion blur and the sloped body. `top_y_approx` is rough.
- `scripts/`: s1 (camera shift + median), s3 (clean background plate = frame 0, right edge from f53, pedestrian area from f36 + inpaint), s5/s6 (masks, wheels, pedestrian), s8 (head), s9 (static), s10 (assemble tracks), s11 (overlay check).
  The background plate `bg_clean.png` was deleted to keep the record small. Re-run s3_cleanbg.py to regenerate it before s4-s9. `bg_clean_preview.jpg` is a JPEG copy. Raw per-detector CSVs are `scripts/raw_*.csv`.

## Key numbers (orange car)
- Wheelbase 509 px. With both wheels detected (f38-43: 509, 509, 505, 508, 508, 508), and 515 at f21.
- Wheel diameter ~106 px. Height from roof to ground is 240 px.
- Bumper-to-bumper length is 776 px at f26 (unoccluded), and 780-782 at f27-30.
- Perspective adds the visible front face when the car is right of centre and the rear face when it is left of centre. Front overhang drops from 147 to 120 px as the car moves left, and rear overhang is 165-175 px at the left.
  The best "side length" is about 780 ± 10 px.
- Leftward pixel motion per frame:
  - front bumper ≈ 34 (f1-5) → 28 (f20-25)
  - axle midpoint ≈ 26 (f25) → 20 (f37)
  - rear bumper ≈ 20 (f37-40) → 12 (f50-53)
  - Steady deceleration.

## Reliability
- Orange car `ref_x`: ±3 px per frame (Hough jitter, e.g. f47 and f51 look off by ~5 px). For smooth late-clip motion, `rear_x` (f37-53) and `front_x` (f1-26) are cleaner, ±1-2 px.
  Front edges at f1-9 are motion blurred. At f31-37 the front is hidden behind the grey car, so x_min there is not the bumper. At f38 x_min = 14, but the front bumper is at ~0 (edge).
- Pedestrian: ±1 px where the head is visible, ±3 px at f25-41 (lamp correction), interpolated at f34-36. Head top bobs 650-654 with the gait. Rest/standing height ≈ 215-218 px, walking 215-221 px.
- Grey car: low reliability; use only for rough speed or timing.
- Depth/focal length: no depth is known here. If a question gives depth_info (distance camera → object origin) and a size prior, f ≈ pixel size × depth / size.
  The orange car is at a constant depth with its side fronto-parallel, so its wheelbase, length or height in px are good for this. Remember that depth is to the origin, not the near surface.
  The pedestrian is farther away (near the wall) than the orange car; the grey car is much nearer. Do not use one scale for all three.

## Ambiguities
- "Car" alone most likely means the orange car (the only car clearly visible). The grey car is a blurred foreground vehicle.
- Wet-road reflections of the orange car appear below y = 982. They were excluded from the masks (mask cut at y = 985).
- Hydrant rust is orange but static; it is excluded by background differencing.
- The vehicle-root vertical position is unknown (axle y = 929, ground y = 982, box centre y = 862). It is constant, so it does not affect speeds.
