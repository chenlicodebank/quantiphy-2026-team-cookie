# internet_0049 — measurement record

Internet video, 2D, 3840x2160, 30 fps, 283 frames (t = frame/30). All values are in full-resolution pixels and
seconds. No metric scale is assumed: per the benchmark convention, convert with ONE scale = prior world value /
prior pixel value, measured the same way as the prior (e.g. scooter length bumper-to-bumper → `length_px` = 264 px).

## Scene
There is a wooden pergola (dark beams, vine lattice) with picnic tables in front of a green basketball court and a peach building.
**One moving object:** a person riding a black electric kick-scooter, from left to right, frames 132–266.
The rider wears a grey cap, a light-grey/white long-sleeve top and khaki trousers. The rider stays between the front
row of posts/tables (which occlude them) and the rear rows. Nothing else moves except leaves and dappled shadows.

## Files
- `scene.json`: inventory (moving and static objects with pixel extents at frame 0), events, camera summary, and the
  rider's manually measured sizes at clear frames 147/190/233.
- `tracks/rider_scooter.csv`: one row per frame 132–264.
  - `x_px, y_px`: reference point in raw image coordinates. This is the centroid of the rider's moving pixels in the torso band
    (shoulders→hips), i.e. the visible body centre. It is about 167 px below the cap top and about 280 px above the ground.
  - `x_bg_px, y_bg_px`: the same point mapped into frame-0 coordinates, which removes the camera drift (background-relative).
  - `bbox_*`: full rider+scooter box from fixed offsets measured on clear frames: x−138 … x+126 (scooter
    rear-wheel back edge to front-wheel front edge), cap top … cap top+450. `length_px` = 264 is the extent along the motion
    direction, and `height_px` = 450 is the cap top to wheel bottom.
  - `mask_*`: raw extents of the optical-flow motion mask. This often misses the dark scooter and the occluded legs, so use
    it only as a lower bound.
  - `torso_mask_px`: support of the torso centroid. `flow_u_px_per_frame`: median DIS flow of the mask (rough).
  - `occluded` / `flags`: `torso_not_visible`, `torso_partly_occluded`, `left/right_edge_truncated`, and
    `centroid_biased_±N` (deviation from a ±4-frame local line). Use unflagged rows for motion fits.
- `camera_motion.csv`: per-frame similarity transform from frame 0 to frame i. It comes from LK-tracked corners on the static
  scene with RANSAC; the median residual is about 1.4 px. `dx_px, dy_px` give the image-centre displacement.
- `scripts/`: all code. `camera_motion.py` → `flow_track.py` (DIS flow masks) → `build_tracks.py` → `write_tracks.py`.
  Checks: `overlay_check.py`, `check_track.py`. Viewers: `zoom_grid.py`, `enh_crop.py`, `view_strip.py`. Early attempts were
  `motion_scan.py`, `detect_rider.py`, `track_rider.py` (background subtraction, too noisy) and `template_track.py` (failed). They are kept
  for the record only. I deleted the packed flow masks (`scripts/fmasks/`) to keep the record small. Re-run `flow_track.py` to
  regenerate them before running `build_tracks.py` or `overlay_check.py`. The per-frame statistics are kept in `flow_raw.npy` / `rows.npy`.

## Rider sizes (manual, contrast-enhanced zooms, ±5 px)
| item | f147 (left) | f190 (centre, clearest) | f233 (right) |
|---|---|---|---|
| cap top → wheel bottom | 450 | 450 (1060→1510) | 440 |
| rider cap top → shoe sole | – | 420 | – |
| scooter length (wheel edge to edge) | ~263 | 263 (1297→1560) | ~265 |
| wheelbase (centre to centre) | ~208 | 207 | ~208 |
| wheel diameter | ~55 | 53–60 | ~55 |
| scooter height (ground → handlebar) | – | 280 | – |
The apparent size is constant across the frame, so the motion is effectively parallel to the image plane.

## Motion (for orientation only; fit your own)
The rider moves monotonically to the right with no stop or turn. Linear fits of the torso x step: 25.8 px/frame (frames 143–160),
27.9 (160–176), 31.7 (183–200), 32.4 (200–217) and 33.3 (230–255), so the rider speeds up over roughly frames 150–200. The
background-relative values are about 0.3 px/frame higher because the camera drifts left. Vertical motion is small (the y drift is
mostly camera tilt). The frame-to-frame jitter of the centroid is about 2.5–3 px rms, so smooth over several frames before differencing.

## Events
Scooter front enters at the left edge at frame 132 (t = 4.40 s). The torso is fully in frame from 143. The rider is behind the front-left post
in frames 177–182 (torso hidden 179–180) and behind the front-right post in frames 224–229 (torso hidden 225–227). The torso
reaches the right edge at about frame 260. The last sliver is visible at 265–266, and the rider is gone from frame 267 (t = 8.90 s).

## Camera
The camera is not static: it drifts slowly and smoothly, with no pan or shake. By the end, dx = −60 px, dy = +105 px, roll ≈ 0.65° and scale ≈ 0.985
(partly parallax, because the pergola is near and the building far). During the rider pass the horizontal background shift is
only about 0.2 px/frame, about 0.7 % of the rider's motion. Use `x_bg_px` to measure against the background.

## Reliability / ambiguities
- Torso x is good to about 3 px on unflagged frames. Flagged frames (posts, frame edges, bushes at the far right) are biased by up to
  30 px.
- The scooter is in deep pergola shade and is often behind benches, so its extents come from three clear frames plus fixed offsets,
  not from per-frame segmentation.
- The rider's legs are hidden by the front tables in many frames (about 150–165, 195–225 and 238–266).
- Dappled lattice shadows and moving leaves cause false motion in background subtraction, which is why optical flow was used.
- Static extents in `scene.json` were read by eye from gridded frame-0 images (±5–10 px).
