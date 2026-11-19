# simulation_0036 – measurement record

3D Blender render, 1080x1080, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). Static camera. A red fishing boat
("AH805") sails leftward across the bay while a small person walks rightward along a walkway on the left shore.
All values are pixels / frames; no metric scale was assumed.

## Files
- `scene.json` – inventory, camera, static objects, events, first/last apparent sizes.
- `tracks/boat.csv` – every frame 0-71: `cx,cy,x0,y0,x1,y1,width_px,height_px` = bbox of the whole boat mask
  (mast top to keel bottom, bow to stern incl. the aft whip aerial); `hull_*` = bbox of the red hull only;
  `mask_cx,mask_cy` = mask centroid; `area_px`; `occluded` (always 0).
- `tracks/person.csv` – every frame 0-71: bbox (`x0..y1`, `width_px`, `height_px` head to feet), `pelvis_x`
  (mask centroid x), `pelvis_y` (top + 0.47 x height, approximate hip), `feet_y`, `area_px`, `occluded` (0).
- `track_summary.json` – first/last values and linear slope (px/frame) of each track column (descriptive only).
- `scripts/explore.py` (camera-shift check), `scripts/track.py` (segmentation + tracks + overlays),
  `scripts/summarize.py` (summary).

## Method
- Camera: phase correlation of hill/sky bands against frame 0 → shift < 0.015 px everywhere: static.
- Boat: red HSV mask (largest component, keeps the waterline reflection out) = hull; plus |frame − background|>28
  in a window around the hull above the keel, background = frame 0 for x<510 and frame 71 for x≥510 (boat-free
  regions); closed and the hull-connected component kept. Overlays (frames 0, 24, 48, 71) show the mask covers
  hull, wheelhouse, rails and mast; the thin stay wires are partly included.
- Person: |frame − per-pixel median of the left-shore band| > 30, nearest component to previous position, x<250.
  Overlays at 5x confirm head-to-feet coverage (feet may be clipped by ~1 px).

## Results (pixels)
- Boat: hull_cx 608.5 → 398.5 (≈ −3.05 px/frame, steady, per-frame step sd 0.8 px from mask jitter), image y
  almost constant (keel bottom 765 → 770). Apparent size grows linearly ~11 %: hull width 176.7 → 196.7 px, full
  bbox 178.7x221.3 → 199.0x234.7 px (w x h), hull height 64 → 68 px ⇒ the boat approaches the camera by ~10 % of
  its depth while moving left (depth ratio ≈ size ratio). Seen obliquely (bow left, starboard side), so image width
  mixes length and beam; full height (mast to keel) is the cleanest vertical size: 221 px at frame 0.
- Person: pelvis_x 128.9 → 201.1 (≈ +1.05 px/frame, steady), head top y 705 → 711, feet ~746 → 751, height
  37-45 px (mean ~41, gait oscillation), width 9-19 px (leg swing). Constant apparent height ⇒ depth ~constant.
- Static: far shoreline (water/hill base) y≈707 across the frame (horizon itself hidden by dunes); walkway x 0-355,
  y≈742-765; seawall x 0-145 y≈715-742 with dark wooden block x≈143-157 y≈728-742; pale sand bank x 0-70.
- Events: both objects move during the whole clip; no start/stop, contact, bounce or impact. They never overlap.

## Reliability / ambiguities
- Boat bbox edges ±1-2 px (antenna and wires are thin and faint against the sky; red reflection excluded).
  The Blender origin of the boat is not visible: hull centre (hull_cx, hull_cy) or bbox centre are candidates;
  use differences (displacements) which are insensitive to this choice.
- Person is tiny: ±1-2 px ⇒ 3-5 % height error; pelvis_y is an estimate (47 % down from the head).
- Water reflection of the boat (red streaks below y≈775) is not the boat.
- Depth change of the boat means pixel speed ≠ proportional to world speed at one scale; use the given depth_info
  and the size change (apparent size ∝ 1/depth) to recover 3D motion.
