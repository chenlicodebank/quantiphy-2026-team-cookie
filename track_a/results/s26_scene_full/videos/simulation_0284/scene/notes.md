# simulation_0284 — measurement record (pixels, seconds)

2D simulation render, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s), 2560×1440. Letterboxed: the picture
covers rows y = 80…1359. Top-down camera, **static** (no pan or shake). One moving object: an **aircraft**
(nose pointing left) that flies in a straight horizontal line from right to left. Its soft shadow moves on the
white floor below it.

## Files
- `scene.json`: the inventory (aircraft, its shadow, floor, the static dark backdrop edge at the right), the
  aircraft's pixel sizes, events and camera notes.
- `tracks/aircraft.csv`: one row per frame (0–71).
  - `ref_x, ref_y`: the reference point, which is the centre of the full 2D bounding box (pod tips to tail tip,
    wingtip to wingtip). It is extrapolated when part of the aircraft is off-screen. Use it as the origin.
  - `centroid_x, centroid_y`: the silhouette area centroid, a fixed offset (−38.4, −0.4) px from `ref`.
  - `bbox_*`: the visible bounding box, clipped to the image. `full_x0/full_x1`: the unclipped x extent.
  - `length_px` = 566 (x, along the motion) and `width_px` = 725 (y, wingspan). These are constant.
  - `visible_length_px`.
  - `raw_mask_*`: the raw per-frame silhouette box. Diagnostic only, because the shadow and lighting
    contaminate it.
  - `truncated_by_frame`, `occluded` (always 0), `pos_source` (`template` or `tail_edge`), `match` (the
    normalised cross-correlation (NCC) score).
- `scripts/`:
  - `bg.py`: median background and camera check.
  - `track.py`: per-frame gradient silhouette, plus normalised cross-correlation template matching of
    gradient images against frame 24.
  - `stack.py`: a shadow-free median of the aligned aircraft crops, used for the clean extents.
  - `profile.py`: intensity profiles that locate the tail tip and pod tips.
  - `build_record.py`: writes the track CSV.
  - `overlay.py`, `verify.py`: visual checks.
  - `diag.py`, `area.py`: diagnostics.
  - `bg_half.png`: the median background at half resolution.

## How measured / reliability
- **Position.** Sub-pixel template matching of the gradient magnitude against frame 24. This method is
  insensitive to the strong lighting change: the aircraft looks black near the picture edges and light grey in
  the middle.
  - Frames 0–60 (NCC ≥ 0.5): frame-to-frame dx = −34.1 … −34.6 px, with one outlier of −35.2 at frame 40→41.
    Expect about ±0.3 px of noise per frame. dy ≈ 0 (y = 729.0 ± 0.03).
  - Frames 61–71: the aircraft is partly off the left edge, so position comes from the per-frame tail-tip edge.
    That edge is corrected by +9.2 px, a mean offset calibrated on frames 50–62. Per-frame noise is about ±1 px.
- **Size.** Measured on a median of shift-aligned crops (frames 5–55). Because the shadow moves relative to the
  aircraft, the median removes it.
  - Length 566 px: from the forward tips of the under-wing pods (x = 1133 at frame 24) to the fuselage tail tip
    (x = 1698).
  - Wingspan 725 px: y = 367–1091.
  - Accuracy is about ±3 px. The apparent size does not change (2D, constant depth).
  - Plain per-frame silhouettes read the length as 562–583 px, because the shadow merges at the tail and the
    thin tail tip is lost in the dark frames. Use 566.
  - Height cannot be observed (top-down view).
- **Motion.**
  - Frames 0 and 1 are identical (mean |Δ| 0.03 grey levels). The aircraft is stationary there, and motion begins
    between frames 1 and 2.
  - After that it moves left at an essentially constant ~34.25 px/frame. No acceleration is visible.
  - The ref point leaves the image (x < 0) at frame 66. Only about 90 px of the tail remains at frame 71.
- **Events.** None besides the motion start and leaving the frame: no bounces, contacts or turns.

## Ambiguities
- The **shadow** is a blurred dark copy of the aircraft, and its offset from the aircraft changes over the clip.
  Do not confuse it with the aircraft. It is excluded from every measurement.
- The aircraft's **origin** is unknown. The box centre is used, and the centroid is about 38 px further forward.
  Displacements and speeds are identical for either, since the aircraft is rigid and only translates.
- The dark curved region at the far right (x ≳ 2390–2516) is the static edge of the backdrop, not an object.
  At frames 0–1 the aircraft's tail (x = 2486) is close to it, and dark.
