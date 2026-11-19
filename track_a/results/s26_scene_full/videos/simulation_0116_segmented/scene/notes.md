# simulation_0116_segmented – measurement record

2D segmentation clip (Blender render, background replaced by uniform white RGB 253), 24 fps, 32 frames
(t = frame/24, 0 … 1.2917 s), 1386 × 1920 px (portrait). Pixel coords: x right, y DOWN, full resolution.

## Files
- `scene.json` – inventory, static-object extents, events, camera.
- `tracks/football.csv` – every frame 0-31: `cx,cy` (mask centroid = reference point / proxy for the
  object's origin), `bbox_cx,bbox_cy`, bbox `x_min..y_max`, `bbox_w,bbox_h`, principal-axis `axis_len`
  (length along main axis), `axis_wid` (across), `axis_angle_deg` (0 = +x, 90 = vertical), `area_px`,
  `occluded` (always 0), `appearance` (textured / grey_silhouette).
- `static_components.json` – raw connected components of the cabinets at frames 0 and 31.
- `scripts/` – `probe.py` (threshold choice), `crops.py` (appearance montage), `measure.py` (track + statics + overlays).

## Scene
- **football** (only moving object): American football, dark brown with white stripes, right side (x ≈ 1010-1065).
  Falls straight down: x stays 1035-1038, cy 228.5 (f0) → 1730.2 (f31). Per-frame Δy rises steadily from
  ~2 px (f0→1) to ~95 px (f30→31), consistent with release from (near) rest at frame 0 under constant
  acceleration. No bounce/impact/contact; still falling at the end. It tumbles only slightly (long axis
  stays ~vertical, 79-99°). Pixel size: long axis ≈ 68 px (f0-15), ≈ 62 px (f16-31); short axis ≈ 45 / 41 px;
  overall ≈ 65 × 44 px. Long axis is vertical, so for a size prior "length" ≈ bbox_h / axis_len and
  "width" ≈ bbox_w / axis_wid.
- **upper_cabinet**: yellow cabinet with dark-grey top band, x 647-807 (161 px wide), y 824-1151 (~328 px tall),
  centre (727, 988). Bottom edge ragged (segmentation fragments to y ~1170) and a white gap at y ~1040-1045.
- **lower_cabinet**: yellow cabinet/door with dark-grey top band and handle, x 646-807 (162 px), y 1374-1718
  (345 px), centre (727, 1546). Clean edges. Gap between cabinets 223 px.
- Camera static (cabinet masks identical at f0 and f31 within 1-2 px). No ground, horizon or vanishing
  points; 2D plane facing camera, so one m/px scale applies (football and cabinets assumed at the same depth –
  unverifiable).

## Method & reliability
Mask = min(R,G,B) < 240; football = largest connected component in x ≥ 880. Overlays (frames/overlay_*.png)
checked: mask covers the full ball, no stray pixels. Centroid accuracy ~±1 px in y for frames 0-25.
Caveats: (1) frames 26-31 the football is rendered as a flat pale-grey silhouette with a dark rim – mask is
still full but slightly wider (area ~2150 vs ~1850 px), so centroid/extent there carry ~±2 px extra error;
(2) frame 0 mask includes a small dark tip at the bottom (bbox_h 73); (3) slight motion blur in the
fastest frames could lengthen bbox_h by a few px; (4) the centroid of the visible silhouette is used as the
origin – for a symmetric ball this matches the rigid-body centre. Cabinet heights ±20 px (upper) because of
segmentation artifacts; widths ±2 px.
