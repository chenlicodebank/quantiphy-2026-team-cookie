# simulation_0100 — measurement record (pixels, seconds)

2D simulation, 1920x1080, 24 fps, 58 frames (t = frame/24). Static camera. Side view of a sea: grey sky,
horizon at y≈567, grey sea surface to y=672, and a flat blue underwater panel from y=673 to the bottom.

## Objects
- **boat** — red fishing boat "AH805" (white wheelhouse, mast, aft rail), upper half. Moves RIGHT.
  Frames 0–1 identical (at rest), then constant +17.876 px/frame (linear-fit residual 0.03 px, step std 0.04 px)
  through frame 57. No vertical motion. Stern is cut off by the left image edge in frames 0–20; whole hull visible
  from frame 21. Mast top always above the image, so the full boat height is NOT measurable.
  Sizes (frame 57): length stern→bow 859 px (x 665–1523); hull height bow gunwale top (y 357) to keel/rudder bottom
  (y 640) 283 px; wheelhouse roof y≈237, wheelhouse x≈1077–1253; mast x≈1150. Mask bbox y1=672 includes the
  water reflection under the hull (use 640 for the keel).
- **shark** — grey/white shark in the underwater panel, head left. Moves LEFT. Frames 0–1 identical, then
  −10.73 px/frame (fit slope −10.746, per-frame centroid noise ~0.3–0.4 px), y constant 905.5. Always fully
  visible. Length snout→tail tip 270–278 px (median 274; variation is tail-tip/segmentation jitter, mostly a rigid
  slide), bbox height 106 px incl. dorsal/pectoral fins (y 852–957), body only ≈60 px.
- static: horizon line (y 567), underwater panel (y 673–1079). Nothing else in the scene.

## Files
- `scene.json` — inventory, sizes, events, camera.
- `tracks/boat.csv` — per frame: `ref_x, ref_y` = estimated origin = hull bbox centre (x = stern/bow midpoint,
  derived from the sub-pixel bow edge shifted by the frame-57 half-length; y fixed 498.5); `bow_edge_x_subpix`
  (mean bow edge over rows 400–600, the most precise position signal); `bow_shift_px`; `tm_dx/tm_dy` (template
  match — has ±8 px glitches at frames 5 and 13, do NOT use for speed); mask bbox (x0 = 0 while stern is cut);
  `length_px_visible`; `full_length_visible`.
- `tracks/shark.csv` — per frame: `ref_x, ref_y` = mask centroid; bbox centre; template-match shift; bbox;
  length/height/area; occluded (always 0).
- `scripts/track.py` (background-difference masks vs. clean plate stitched from frames 0 and 57 → raw_tracks.json),
  `scripts/finalize.py` (template matching → match.json), `scripts/write_tracks.py` (CSV), `scripts/check.py`
  (overlays + fit summary). Overlays in `../frames/` (check_10/45, mask_*.png) confirmed the masks cover the
  full boat (incl. mast, rail, reflection) and the full shark.

## Events
- Both objects start moving between frame 1 and 2 (t≈0.042–0.083 s); both still moving at the last frame 57.
- Boat fully in frame from frame 21 (t=0.875).
- Boat bow tip passes above the shark centroid at ≈frame 40 (t≈1.667); boat hull centre and shark centroid
  vertically aligned at ≈frame 55 (t≈2.29).
- No bounces, contacts or direction changes.

## Reliability / ambiguities
- Boat horizontal motion: excellent (±0.05 px). Boat origin is not observable: x-centre is well defined (hull
  midpoint); ref_y = 498.5 is the hull bbox centre — the real origin could be elsewhere (e.g. waterline y≈567 or the
  full bbox centre including the cut-off mast). This only matters for boat–shark distances, which also depend on
  whether the two panels share a scale.
- Boat pixel length 859 ±2 px is the best size reference for a boat prior; boat height is unmeasurable (cut).
- Shark: position ±0.4 px per frame; for speeds prefer a span/fit (e.g. (x57−x1)/56 = −10.73 px/frame).
- Both motions look uniform (constant velocity after the start at frame 1); the start is an instant jump from 0 to
  full speed in the sampled frames.
- The underwater panel is a separate view; boat and shark could have different px/m scales. If a question gives a
  prior on one object only, the single-scale 2D convention applies to both.
