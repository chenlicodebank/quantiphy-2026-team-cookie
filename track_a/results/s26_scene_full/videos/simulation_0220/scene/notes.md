# simulation_0220 – measurement record

Video: 1920x1080, 24 fps, 50 frames (t = 0 … 2.0417 s), Blender simulation, **2D** scene.
Static camera. One moving object: a grey cartoon **robot** with a big dome (mushroom) head walking
right-to-left in front of a hall wall (pillars, window slats, curtains, ceiling lights) on a dark floor
with two white horizontal stripes and two white diagonal markings. All values are pixels / seconds.

## Files
- `scene.json` – inventory (robot + static features with pixel extents), camera, events, size ranges.
- `tracks/robot.csv` – one row per frame (0-49):
  - `ref_x, ref_y` – centre of the robot's dark belly disk (torso landmark near the pelvis). `ref_source`
    = measured / interpolated (arm covers the disk: frames 9-13, 27-29) / extrapolated (frames 47-49, linear
    fit of frames 38-46). `occluded`=1 for those rows. `ref_match_score` = NCC template score.
  - `mask_cx, mask_cy` – centroid of the segmented body mask (head partly missing in the mask, so mask_cy is low-biased toward the body).
  - `bbox_x0..y1` – full-extent box (top = dome top from edge detection; bottom = foot bottom).
    `length_px` = horizontal extent (walk direction, includes swinging arms/feet), `height_px` = dome top
    to foot bottom. `head_top_y`, `foot_bottom_y`, `mask_area_px`.
- `scripts/`: `seg.py` (background subtraction mask, bbox), `headtop.py` (dome top via gradient edges),
  `disk3.py` (belly-disk NCC tracking; `disk.py`, `disk2.py` were failed attempts), `static.py` (static
  features), `strip.py` (visual check montages), `assemble.py` (writes the CSV). Scratch outputs are in `../frames/`.

## Method
Background = frame 0 for x<1470 and frame 49 for x≥1470 (robot absent there in those frames); camera
static (top-region diff ≤0.42 grey levels). Body mask: |diff|>18 + morphology. The dome head is almost the
same grey as the wall, so its top was found from vertical-gradient edges not present in the background
(checked visually, ±1-2 px). Belly-disk centre by template matching to the frame-0 disk; checked on
overlays (frames/disk3.png, frames/final.png).

## Key numbers
- Ref point x: 1612.3 (f0) → 1193.6 (f49, extrapolated), ≈ −8.5 px/frame (≈205 px/s), steady; per-frame
  steps 7.5-12.7 px because the torso sways with the gait. Mask-centroid x: 1605.2 → 1190.8.
  Vertical: ref_y oscillates 843-864 (bob with gait, period ≈ 19-20 frames for two steps).
- Height (dome top → foot bottom): 297-321 px, frame 0 = 310, median 307; max at mid-stance (f 9-13, 47-49).
- Length along walk direction: 121-224 px (arm/leg swing). Head dome ≈ 122 px wide, ≈ 79 px tall.
- Floor stripes y 841-845 and 905-910; pillars x 642-716 (74 px) and 1572-1654 (82 px), wall base y≈818-825.

## Reliability / ambiguity
- No visible pelvis marker: the belly disk is ~20-30 px above the probable hip/pelvis origin; horizontal
  displacement/speed are equally valid from it, but per-frame values include torso sway (±2-4 px). For
  average speed use long baselines (e.g. measured frames 0→46: 1612.3→1219.6 = 392.7 px in 46 frames).
- Interpolated/extrapolated ref rows (occluded=1) are ±3-5 px.
- Head top is low-contrast (±2 px); bbox width depends on arm swing and is not a rigid size.
- The robot is already walking at frame 0 and still walking at frame 49; no start/stop, bounce or contact
  with other objects. Shadows are faint under the feet and not included in the mask.
