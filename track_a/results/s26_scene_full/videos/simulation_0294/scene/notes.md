# simulation_0294 – measurement record

2D simulation (Blender) at 24 fps, 72 frames (t = frame/24, 0–2.958 s), 2560×1440. One blue butterfly (black body, legs and antennae) is seen from the side with its head to the left. It flies from right to left across a seamless grey studio: a gradient backdrop above a light floor. The floor/backdrop brightness step is at y≈937. A soft shadow on the floor follows it (y≈1185–1278). Nothing else moves, and there are no other props.

## Files
- `scene.json`: inventory, camera, events, summary pixel numbers.
- `tracks/butterfly.csv`: one row per frame, 0–71.
  - `body_x`, `body_y_meas`: the **reference point** (body centre, used in place of the origin).
  - `x0 y0 x1 y1`, `bbox_w/h`, `bbox_cx/cy`: full mask box, including wings, legs and antennae.
  - `mask_cx/cy`, `area`: mask centroid and pixel area.
  - `wing_cx/cy`: centroid of the blue wing pixels.
  - `main_axis_len`, `across_w`, `main_axis_deg`: PCA extents of the mask.
  - Flags: `cut_by_frame_edge`, `wings_flat`, `body_x_interpolated`.
- `tracks/butterfly_shadow.csv`: centroid, box and area of the floor shadow.
- `scripts/`: `track.py` (mask, box, shadow), `body_track.py` (body point), `finalize.py` (horizon, overlays, scene.json), plus probe scripts.

## How it was measured
- **Butterfly mask:** pixels with saturation > 35 or |grey − background median| > 22, above y = 1050. I kept the largest blob after a 9 px morphological close. Overlays at frames 8, 40 and in `frames/verify.png` show that the mask and box cover the whole butterfly.
- **Reference point, x (`body_x`):** x-centroid of the dark, low-saturation leg pixels in rows 700–719.
  - At frames 0 and 12, zoomed views show it falls within ~3 px of the head-to-abdomen midpoint.
  - In the wings-flat frames (19–21, 40–42, 61–63) the flat wing edges get into that band, so `body_x` there is linearly interpolated (flag = 1). Those frames are in the middle of a very regular track, so the error is small.
- **Reference point, y:** the body sits at y≈665 (mean 665.4, sd 4, noisy because of wing shading). The leg tips end at y = 717–719 in every frame, so there is **no vertical motion**: the flight is horizontal.

## Key numbers (pixels, frames)
- **Motion:**
  - `body_x` goes from 2310.8 (frames 0 and 1) to 147.5 (frame 71).
  - The per-frame step is −30.9 px on average and steady (−29.4 to −32.4).
  - No visible speed-up or slow-down.
- **Frames 0 and 1 are identical**, so motion is first visible between frames 1 and 2. This affects speed at t = 0 to 0.04 s.
- **Wingbeat:** the period is ~21 frames.
  - Wings flat: frames 0–1, 19–21, 40–42, 61–63.
  - Wings fully raised (box height ~330–336 px): frames 8–10, 29–30, 50–51.
- **Size (unclipped frames 0–63):**
  - Box width ranges from 388 (wings up, frame 30) to 525 (wings flat, frame 63).
  - Box height ranges from 85 (wings flat) to 336 (wings up, frame 51).
  - Body length from head to abdomen tip is ~145–155 px.
- **Leaving the frame:** from frame 64 on, the butterfly is cut by the left image edge (`cut_by_frame_edge` = 1), so box and extents there are partial. `body_x` is still valid because the legs stay in view.

## Camera
Static: no pan or shake, background shift 0. The per-pixel background median is clean and the horizon line stays fixed.

## Ambiguities and reliability
- **Width is not wingspan.** We see the butterfly side-on, so `bbox_w` is its front-to-back extent (forewing tip to hindwing/antennae). The true wingspan lies along the viewing direction and cannot be measured.
  - Width changes during the beat (flat wings ≈ 420–525 px), partly because the wings sweep forward and back.
  - For "max/min width or height during flight", use the `bbox_w`/`bbox_h` columns and exclude frames where `cut_by_frame_edge` = 1.
- **Shadow:** soft and very faint when the wings are raised (area falls to ~5k px), so its centroid is approximate. Use it only as a rough cue, not as the object.
- **Accuracy:** box and mask are good to about ±2 px. The body point is good to about ±3 px in x and ±5 px in y.
- **Scale:** no metric scale is assumed. A single metres-per-pixel scale from the question's prior applies, since the scene is 2D with motion in one plane.
