# simulation_0211 — measurement record

3D Blender render, 1920x1080, 24 fps, 50 frames (0-49, t = frame/24, 0 to 2.0417 s). Static camera.
A black cat (white paws, plain grey head, raised tail) walks from the lower left toward a furnished
corner on the right: wooden side table with lamp (white pleated shade, dark base), blue-white porcelain
vase, and a tall leaning floor mirror against the back wall. The cat is the only moving object.
All values in pixels / seconds; no metric scale assumed.

## Files
- `scene.json` — inventory (cat, side_table, table_lamp, mirror, vase, walls, floor), static pixel extents,
  camera/perspective cues, events.
- `tracks/cat.csv` — one row per frame 0-49:
  - `bbox_x0,y0,x1,y1,w,h,cx,cy`: full mask box (tail tip to nose, ear tip to lowest paw).
  - `mask_cx,mask_cy,mask_area`: centroid/area of the full mask (includes tail and legs).
  - `torso_cx,torso_cy`, `torso_x0..y1`: dark torso after a 31 px elliptical opening removes legs, tail
    and the grey head. **Recommended reference point (proxy for the rig root/body centre).**
  - `torso_len_axis,torso_wid_axis,torso_axis_deg`: torso extents along / across its principal axis.
  - `feet_y`: lowest mask row (ground contact row; includes a few px of contact shadow).
  - `occluded`: always 0.
- `scripts/segment_cat.py` (track), `scripts/static_objects.py` (+`static_raw.json`, furniture extents and
  camera-shift check), `scripts/perspective.py` (+`perspective_raw.json`, floor lines, horizon), `bg_crop.png`
  (half-size median background band).

## Method
Per-pixel median background over all 50 frames in band y 560-1080; cat = max channel difference > 28,
opened/closed, largest component plus nearby fragments. Overlays drawn on frames 0, 7, 14, ..., 49 and
inspected: the mask covers the whole cat (tail, ears, all four legs, grey head) and nothing else except a
thin contact shadow under the paws.

## Key numbers
- Cat torso centre: (407.0, 842.0) at f0 → (1234.0, 787.6) at f49; ≈ 15-23 px/frame in x, smooth monotonic
  rightward motion with small gait bobbing (±5 px in y). Walking at both clip ends (no start/stop event).
- Apparent size shrinks: torso length 262 → 176 px (×0.67), sqrt(area) 189 → 138 (×0.73), bbox h 273 → 202
  (×0.74), bbox w 378 → 260. So the cat recedes (depth up ≈1.35-1.5×) while moving right.
- Static (frame 0): table bbox (1288,652)-(1667,839), 380×188; table top slab y 652-699. Lamp
  (1276,399)-(1466,664): shade 191×93, base ≈44×162. Mirror ≈(1395,307)-(1600,820), 205×513. Vase ≈(1501,469)-(1588,653),
  87×184.
- Perspective: back-wall/floor line y = −0.0753x + 909.2; right-wall/floor line y = 0.1279x + 565.2; floor corner
  (1693.5, 781.7). Horizon roughly y ≈ 590-620 (weak). Focal length unknown — must come from depth_info.
- Camera static (≤0.01 px shift over the clip).

## Reliability / ambiguities
- Cat bbox/mask: ±2 px; bottom edge (`feet_y`) includes 2-8 px contact shadow. Tail and legs make bbox and
  mask_cx vary with gait; torso centre is steadier but its length/width per frame are noisy (±15 px) because
  leg masses near shoulder/hip partially survive the opening. Average several frames for sizes.
- The cat's true origin (rig root) is not visible; torso centroid is a proxy, probably within ~10-20 px.
- Furniture extents: table and lamp shade from colour masks (±2 px); lamp base, mirror and vase read manually
  from zoomed grids (±4 px). The mirror shows a reflection of the vase (x≈1438-1478) — not a second vase.
- Horizon estimate is weak (two methods: 611 and 742; cat-path/wall-line intersection 588).
- Near the end (f44-49) the cat's head overlaps the table leg/shelf in the image only; the cat is in front, no contact.
