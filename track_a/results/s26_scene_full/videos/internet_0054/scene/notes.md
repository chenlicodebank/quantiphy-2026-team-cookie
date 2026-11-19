# internet_0054 – measurement record (pixels, seconds)

Video: 3840x2160, 30 fps, 94 frames (t = frame/30, 0 … 3.1 s). Internet footage, 2D scene.
Content: one person on a black two-wheel electric kick scooter rides **right to left** along a light
paved path, seen side-on, in front of hedges and an ivy pergola with four wooden benches. Green
court with white centre circle + centre line in the foreground; beige building and trees behind.
The rider is the **only moving object** and is visible, unoccluded, in all frames 0–93; already moving
at frame 0, still moving at frame 93 (no start, stop, bounce or direction change).

## Files
- `scene.json` – inventory (moving + static objects, pixel extents/positions), camera, perspective, events.
- `tracks/rider_scooter.csv` – **final per-frame track** (94 rows). Columns:
  - `cx,cy` reference point = centre of the rider+scooter bounding box;
    `bbox_x0` = front tyre front edge (leftmost point), `bbox_x1` = rear tyre rear edge,
    `bbox_y0` = cap top, `bbox_y1` = lowest tyre bottom (ground contact).
  - `length_px` (= `scooter_len_px`, front tyre front → rear tyre rear: the scooter "bumper-to-bumper" length;
    also the rider+scooter length since nothing of the person sticks out beyond the tyres),
    `height_px` (cap top → tyre bottom), `width_px` empty (not observable).
  - `wheelbase_px`, `front_wheel_x/y/r`, `rear_wheel_x/y/r` (tyre circle centre = axle, radius),
    `ground_contact_y`, `torso_x/y` (upper-chest NCC track point), `torso_ncc`, `cap_top_y`.
  - `*_stab`: the same points mapped into frame-0 pixel coordinates (camera drift removed).
  - `occluded` = 0 everywhere.
- `tracks/wheels_circlefit.csv` – raw tyre-circle fits (0.5 px grid).
- `tracks/parts_raw.csv` – raw NCC template tracks (front wheel OK, **rear wheel drifts ~25 px by the end – do not use**, torso OK).
- `camera_affine.csv` – per-frame affine frame0→frame i (`band_*`: hedges/benches at the rider's depth; `top_*`: building).
- `camera_shift.json` – phase-correlation shift of the building region vs frame 0 ([frame, t, dx, dy, response]).
- `scripts/` – all measurement code: `camera_bg.py`, `camera_regions.py`, `camera_affine.py`,
  `track_parts.py`, `wheel_circles.py`, `build_track.py` (makes the final csv), `check_*.py` (overlays),
  `static_objects.py` (+ `static_raw.json`), `summary_motion.py`, `probe_rows.py`;
  `track_rider.py` is a superseded mask approach (kept for reference; writes only scratch output).
  `scripts/bg_band.png` is a scratch median background (blurred by the camera drift; not used for results).

## How it was measured
- **Camera**: LK-tracked background corners, affine RANSAC, chained per frame. The camera is not
  perfectly static: smooth drift, background at the rider's depth shifts +31 px in x and +6…+16 px
  in y (slight roll ≈0.36°) over the clip, i.e. ≈ +0.34 px/frame in x, versus the rider's ≈ −16.6 px/frame.
  Effect on rider displacement ≈ 2 %. Raw image coords and stabilised (`*_stab`) coords are both given;
  the stabilised ones are "measured against the background" as the convention asks for a panning camera.
- **Wheels**: for each frame a circle (centre, r 16–25 px) is fitted to the lower half of each tyre
  (dark tyre ring vs. light path) by maximising outside-minus-inside brightness. Checked on overlays
  (frames 0, 45, 93): circles sit on the tyres. Precision ≈ ±1 px centre, ±1 px radius.
- **Scooter length** = (rear_cx + rear_r) − (front_cx − front_r). The rear fender tip ends about where
  the rear tyre ends (within ~3 px). Grows 181 → 193.5 px over the clip (rider drifts slightly toward
  the camera; contact line y 1122.5 → 1137); mean over the clip ≈ 186 px. Frame-to-frame noise ±2–3 px.
- **Cap top**: topmost row of the rider in a two-reference (frames i±22, camera-warped) min-difference
  mask, columns around the torso, requiring ≥20 consecutive rows (excludes twigs). 815–820 px, ±2 px.
- **Torso point**: frame-to-frame NCC of a cap+shirt template (from frame 0, centre x 2895, y 885).
  Sits at the front of the upper chest. NCC 0.76–0.97; no visible drift on overlays (frames 0, 30, 66, 93).
- **Static objects** (frame 0): benches from wood-colour columns plus manual zoom (bench_1 left half is
  in deep shadow → read manually); court markings from white pixels; path from brightness profiles.
  Pergola, hedge and building extents are rough (±15 px) from the full-frame view.
- **Person height** (cap top → shoe sole on deck): ≈279 px at frame 0, ≈292 px at frame 93 (manual, ±4 px).
  Overall rider+scooter height (cap top → tyre bottom) per frame in `height_px` (304.5 → 318).

## Motion summary (descriptive only)
10-frame displacement of the reference point ≈ −157 … −168 px raw (−159 … −172 px stabilised);
per-frame front-axle displacement (stabilised) −15.3 … −17.9 px, mean −16.6 px/frame. Vertical motion
only the slow drift toward the camera (+14 px in contact y over the clip).

## Ambiguities / cautions
- Apparent size changes ~6 % over the clip (slight approach to the camera). A single scale factor
  (annotator convention) taken at a different frame gives a few % different results; the scooter length
  at the frame(s) the question refers to is in `scooter_len_px`.
- The rider casts a long, very dark shadow trailing to the right at wheel-contact level (rows ≈1115–1135);
  it is excluded from all extents. Segmentation masks were unreliable (dark tyres on dark hedge), hence the
  wheel-fit approach.
- Face is blurred (dark rectangle) in the source; cap top is still clearly visible.
- Motion blur is small (≈16 px/frame motion but sharp frames).
- Court markings are much nearer to the camera than the rider (foreground) – do not use them with the
  rider's scale.
- Benches/hedges are at roughly the rider's depth (just behind the path), so their pixel sizes are
  comparable with the rider's scale.
