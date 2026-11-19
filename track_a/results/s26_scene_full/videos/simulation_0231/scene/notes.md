# simulation_0231 – measurement record (pixels, seconds; no metric scale)

Video: Blender render, 2D scene, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s).
Classroom front wall seen head-on: green blackboard, wall clock, teacher's desk at left, student chairs/desks
in the foreground. **Camera is static** (no pan/shake; background difference f0 vs f49 ≈ 0.6 grey levels).
The wall is parallel to the image plane and both moving objects move parallel to it, so a single
px→m scale from the given prior applies (2D convention).

## Moving objects
1. **cat** – black-and-white (tuxedo) cat, black body, white paws, raised tail. Walks left→right on the top
   of the teacher's desk in all 50 frames, at a steady pace, no start/stop/turn. Feet on y ≈ 741.
   Torso centre x 269.5 (f0) → 703.0 (f49): 433.5 px in 49 frames (≈ 8.85 px/frame mean; per-frame steps vary
   ~6–12 px with the gait). Vertical body bob ±3 px.
2. **paper_airplane** – white paper airplane seen side-on, flies left→right in front of the wall: enters at
   the left edge f7, climbs, crosses onto the board f13, apex f23–24 (centre y ≈ 342), descends, leaves the
   board f33–36, exits the right edge f39–42; not visible from f43. Not ballistic: horizontal step rises
   64→74 px/frame (f13–21) and then falls to ~40 px/frame (f38) (a gliding flight); nose follows the path
   (axis angle −15° at f7, 0° at f23–24, +17° at f38; + = nose down in image).
   Full length ≈ 141 px (nose-to-tail, PCA axis, median of board frames 14–33, range 135–146);
   side-view height ≈ 12–13 px (strict mask).

## Static objects (median background, full res)
- blackboard green surface x 342–1670, y 315–716 (1328 × 401 px); with wooden frame x 322–1692, y 296–737 (1370 × 441).
- wall clock centre (1758, 292), diameter ≈ 108 px (h) / 113 px (v).
- teacher's desk top x 72–797 (front edge y 766, rear y 735); front panel x 95–790, y 766–~1005 (≈ 240 px tall).
- student chairs/desks (foreground, cut by bottom edge), a wooden chair against the wall at right
  (x 1600–1790, y 737–1010), four ceiling light panels. Exact extents of these are approximate.

## Files
- `scene.json` – inventory, static extents, summary sizes, events, camera.
- `tracks/cat.csv` (frames 0–49): `cx_bbox,cy_bbox` bbox centre (incl. tail); `cx_mask,cy_mask` mask centroid;
  `cx_dark,cy_dark` centroid of the near-black body; `bbox_*`; `body_*` (columns with ≥35 px mask, noisy);
  `nose_x` (= bbox_x1), `feet_y`; `torso_x0/x1/len/cx` – horizontal extent of the body in rows y 650–680
  (excludes tail and legs; **recommended length and x reference**, median 146 px, range 140–151);
  `head_top_y`, `height_no_tail` (feet to top of head/ears, median 96 px); `occluded` (always 0).
- `tracks/paper_airplane.csv` (frames 7–42): bbox/mask centre, `len_axis,width_axis,axis_angle_deg` (PCA),
  `background` (board / wall), `reliability`, `nose_*`/`tail_*` (ends of the mask on its axis),
  `cx_from_nose`/`cx_from_tail` (centre = visible end ∓ 141.3/2 px along the axis),
  **`cx_best,cy_best` recommended centre** with `best_method`: bbox centre when fully visible (f13–38),
  tail+L/2 for the left-wall frames 10–12 (nose tip invisible on the wall) and right-edge clipped frames 39–42,
  nose−L/2 for left-edge clipped frames 7–9. `occluded`=1 when clipped by the image edge.
- `scripts/`: `bg.py` (moving-object discovery by median-background difference), `track.py` (cat track and
  first-pass airplane), `plane_refine.py` (final airplane track: hysteresis LAB difference, window propagated
  from the previous detection), `finalize.py` (cat torso/height columns, airplane end-based centres),
  `static.py` (edge profiles of static objects). Run in order: track.py, plane_refine.py, finalize.py.

## Reliability / ambiguities
- Airplane on the board (f13–33): sharp, centre ±1–2 px, length ±3 px. The bbox centre is used as the
  origin proxy (the paper plane's origin should be near its geometric centre; the rear fold makes the mask
  centroid sit ~5 px behind the bbox centre – `cx_mask` also given).
- Airplane over the grey wall (f7–12, f34–42): faint dark-grey silhouette, only ~10 grey levels from the
  wall; the visible length drops to 105–135 px, so centres there are ±5–15 px. Frames 7–9 use the faint nose
  end (likely biased ~10–15 px to the left). Prefer board frames 14–33 for speed/size questions.
- The airplane's 141 px length is the real object (crisp pointed nose and rear fold), not motion blur;
  no visible motion blur on either object.
- Cat: whole silhouette visible all frames. Tail tip over the dark board (f~19–30) is low contrast so
  bbox_x0/y0 there may be a few px short; torso columns are unaffected. bbox width varies with the tail/leg
  pose (178–212 px). Frame 0 has a faint semi-transparent ghost in front of the cat's head (rendering
  artefact) that slightly enlarges the f0 bbox/height. Cat "origin" (rig root/pelvis) is not visible;
  torso_cx/cy_dark (body centre) is the best proxy; its per-frame steps carry gait oscillation, so per-frame
  cat speeds are noisy (smooth over a stride, ~8–10 frames, if a question allows).
- Only one cat and one airplane; no other moving objects, no shadows of note, no collisions/contacts
  (the airplane passes ~10–30 px above the cat's tail near f11).
