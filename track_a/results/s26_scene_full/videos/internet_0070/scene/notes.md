# internet_0070 – measurement record (pixels, seconds)

Video: 1920x1080, 29.970032 fps, 185 frames (t = frame/fps). Internet footage, 2D scene. A motorboat crosses a
river from left to right in side view while the camera pans slowly to follow it. No metric scale is assumed anywhere.

## Files
- `scene.json` – inventory (objects, what tells them apart, visible frames), static object positions, events, camera
  summary, boat length/height summary.
- `tracks/boat.csv` – one row per frame (0-184). Columns:
  - `visible`, `cut_by_edge` (1 = part of the boat is outside the image: f5-20 entering, f140-154 leaving), `occluded` (always 0).
  - `ref_x, ref_y` – reference point = visible centre = centre of the bbox (bow tip .. stern end, canopy top .. hull bottom).
  - `bbox_x0 (=stern end), bbox_x1 (=bow tip), bbox_y0 (=canopy top), bbox_y1 (=hull bottom)`, clipped to the image.
  - `length_px` = bow tip − stern end (only when fully in frame, f21-139), `visible_length_px`, `height_px` (canopy top to hull bottom).
  - `bow_x, bow_y` – bow tip. `stern_end_x` – rearmost point of the boat. `stern_flag_x` – left edge of the stern flag.
  - `canopy_x0, canopy_x1, canopy_cx, canopy_top_y, canopy_bot_y` – white bimini canopy bbox (threshold blob, ±1 px);
    `canopy_tm_x` – sub-pixel template position of the canopy (equals canopy centre 733 at f61); the smoothest track.
  - `bg_dx, bg_dy` – camera background shift; `*_bg` columns = same points in frame-0 background coordinates (x − bg_dx).
- `tracks/bank_figure.csv` – small figure on the far-bank path, f0-58 (`detected`=0 rows are interpolated).
- `camera_shift.csv` – per-frame background shift vs frame 0 (median of 10 template-matched bank patches), plus
  similarity-fit scale/rotation and the patch spread.
- `scripts/` – all measurement code. Order: `camera_check.py` → `track_boat.py` (coarse) → `landmarks.py` →
  `edges.py`, `canopy.py` → `build_tracks.py`; `bank_person.py` → `build_bank_figure.py`. Viewers: `zooms.py`,
  `zoom_ticks.py`, `montage_ticks.py`, `check_overlay.py`, `check_final.py`, `bank_strip.py`, `show_csv.py`.
  `camera.py` (accumulated estimate) and `seg_boat.py` (background-difference mask) are superseded early attempts;
  `seg_boat.py`'s mask leaked along the shoreline, so it is not used.
  `*_raw.csv` in scripts/ are intermediate results.

## How it was measured
- **Camera**: the bank (y<420) was template-matched against frame 0 in every frame (10 patches, median).
  The camera pans right: the background moves left by up to 58.7 px (f~135), then back to −52.5 px at f184;
  vertical drift up to +11 px. Scale change <0.16 %, rotation <0.22° – ignore both. Patch spread is mostly
  <4 px in x (some patches fail where the boat/water passes; the median is robust). **For speeds, use the `*_bg`
  columns or subtract bg_dx yourself.** The pan is ~4 % of the boat's image motion, so it matters.
- **Boat landmarks**: small templates (bow tip, stern+flag, canopy, whole hull) cut from frame 61 and matched in each
  frame, giving smooth sub-pixel frame-to-frame tracks. Because the boat's look changes slowly (yaw change), the
  fixed templates drift slowly: by f139 the bow template is ~11 px ahead of the real tip. So the true bow tip and
  stern end were read by eye on 6x tick-marked zooms at 15-16 key frames (listed in `build_tracks.py`, ±1 px for
  the bow, ±2 px for the stern) and the template tracks were corrected by piecewise-linear interpolation of the
  differences. Frames 5-8: bow from background differencing (`edges.py`), ±2 px.
- **Stern end**: up to ~f95 the rearmost point is the left edge of the waving stern flag (spray hides the lower
  transom); from ~f100 a white rear-deck/swim-platform edge is visible behind the flag, up to 15 px further back
  (f139-150). `stern_end_x` follows that rule; `stern_flag_x` is the flag edge throughout. Per-frame stern noise ±2-3 px
  (flag flutter).
- **Vertical extents**: canopy top from the canopy blob (±1 px); hull bottom = bow-tip row + 22 px (checked on zooms at
  f30: 505, f130: ~509; ±3 px – the hull bottom blends into spray and reflection).
- Overlays (`frames/final_check.png` from `check_final.py`) confirm the bbox, bow and stern lines sit on the boat at
  f12-148.

## Key numbers (px)
- Boat length (bow tip to stern end, horizontal) is NOT constant: 227.7 (f21), 218.7 (f30), 213.9 (f45), 202.0 (f61),
  194.5 (f75), 190.7 (f90), 186.7 (f105), 179.3 (f120), 179.0 (f138); mean 199.6 over f21-139. The canopy width stays
  67-68 px and the height ~58-62 px, so the boat's distance from the camera is ~constant; the shrinking length is the
  boat turning slightly away from the camera (more rear deck visible later). If a question gives the boat's length as
  the prior, the annotators would probably have measured it at one clear frame – consider which frame/time the
  question refers to; f61 (202 px, mid-clip, sharp) is a typical choice; flag-edge-to-bow length ≈ the same before f95.
- Boat height (canopy top to hull bottom): 57-64 px, mean 59.6. Canopy width 67-68 px, canopy thickness 8-10 px.
- Image motion (orientation only, no model): background-compensated canopy moves ~15.8 px/frame in f21-50,
  ~14.9 in f50-79, ~14.1 in f79-108, ~13.5 in f108-138 – the boat slows in the image (possibly partly the heading change).
  Raw image (uncompensated) speeds are ~0.1-0.8 px/frame lower while the camera pans (f21-138 mean 14.07 raw vs 14.53 compensated).
- Events: bow enters f5 (t 0.167 s); fully in frame f20-139; bow reaches right edge ~f141 (4.705 s); stern gone ~f155
  (5.172 s). Moves continuously, no stops/turns/bounces.

## Ambiguities and reliability
- Which "length" the annotators used: bow tip to stern end (bumper to bumper) is recorded; the flag and swim platform
  make the stern end uncertain by up to ~10-15 px late in the clip, and the length itself changes by 20 % over the clip.
- Reference point: visible centre (bbox centre). Its x is affected by the stern definition; `canopy_tm_x` or `bow_x`
  are cleaner for displacement/speed (all move together within ~1 px/frame).
- Motion blur is small; spray and wake (white) hide the lower stern; the wake persists after the boat leaves.
- `bank_figure` is tiny and low-contrast (±3 px), probably a person on the far-bank path; it moves right ~2.2 px/frame
  (background coords) in f0-58 and is lost afterwards.
- Static objects: far shoreline y≈467 (f0), bank path line y≈455, lone tree at the waterline (crown x 1037-1120,
  trunk x≈1073, top y≈293, base y≈467, 174 px tall) at frame 0; add (bg_dx, bg_dy) for other frames.
