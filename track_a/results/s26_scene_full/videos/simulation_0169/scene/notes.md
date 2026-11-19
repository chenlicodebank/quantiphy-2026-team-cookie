# simulation_0169 — measurement record (pixels, seconds)

2D Blender render, 1920x1080, 24 fps, 80 frames (t = frame/24, 0 … 3.292 s). Static camera.
A white-suited **astronaut** floats in black space to the right of a large grey **moon** surface (left of the
frame, curved limb on its right, flat cut edges at y=86 and y=993, so it looks like a backdrop). A few faint
static stars. The astronaut is the only moving object.

## Files
- `scene.json` — inventory, sizes, camera, events (summary of everything below).
- `tracks/astronaut.csv` — every frame 0-79: `cx,cy` (mask centroid = reference point), `bbox_cx,bbox_cy`,
  bbox `x0,y0,x1,y1,bbox_w,bbox_h`, `axis_len` / `axis_wid` (mask extent along / across its principal axis),
  `axis_angle_deg` (principal axis, image coords, 90 = vertical), `area_px`, `occluded` (always 0).
- `scripts/track.py` — segmentation (gray > 25, connected components; drop the moon = largest component; keep the
  largest remaining blob, merge fragments >= 40 px within 15 px; stars ~10 px are ignored), camera phase-correlation,
  moon-limb sampling, overlays in `frames/ov_*.png`. `scripts/check.py` — consistency, per-frame steps, limb circle
  fit. `scripts/moon_edges.py` — moon top/bottom edges. `scripts/track_summary.json` — limb x per 20-px row, camera shift.

## Astronaut
- Start (frame 0) centroid (1295.6, 518.5); end (frame 79) (1310.9, 244.0). Net (+15.3, -274.5) px, |d| = 274.9 px;
  path length 275.3 px — the path is nearly straight, ~3° right of vertical, moving up the image.
- Motion profile (centroid steps, px/frame): ~0 at frame 1, smooth ease-in (≈2 px at frame 8-10, ≈4 px at 20),
  plateau ≈5.0-5.3 px/frame over frames ~32-47, smooth ease-out (≈4 px at 56, ≈2 px at 70-72, ≈0.5 at 77-78,
  0.04 at 79). Looks like a Blender ease-in/ease-out keyframe, not a constant acceleration — fit what a question needs.
- Size: body length along main axis 90.2-92.4 px (≈91.5), stable → no depth change (truly 2D). Width across
  axis 43-49 px (arm pose). Bbox 44x91 at frame 0 (upright), 62x84 at frame 79 (tilted). Pixel height of the
  upright figure at frame 0: 91 px (bbox) — use this for a "height of the astronaut" prior.
- Orientation: principal axis 94.7° → 120.2°, i.e. the body slowly tilts ~25° (head to upper right) during the move.

## Static
- Moon: x 0…1357, y 86…993 (908 px visible height). Limb x: 840 @ y87, 998 @ y300, 1147 @ y540, 1274 @ y800,
  1357 @ y992. Circle fit to the visible arc: centre (-1666, 2112), radius ≈3222 px (extrapolated, uncertain ±
  a few %). Radial gap astronaut centroid → limb ≈141 px at frame 0, ≈292 px at frame 79.
- Stars: e.g. (1665,127), (1418,771), (1235,549), (1020,316); 2-6 px, irrelevant to motion.

## Reliability / ambiguities
- Centroid of the white mask stands in for the rig's pelvis/origin; at frame 0 it sits at the hip region
  (verified on overlays ov_00/40/79). Its offset from the true origin can shift by ~1-2 px as the body tilts and arms
  move; per-frame centroid noise ≈0.2-0.5 px (visible as jitter in the steps). Dark visor is partly outside the mask
  (≤ ~3 px effect on extents). Mask has soft glow edges; extents ±1-2 px.
- Camera: static (shift ≤ 0.5 px). No occlusion, no contact, no bounce. Motion blur negligible.
- No metric scale is assumed; the answering session must set metres-per-pixel from its prior (e.g. astronaut
  height ≈ 91 px, or the astronaut's pixel speed/displacement).
