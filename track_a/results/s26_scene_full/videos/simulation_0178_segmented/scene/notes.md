# simulation_0178_segmented: measurement record

**Scene.** A 2D segmentation clip: 24 fps, 60 frames (t = 0 to 2.458 s), 1920x1080. The background is pure white. Two elephants walk to the right in side view along a common ground line at y ≈ 694 px:
- **adult_elephant**: the larger one, on the right and in front. It has a light-grey patch on its ear.
- **calf_elephant**: the smaller one, on the left, following the adult.

Both are visible and unoccluded in every frame, and they never touch. There are no static objects, ground markings or props. The camera is assumed static. It can't be checked against a background, but the feet stay at y 690–695 throughout.

## Files
- `scene.json`: inventory, size summaries, camera notes, pair separation and events.
- `tracks/adult.csv`, `tracks/calf.csv`: one row per frame (0–59). Columns:
  - `frame`, `t`.
  - `ref_x`, `ref_y`: bbox centre.
  - `cx`, `cy`: mask centroid.
  - `bbox_x0..y1`: bounding box.
  - `length_px`: bbox width, tail tip to trunk tip.
  - `height_px` (= `width_px` in this side view): feet to top of back.
  - `area_px`.
  - `body_span_at_cy_px`, `body_x0_at_cy`, `body_x1_at_cy`: horizontal mask span on the centroid row, i.e. rump to front of head/ear, excluding the tail and the trunk tip.
  - `gap_to_other_px`: empty columns between the two masks.
  - `occluded`: always 0.
- `scripts/track.py` builds the tracks. `scripts/overlay.py` draws the check image `frames/overlay.png` for frames 0, 30 and 59. `scripts/probe.py` was a first look at the threshold.

## Method
- **Mask:** pixels whose darkest RGB channel is more than 25 below white. Specks under 30 px are dropped. The thresholds 10, 25 and 40 give nearly identical extents.
- **Splitting the two animals:** at the widest empty column gap, which is always 37–97 px.
- **Check:** the overlays show the boxes cover each animal fully (tail, trunk, feet, and the pale ear patch is included).

## Reference point
The simulation origin (the rig root, roughly at the body centre or pelvis) can't be seen directly. I recorded both the mask centroid and the bbox centre.
- Their per-frame x steps agree on average: adult 7.06 / 7.08 px per frame; calf 6.12 / 5.97 px per frame.
- Single-frame steps jitter by ±1–2 px because the legs swing. For speeds, use differences over many frames or a linear fit.

## Motion and sizes
- **Motion:** both walk steadily to the right with no starts, stops, turns or contacts.
  - Adult: +416 px over 59 frames, about 7.06 px/frame (169 px/s).
  - Calf: +361 px, about 6.12 px/frame (147 px/s).
  - So the gap between them grows from 37 to 97 px. Centroid separation goes from 346 px (frame 0) to 401 px (frame 59).
  - Vertical bob of the centroid: about 8 px (adult) and 7 px (calf).
- **Sizes (median, with the range over the walk cycle):**

  | | Adult | Calf |
  |---|---|---|
  | Length (tail to trunk) | 404 (371–424) | 262 (229–283) |
  | Height | 228 (220–233) | 153 (148–158) |
  | Body span (rump to head) | 310 | 213 |

## Reliability and ambiguities
- **Length** changes with the swing of the tail and trunk. Medians are the most robust value. Use the max/min if a question asks for those.
- **Height** is stable to ±3%.
- **Calf's tail:** in some frames it is thin or hangs against the legs, so calf length is less certain (about ±10 px).
- **Scale:** this is a 2D scene, so use one scale (m/px) for both animals, derived from whichever prior is given.
- **Ear patch:** the adult's pale ear patch is part of the animal, not a separate object.
