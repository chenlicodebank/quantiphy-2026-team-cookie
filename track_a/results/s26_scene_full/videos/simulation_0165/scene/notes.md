# simulation_0165 – measurement record

Video: 1920x1080, 24 fps, 80 frames (3.333 s), Blender render, declared **2D**. t = frame/24.
All values are pixels (x right, y down) and seconds. No metric scale is assumed.

## Scene
Night/dusk street seen along the road (vanishing point ~(1000,590)). **One moving object: a cyclist** (green
jacket, light-blue/white helmet, orange shorts, yellow handlebar basket, pale pink bicycle) riding left -> right
across the road along the far white stop line (wheel hubs at y ~706). Everything else is static: buildings, houses,
fences, lamp posts, traffic-light pole, three strings of red/white bunting, road markings. Camera is static
(phase correlation shift < 0.02 px; background difference shows only the cyclist).

Although the street has strong perspective, the cyclist moves parallel to the image plane at one depth: its pixel
length (163 px) and height (163 px) and its y position stay constant, so a single px scale from the prior applies.

## Files
- `scene.json` – inventory, static object positions, camera, events, cyclist summary (sizes, line fits).
- `tracks/cyclist.csv` – every frame 0-79: `ref_x, ref_y` (midpoint of the two wheel hubs = proxy for the bike
  root/centre), `ref_source` (measured = both hubs found by Hough circles and consistent; line_fit_fill = hubs
  taken from the straight-line fit because a wheel was hidden or detection failed), `pelvis_est_x/y` (rear hub +
  (44,-46), hip on saddle judged on zoomed frame 60, ±5 px), rear/front hub positions, mask bbox (x0,y0,x1;
  y1 = hub y + tyre radius 33, i.e. without shadow), `hub_based_x0/x1` (tyre extents from hubs, robust to
  occlusion/shadow), `length_px`, `height_px`, `mask_y1_incl_shadow`, mask centroid, area, `occluded` + reason.
- `tracks/cyclist_raw.csv` – raw output of the mask/Hough step.
- `scripts/` – `bg.py` (camera + motion check), `track.py` (band background median, |diff|>22 mask, components
  within 140 px of the largest, Hough wheels; writes overlays to frames/ov), `finalize.py` (validation, fills,
  flags), `check.py`.

## Key measurements (reliable)
- Motion: uniform, straight, horizontal for the whole clip. Rear hub x = -92.6 + 21.015·frame, front hub x =
  2.3 + 21.023·frame (44 clean frames, residual std 0.6-0.8 px). Front bbox edge slope 21.07, rear edge 20.96
  px/frame. => ~21.0 px/frame ≈ 504 px/s, zero acceleration, y constant (705-707). Per-frame differences of
  measured points jitter by ±1 px (detection noise), so fit lines rather than single differences.
- Size (unoccluded frames): bike+rider length 163 px (158-168), height helmet top (y 577) to tyre bottom (y ~739)
  163 px (161-164), wheelbase 95.5 px, tyre outer diameter ~66 px.
- Events: enters from left edge at frame 0 (already moving; fully in frame from frame 6), behind near-left
  fence/lamp pole frames 14-33, ref point crosses x=960 at frame 48, front wheel behind traffic-light pole frames
  76-79, still moving and in frame at the end (ref x ≈ 1615). No stop, bounce, impact or turn.

## Ambiguities / reliability
- Reference point: the benchmark's origin could be the bike root or the rider's pelvis; both move identically
  (only a constant offset), so speeds/distances are the same. Use `ref_*` for positions.
- Frames ~8-15: a thin vertical strip is hidden behind the grey utility pole (x 205-230); extents still fine.
- Overlays (frames/verify.png, frames/ov/) confirmed the boxes cover rider+bike and the hub midpoint and pelvis
  estimate sit on the bike / hips.
- Frames 0-5: object cut by image edge; bbox width there is not the object size. Frames 14-33: lower/rear part
  hidden (lengths smaller), hubs from line fit. Frames 36-41: mask x0 includes the ground shadow; use hub_based
  values. Frame 9 mask bbox glitch (length 143).
- Mask bottom in raw data includes the ground shadow (up to y 761); the final y1 excludes it.
- Static object coordinates in scene.json are read off a gridded full frame (frame 42) and are ±5-10 px.
