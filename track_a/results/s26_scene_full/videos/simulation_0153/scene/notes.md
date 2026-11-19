# simulation_0153 — measurement record (pixels, seconds)

2D simulation, 24 fps, 42 frames (t = 0 … 1.708 s), 1920x1080. t = frame/24.

## Scene
A static camera looks down an underground parking-garage aisle (one-point perspective). The only
moving object is a **light-blue utility cart** with a roof canopy. It drives side-on across the
foreground from left to right (+x) at a constant depth: the wheel–ground contact stays at y ≈ 947 in every frame,
and once the cart is fully in view its pixel size stays constant (length 547–553 px, height 482–484 px). So the motion
is planar and one px→m scale fits the cart. There are no bounces, collisions or direction changes.
The background features (speed-limit sign "30", fire extinguishers, "B1" signs, pillars, floor arrow, ceiling light strips)
are all static. Their pixel boxes are in scene.json. They lie at other depths than the cart, so the cart's scale does
not apply to them.

## Files
- `scene.json`: inventory, cart size, static-object boxes, camera, events.
- `tracks/cart.csv`: one row per frame (0–41). Columns:
  - `ref_x, ref_y`: centre of the mask bbox. Valid only where `occluded=0` (frames 23–41). Frames 28–30 have the front edge
    contaminated (see below), so ref_x there is biased by about +15–20 px.
  - `bbox_x0..y1`: mask bounding box. y1 is capped at the ground line 948. `length_px`, `height_px` are its extents.
  - `body_x0, body_x1, body_length_px`: extents using rows y ≤ 925 only (almost the same as the bbox).
  - `front_upper_x`: right-most mask pixel in rows 700–825 (the front face/headlight of the upper body). This is the only
    feature visible in **every** frame 0–41, so use it for early motion.
  - `panel_x, panel_y, panel_score`: sub-pixel template track (NCC, template from frame 30) of the lower body panel with the
    3 orange lights between the wheels, near the bottom centre (close to where a vehicle root usually sits).
    Valid frames 18–41.
  - `centroid_x/y`, `mask_area`: mask centroid and area (biased while the cart is clipped).
  - `clipped_left` / `occluded`: 1 for frames 0–22 (rear not yet in view or blending into the dark left wall).
- `scripts/`: explore.py (camera-static check, composite background), seg.py (first mask pass), track.py (final
  track → cart.csv, overlays), multitemplate.py (consistency check of 8 rigid patches), wheels.py (Hough wheel attempt,
  too noisy to use), static.py (static-object boxes).

## Method
Background = frame 41 for x < 900 and frame 0 for x ≥ 900 (the cart is absent from those parts). Mask =
max-channel |frame − bg| > 30, open 5 / close 15, union of components > 1500 px, rows below y = 948 removed (floor
reflection). I checked overlays (frames/ov, not part of the record) at every 3rd frame: the mask covers the cart
including the canopy.

## Reliability / ambiguities
- Cart length (550 ± 3 px) and height (483 ± 2 px, canopy top 465 to tyre bottom 947) come from frames 31–41.
  Wheel diameter ≈ 105 px and wheelbase ≈ 337 px are visual (± 4 px).
- **Floor reflections/glare**: the glossy floor's light streaks change when the cart passes. In frames 28–30 this adds
  false pixels in front of the cart (x1 = 924/955/991 instead of ≈ 875/923/972). Frames 23–27 are inflated by a few px
  (length 553–570).
- **Different rigid points disagree slightly.** Per-frame x increments differ by up to ~1 px/frame. Over frames 31→41
  the rear edge (x0) moves 461 px, the front edge (x1) 467 px and the panel template 472 px. Over 22→30, rear-box and
  rear-lamp templates move 387.7 px against 392.7 px for the panel. The size grows about 1 %, which may mean slight yaw
  or depth change. The panel template may also be slightly affected by the bright floor seen under the body. Expect
  ~1–2 % uncertainty in pixel speeds depending on the point used.
- Motion profile (descriptive only): the cart is already moving at frame 0 but very slowly (front +1 px from frame 0 to 1).
  It speeds up steadily to ≈ 50 px/frame around frames 29–31 (t ≈ 1.25 s), then slows to ≈ 43 px/frame by frame 41.
  Panel-template increments over frames 18–41: 43.1, 44.4, 45.5, 46.4, 47.3, 48.0, 48.7, 49.2, 49.6, 50.0, 50.0, 50.0,
  50.0, 49.9, 49.6, 49.2, 48.6, 48.1, 47.3, 46.4, 45.6, 44.4, 43.1. Ignore the bbox_x1 jump at frame 6: that is where the
  lower bumper enters the frame.
- Early frames 0–17: only the front of the cart is visible. The dark parts of the cart (interior, left canopy) blend into
  the dark left wall, so bbox_x0 there is meaningless.
- Frame-to-frame noise in background regions is < 1 grey level, so the camera is static.
