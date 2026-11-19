# simulation_0188_segmented — measurement record

3D scene, segmentation video (Blender render with the background replaced by plain white), 1920x1080, 30 fps,
60 frames (t = frame/30). Everything is in pixels and seconds; no metric scale was guessed.

## Content
One object: a **truck** (aircraft catering high-loader: white MAN-style cab facing right, long grey cargo box behind
it, grey railing/stair platform on top of the box above the cab). It drives straight, to the right and toward the
camera, starting essentially at rest at frame 0 and speeding up the whole time. No other objects, ground, markings or
shadows are visible (white background), so there are no static objects to measure.

## Files
- `scene.json` – inventory, key pixel sizes at frames 34 and 43, events, camera/perspective notes.
- `tracks/truck.csv` – one row per frame 0–59:
  - `visible`, mask bbox (`bbox_x0..y1`, `bbox_w`, `bbox_h`), mask centroid `mask_cx/cy`, `area`, `clipped` (L/R image
    edge), `fully_visible` (only frames 34–43).
  - Tracked points, each with an `_in` flag (1 = inside the image; 0 = **extrapolated** off-screen position, use with
    care): `front_hub`, `rear_hub` (wheel hub centres), `front_bumper_right` (leading corner of the bumper),
    `box_rear_top`, `box_rear_bottom` (rear vertical edge of the box), `stairs_top` (top rail of the platform).
  - Derived: `axles_mid_x/y` (midpoint of the two hubs – best proxy for the vehicle root/centre, at axle height),
    `wheelbase_px`, `hubline_angle_deg`, `length_bumper_to_boxrear_px` (apparent overall length), `box_rear_height_px`,
    `stairs_top_to_front_hub_px`, `front/rear_tyre_bottom_y` and `front/rear_wheel_radius_px` (hub to lowest mask pixel
    below it, i.e. ground contact), `boxtop_slope/icpt` (box top edge line y = slope·x + icpt) and `vp_len_x/y`
    (vanishing point of the truck's length direction).
- `scripts/` – `mask_track.py` (mask = pixels with min(B,G,R) < 235, small blobs removed), `anchors_ref.json` +
  `anchors_klt.py` (anchor points clicked at frame 34 and propagated forward/backward with pyramidal KLT, local affine
  from the 40 nearest forward-backward-checked features), `build_record.py` (writes the CSV), `profile.py`,
  `extremes.py`, `wheels_hough.py` (exploration), `view.py`, `overlay.py` (visual checks).

## Key facts
- Fully in view only frames 34–43. Frames 0–33 rear cut by left edge; frames 44–58 front cut by right edge; frame 58
  tiny remnant; frame 59 empty. Hubs in view: front hub frames 0–46, rear hub frames 25–54.
- Events: start of motion ≈ frame 0 (front hub step 0.56 px f0→f1, then steadily growing); rear hub enters f25;
  whole truck in view f34; bumper reaches right edge f44; front hub exits f47; rear hub exits f55; last visible f58.
  No bounce, contact, braking or turning.
- Sizes at frame 34 / 43 (px): bumper-to-box-rear length 1129 / 1384, wheelbase 498 / 668, box rear edge height
  292 / 328, front wheel radius 69 / 79.5, rear 61 / 70.6, full bbox 1112×581 / 1378×679 (bbox height = top of
  platform to bottom of front tyre).
- Perspective: the vanishing point of the truck's length direction (box top edge ∩ hub line) is stable at about
  (−3030, 538) for frames 16–56 → the truck drives straight along its own axis (its hub trajectory points at that VP)
  and does not yaw. VP row ≈ 538 ≈ image centre row → ground-plane horizon at y ≈ 538, camera essentially level.
  The truck approaches the camera: apparent sizes grow ~1.3× (heights) to ~1.5–2× (lengths) between frames 0 and 43,
  ~1.6–3.8× by frame 57 (see CSV columns).
- Camera: assumed static (simulation convention); cannot be checked against background since it is uniform white.

## Reliability
- Mask bbox: ±1–2 px; the mask includes the dark under-chassis and a thin tail-lift plate sticking out at the rear
  (visible from ~frame 50). bbox/centroid are cut-off measures except in frames 34–43.
- Tracked points: verified on overlays at frames 0, 20, 43, 46, 50, 54 – stay on target within ~5–10 px. Hub clicks
  at frame 34 are ±3 px (hubs are dark). Off-screen (`_in` = 0) values are affine extrapolations from the visible part
  and degrade with distance from the visible area (rear hub before frame 25, front hub/bumper after frame 46).
- Wheel radius: tyres are slightly elliptical in perspective; radius is hub-to-ground along image vertical, ±2 px.
- The Blender vehicle root is not visible; axles_mid is a proxy (if the root is at ground level, use the tyre-bottom
  rows). For speeds, any rigid point gives nearly the same 3D motion since the truck does not rotate, but pixel speed
  depends on the point's depth/position.
