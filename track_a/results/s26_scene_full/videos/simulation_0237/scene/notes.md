# simulation_0237 — measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s). Source: simulation (Blender), **2D** scene.
Near top-down (bird's-eye) camera over a house roof, lawn and trees. One moving object: a chestnut **horse**
walking to the right (+x) just below the house. Image coords: x right, y down.

## Files
- `scene.json` — inventory, camera, static object extents, horse size/motion summary, events.
- `tracks/horse.csv` — one row per frame (0–49):
  - `ref_x, ref_y`: **reference point** (best proxy for the rig root / body centre) = trunk centre measured in
    frame 0 (centroid of mask pixels in the rear 10–65 % of the body length, i.e. barrel without neck/head)
    plus the sub-pixel template-match shift of that frame. **Use these for positions/displacements.**
  - `shift_dx, shift_dy`: template-match shift vs frame 0; `match_score`: NCC peak (0.71–1.0).
  - `mask_cx, mask_cy`: centroid of the whole colour mask; `trunk_cx, trunk_cy`: per-frame mask trunk
    centroid (noisier, ±2–4 px, because the mask edge flickers with grass).
  - `bbox_x0..y1, bbox_w, bbox_h`: colour-mask bounding box (x0 = rump, x1 = nose tip).
  - `axis_deg` (principal axis, ~0 = horizontal), `length_px`/`width_px` (mask extent along/across axis),
    `trunk_width_px` (median vertical extent over 20–60 % of body length), `mainblob_y0/y1`, `area_px`,
    `occluded` (always 0).
- `scripts/`: `probe.py` (camera-shift / change detection), `track_horse.py` (**final tracker**),
  `track_horse_bg.py` (rejected background-subtraction attempt), `sample_colors*.py` (colour sampling),
  `house.py` (house extents), `summary.py` (track statistics).

## Camera
Static: phase correlation on a background patch gives |shift| <= 0.02 px for every frame. A small global
lighting/colour change occurs between frames 17 and 18 (mean |diff| vs frame 0 ~0.2 → ~1.1 grey levels); it is not
motion. As a 2D scene, one px→m scale applies (the horse walks on flat ground, constant depth).

## Horse (moving, visible and unoccluded in all frames 0–49)
- Chestnut coat, darker neck/head, white blaze at the nose tip, head pointing right. Only animal / only mover.
- Motion: walks steadily right the whole clip (already moving at frame 0, still moving at frame 49; no start/stop).
  ref point (747.17, 776.28) at f0 → (876.59, 774.91) at f49. Net displacement 129.4 px, path length 130.3 px
  (sum of per-frame steps). Per-frame step mean 2.66 px (sd 0.28, range 1.6–3.2; the scatter is mostly
  gait/matching noise). First and second halves have the same mean step (2.66 px/frame) — no visible
  acceleration. ref_y sways 772.7–778.7 px (gait bob/sway or matching wobble).
- Size (top-down view, so "length" = nose-to-rump along x, "width" = across body; height not observable):
  - length (bbox_w) in clean frames 143–149 px, **best ≈ 145 px** (frames 0, 13–17, 22, 39–42, 44–46 are
    cleanest); larger values (150–162 px) include grass specks near the nose/rump.
  - barrel (trunk) width ≈ 32–34 px; full mask vertical extent incl. ears/neck ≈ 40–48 px (median 43.5).
- Reliability: ref point ±0.5 px per frame (template matching, rigid-body assumption; leg swing hidden in
  top view). Per-frame mask extents ±2–4 px (dark head/neck has low contrast to shaded grass).
- Reference-point caveat: the true rig origin is not visible; the trunk centre is used. Displacements and speeds
  are unaffected by this choice (the horse translates almost rigidly).
- Overlays verified on frames 0, 8, 17, 24, 30, 39, 44, 49 (frames/ov_XX.png): contour covers rump to nose tip.

## House (static, measured at frame 0)
Grey/beige tiled roof, two wings joined by a wider central cross-wing. bbox x 617–1425, y 22–745
(809 x 724 px). Main block x 662–1363 (701 px wide), y 24–745 at x≈1025 (721 px). Cross-wing x 621–1424
(~805 px) at y≈380, y 273–519 (~247 px) at x≈650. Top/bottom roof edges form shallow chevrons (y≈97 at the
corners vs 24 at the centre line), so vertical extent depends on the column. Reliable to ±3 px.

## Other
Lawn (sunlit yellow-green, right side), darker grass, trees and tree shadows (left and bottom). No markings,
no other props, vehicles or people.

## Events
None besides continuous walking: no release, bounce, impact, contact or direction change.
