# captured_0010 – measurement notes

Lab recording (Orbbec, 24 fps, 49 frames, 1280x720, 3D). A woman in blue overalls stands still with her right
arm out and holds a string; an orange ball hangs on it and swings as a pendulum, mostly **towards/away from the
camera**. The background (seated person, desk, monitor) is blurred for privacy. The camera is static.
Lab convention: f = 0.5959 x 1280 = 762.75 px, principal point (640, 360).

## Files
- `scene.json` – inventory, pivot, person extents, static objects, events, camera.
- `tracks/ball.csv` – every frame 0-48: frame, t_s, cx_px, cy_px (mask centroid = visible centre), bbox x0/y0/x1/y1,
  width_px, height_px, equiv_diameter_px (2*sqrt(area/pi)), area_px, occluded (always 0), ray_x = (cx-640)/762.75,
  ray_y = (cy-360)/762.75. Given camera distance d to the centre: P = d * (ray_x, ray_y, 1)/norm(ray_x, ray_y, 1).
- `tracks/string.csv` – string top end (hand pinch = pivot) and bottom end per frame, found by following
  the thin bright line upward from the ball. Rows with `n_string_px` > ~100 (frames 9-26, 38-48) have a reliable top;
  at the far end of the swing the string is foreshortened/faint and the top is either missing or is a
  point partway up the string (not the pivot), so ignore those rows.
- `scripts/` – `track_ball.py` (HSV mask: hue <=12 or >=172, S>150, V>150, largest blob in x 450-800, y 250-520),
  `track_string.py`, `camera_check.py` (phase correlation), `crops.py` (visual check montage).

## Key numbers (pixels)
- Ball apparent diameter: ~26.2-27.5 px at the far end (f0-5, f29-34), ~36-37 px at the near end (f13-22, f42-48).
  Ratio ~1.39, so the far end is ~1.39x the near-end camera distance. Equivalent diameter is accurate to about
  ±1 px. The strict mask stops slightly inside the soft orange rim, so the true edge is probably 1-2 px larger
  (bbox width 36-41 px when near). A looser colour threshold was tried and rejected because it merges with the
  reddish floor marks behind the ball.
- Ball image path: x 637-680, y 302-394. In image space it moves mostly vertically.
- Pivot (hand pinch): about (636.5, 228) ± 3 px. Drifts from x~639 (f10-26) to x~634 (f38-48).
- Image length from pivot to ball centre: 148-172 px over the near half of the swing; much shorter at the far end
  (foreshortening).
- Person: head top y≈18, feet y≈617 → ~599 px tall at frame 24, body x 755-910, x 615-933 including the arm.
  The image is blurred, so allow ±5 px. She does not move.

## Events
Turning points:
- Far (smallest, highest in image): f3 (t=0.125 s) and f32-33 (t≈1.33-1.375 s).
- Near (largest): f17 (t=0.708 s) and f46-47 (t≈1.92-1.96 s).
Period ≈ 29.5 frames ≈ 1.23 s. The ball swings throughout (no release or impact in the clip). At f0 it is
moving away from the camera.

## Reliability / ambiguities
- Ball centroid: ±0.5 px. Mild motion blur in mid-swing frames (f7-11, f24-28, f36-39) elongates the mask by
  2-4 px along the motion, but the centroid is still fine. The ball is never occluded.
- Because the swing is mostly along the depth axis, image displacement badly underestimates 3D motion. For 3D
  speeds or distances, use the given depth_info. If only some depths are given, apparent size (∝ 1/depth)
  interpolates depth between frames: depth_i ≈ d_ref x D_ref / D_i, with D from equiv_diameter_px (noise about ±3%).
- Only one ball and one standing person matter. The seated background person and the furniture are blurred and
  were not tracked.
