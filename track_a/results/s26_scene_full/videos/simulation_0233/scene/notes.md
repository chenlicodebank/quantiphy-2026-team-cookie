# simulation_0233 — measurement record

**Scene:** a Blender render (2D, 24 fps, 50 frames, 1920x1080) viewed straight down onto a classroom. A black cat walks steadily from left to right along a light-wood table top on the left. Also in view: a tan student chair with a writing tablet on the parquet floor at the right, and a green chalkboard strip along the top. The camera is static: the background differs by less than 1 grey level between frames, and the phase-correlation shift from frame 0 to frame 49 is about 0.5 px.

## Files
- `scene.json`: inventory, static-object pixel extents, events, camera, and advice on the cat's pixel sizes and reference point.
- `tracks/cat.csv`: one row per frame (0-49). Columns:
  - `bbox_*`: bounding box of the full mask, tail included.
  - `bbox_cx/cy`: centre of that box.
  - `mask_cx/cy`, `mask_area`: centroid and area of the full mask.
  - `body_*`: the mask opened with a 21 px disc, which removes the tail; extents and centroid.
  - `length_with_tail_px`, `length_body_px`, `width_px`: mask extents. `width_px` is across the cat, along image y.
  - `nose_x`: rightmost mask pixel. `tail_tip_x`: leftmost mask pixel.
  - `head_front_robust_x`: rightmost column with at least 15 mask pixels, so whiskers and ears are ignored.
  - `rump_x`: leftmost column with at least 25 mask pixels (the tail is excluded).
  - `torso_mid_x`, `torso_len_px`: midpoint and length between `head_front_robust_x` and `rump_x`.
  - `head_grey_px`: number of grey-head pixels added to the mask.
  - `cut_by_left_edge` / `occluded`: 1 while the cat is cut off by the image's left edge.
- `scripts/`:
  - `track_cat.py`: segmentation and tracking; it also writes the check overlay.
  - `static.py`: table, chalkboard and camera check.
  - `probe.py`, `crops.py`: viewers.

## Method and reliability
- **Cat mask:** black pixels (max channel < 40) inside the table region, taking the largest component.
  - From frame 45 the head renders as a flat grey-brown blob, which is a render artifact. It is added using a colour test limited to a window just ahead of the black body. Overlays at frames 0, 10, 20, 30, 40, 44, 46 and 49 were checked by eye, and the masks cover the whole cat including the tail. The shadow, which falls above the cat, is excluded.
  - The small white muzzle and nose tip (frames 0-44) is not in the mask, so the true nose is about 5-10 px right of `nose_x`.
- **Accuracy:** extents are good to about ±2 px. For frames 45-49 the head front depends on the grey-head segmentation, so it is about ±4 px (at frame 45 the step is +16 px instead of about 13.5).
- **Reference point:** the cat's origin/root cannot be seen.
  - `head_front_robust_x` moves very uniformly, about 13.55 px/frame (49 → 713 over frames 0-49). Over frames 22-49 the tail tip averages 13.96 px/frame.
  - `torso_mid_x`, `body_cx` and `rump_x` wobble by 10-30 px with the gait: hind legs stretch back, and before frame 22 part of the cat is outside the image.
  - Body-centre y stays at 528-535, so the motion is purely +x.
  - For speed, distance or acceleration, use the slope of `head_front_robust_x` (or a fit to it). This is the same as the slope of a body-fixed origin. The walk looks like constant speed, so per-frame acceleration is about 0 apart from jitter.
  - Origin position ≈ `head_front_robust_x` minus about 120 px (mid-torso). This offset is an estimate.
- **Cat sizes (pixels):**
  - Full length, nose to tail tip, while fully visible (frames 22-49): 324-339 px. The tail curls, so this varies.
  - Torso, head front to rump: about 240 px with the legs under the body, up to about 295 px with the hind legs stretched back.
  - Width: 64-68 px.
  - Height cannot be seen from a top-down view.
  - Before frame 22 the cat is cut off by the left image edge, so lengths there are not full lengths.
- **Static objects:**
  - Table top: x 0-714 (it continues past the left edge), y 366-848, so 482 px wide. Edges come from gradient profiles, ±2 px.
  - Chair (on the floor): whole chair x 1540-1835, y 502-718. Seat 1587-1762 × 550-715. Tablet 1595-1835 × 502-540. Read by eye from a zoomed grid, ±3 px.
  - Chalkboard green: y 93-199, full image width.
- **Depth caveat:** the chair and floor are at a different depth (farther from the camera) than the table top. Using one metres-per-pixel scale is valid only within the table-top plane, where the cat is.
- **Events:**
  - The cat is already walking at frame 0 and never stops, turns or jumps.
  - The tail enters the image at frame 22 (t = 0.917 s).
  - The head reaches the table's right edge at frame 49 (t = 2.042 s), the last frame.
