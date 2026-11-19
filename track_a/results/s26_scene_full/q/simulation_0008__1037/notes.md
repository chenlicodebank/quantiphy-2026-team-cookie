# Q1037 – width of the wooden pier (m)

Prior: boat height = 0.75 m. depth_info: boat 7.452 m (t=0), 6.655 m (t=1); pier 11.579 m; stairs 17.623 m.
Camera static (scene record). The "pier" is the small stepped wooden dock in front of the boathouse, seen end-on
(front beam x 459-637 px, y 630-645; steps rise back toward the bank to y~592). The "stairs" are the steps under the
boathouse further back. Pier width = its horizontal extent across the image (the length runs away from the camera).

## Time base
t=1 s -> frame 24 (question_fps 24, the probable Blender rate; the file's 22.8 fps looks like a re-timing). Using
frame 23 changes f by only 3 % and the final answer by under 1 % (route B barely depends on it).

## Measurements (scripts in this folder)
- Boat, bbox top = bow post top y 620; waterline at the hull centreline = the mirror axis between hull and reflection at the
  bow/stern ends ~745-747 (`mirror_axis.py`, `mirror_mid.py`; mid-hull the near side bulges toward the camera, so the
  contact line there sits lower at ~766). The scene record's waterline (751-760) is that bulged near-side contact line, not the centreline.
  Height above water = 126 px.
- Focal length from the two boat distances, assuming constant boat depth (apparent length and post height constant;
  origin = bow_x + 324 px): f = 1001 px at frame 24 (973 px at frame 23), Z_boat = 5.85 m (`focal3.py`) ->
  metres/px at boat depth s_b = Z/f = 0.00584. Height check: 126 px x 0.00584 = 0.74 m, close to the 0.75 m prior with almost no
  hull below water. So the depth pair and the height prior agree: s_b = 0.0059 ± 0.0001 m/px.
  (This is badly conditioned: if the boat is assumed to approach the camera, f changes a lot; the height prior pins it.)
- Pier front beam: pixel width 177.5 px (row profiles, `pier_prof.py`). Water level at the beam: mirror axis of
  the beam and its reflection (beam 630-645, reflection 707-722) = y 676 (`profile.py`).
- Horizon from the water plane: water under the boathouse railing/roof by reflection symmetry is ~600-605 (house at
  ~18-20 m, just behind the stairs at 17.6 m), boat centreline 746 at 5.85 m -> vh ≈ 536-538 (camera almost level, cy=540).

## Answer
Route B (water plane): Z_front/f = s_b x (746 - vh)/(676 - vh) = 0.0059 x 1.50 -> W = 177.5 x 0.00885 = 1.57 m
(vh 540 -> 1.59; vh 527 -> 1.54).
Route A (pier origin depth): if the origin is the bbox centre, Z_front = 8.86 m -> Z_c/Z_front = 1.30, so the back of the
pier is at ~1.6 Z_front, and the back step should look ~111 px wide; it measures ~100-117 px, which fits.
W = 177.5 x 11.579/(1.30 x 1000) = 1.58 m.
Naive (front width at the origin depth, no front/centre correction): 178 x 11.579/1000 = 2.06 m. This is rejected because the front beam is much closer to the camera than the pier origin.

Answer: 1.57 m. Confidence moderate (±8 %): the main uncertainties are the horizon row and the boat's draft.
