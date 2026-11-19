# internet_0052 — measurement record

Video: 1920x1080, 30 fps, 56 frames (t = frame/30, 0 … 1.833 s). Internet footage, 2D (side view).
Content: one person standing on an electric kick scooter rides **right → left** along the road in front of a
curb/planting strip with palm trees, a "NO PARKING FIRE LANE" sign pole, a parked bicycle (right) and a parking
lot behind. The rider+scooter is the only moving object; it is visible in all frames 0–55 and never occluded.

## Files
- `scene.json` – inventory (moving + static objects with pixel extents), sizes, events, camera, perspective.
- `tracks/rider_scooter.csv` – one row per frame (0–55). Columns:
  - `bbox_cx, bbox_cy` visible centre of the rider+scooter box; `bbox_x0,y0,x1,y1` box (cap top to wheel bottom,
    front wheel to max(person right edge, scooter rear)).
  - `scooter_front_x` leading edge of the front wheel (most reliable point, ±1–2 px every frame);
    `scooter_rear_x` rear fender/wheel edge; `scooter_cx` scooter midpoint; `scooter_length_px`;
    `rear_reliable` = 1 where the rear edge was measured cleanly (|length−203| ≤ 6). Where 0, the CSV
    `scooter_rear_x` is set to front+202 (i.e. assumed length), and `scooter_length_px` holds the raw
    (shadow-contaminated) value — do not use it as a size in those frames.
  - `wheel_bottom_y` lowest scooter pixel (~1022–1032); `person_x0, person_x1, person_cx` person extent incl.
    steering stem and bag; `person_top_y` cap top; `person_height_px` = wheel bottom − cap top (+1).
  - `*_orig` columns: same points in raw frame pixels (un-stabilised). Columns without suffix are in
    frame-0 (background) coordinates — use those for motion.
  - `occluded` = 0 throughout.
- `camera_transform.json` – per-frame similarity transform A (frame-0 → frame-i) from ~2000 LK-tracked
  background features (RANSAC), and the background shift at curb level.
- `scripts/` – camera_bg.py (phase-correlation check), camera_affine.py (camera transform), segment.py
  (median background on stabilised frames, diff masks → masks.npz), track.py (track extraction + overlay
  frames/track.png), viz_masks.py, probe.py (pixel colour probes), check.py (overlap/event checks).

## Key measurements (pixels)
- Scooter length (front wheel front edge → rear fender end): **203 px** (median of frames 0–30, range 199–207).
  Visual checks at frames 20 (893→1095 ≈ 202), 50 (343→547 ≈ 204) and 54 (≈261→465 rear wheel/fender) agree.
- Rider+scooter height (wheel bottom to cap top): median **333 px** (326–345). Rider alone (shoe sole on deck
  ≈ y1003 to cap top ≈ y698): ≈ **305 px** (visual, ±5). Scooter handlebar height above ground ≈ 200 px; wheel
  diameter ≈ 45 px (visual).
- Motion: front edge moves ≈ −18.7 px/frame in x, very uniform (per-frame steps −16…−21, mostly −18/−19);
  total front-edge displacement 1262 → 235 = 1027 px over frames 0–55 (stabilised). Vertical position constant
  (wheel bottom 1022–1032; slight dip mid-clip follows the road/curb geometry). No start/stop, no direction change.
- Static objects: see scene.json (sign plate 48×70 px at x948–996,y535–605; pole width ~13 px; bicycle box
  x1620–1745, y780–955; curb top y≈965, road edge y≈1005).

## Camera
Not perfectly static: smooth drift, background moves +9 px x / −2 px y (curb level) over the clip, rotation
0.18°, no zoom. ~1% of the rider's motion; stabilised columns remove it. For annotator-style raw-pixel
measurements use `*_orig` columns (difference in velocity ~0.17 px/frame).

## Perspective / scale
Rider moves parallel to the image plane at constant depth (scooter length constant within ±2 px), so one
planar scale (prior world value / prior pixel value) applies. The parked bicycle is end-on (foreshortened) and
sits behind the curb (different depth) — do not use it as a scale for the rider's plane.

## Reliability / ambiguities
- Cast shadow of the scooter trails to the right of the rear wheel (on curb in shade, on the road in sun).
  Rear-edge extraction removes it only while the scooter is in shade (rear_reliable=1 in frames 0–31 except 1,
  13–15, 17, 20). Front edge and person edges are unaffected by shadow.
- From ~frame 33 the scooter is in sunlight (grey instead of black); masks are still fine for the front.
- Frame 54: background blob merged above the head; `person_top_y` (670) is ~13 px too high; true cap top ≈ 683
  (visual). Frames 46–55 the rider is in front of the left palm trunk; mask edges slightly noisier (±3 px).
- `person_x0/x1` include the steering stem (left) and bag/arm (right), so person width varies (100–140 px) with pose.
- "Scooter length" for a question likely means front wheel to rear of deck/fender along the motion direction
  (bumper-to-bumper convention): 203 px. If a question gives rider height, use ≈305 px (rider alone) or 333 px
  (rider on scooter, to ground) as appropriate.
