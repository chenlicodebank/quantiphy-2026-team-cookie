# simulation_0134 — measurement record (pixels, seconds; y points DOWN)

Video: 1080x1920 portrait, 24 fps, 60 frames (t = frame/24). Source: simulation, 2D scene.
Content: a red retro toaster on a kitchen counter in front of an olive backsplash, with wood upper cabinets
and dark green lower cabinets. A single slice of toast pops up out of the slot, flies straight up, falls back
into the slot, bounces slightly and comes to rest a little higher than where it started. Static camera.

## Files
- `scene.json` — inventory (toast, toaster, countertop, backsplash, cabinets), static pixel sizes, events, camera.
- `tracks/toast.csv` — one row per frame 0-59: `cx, cy` (centre of the full toast box = origin proxy),
  `top_y` (topmost toast pixel), `top_flat_mid_y` (median top over the middle columns x 440-570),
  `bottom_y_full_est` (= top_y + 231), visible bbox (`bbox_x0..y1`, cut at the slot lip y = 1114),
  visible / full height and width, `occluded` (1 = lower part hidden inside the toaster).
- `scripts/` — `diff.py` (motion detection vs frame 0), `edges_all.py` (per-frame top/left/right edges →
  toast_edges.json), `bottom.py` (full height/width in frames 41-44), `track_toast.py` (independent template
  match → toast_match.json), `static.py` (toaster/counter extents), `lever.py` (levers don't move),
  `write_tracks.py` (builds the csv), `overlay.py` / `montage.py` (visual checks).

## How it was measured
- Toast mask = colour difference > 30 (RGB sum) from a per-row background colour (taken at x 800-1000, where
  the backsplash is plain), restricted to x 300-720 and y < 1114 (slot lip). The top edge comes from that mask.
- Full toast size from frames 42/43, when the toast is completely out of the slot: x 406-601 (width 196 px),
  top 839 to bottom crust 1070 at frame 43 (height 232 px). The bottom crust is bright; the shadow under it is dark.
- The toast is rigid and moves only vertically: template matching from frame 43 gives dx = 0 and rotation ≈ 0
  in every frame where it locked on. It agrees with the edge top to within 1 px in frames 41-59 and in the rest
  frames (it failed only in frame 40, where the edge result was kept). So cy = top_y + 115.5 and cx = 503.5 in
  every frame, including frames where most of the toast is hidden in the slot.
- Overlays (`frames/overlay.png`, not part of the record) confirm the boxes cover the toast in frames 0 and 40-59.

## Key numbers
- Rest before the pop (frames 0-39): top 1055, cy 1170.5. Apex at frame 43 (t = 1.792 s): top 839, cy 954.5,
  so the rise is 216 px. Final rest (frames 52-59): top 1038, cy 1153.5, which is 17 px higher than at the start.
- Top_y by frame: 39:1055, 40:919, 41:866, 42:847, 43:839, 44:872, 45:949, 46:1038, 47:1023, 48:1028,
  49:1033, 50:1038, 51:1032, 52+:1038.
- Events: release between frames 39 and 40 (first moving frame 40, t = 1.667 s); apex at frame 43 (from the
  tops at frames 42-44, the true apex is between frames 42 and 43, near 43); back in the slot at frame 46
  (t = 1.917 s); small rebound at frame 47; settled by frame 50; a one-frame 6 px blip at frame 51; at rest from frame 52.
- Toaster (static, frame 0): red body x 294-723 (430 px wide), body y 1124-1357; slot lip top y ≈ 1114;
  cream base x ≈ 278-740 (462 px), bottom y ≈ 1390; overall height ≈ 276 px; centre ≈ (508, 1252).
  Levers and dials never move.
- Scenery: worktop back edge y ≈ 1355, front edge band y ≈ 1360-1480; upper cabinets end y ≈ 495; light strip
  y ≈ 540-700; lower cabinets below y ≈ 1500.

## Reliability and ambiguities
- top_y: ±1 px. Full height 232 ±3 px and width 196 ±2 px: the crust is irregular, with a bulge at the lower
  left and a notch at the bottom middle. In the image the toast's height is vertical and its width horizontal.
- cy is inferred from the top edge plus a fixed half-height, which is valid for a rigid, non-rotating toast
  (checked). Its absolute value depends on the measured height: ±2 px.
- The toast's shadow on the backsplash is brownish and close to the toast's own colour. It lies below and to the
  right of the toast, so the bottom and right extents were measured on the bright crust edge and above the shadow.
- Frame 40 has slight motion blur: ±2 px.
- 2D scene: use one metres-per-pixel scale from the prior (for example the toast height of 232 px or width of
  196 px, or the toaster's 430 px body width), then apply the speed and acceleration conventions to cy over time.
  The motion is purely vertical.
