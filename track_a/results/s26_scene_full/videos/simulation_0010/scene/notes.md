# simulation_0010 – measurement record

Simulation (Blender), 3D scene, 22.892308 fps, 59 frames (0–58, t = frame/fps, 0–2.534 s), 1920×1954 px.
All values in full-resolution pixels (x right, y down) and seconds. No metric scale is assumed.

## Scene
A timber-framed cottage (centre-left), two barrels, leaning poles, flower bushes, a rail fence and a wooden
hand cart (right) on a sunny grassy yard; a near tree's leafy branches hang in from the right edge.
**The only moving object is one black bird** (crow/magpie-like, grey-white sheen on wings, grey head/beak) flying
left → right in front of the house, head toward +x. It is already flying at frame 0 (no take-off, no landing) and at
the end flies behind the foreground leaves. Its shadow crosses the ground (not tracked).

## Camera
Static. Phase correlation of house and ground regions over all frames: shift < 0.03 px. No background correction needed.
Perspective: camera roughly level, house front almost fronto-parallel; horizon hidden, roughly at y ≈ 1080–1100.
Focal length unknown – derive it from given depth_info + a known size.

## Files
- `scene.json` – inventory (all objects, static pixel extents at frame 0), camera, events, bird summary.
- `tracks/bird.csv` – the bird, every frame 0–58. Columns: frame, t_s; `cx,cy` = full-mask centroid (recommended
  origin proxy); `body_x,body_y` = centroid of the thick core of the mask (distance transform ≥ 0.6·max – body
  without thin wings); `bbox_cx,bbox_cy`, `x0,y0,x1,y1`, `bbox_w,bbox_h`; `len_main_axis`, `width_across` (PCA
  extents of the mask); `area_px`; `occluded` (0 none, 1 slight leaf overlap, 2 mostly hidden).
- `tracks/bird_raw.csv` – first pass (dark pixels only; misses the grey head/beak); kept for reference, prefer bird.csv.
- `scripts/` – bg.py (camera check), track_bird.py (first pass), track_bird2.py (final mask/track),
  overlay.py (visual check crops), summarize.py (size trend, wingbeat).

## Method
Median background (band y 300–1150) from every 2nd frame; bird = pixels differing > 28 (max over BGR) from the
background within 35 px of a dark (>35 diff, gray < 110) seed blob linked frame to frame. Overlays checked at frames
0,4,…,56,58: boxes enclose the whole bird (wings, tail, beak) in frames 0–52.

## Key numbers (pixels)
- Path: mask centroid (354.8,779.6) at f0 → (1383.8,790.1) at f52; mean +21.4 px/frame in x, y essentially
  flat (oscillates ~760–820 with the wingbeats). Per-frame x step varies 10–32 px with the flap cycle, so per-frame
  speeds from the centroid are noisy (wing shape moves the centroid); smooth over a wingbeat (~8.7 frames) if needed.
  Path length of centroid f0–f52 ≈ 1100 px (includes flap wobble); net ≈ 1029 px.
- Apparent size: bbox width 130–190 px, median ~155 (f0–20) → ~167 (f40–52): roughly constant depth, maybe up to
  ~10 % closer at the end (some of the growth is wing pose). Wings-level frames (bbox_h < 70: f1, 2, 19, 36, 44)
  give tip-to-tail length ≈ 152–172 px. bbox height 56 (wings level) to 134 px (wings fully spread up/down,
  f14, f31–32, f49) – use the max bbox_h/len for "maximum wingspan as seen", but the wings are seen in
  perspective (bird flies across the view, wings point toward/away from camera), so image extents underestimate
  true wingspan.
- Wingbeat: bbox_h maxima ≈ frames 5–6, 14, 23–24, 31–32, 40–41, 49; period ≈ 8.7 frames ≈ 0.38 s.

## Events
f0 bird already in flight; ~f30 crosses past the roof edge into open sky; f39 leaves first overlap it (slight);
f53–58 mostly behind the foreground branch (centroid/bbox from visible wing/tail only – unreliable, biased);
f58 last frame. No impacts/bounces.

## Static objects (frame 0, ±5–10 px, read off a gridded image)
House walls x 210–910 (700 px wide), ground line y≈1175, eaves y≈790, roof eaves x 80–1025, roof apex y≈480,
top of crossed ridge boards y≈350. Doorway x 505–625, y 880–1160. Barrels: left x 742–822, right x 822–916,
y 1062–1175 (≈113 px tall). Fence x 1045–1330, y 1005–1180. Cart x 1295–1890, y 1010–1270; its wheel x 1643–1833,
y 1053–1263 (190×210 px, centre ≈ (1738,1158)). Flower bush left x 265–372, y 1108–1200. Static objects lie at
different depths from the bird (bird is in front of the house wall at the start), so their pixel sizes do not share
the bird's scale.

## Reliability / ambiguity
- Mask centroid ≠ exact rig origin; the origin is probably near the body. body_x/body_y is an alternative; both agree
  within ~5–15 px except when wings are spread (≤ 20 px in y).
- Frames 53–58: heavy occlusion; frames 39–52 slight overlap by leaves (a leaf in front can hide a small part of the
  bird, so the mask and bbox may lose a few px; otherwise fine).
- The bird's shadow on the ground is a second dark moving blob, excluded by restricting y < 1150.
- Mild motion blur on wingtips; low-contrast grey head against the grey wall is partially caught (threshold 28).
