# simulation_0205 — measurement record (pixels, seconds)

Video: 2124x1080, 24 fps, 30 frames (t = frame/24, frame 0 at t = 0, last frame 29 at t = 1.208 s). Simulation (Blender) render, 3D scene.

## Content
A magnifying glass (metal lens ring, silver ferrule, light-brown wooden handle pointing to the right) is already falling at frame 0, with its top edge at y≈10 px. It falls almost level onto the green leather top of a dark wooden desk. It lands between the typewriter (left) and the paper card/revolver (right, further back). The lens-ring end rebounds/tilts up and comes back down, and the glass is at rest from frame 19. It is the **only moving object**. Static objects: desk, typewriter, revolver, paper card. There are no people, animals or vehicles, and no floor is visible.

## Files
- `scene.json`: inventory (description, how to tell objects apart, visibility, static extents), camera and perspective cues, events.
- `tracks/magnifying_glass.csv`: one row per frame 0–29. Columns:
  - `ref_x, ref_y`: bbox centre, the recommended estimate of the object origin.
  - `mask_cx, mask_cy`: mask centroid.
  - `lens_cx, lens_cy`: estimated centre of the lens ring.
  - `bbox_x0..y1`, `bbox_w/h`.
  - `len_main_axis, width_across`: minimum-area rectangle of the mask.
  - `height_px`: bbox height. `area_px`. `occluded` (always 0). `phase`.
- `tracks/magnifying_glass_raw.csv`: raw mask output, which adds the heuristic ring extents.
- `scripts/`:
  - `track.py`: mask and track. Difference against a clean background: frame 0, with rows <120 taken from frame 29. Threshold 30, morphology, largest component plus nearby components, holes filled.
  - `finalize.py`: writes the CSV and the JSON.
  - `check_overlay.py`: draws the track on the last frame.
  - `probe.py`: pixel profiles.
  - `diff.py`: camera/background check.

## Measurements and reliability
- **Camera**: static. The background difference in a static region is ≤0.2 grey levels in every frame. The view is elevated and looks down at the desk; there is no horizon (plain backdrop). Perspective cues are the desk-top corners in scene.json: front edge ≈1316 px, back edge ≈1153 px, side ≈309 px (±5 px). Focal length and depth are unknown; derive them from the question's depth_info and prior.
- **Fall (frames 0–11)**:
  - Bbox top goes 10, 16, 32, 60, 98, 147, 206, 274, 352, 439, 534, 637 px. The per-frame step grows steadily, so the fall accelerates. Mask edges are sharp, about ±1 px.
  - x drifts slightly left: bbox centre 1357 → 1340, mask centroid 1340 → 1316.
  - The object is seen nearly edge-on (bbox height 21 → 40 px, because the view tilts more as it drops).
  - Apparent length shrinks 183–186 → 175 px. Part of this is depth/perspective, part is small rotation.
- **Impact**: frame 11 is still about 20 px above the rest level, so first contact happens between frames 11 and 12. Impact frame is 12 (t = 0.500 s).
- **Rebound/tilt (frames 12–17)**: the ring end lifts off the desk. The highest point is at frame 14 (bbox top 616 vs 658 at rest; mask centroid y 643.6). The ring comes back down around frame 17–18.
  - This is a rocking/tilting rebound, not a clean ballistic bounce of the whole object; the handle tip stays near the desk.
  - Second contact and settling at frame 18 (t = 0.75 s). At rest from frame 19 (t = 0.792 s); frames 19–29 are identical.
- **Rest pose**:
  - bbox (1255, 658)–(1429, 703), length ≈174 px.
  - Lens ring outer diameter ≈80 px horizontally.
  - Handle tip ≈(1429, 693). bbox centre (1342, 680.5). Lens centre ≈(1295, 677).
- **Static objects** (frame 0; ±3–5 px):
  - Typewriter bbox (858, 573)–(1150, 753): 292 px wide, 180 px tall.
  - Revolver bbox (1354, 605)–(1507, 642): 153 px long.
  - Paper card (1332, 620)–(1412, 641): 80 px.
  - Desk top bbox (460, 525)–(1995, 890). The desk legs leave the frame at the bottom, so the full desk height is not visible.

## Ambiguities
- **Origin**: the true Blender origin of the magnifier is unknown. It could be the bbox centre (`ref_*`) or the lens centre (`lens_*`). They are about 47 px apart horizontally and their vertical motion is almost the same. Use `ref_*` unless the question suggests otherwise.
- **Lens centre**: `lens_cx` is estimated as x0 + 0.23·(x1 − x0), since the ring diameter is about 0.46 of total length. `lens_cy` comes from the ring rows. Accurate to about ±4 px.
- **Bottom edge at rest and during 12–18**: it includes a soft bright glow/caustic plus defocus blur below the ring. The mask bottom 703 may sit about 5–8 px below the true rim, so treat rest `bbox_h` / `ref_y` as uncertain by ±4 px.
- **Rebound frames**: heights and widths in 12–16 change because the object tilts, not because of depth.
- **No motion blur problems**: there is no occlusion, and the object stays fully in frame (frame 0 top edge at y = 10).
- **Speeds/accelerations** are not computed here: difference `ref_y` (or `ref_x/ref_y`) per frame as each question requires.
