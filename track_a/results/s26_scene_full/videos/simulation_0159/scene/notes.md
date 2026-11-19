# simulation_0159 — measurement record

3D Blender render, 24 fps, 41 frames (t = 0 … 1.667 s, t = frame/24), 1920×1080. Everything is in pixels and seconds. No metric scale is assumed.

## Scene
An underwater scene with a static camera. Two animals swim from right to left:
- **shark**: a great white shark, the large upper animal (y ≈ 0–430 px). It swims leftward and also toward the camera: its image size roughly doubles between f0 and f40.
- **turtle**: a sea turtle, the smaller lower animal (y ≈ 645–875 px). It flaps its front flippers and stays at about the same depth.
- Static items: the seabed dunes along the bottom (crest y ≈ 915–975 px) with animated light caustics, and vertical sun rays that flicker slightly. There are no other objects.

## Files
- `scene.json`: inventory, camera, perspective cues, apparent-size change, key positions per object, events.
- `tracks/shark.csv`, `tracks/turtle.csv`: one row per frame (0–40) with these columns:
  - `frame`, `t_s`
  - `cx_px, cy_px`: centroid of the full mask.
  - `bbox_*`: the bounding box of the full mask, inclusive pixel coordinates, plus `bbox_w_px` and `bbox_h_px`.
  - `mask_area_px`
  - `mask_len_main_axis_px` and `mask_width_across_px`: PCA extents of the full mask (fins and flippers included).
  - `main_axis_angle_deg`
  - `cut_by_frame_edge`: 1 means the mask touches the image border, so it is truncated.
  - `core_*`: the same quantities for the **body core**. This is the mask after a morphological opening with a disk of about 0.3 × mask width, which removes thin fins, the tail and flippers. `core_cx/core_cy` is the steadiest proxy for the animal's origin (rig root, near the body centre).
- `scripts/`:
  - `track.py`: segmentation and tracking; writes the CSVs and the overlays.
  - `bgcheck.py`: camera-stability and background check.
  - `raycheck.py`: light-ray artifact analysis.
  - `montage.py`: overlay sheets.
  - `summarize.py`: per-frame dx and size lists, written to `scripts/summary_tmp.json`.

## Method
- **Background:** frame 0 everywhere, except the area x ≥ 1450, 150 ≤ y < 800, which is taken from frame 40 (both animals are elsewhere by then).
- **Mask:** max-channel |frame − bg| > 14. The seabed polygon is excluded because its caustics animate. Sun-ray flicker is also excluded: G and B rise by ≤ 26 while R is almost unchanged.
- **Clean-up:** open/close, then fill holes. Per animal, the largest component inside a gate around its previous bbox is kept, together with nearby pieces of ≥ 400 px.
- **Check:** overlays were drawn every 4 frames and inspected. Masks cover the full shark (fins and tail included) and the turtle's body and flippers.

## Reliability
- **Camera:** static, no shake (background difference < 2 grey levels).
- **Shark:**
  - Fully inside the image only for **f20–f37**. In f0–f19 the tail is beyond the right edge; in f38–f40 the snout is past the left edge, and at f40 the dorsal fin touches the top edge.
  - Centroids and lengths from truncated frames are biased; use `cut_by_frame_edge`. In f0–f37 the snout (`bbox_x0`) is a reliable leading-edge point.
  - Full-length estimates: 554 px (f20), 608 (f24), 681 (f30), 718 (f32), 858 (f36), 901 (f37).
  - Mask edges are accurate to about ±3–5 px. The dark snout against dark water at f0–f5 may be under-segmented by ~20–30 px.
  - The image speed of the core centroid grows smoothly from about 1 px/frame (f0–f3) to about 105 px/frame (f37). The values after f37 are cut by the edge.
  - The shark comes closer to the camera: core height grows 154 → 319 px from f0 to f40. Its depth therefore shrinks, roughly in inverse proportion to apparent size, if orientation is similar. The shark also turns more side-on over time, so length foreshortening changes as well. Use height/width rather than length for depth ratios.
- **Turtle:**
  - Always fully visible.
  - Its flippers change the full-mask extents a lot: bbox bottom 749 px at f0 → 873 px at f21–24 (downstroke) → 787 px at f40. Use the core columns for position.
  - Core centroid noise is about ±5–10 px, with a jump at f6 when the flipper root detaches from the core.
  - Image motion is slow at f0–f12 (≈1–5 px/frame left), then about 12–27 px/frame left (f19–f40). Vertical motion is small (core y 695 → 717).
  - The thin leading flipper tip and head are sometimes under-segmented: full-mask x0 jumps ±20 px, for example at f33.
  - The turtle's apparent size is roughly constant (core height ~98–123 px; shell top y 645–658), so its depth is roughly constant.
- **Origins:** the rig origins are not visible. Centroids are proxies; for elongated animals, the core centroid ≈ body middle.
- **Focal length:** unknown. To estimate it, combine a given depth with a known size, for example f = pixel size × depth / size, using a fully visible frame (shark f20–f37). Back-project positions as X = (u − 960)·Z/f.
- **Ambiguities:** none between objects. There is only one shark and one turtle; they never overlap or touch. The shark's volumetric shadow in the sun rays below it at f36–f40 was excluded from its mask.

## Events
- Both animals are swimming from f0.
- The shark is fully in view from f20 (0.833 s) to f37 (1.542 s). Its snout reaches the left edge at f38 (1.583 s).
- The turtle's flipper downstroke is about f3–f21, lowest at f21–f24 (0.875–1.0 s), then upstroke to f40.
- There are no contacts, bounces or releases.
