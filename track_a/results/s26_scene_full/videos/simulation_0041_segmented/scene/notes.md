# simulation_0041_segmented — measurement notes

2D-labelled Blender render (segmented: background is plain white), 1080x1080, 24 fps, 72 frames (t = frame/24).
Two objects, both moving, both visible in all 72 frames; no static objects, no ground features.

## Files
- `scene.json` — inventory, reference points, frame-0 extents, motion summaries, events.
- `tracks/boat.csv` — per frame: mask centroid `cx,cy`; bbox `x0,y0,x1,y1`, `bbox_cx,bbox_cy`, `bbox_w,bbox_h`;
  principal-axis length/width/angle of the mask; area; `touches_edge`; `occluded` (always 0);
  `tm_dx,tm_dy` = template-matched translation vs frame 0 (sub-pixel), `tm_cx,tm_cy` = frame-0 bbox centre + that shift; `tm_err`.
- `tracks/person.csv` — same columns without tm_*.
- `scripts/track.py` (mask = pixels with min RGB channel < 215, closed 3x3; components with centroid y<700 → person, else boat),
  `scripts/boat_template.py`, `scripts/boat_extent.py`, `scripts/check.py` (frame differences, overlays in `frames/`).

## Objects
- **boat**: red/white fishing boat with red cabin and mast, lower half, bow pointing left-up. Rigid; moves left and slightly up at
  ~5.8 px/frame, nearly constant (per-frame steps 4.7–6.7 px from centroid noise). Net (tm) displacement frames 1→71: (−396, −111) px.
  Frame-0 size: bow tip (347,924) to stern (682,1055) = 359.7 px along the hull axis (21.4° below horizontal toward the stern);
  bbox 337 x 234 px (height includes mast); min-area rect 338 x 186 px. The boat is a 3D model seen obliquely, so "width" in
  pixels mixes beam and freeboard/cabin height — treat with care. Bow touches the left edge from frame 63 → use `tm_cx,tm_cy`
  (rigid template match, agrees with bbox centre to ~1–2 px before truncation) for positions; centroid/bbox biased after frame 62.
- **person**: one small walking human (white shirt, dark trousers) at x≈358–367, walking down the image from y≈387 to y≈494
  (centroid), net (7.9, 107.1) px in 71 frames, ~1.5 px/frame with gait oscillation (0.6–2.7 px/frame). Bbox height 39–51 px
  (median 46.5) oscillating with the stride; width 18–20 px. Centroid ≈ waist; pelvis ≈ y0 + 0.5–0.55·bbox_h. Small object → ±1 px noise.

## Events
- Frames 0 and 1 are nearly identical (mean abs diff 0.09 vs ~1.3 later): motion of both objects starts at frame 1 (t=0.042 s).
- Frame 63 (t=2.625 s): boat bow reaches left image edge. No contacts, no bounces, no direction changes.

## Camera / scale
- Camera assumed static (simulation; white background gives no reference, but both tracks are smooth). View is oblique from above,
  but inputs say 2D: use one metres-per-pixel scale from the prior object. Caveat: the person (upper) and boat (lower) may be at
  different depths in the original render; the person's apparent height does not trend over time (gait oscillation only), and the
  boat's size is constant until truncation, so no visible depth change within each track.

## Reliability
- Boat tm positions: ~±0.5 px; boat frame-0 extents ±2 px (antialiased edges, thin mast/railings).
- Person centroid ±1 px per frame; heights ±1–2 px. Speeds from one-frame differences of the person are noisy — average over frames.
