# simulation_0257 – measurement record (pixels, seconds)

Video: Blender simulation, **2D** scene, 1920x1080, 24 fps, 40 frames (t = frame/24, 0 – 1.625 s).
Camera is **static** (scripts/camera_check.py: phase correlation of AC unit, window and table regions vs frame 0 gives
|shift| <= 0.03 px in every frame). View is fronto-parallel to a blue wall; the fall happens in a plane facing the
camera, so a single px scale from the prior's object applies.

## Scene
A small white flower pot with a pale yellow-green succulent starts at the top centre of the frame (x ~1066, y 26–92),
falls straight down onto a long dark console table, lands at frame 15 and then rocks side to side on its base without
bouncing or leaving the table. Static: the table, a white LG outdoor AC unit (bottom-left), a notebook with a pen and a
black phone on the table (left / right of the landing spot), a white window frame at the right edge, the blue wall.

## Files
- `scene.json` – inventory, static extents, camera, events, summary of the pot's motion.
- `tracks/potted_plant.csv` – every frame 0–39: `mask_cx, mask_cy` (centroid of the segmented pot+plant),
  `bbox_cx, bbox_cy`, bbox `x0 y0 x1 y1` (inclusive), `bbox_w, bbox_h`, `main_axis_len / across_axis_w` (PCA extents
  of the mask), `main_axis_angle_deg` (PCA axis angle, ~90 = upright; >90 = top leaning right, <90 = top leaning
  left; crude because the silhouette is nearly as wide as tall), `area_px`, `occluded` (always 0), `bg` (which
  background frame was subtracted).
- `scripts/track_pot.py` – segmentation/tracking (difference vs a clean background: last frame while the pot is high,
  frame 0 once it is low; keeps pixels brighter than background so shadows are excluded; rows y >= 869 removed because
  the glossy table top mirrors the pot). Writes overlay crops `frames/ov_XX.png` (checked visually: masks sit on the pot).
- `scripts/static_profiles.py` – intensity profiles used for the static extents.
- `scripts/camera_check.py` – camera-motion check.

## Pot measurements and reliability
- Size at frame 0 (dark wall, best segmentation): bbox 1043–1089 x 26–92 → **width 47 px, total height 67 px**
  (pot + plant); pot body width ~46 px. The white pot body is segmented reliably; the pale leaf tips are partly lost on
  the light middle/lower wall (frames ~6–39), so bbox_h there reads 59–62 px (top y0 a few px too low). Use frame 0–5
  for height.
- Fall: x stays 1065–1066 (±0.5 px) – purely vertical. Bottom edge y1 (most robust coordinate during the fall):
  92, 96, 107, 124, 148, 179, 215, 259, 311, 370, 436, 510, 589, 677, 770, 868 (frames 0–15). Centroid y: 59.2 → 839.4.
  Centroid y in frames ~6–14 may be biased ~+2–3 px (lost leaf tips); bottom edge or bbox bottom avoids that. No
  noticeable motion blur.
- Object origin: unknown exactly; the mask centroid / bbox centre is the stand-in. A uniform offset does not affect
  displacements/speeds of a rigid translation, but during rocking (frames 15–39) the centroid moves sideways
  ±16 px while the origin may move differently (depends on where the origin sits relative to the pivot).
- After landing the bottom stays at y 867–868 (frames 15–39): no bounce. Table contact line y ≈ 868 (±2 px; the
  pot base merges with its reflection).

## Events
- Frame 0 (t 0): fall starts from (near) rest (bottom steps +4, +11, +17 px…).
- Frame 15 (t 0.625): impact on table (frame 14 bottom 770, frame 15 bottom 868 resting). Contact at or just before
  frame 15.
- Rocking: top leans right, max at frame 21 (centroid x 1082.3); upright ~26; leans left, max ~32 (x 1050.6);
  upright ~38; leaning right again at 39. Pot never leaves the table.

## Static objects (frame 0, px)
- Table: top surface from back edge y 865 to front edge y 895; front wood band 895–911; apron to ~927; left end x 518
  (in front of the AC unit), right end x 1539 → **length 1021 px**; legs at x 680–704 and ~1500–1507, running off the
  bottom of the frame (table height not fully visible).
- AC unit (white, LG logo at ~(489, 830)): x 132–637 (**width 505 px**), top y 758, bottom cut by frame (visible
  height 322 px); round fan grille ~250 px diameter on its left part.
- Notebook + pen: bbox x 890–969, y 858–873 (80 x 16 px). Phone: x 1141–1191, y 866–876 (51 x 11 px). Both thin
  objects seen almost edge-on – lengths are reliable to ~±2 px, heights are not meaningful.
- Window frame: x ~1634–1750, y 0–~833 (in a side wall, slightly perspective).

## Ambiguities
- Table reflection of the pot (removed by the y >= 869 cut). Faint shadow of the pot on the wall at frame 0 (excluded by
  the brighter-than-background test). Only one moving object, no similar objects to confuse.
