# simulation_0031 — measurement record

3D Blender render, 960x960 px, 25 fps, 75 frames (t = frame/25, 0 … 2.96 s). **Camera is static** (cliff band
phase-correlation shift ≤ 0.01 px over the whole clip). Elevated oblique view of a beach: cliff wall at the top,
sand in the middle/right, sea on the left and along the bottom. No horizon visible. No metric scale is assumed
anywhere; all values are pixels / frames.

## Objects
| name | what | moves | frames |
|---|---|---|---|
| boat | red-hulled fishing boat, white/grey cabin with red roof, mast with cross-tree, black davit, white rails | yes, steadily up-left (receding, apparent scale 1.00→0.92) | 0–74; stern cut by left edge from 52 |
| person | one man, white T-shirt, dark jeans, sand-coloured bald head, long shadow to his right | yes, walks steadily down-left | 0–74, never occluded |
| bird | dark bird (eagle/kite-like), grey wingtips, flapping | yes, flies left→right, slightly down, ~12.4 px/frame | 0–58 (fully in frame 0–53, cut by right edge 54–58) |
| cliff, sand beach, water, shoreline | static scenery | no | all |

There is only one of each moving object, so no identity ambiguity.

## Files
- `scene.json` – inventory, frame-0 boat geometry, pixel sizes, static features, events, camera.
- `tracks/boat.csv` – every frame: `ref_x,ref_y` = centre of the hull box (stern→bow, deck/cabin-body→hull bottom);
  `scale_vs_f0` (apparent size relative to frame 0); `ncc` (match score); `full_*` = whole-boat box including the
  mast top; `hull_*` = hull box; `hull_len_px`, `full_h_px`; tracked points `bow_tip`, `mast_top`,
  `cabin_roof_centre`; `occluded` = 1 when the stern is outside the left edge (boxes then extend to negative x —
  they are the extrapolated full extent, `visible_x0` is clipped).
- `tracks/person.csv` – every frame: `ref_x,ref_y` = pelvis estimate (y = head_y + 0.47·(feet_y − head_y), x = mask
  mean in that row); `centroid_*`; `head_y`, `feet_y` (lowest foot), `shirt_top_y`, `head_found`; bbox; PCA
  `mask_len`/`mask_wid`/`axis_deg`; `area`.
- `tracks/bird.csv` – frames 0–58: `ref_x,ref_y` = mask centroid; bbox; `mask_len` (PCA main-axis length ≈ image
  wingspan when the wings are spread), `mask_wid`, `axis_deg`, `area`; `occluded`=1 when touching the right edge.
- `scripts/` – `bg.py` (clean plate: median of frames, boat area patched from frames 0/74; `bg.png`),
  `track_person_bird.py`, `track_boat.py`, `camera_static.py` (+`static_measure.json`), `summarize.py`,
  `view_person.py`, probes. Overlays were written to `../frames/` and inspected.

## Method and reliability
- **Boat**: multi-scale (0.80–1.03) NCC template matching of the frame-0 bow + right half of the cabin
  (x 290–457, y 670–925), with sub-pixel refinement; the frame-0 boat geometry (measured by eye on a 2× zoom,
  ±3 px) is mapped by the found offset and scale. Overlays at frames 0, 25, 50, 74 sit on the boat. NCC falls from
  1.0 to 0.83 (waves, recession, slight view change). Track positions are smooth (~4.3 px/frame early, ~3.8
  late); scale is quantised at 0.005 steps (±0.5 %). The Blender origin of the boat is unknown; hull-box centre is
  the best proxy (bow_tip / mast_top are also given). Frame-0 sizes: hull length along the image x 272 px
  (stern deck corner (186,705) → bow tip (455,885) = 324 px diagonal), full height mast top → hull bottom 456 px.
  The boat's shadow/dark wake on the water trails to its lower right; not part of the boat.
- **Person**: |frame − clean plate| > 8 in a moving window, closing + hole fill (the head differs from sand only
  at its outline), vertical opening (1×11) removes the thin cast shadow, plus an explicit head-top search above the
  shirt. Visual checks (frames 0, 10, 16, 33, 47, 65, 74) show head top and feet hit within ~2 px. Height
  (head→lowest foot) ~79 px early, ~76 px later, noise ±3 px (frame 50 = 65 px outlier, 74 = 83 px may include a
  shadow pixel row). The pelvis ref inherits that noise (±2 px per frame) – smooth over a few frames before
  differencing. Walking legs make width vary 20–30 px.
- **Bird**: dark core (V < 90, diff > 40) over the sand plus grey wingtips (diff > 20 within 9 px of the core).
  Centroid is reliable to ~1 px; extents change with the wing beat (mask_len 44–75 px). Span maxima (wings flat)
  frames 6, 17, 32, 43; minima 0, 11, 21, 47. Max/min "wingspan in flight" should be taken from frames 0–53 only.
  Frames 54–58 are truncated by the image edge.
- **Static**: cliff foot y ≈ 102–128; shoreline polyline in scene.json is a visual estimate (±10 px, wave fringe).

## Ambiguities
- 3D scene: pixel motion mixes with depth change (boat recedes; person approaches slightly – feet_y 639→687 while
  apparent height stays ~76–79 px, within noise). Use depth_info and a focal estimate for 3D answers.
- Bird altitude unknown from the image alone; its shadow appears faintly on the sand (frame 0 near (830,600)).
- No release, bounce, impact or contact events; all three objects move through the whole time they are visible.
