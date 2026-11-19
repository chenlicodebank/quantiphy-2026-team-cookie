# simulation_0052 – measurement record

3D Blender render, 1080x1080, 91 frames at 30.003297 fps (t = frame/fps). Static camera looking straight at a
white brick building wall across a wet street. Two cars drive right-to-left, parallel to the image plane:
an **orange sports sedan** in the far lane (next to the curb) that decelerates smoothly to a stop, and a
**dark green/black vintage coupe** in the near lane that passes at constant speed in front of it.
All values are pixels / frames; no metric scale has been assumed.

## Files
- `scene.json` – inventory (moving + static objects with pixel extents), camera notes, events.
- `tracks/orange_car.csv` – every frame 0-90. Columns: frame, t, ref_x (reference x = midpoint of the
  near-side front and rear wheel hubs), ref_y_hub (745), ground_y (794, tyre contact row), ref_source,
  front_hub_x / rear_hub_x (when measured), bbox_x0/x1/y0/y1 (mask extents of the visible car, blank where
  merged with the black car), length_px, height_px, clipped_left/right (touches image edge), occluded.
- `tracks/black_car.csv` – frames 24-53 (its visible frames). Same reference definition (hub row ~852,
  ground_y 900); side_front_x_est / side_rear_x_est = side-profile ends computed from the hubs with the
  overhangs measured at f39; bbox = those ends clipped to the image, rows 637-900.
- `tracks/raw_masks.csv` – intermediate per-frame mask extents from `track.py`. The `or_*` columns are the
  orange car mask (good when not occluded); the `bk_*` columns are contaminated (they include orange-car
  wheels/windows and road reflections) – do not use them.
- `scripts/` – common.py (decoding, background), track.py (masks), orange_wheels.py / black_wheels.py
  (hub exploration), build_tracks.py (hub tracking → frames/hubs.npy), write_tracks.py (CSV + overlay),
  black_edges.py, black_profile.py, explore.py, strip.py (viewing), statics.py, summary.py.

## How measured
- Background: composite of frame 0 (left half, empty) and frame 90 (right half, empty) – exact since the
  camera is static.
- **Orange car hubs**: normalized template matching of the rear wheel at f60 (blurred gray), hub row 745,
  sub-pixel peak. Pair separation constant at 323.2 px (322.6-323.8) → good depth-constancy check.
  ref_x: both hubs f19-26 and f54-58; front hub + 161.6 for f6-34; rear hub − 161.6 for f46-90.
  f0-5 (wheel off right edge): quadratic extrapolation of f6-16 (ref_x > 1079, off-screen, until ~f3-4).
  f35-45 (both wheels behind the black car): cubic fit through f27-34 and f46-53 (fit residual ≤0.4 px) –
  interpolated, accuracy ~±1-2 px. Hub tracking precision otherwise ~±0.3 px.
- **Black car hubs**: bright low-saturation chrome hubcap blobs (y 820-884) in the background difference,
  intensity-weighted column centroid (blur-symmetric). Front hub f28-42, rear f35-49; wheelbase 489.6 px
  (488.7-490.9). Motion is uniform: linear fit −69.84 px/frame, max residual 2 px. f24-27 and f50-53 are
  linear extrapolations (ref_x outside the image).
- Overlays (frames/tracks_overlay.png, not kept in the record) confirmed the hub circles and reference marks
  sit on the correct wheels and between the axles.

## Sizes (side profile, pixels)
- Orange car: length 518 (517-519 at f21-23 and f54-56, both ends in view; includes ~10 px motion blur at
  ~20 px/frame), height 151 (roof 643 → tyre contact 794), wheelbase 323.2, wheel Ø ~95.
  The body end positions in bbox columns include perspective faces: on the right side of the image the
  front face shows (f0-~18), on the left side the rear face shows (rear end at 370 when stopped, rear
  hub 237.7 → 132 px instead of ~102 px side-profile overhang). Use the hubs for positions.
- Black car: length ~834 ±20 (front overhang ~137, wheelbase 489.6, rear overhang ~207; edges read at
  mid-blur at f39, blur ~40-45 px), height 263 (roof 637 → tyre contact 900), wheel Ø ~100.
  Apparent extents differ by up to ~80-120 px near the image edges because of the front/rear faces (f28
  front appears at ~790 vs side-profile estimate 874; f52-53 rear sliver reaches x≈145/80).
- The black car is nearer the camera: ground rows 900 vs 794; its pixel scale is larger than the orange
  car's. If the camera is level (horizon ≈ y 540, not observable), the depth ratio orange/black ≈
  (900−540)/(794−540) ≈ 1.42 – only a cue; use depth_info when given.

## Motion summary (for orientation only, no models)
- Orange car: per-frame ref displacement −28.9 px at f1, shrinking almost linearly (~0.33-0.34 px/frame²)
  to 0; at rest from f87 (ref_x 76.1). ref_x f0 1343.7 (extrapolated) → f90 76.1.
- Black car: −69.84 px/frame throughout (f24-53).

## Static objects
Two identical black street lamps (pole x 201 and 897, top 366, base 757, height 391 px, lantern ~55 px
wide), white fire hydrant (x 105-165, y 663-757, 94 px tall), "MEOW" graffiti (x 522-762, y 568-712),
6 windows (~85x145 px), far sidewalk y 728-763, curb face 763-790, white dashed lane line y 844, near
curb y 951-966, wooden board at right edge (x 1065-1080, y 495-722). Pixel values ±3 px (read on zoomed
frames). All static objects lie in/near the wall plane, i.e. at the orange car's depth or slightly
behind it, not at the black car's depth.

## Events
orange car moving from f0 (enters at right) · black car enters f24 · black car occludes orange car f24-46 ·
image-x crossing of the two references ~f39.4 (different depths) · black car leaves after f53 (gone f54) ·
orange car stops f87 (t 2.90 s).

## Ambiguities / reliability
- Vehicle "root" assumed at the wheelbase centre (between the axle hubs); if the rig root is the bbox centre
  instead, add ≈ (rear_overhang − front_overhang)/2: orange ≈ +4 px, black ≈ +35 px (toward the rear, i.e. +x).
- Black car strongly motion blurred; its body extents are ±20 px; hub positions are reliable (±2 px).
- Wet road shows reflections of both cars below the tyres (excluded from masks, y > 794 for the orange car).
- Orange-car positions f35-45 are interpolated (occluded); f0-5 extrapolated.
