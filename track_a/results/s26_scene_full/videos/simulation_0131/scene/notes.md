# simulation_0131 – measurement notes

**Scene**: 2D Blender render, 1080x1080, 24.00396 fps, 97 frames (t = frame/fps, 0 – 3.999 s). A single hot-air
balloon (dark-blue envelope, ring of coloured squares near the top, red/yellow/purple/green gores, burner flame at
the neck, small brown basket on ropes) rises straight up against a uniform blue-grey sky (RGB ≈ 137,168,196).
No other objects, no ground, horizon or markings. Camera static (background uniform, nothing to shift).

## Files
- `scene.json` – inventory, extents, motion summary, camera, events.
- `tracks/balloon.csv` – every frame 0–96: frame, time, full bbox (x0,y0,x1,y1, inclusive pixels, y down),
  bbox centre, mask area-centroid (mask_cx, mask_cy), area, height_px/width_px, env_* (largest connected component –
  here identical to the full silhouette because the ropes connect basket and envelope), basket x-extent and bottom y,
  occlusion flag (always 0).
- `scripts/probe.py` (background colour), `scripts/track.py` (segmentation + tracking + overlays),
  `scripts/analyze.py` (per-frame displacement statistics, fits, sub-part extents).

## Method
Mask = pixels with |RGB − sky| summed over channels > 30, components > 20 px. Overlays at frames 0/48/96 were checked
visually: contour hugs the envelope, ropes and basket; bbox = full balloon.

## Key numbers (pixels)
- Frame 0: full height 472 px (y 504–975), max width 358 px (x 361–718, widest at row 641); basket ≈ 32 px wide ×
  ≈ 34 px tall (y ≈ 941–975); envelope + burner ≈ 416 px tall (to neck ≈ y 920); ropes ≈ y 920–940.
- Frame 96: height 479 px (y 113–591), width 358 px.
- Motion: purely vertical upward, x fixed at 539.55 ± 0.05. Centroid moves −4.020 px/frame (std 0.035, linear fit
  rms 0.17 px, no measurable acceleration); basket bottom exactly −4.000 px/frame (975→591); envelope top −4.07
  px/frame. Net rise frames 0→96: ≈ 384–391 px depending on the point (centroid 385.9 px).
- Events: none – the balloon is already moving at frame 0 and keeps a constant speed to the end.

## Reliability / ambiguities
- Blender origin of the balloon is unknown (could be envelope centre or basket); all candidate points move at
  4.00–4.07 px/frame, so speed/acceleration answers are insensitive to the choice (≤ 2%).
- Apparent height grows 1.5 % (472→479) while width is constant – slight perspective/view-angle change, not real
  growth; for a size prior use frame-matched pixel size (e.g. frame 0 or the frame of the question). Width (358 px)
  is the most stable size measure.
- Edges are integer-pixel (±1 px); antialiasing at the thin ropes makes basket-top/neck rows approximate (±2 px).
- No occlusion, no motion blur of note.
