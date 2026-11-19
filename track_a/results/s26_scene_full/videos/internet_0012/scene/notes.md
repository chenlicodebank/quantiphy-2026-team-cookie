# internet_0012 — measurement record (pixels, seconds)

**Video:** 2160x3840 portrait, 59.346597 fps, 108 frames (t = frame/fps, 0 to 1.803 s). An internet clip shot straight
down by a drone over a long bridge or highway crossing water. Treated as 2D: the road plane faces the camera.

## Scene and inventory (details in scene.json)
- The road runs vertically and is tilted about 0.4° (x drops about 7 px per 1000 px down the image).
  - **Left carriageway** (x≈690–1040): traffic moves **down** the image (+y).
  - **Right carriageway** (x≈1080–1400): traffic moves **up** (−y).
  - A concrete median (x≈1036–1080) separates them. Railings, lamp posts and water lie on both sides.
- Moving objects: 4 vehicles, all visible and moving in every frame 0–107. None stops or changes lane.

| name | what it is / how to tell apart | body L x W (px) | centre f0 → f107 (px) |
|---|---|---|---|
| white_car_upper | white sedan, left carriageway, lane x≈868, starts y≈1462 | 121.5 x 48 | (868.5,1461.8) → (869.8,2127.4) |
| white_car_lower | smaller white car, left carriageway, lane x≈829, starts y≈2620 | 105.5 x 46 (105.7–108.9 per frame) | (829.0,2620.3) → (819.8,3166.3) |
| dark_car | dark grey SUV, right carriageway, lane x≈1200; starts level with truck cab and overtakes it | ≈127 x 55 (123–131) | (1200.5,3159.7) → (1200.5,2176.9) |
| truck | semi-truck with a yellow cab and long white trailer, right carriageway, outer lane x≈1320 | 457 x 72.7 (outer ≈77) | (1318.4,3323.6) → (1321.0,2653.0) |

- Lengths run along the road (y). This is the main motion direction, measured bumper to bumper on the physical body.
  Shadows fall below and to the right of each vehicle and are excluded.
- Static objects (scene.json → static_objects):
  - Lane dashes and their y ranges.
  - Lane width, ≈96–98 px between line centres.
  - Solid edge lines and the median.
  - 12 lamp heads with positions; spacing ≈711 px along the road.
  - Deck extent, x≈600–1530.

## Files
- `scene.json`: inventory, sizes, f0/f107 centres, net displacement, camera, frame duplication, static objects and events.
- `tracks/<vehicle>.csv`: one row per frame (0–107). Columns:
  - `cx,cy`: **reference point**, the centre of the physical body box.
  - `bx0,by0,bx1,by1`: body box.
  - `front_y,rear_y`: front and rear ends. Front = by1 for the white cars (they move down) and by0 for the dark car and truck.
  - `body_length_px,body_width_px`: constant reference size.
  - `match`: template score.
  - `tb*`: template box, which includes margin and shadow.
  - `edge_y0,edge_y1,edge_cy,edge_length_px`: per-frame ends measured independently, at the steepest brightness rise or fall
    along the centre column.
  - Cars only: `mask_*`, extents from background subtraction. These **include shadow** and sometimes a lane dash, so treat them as rough.
    - mask_length_px / mask_width_px come from a minimum-area rectangle around the mask.
  - `occluded`: occlusion flag.
  - `dup_of_prev`: 1 if the frame repeats the previous one.
- `tracks/camera_shift.csv`: per-frame phase-correlation shift of the bridge strips (railings and median) between consecutive frames, plus the running total.
- `tracks/frame_duplicates.csv`: mean absolute difference from the previous frame, and the duplicate flag.
- `scripts/`, run in this order:
  1. camshift.py
  2. blobs.py (median background)
  3. track.py (template tracking, body boxes, edges, duplicates)
  4. edges.py, profiles.py (edge profiles used to set the body boxes)
  5. static.py, zoomcheck.py
  6. overlay.py (visual check)
  7. make_scene.py

## How it was measured, and how reliable it is
- **Positions:**
  - Each vehicle was tracked by template matching with a subpixel peak, using a rigid top-down template from frame 0
    (frame 107 for the truck).
  - The body box was fixed once from half-maximum brightness edges at frames 0, 54 and 107, then moved with the match offset.
  - Overlays at frames 0, 33 and 100 confirm the boxes sit on the vehicles.
  - Along-road (y) positions are good to about ±1 px for the white cars and truck, and about ±2 px for the dark car.
    - The independent `edge_cy` agrees within 1 px for the white cars and within 1–3 px for the dark car.
    - For the truck, `edge_cy` is unreliable: the front edge flips between the bumper and the windshield.
  - Lateral x for the dark car may be off by up to about 3 px.
- **Camera:** static, so no background compensation is needed.
  - Lamp heads move ≤2 px over the clip, and the gap between the top and bottom lamps stays constant within 0.5 px, so there is no zoom.
  - Bridge-strip drift is ≤1.1 px.
- **Frame duplication (important):**
  - 46 of the 108 frames copy the previous frame. The pattern is regular: 3 in every 7 frames. The list is in scene.json.
  - So one-frame differences alternate between 0 and about 1.75 times the true per-frame step.
  - Approximate step sizes between distinct frames (raw tracks, positions only): white_car_upper ≈11 px down,
    white_car_lower ≈9 px down, dark_car ≈16 px up, truck ≈11 px up.
  - Use differences over several frames (or fits) for any rate, with t = frame/fps.
- **Scale non-uniformity:**
  - Lane dashes are evenly spaced on the road, yet their period is 392–397 px near the image centre (y≈1800–2200)
    and 403–406 px near the top and bottom. That is about ±1.7%, symmetric about the centre, most likely lens distortion.
  - Vehicle pixel lengths follow this: white_car_lower grows 3% as it moves down; dark_car shrinks from 131 to 123 px as it moves toward the centre.
  - The benchmark uses one scale factor, prior value divided by prior pixel size. The constant `body_length_px` values are
    mid-track measurements. Per-frame sizes are in `edge_length_px`; these are noisy for the truck.
- **Sizes:**
  - White cars: ±1 px.
  - Dark car: ±3 px, because the dark body, reflections and shadow blur its ends.
  - Truck length (front of cab to rear of trailer): ±3 px at frame 107, where the truck centre is at y≈2653. Near y≈3300
    (frame 0) its true pixel length is probably about 1–2% larger.
  - Truck width is 72.7 px at the trailer half-maximum, or about 77 px including the edge dark ring and mirrors.
- **Occlusion:** none for the cars. During frames 19–90 a thin overhead lamp arm (y≈2977, x≈1300–1400) crosses the
  truck. It covers less than 10 px and does not affect tracking.
- **Events** (frame/t, interpolated on the track; because of duplicate frames, true crossing times are uncertain by about ±1 frame):
  - Frame 0–1: the dark car's front is level with the truck's front.
  - Frame 22 (0.374 s): the dark car's centre is level with the truck's front.
  - Frame 37 (0.630 s): white_car_lower and dark_car pass each other, centres level in y.
  - Frame 43 (0.729 s): the dark car's rear bumper is level with the truck's front, so the dark car is fully ahead.
  - Frame 62 (1.050 s): white_car_lower and truck centres are level in y.
  - white_car_upper and dark_car almost meet at the end: cy 2127 vs 2177 at frame 107.
- **Ambiguities:**
  - There are two white cars: "upper" is the larger sedan in the inner lane; "lower" is smaller, in the lane further left, and lower in the image.
  - Car shadows add about 5–10 px below and to the right of each car; they are excluded from the body boxes but included in the mask boxes.
  - No metric scale is assumed anywhere.
