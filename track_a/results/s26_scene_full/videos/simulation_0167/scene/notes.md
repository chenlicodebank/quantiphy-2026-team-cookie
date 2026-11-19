# simulation_0167 – measurement record

**Scene:** a Blender render (2D) seen from a static camera looking straight down on a street, 1920x1080, 24 fps,
80 frames (t = frame/24). A **white police car** with a flashing blue roof lightbar drives along +x in the lower lane
(between the yellow centre line at y≈544 and the white edge line at y≈739). It follows a **cyclist** (delivery rider:
pale-blue helmet with an orange stripe, green box backpack, yellow front crate) who is riding ahead of it in the same lane, also along +x.
Both are visible and moving in every frame. Nothing else moves. All values are in pixels and seconds; no metric scale is assumed.

## Files
- `scene.json` – inventory, sizes, static features, events, camera.
- `tracks/police_car.csv` – **final car track**: `x,y` = centre of the bumper-to-bumper/side-to-side box (vehicle root
  approximation); `bbox_*` = template box (289 x 120 px incl. mirrors) at the tracked position; `mask_*` = per-frame
  background-difference mask extents; `mask_extent_reliable` = 0 where the mask is polluted (lamp post early, cyclist at the end);
  `occluded` = lamp-post head over the car edge (frames 0-16, minor); `track_source` = which sub-templates were used.
  `mask_body_width_px` is underestimated (threshold artefact). Use 111-115 px for the body width.
- `tracks/cyclist.csv` – **final cyclist track**: `x,y` = pelvis estimate (see below); `x_mask_centroid,y_mask_centroid`,
  `bbox_*`, `mask_length_px`, `mask_width_px` = shadow-suppressed difference mask (the thin dark rear tyre is often missed,
  so the bbox can be ~10-20 px short at the rear); `gap_car_front_to_cyclist_bbox_px` uses that mask bbox, so it overstates the true bumper-to-tyre gap.
- Intermediates: `*_raw.csv` (masks, from `track.py`), `*_tm.csv` (fixed-template matching, from `track2.py`; the
  cyclist one slides along the rider, so don't use it for positions), `cyclist_chain.csv` (source of the final cyclist x,y),
  `cyclist_helmet.csv` (helmet-colour attempt; mostly NaN in shaded road, not used).
- `scripts/`: `bg.py` (median background + camera-shift check), `track2.py` (car template tracking), `track.py`
  (masks), `cyc_chain.py` (cyclist chained tracking), `gap.py` (bumper-tyre gap, body width), `static.py` (road
  markings), `build.py` (merge + overlay + events), `cyc_strip.py`/`check_cyc.py` (visual checks), `helmet.py`.
  Run order: bg → track2 → track → cyc_chain → build (bg.py writes its cache to `frames/`, outside the record).

## How it was measured, and how reliable it is
- **Camera:** static (phase-correlation shift < 0.011 px). It looks straight down with a perspective lens, so tall parts are pushed
  radially away from the image centre. The car's roof features move about 16 px relative to its bumper/bonnet features
  between the left and right of the image (−0.22 px/frame). The reference points average roof and bumper features, so the
  bias is ≲ 4 px. The road plane is parallel to the image, so a single px scale applies along the lane.
- **Police car:** sub-pixel template matching on gradient-magnitude images, using a rear and a front sub-template from
  frame 40. The middle (lightbar plus blue glow) is excluded because the flashing light breaks intensity matching. Frames where one
  sub-template failed (front: 0-2, 8, 10-12, 78, 79, where the lamp post or the cyclist was in the window; rear: 32) use the other one plus
  the fitted offset. Result: straight motion at y=639.0, dx = 18.04 px/frame (per-frame scatter ±0.15, linear-fit
  residual 0.27 px), constant over the whole clip. **High reliability.** Size: bumper to bumper 289 px (mask 286-290
  in clean frames), 120-121 px wide including the side mirrors, body ≈111-115 px. The blue glow on the asphalt is not part of the car
  and was removed from the masks.
- **Cyclist:** a pelvis point was picked at frame 40 (1272, 645), on the rear half of the green backpack above the saddle,
  then tracked frame to frame by template matching (forward and backward from frame 40). Visual checks at frames 0, 20, 40, 60, 70 and 79
  keep it on the same spot within ~3-5 px. A chain started at frame 0 differs by ≤4 px from the anchored chain, so drift is small.
  Mean 14.42 px/frame (linear fit, residual 1.1 px). The per-frame dx genuinely oscillates between 13.0 and 15.8 with a
  ~10-frame period (pedalling surge), and y sways ±2.5 px with a ~19-frame period. For speed questions, average over
  several frames or fit. The absolute pelvis location is uncertain by ~±8 px along x, because the pelvis is hidden under the
  backpack. Size: ~105-110 px from rear-tyre tip to front crate and ~42-48 px wide. Height is not observable from above.
- **Distances:** the car-to-cyclist reference-point distance is 471.6 px (f0), 325.5 (f40) and 185.4 (f79), closing at ≈3.6
  px/frame. The bumper-to-rear-tyre gap is about 10-15 px at frame 79 (row-profile measurement). There is no contact in the clip.
- **Events:** neither object starts, stops, turns or bounces; both move from frame 0 to frame 79. The transverse white line at x≈1181
  is crossed by the cyclist's front at f≈28.7 and its pelvis point at f≈33.7, then by the car's front at f≈45.0, centre at
  f≈53.0 and rear at f≈61.0. The car centre passes the image centre (x=960) at f≈40.8 and the cyclist at f≈18.1.
- **Static features (scale candidates):** lane width 194.5 px between line centres (yellow y 544.5 → white y 739);
  centre-line dashes ~18 px long on a ~47 px period; the remaining features are listed in scene.json.
  Lamp-post and fence positions are approximate (read off a 100-px grid) and are only given for orientation.

## Ambiguities
- The flashing blue light changes the car's appearance from frame to frame. The glow halo is not part of the car's size.
- The cyclist's shadow falls to the lower-left. It was suppressed in the masks but may still trim or extend the bbox by a few px.
- A prior given as the "car length" most likely corresponds to the 289 px bumper-to-bumper value. A "car width" prior probably
  corresponds to the body width (≈111-115 px) or, if mirrors are included, 120 px.
- The top-down view hides heights. Any "height" prior can only be used through its world value, not through pixels.
