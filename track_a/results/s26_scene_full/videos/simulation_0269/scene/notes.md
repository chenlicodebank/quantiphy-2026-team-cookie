# simulation_0269 — measurement record

2D simulation (Blender), 2560x1440, 24 fps, 72 frames (t = frame/24, frame 0 at t = 0). All values are pixels / frames; no metric scale is assumed.

## Scene
- **Camera**: static. The background is a plain light-grey backdrop with a fixed radial vignette (grey 203–224); there is no texture and nothing moves except the bird and its shadow.
- **bird** (the only real object): a phoenix/peacock-like bird with a green body, purple/red/orange wing feathers, orange peacock-eye tail fan and a red beak tip. It is seen face-on to the motion plane, from above or below. The head points to image −x (left), the wings spread along image y, and the tail fans out to the right. It flies **leftward, almost exactly horizontally**, from beak x = 1484 (frame 0) to 432 (frame 71): net −1052 px, with beak y staying in 712–720. It is never occluded and never touches the image edge.
- **bird_shadow**: a dark-grey flat silhouette on the backdrop, up-left of the bird and partly hidden behind it. It is a shadow, not an object; do not confuse it with a second bird.
- No ground, markings, furniture or other props.

## Files
- `scene.json`: inventory, camera, size summary, events and the recommended reference point.
- `tracks/bird.csv`: one row for each of the 72 frames.
  - `beak_x, beak_y`: the leftmost colour-mask pixel, i.e. the beak tip. **Recommended reference point for motion.**
  - `axis_y`: the body axis row (median y of the mask within 40 px of the beak).
  - `body_est_x/y`: a rough guess at the body/rig origin, = beak + 130 px.
  - `torso_col_maxmask_x`: the column where the mask is densest. Noisy, because the wings change it; don't use it for motion.
  - `bbox_*`, `bbox_cx/cy`, `centroid_x/y`: bounding box, its centre and the mask centroid. These shift with wing and tail pose, so they are poor for speeds.
  - `length_x_px`: bbox x-extent, beak to tail tip.
  - `height_y_px`: bbox y-extent, which is the wingspan when the wings are spread.
  - `above_axis_px` / `below_axis_px`: the part of the mask above and below the body axis.
  - `pca_*`: principal-axis extents of the mask.
  - `area_px`, `occluded` (always 0), `cut_by_edge` (always 0).
- `tracks/bird_shadow.csv`: centroid and bbox of the *visible* part of the shadow.
- `scripts/`:
  - `common.py`: frame decoding.
  - `seg.py`: segmentation.
  - `track.py`: builds the CSVs.
  - `make_scene_json.py`: builds `scene.json`.
  - `viz_masks.py` / `viz_tracks.py`: draw overlays for checking.
  - `head_track.py`: a template-matching head tracker that I tried and **rejected** (match scores fell to 0.4–0.7 and it jumped by up to 30 px). Its output is not in the record.
  - `probe.py` / `inspect_tracks.py`: diagnostics.

## Method
- **Bird mask**: pixels with chroma (max−min RGB) > 18, closed with a 7x7 kernel, keeping components of at least 40 px.
- **Shadow mask**: neutral pixels more than 15 grey levels darker than a quadratic fit of the backdrop vignette.
- **Checks**: I drew the overlays on frames 0, 9, 47 and 71 and looked at them. The box covers the beak tip, both wing tips and the tail fan. The beak track lies on the beak in every frame.

## Key numbers (px)
- **Beak step per frame** (leftward):
  - frames 2–6: ~4–6
  - frames 7–24: ~6
  - frames 25–29: rising to ~16
  - frames 30–49: ~16
  - frames 50–71: ~20–30
- **Speed is not uniform**: the step changes with the flap phase.
- **Beak path length** over frames 0→71: 1055 px.
- **Body length (beak to tail tip)**:
  - median 438 px, range 396–450.
  - Dips (~400–420) at frames 10–11, 36 and 61, when the tail fan compresses.
  - The faint grey tip of the long central tail spike is partly missed by the colour mask (by up to ~10–60 px), so treat the length as about ±10 px.
- **Vertical extent (wingspan)**:
  - Maxima at frames 10 (544), 21 (624), 35 (540), 46 (630) and 60 (542); frame 71 is also high (626) and is the last frame.
  - The two kinds of maxima alternate, ~540 and ~628, probably the up-stroke and down-stroke spread.
  - **Max wingspan ≈ 630 px** (frame 46).
  - **Minimum y-extent ≈ 238 px** (frames 12, 37 and 62, wings folded).
  - Frame 0: 274 px.
- **Flap period**: about 25 frames.

## Events
- Frames 0 and 1 are identical. The beak first moves at frame 2 (t = 0.083 s).
- Wing-spread maxima and minima are listed above.
- There is no contact, bounce or reversal. The bird is still moving left in the last frame.

## Reliability and ambiguities
- **Pixel quantisation**: edges move in 2 px steps, because the render was upsampled about 2x. Per-frame beak steps therefore carry about ±2 px of error, so prefer differences over several frames.
- **Unknown origin offset**: the rig origin is probably at the body, not the beak. Distances and speeds of the origin should match the beak's apart from head bob, which is ±4 px in y and possibly a small fore-aft flex.
- **Mask holes**: a few greyish feathers inside the wings are misclassified as shadow. This does not affect the extents.
