# simulation_0124_segmented — measurement record

2D top-down simulation (segmentation version), 24 fps, 72 frames (3.0 s), 1080x1080 px. t = frame/24.
Pixel coords: x right, y down. Angles/headings in image coords (0° = right, 90° = down).

## Scene
- Frames 0–60: white background, only two cars visible. Frames 61–71: the full rendered background (S-shaped two-lane
  road, grass, trees) with **no cars** (both have left through the bottom edge).
- **car_dark** – dark navy/black car. It **leads** and drives in the right-hand (outer) lane. Visible frames 0–49,
  fully inside the image frames 4–45.
- **car_silver** – silver car with three red stripes. It **follows**, roughly on the yellow centre line. Visible frames 0–60,
  fully inside the image frames 5–54.
- Both drive down the road: down-right at first (heading ~37°), then curving to straight down (dark at frame ~14,
  silver at ~19, their right-most x points), then down-left (heading peaks ~128° around frame 34 for dark and ~42 for silver),
  then back toward ~100–105° as they exit at the bottom. The per-frame pixel step is nearly constant
  (dark ~27 px/frame, silver ~22 px/frame, scatter about ±1 px), so the gap between them grows from 87 px to 218 px. There is no contact.
- The camera is static (the background frames are identical, and car pixel sizes stay constant along the path). Top-down view:
  one metres-per-pixel scale applies everywhere (car length varies by only ±1 %). Car heights cannot be seen.

## Files
- `scene.json` – inventory, sizes, road measurements, events, camera.
- `tracks/car_dark.csv`, `tracks/car_silver.csv` – one row per visible frame. Key columns:
  - `ref_x_px, ref_y_px` – **the reference point to use**. This is the centre of a rigid silhouette template (the convex hull
    of the car mask from a clean frame: dark frame 29, silver frame 30), fitted by translation and rotation to each frame's mask.
    It is the footprint centre, i.e. the vehicle origin seen from above. On clean frames it agrees with the plain mask centroid
    (`cx_px, cy_px`) within ~1 px. On clipped and occluded frames it is much better than the centroid.
  - `step_px` – distance between consecutive ref points; `heading_deg` – direction of that step.
  - `quality`, `occluded`, `edge_clipped`.
  - `bbox_*` – axis-aligned box of the convex hull of the mask. `length_px`, `width_px`, `axis_deg` come from the
    minimum-area rotated rectangle of the hull (length along the car's main axis). `fit_angle_deg` is the template orientation.
  - `hull_area_px`, `raw_area_px`, `mean_brightness`, `fit_symdiff_frac` (fit residual as a fraction of template area) are diagnostics.
- `tracks/pair_dark_minus_silver.csv` – dark minus silver offset (dx, dy) and centre distance per frame, frames 0–49.
- `scripts/` – run from `scene_ws` in this order: `track.py` (segmentation, masks, extents) → `fit_template.py` (template-fit centres)
  → `finalize.py` (reference columns, quality, pair file). Also: `summarize.py` (statistics), `check_crops.py` (visual check
  montages), `paths_on_bg.py` (paths drawn on the background), `road_profile.py` (road line positions), `explore.py`.

## Sizes (pixels, clean frames only)
- car_dark: length 115.8 (10–90 %: 114.5–117.1), width 49.4 (47.5–50.9).
- car_silver: length 126.0 (124.0–127.1), width 51.6 (50.3–53.3).
  Masks include side mirrors and wheels as seen from above. Anti-aliased edges were thresholded at RGB min ≤ 235, so the
  values may run ~1 px larger than the true outline. Masks were checked visually and cover the full car body.
- Road (background frame 66): at row y=300, white edge lines are at x=671 and x=842 with the yellow centre line at x=755
  (171 px edge to edge, lanes ~84–87 px). Measured perpendicular to the road near (414,926), it is 190 px edge to edge.
  Near (600,660) it is ~169 px, with the right edge partly under the tree. The road width varies along the curve.

## Reliability and ambiguities
- Clean frames: ref point ±0.5–1 px, length ±1–2 px, width ±1.5 px.
- Entry (dark 0–3, silver 0–4): the cars are clipped by the top edge. The template fit puts the centre slightly above the visible
  part, and the bbox/length columns describe only the visible part. The ref centre is good to ~1–2 px.
- **Occlusion:** dark car frames 31–35 lie under the roadside tree canopy at about (590–700, 700–850). The segmentation mask
  has large holes there, so `cx/cy`, bbox, length and width are wrong for those frames. The template-fit ref points are
  consistent with the neighbouring frames, but treat them as ±2 px.
- Exit: dark frames 46–49 and silver frames 55–60 are clipped at the bottom. The ref centres continue the path smoothly
  through dark frame 48 and silver frame 58. Dark frame 49 and silver frames 59–60 show only a thin sliver: quality is `poor`
  and the centre is unreliable (it hits the search limit at y≈1100–1111). Avoid these frames, or extrapolate.
- Frames 0 and 1 are almost identical: centre shifts of 0.4 and 0.8 px, against ~27 and ~22 px on every later step.
  This is most likely a duplicated first render frame, not a real start from rest. Steps from frame 1→2 onward are already
  at full size, with no visible acceleration phase. A backward difference at frame 1 will therefore give ~0.
- The vehicle root is assumed to be at the footprint centre. If a rig root sat at the rear axle instead, positions would shift
  ~20–30 px along the car axis. Speeds and path shapes would barely change.
- The cars are told apart by brightness (dark mean ~50–70, silver ~80–110), with no confusion. Neither car casts a visible
  shadow on the white background.
