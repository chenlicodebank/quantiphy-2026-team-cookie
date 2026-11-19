# simulation_0212 — measurement record (pixels, seconds)

3D Blender render, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s). Static camera.
Scene: a room corner with a wooden side table on the right (lamp and blue-white vase on it, tall framed mirror
leaning on the wall behind). Two animals walk across in opposite directions:
- **cat**: the small black cat with white paws and a raised tail. Its head is a flat grey patch. It walks left → right
  and **away** from the camera (feet y 959 → 880), so its apparent size shrinks (bbox height 262 → ~190 px).
- **dog**: the larger brindle dog with white paws and a white tail tip, head lowered, with a grey-beige cone/patch over
  its head. It walks right → left and **toward** the camera (feet y 899 → 960), so it grows (bbox height 268 → ~310 px).
  It is slow in frames 0–8, faster in 9–40, decelerates from ~41 and has nearly stopped by frames 45–49.
- Crossing: the masks first touch at frame 24. The dog passes **in front of** the cat. The cat is mostly hidden in
  frames 28–40 and fully visible again from 45.

## Files
- `scene.json`: inventory (animals + static objects with pixel extents), events, camera and perspective cues.
- `tracks/cat.csv`, `tracks/dog.csv`: one row per frame (0–49). Columns:
  - `frame`, `time_s`
  - `bbox_x0,bbox_y0,bbox_x1,bbox_y1` and `bbox_w,bbox_h`: full-mask bounding box. It includes tail, ears and, for
    the dog, the head cone patch.
  - `bbox_cx,bbox_cy`: bbox centre. `centroid_x,centroid_y`: mask centroid.
  - `core_cx,core_cy` and `core_x0..core_y1`: centroid and box of the torso core. The core is the mask after a
    morphological opening with a disk of ~0.18·sqrt(area), which removes tail, legs, ears and thin parts. **This is
    the recommended proxy for the rig origin/pelvis-body centre**: it is far less noisy than the bbox centre, which
    jumps when the tail is or isn't picked up.
  - `axis_len,axis_wid,axis_angle_deg`: extents along and across the mask's principal axis.
  - `mid_top_y,mid_bottom_y`: top and bottom of the mask within the middle 50 % of the bbox columns (back height
    without the tail tip).
  - `area_px`, `visible_area_frac` (area / median area in non-touching frames; it also changes with perspective)
  - `touching_other`: the two masks touch in the image.
  - `occluded`: 0 = clear, 1 = partly hidden, 2 = mostly hidden. The flag was set by visual inspection. For the cat
    it is 1 in frames 24–27 and 41–44 and 2 in frames 28–40. The dog is always 0.
- `scripts/`: `bg.py` builds a background plate (per-pixel mode of 14 frames → frames/bg_full.png, scratch).
  `seg.py` makes the foreground mask (|frame−plate| > 22, floor-shadow suppression below the skirting line, small
  holes filled). `track.py` splits the mask into cat and dog by colour, computes the stats and writes overlays.
  `finalize.py` adds the occlusion flags. `bgcrop.py`, `montage.py` and `probe.py` are inspection helpers.
  `tidy.py` keeps the record small.

## How the animals were separated
Probed colours: cat fur is near-black and neutral (max channel < 30, |R−B| < 10). The dog's fur, even where shaded,
has R−B ≥ 15. Cores are taken by those colour rules, and every other foreground pixel (white paws, the grey head
patches) goes to the nearer core. Overlays (cat blue, dog red, boxes, centroids) were checked on frames 0–49 at a
3-frame step. Separation is correct in all frames where the animals are apart.

## Reliability
- **Camera**: static. The plate subtracts cleanly in every frame, so the background shift is 0.
- **Cat, frames 0–23 and 45–49**: masks are clean. Bbox ±3 px, core centroid ±3 px. Paw tips that are white over
  the beige carpet are sometimes cut by 5–10 px at the bottom.
- **Cat, frames 24–44**: partly or fully hidden behind the dog. In frames 28–40 only the tail, back or leg pieces are
  visible, and the cat's grey head patch sometimes goes into the dog mask. In frames 31–37 the cat's bbox and core
  are **unreliable** (small fragments). Interpolate between frames 27 and 41 instead: core (886,815) at f27 and
  (1177.5,786) at f41. In frames 41–44 the cat's tail is hidden behind the dog's rump, so its bbox is short on the
  left/top.
- **Cat speed in the image**: core x steps ~22 px/frame early, ~17–19 later, and lower after re-emerging (it is
  farther away). The steps after re-emerging are noisy.
- **Dog**: never occluded. The full bbox jitters by up to ±60 px on the right in frames 9–18, because the thin tail
  over the brown table is detected only intermittently (e.g. x1 = 1666 at f9 vs 1537 at f15). The bottom edge of
  the head cone over the carpet is sometimes under-segmented (~10–20 px). In frames 24–28 and 49 the dog box can
  include a few cat-tail pixels. Use `core_*` for position. For body length, use the core width (head + torso
  without the tail) or the bbox in frames where the tail is clear (frames 20–49).
- **Grey patches** (cat head, dog cone): flat grey render patches, treated as part of each animal. Whether the dog's
  cone is part of the mesh's bounding box is unknown.
- **Static objects**: extents were read off gridded crops of the background plate, ±5 px. The "small vase" inside the
  mirror frame is probably the large vase's reflection.
- **Perspective**: both animals change depth. The cat recedes and the dog approaches, so a single pixel scale does
  not hold over time. Use depth_info and a focal length estimate when the question gives them. A ground-contact cue
  is the lowest foot y (`bbox_y1`): larger means closer to the camera.
- No speeds or accelerations are stored. The events in scene.json are from core-x steps and visual checks, ±1–2 frames.
