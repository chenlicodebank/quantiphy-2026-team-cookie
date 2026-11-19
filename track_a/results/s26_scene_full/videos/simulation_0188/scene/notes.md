# simulation_0188 – measurement record (pixels, seconds)

Video: Blender render, 3D scene, 1920x1080, 30 fps, 60 frames (t = frame/30, 0 … 1.967 s).
Content: one white airport catering truck (high-loader with a big white box body, MAN-style cab, folding platform with
railings above the cab, yellow block on the front bumper) drives from the left edge to the right edge, in an
empty grey hangar. It is the only moving object. The camera is static.

## Files
- `scene.json`: inventory (truck, shadows, hangar wall/doors, windows, lamps, floor), camera and perspective cues,
  frame-40 pixel extents of the truck, apparent-scale table, and events.
- `tracks/truck.csv`: one row per frame 0–59. Columns:
  - `frame, time, visible` (59 = not visible).
  - `bbox_x0,y0,x1,y1` = image bbox of the **visible** part of the truck. Left/right ends come from tracked keypoints
    (the rear top light minus 13·scale px for the rear edge, the bumper block plus 22·scale px for the front edge). When
    the end is out of frame the box is clipped to 0 or 1919, flagged by `clipped_left/right`. Top = top of the
    shadow-suppressed motion mask (the railings when the cab is visible, the box top from frame 49 on). Bottom = lowest
    tyre bottom, i.e. hub + scaled tyre radius. `bbox_cx/cy`, `mask_len_px`, `mask_height_px` come from that bbox.
    `mask_area_px` is the mask area, which has holes because the white box is close to the light wall colour.
  - `app_scale`: apparent size relative to frame 40, from vertical pixel separations of keypoint pairs on the same
    vertical (front hub → cab side-window corner; rear plate → rear top light; and others). It is 0.725 at frame 0,
    1.000 at 40 and 1.428 at 57, so **the truck approaches the camera all the time**. The front end grows a bit faster
    than the rear end (at frame 46: front 1.134, rear 1.105) because the truck is oblique and its front is nearer.
    Raw separations: `front_hub_to_cabwin_dy_px` (frames 0–46), `rear_plate_to_light_dy_px` (32/33–57),
    `wheelbase_img_px` (front hub ↔ rear hub image distance, 26–46).
  - `body_centre_x/y`: proxy for the truck origin = centre of the frame-40 full bbox (932.5, 650.0), carried to each
    frame as the mean over visible keypoints of (keypoint + app_scale·offset at frame 40). `ground_centre_x/y` is the
    same idea for a point on the tyre-contact line below the body centre (941.1 at frame 40). A vehicle rig root is
    often on the ground between the axles. Values outside 0–1919 are off-screen extrapolations.
    `proxy_n_kp` = number of keypoints used.
  - `full_len_px_pred, full_height_px_pred` = app_scale × frame-40 image length 1269 / height 636. These are rough
    because foreshortening changes as the truck moves.
  - Keypoints (template-matching tracks, sub-pixel; blank when out of view):
    `front_wheel_hub` (0–46), `rear_wheel_hub` (26–53), `bumper_yellow_block` (0–43), `cab_side_window_top_rear_corner`
    (0–46, directly above the front hub at frame 40), `box_logo_front_top` (10–49, small green/yellow logo at the front
    top of the box side), `box_rear_top_light` (33–57, small orange light at the rear top of the box side),
    `rear_plate` (32–57, white plate on the rear tail-lift bracket).
  - `occluded` is 0 everywhere: nothing passes in front of the truck. Truncation by the image border is in `clipped_*`.
- `scripts/`: `seg.py` (background-difference mask; background = frame 59 for x<1500 and frame 0 for x≥1500),
  `seg2.py` (mask with cast shadow removed), `track_tm.py` (keypoint template tracker, output `_tm.json`), `track_kp.py`
  (earlier LK median-flow tracker, superseded: biased by up to 60 px; its `_kp.json` is not used), `build.py`
  (writes truck.csv), `persp.py` (vanishing points, camera-shake check), `static.py` (wall line, door windows),
  `write_scene.py`, plus the viewers `overlay.py`, `draw_kp.py` and `crops.py`.

## How it was measured / checks
- Keypoints were clicked by eye on zoomed frame 40, where the whole truck is visible. They were then tracked
  frame-to-frame by NCC template matching with a constant-velocity prediction; all NCC values are ≥0.93 except
  where a point is at an edge. Drawn on frames 0, 6, 24, 30, 36, 40, 42, 46, 50, 52, 56 and 57: every marker sits on
  its feature. The front-hub track agrees with an independent LK track within 0.4 px.
- Every tracked point moves on a straight image line (residual ≤1.4 px). That means straight-line 3D motion with no
  turning. Pixel steps grow steadily: the front hub moves 0.5, 1.7, 2.6, 3.8 … px/frame at the start and ~110 px/frame
  at frame 45. The truck accelerates for the whole clip and is (almost) at rest at frame 0.
- Camera: static (background shift ≤0.04 px).
- Perspective: the truck long axis vanishes at ≈(−3450 … −3640, 545). The point trajectories converge at ≈(−3200, 539).
  So the horizon is at y ≈ 540–545, close to the image centre row, and the camera is level (pitch ≈ 0). The truck drives
  roughly parallel to the back wall (the wall-floor line also heads to x ≈ −3000 on the horizon). It moves right and
  toward the camera; its image path slopes down to the right (front hub y 805 → 947).
- Full-truck pixel extents at frame 40: x 298 (rear box edge) → 1567 (bumper), y 332 (railing top) → 968
  (front tyre bottom). Box top is y 422 at the rear and 395 at the front. Rear tyre bottom is y 912. Hubs are at
  (622, 855) and (1220, 900). These were read on 2–3× zooms, ±3 px.

## Reliability / ambiguities
- Keypoint tracks: ±1 px. Bbox left/right ends: ±5 px. Bbox top: ±5 px (it is the railings while the cab is visible,
  so it is not the box top). Bbox bottom: ±5 px, from the tyre radius.
- The body/ground centre proxies are not the true Blender origin. They are ±15 px near frames 30–46 and worse when
  extrapolated (frames 0–12 and 50–57, where only 2–3 keypoints at one end are visible). For speeds of this rigid,
  non-rotating truck, any tracked keypoint gives the same 3D speed. Choose the keypoint whose depth best matches the
  given depth_info, or use the proxy.
- Shadows: a large soft shadow on the floor around and behind the truck. From frames ~15–30 the railings cast a
  shadow on the floor ahead of the cab. From frames ~50–58 a sharp dark quadrilateral shadow lies on the floor to the
  left of the rear, at y ~720–775. All of these are excluded from the bboxes. The raw masks (`frames/masks*`, scratch)
  include some of them.
- The white box against the light wall makes the masks holey, so the mask area is only indicative.
- Frame 58: only a few-pixel sliver of the rear bracket at the right edge (bbox set by eye). Frame 59: truck gone.
- Motion blur is small. The wheels rotate, but the hub templates still match.
