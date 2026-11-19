# simulation_0243 — measurement record

Video: Blender render, 2D scene, 1080x1920 portrait, 30 fps, 75 frames (t = frame/30, 0 … 2.4667 s).
Units: full-resolution pixels; y increases downward. No metric scale has been assumed.

## Scene
One moving object: a horse-like **creature** (unicorn/kirin type: tan-grey body, pale blue-white chest and
face, a big curled grey mane-crest sweeping back over the neck, small horn/ears, long thin tail). It faces
right and **walks to the right (+x)** across an asphalt road, in front of roadside bushes, with tall pines at
both edges and a snowy mountain peak in the far background. No other animals, people, vehicles or props.
It is fully in frame and unoccluded in all 75 frames.

**Camera: static.** Phase correlation of the upper image (rows 0–1000) frame 0 vs 74 gives a shift of
(−0.005, +0.003) px (response 0.99). Background pixels do not change apart from noise.

**Geometry**: the road recedes to a vanishing area near (530, 1400). The creature walks across the road at
constant depth: its hoof line stays at y ≈ 1547 (±1–3 px) and its height stays 413–428 px all clip, so
there is no visible change in apparent size. The motion is a fronto-parallel horizontal translation, which
fits the 2D-scene label. One px/m scale from the prior should be valid for the creature.

## Files
- `scene.json`: inventory, camera, static objects (approximate pixel positions/extents), size summary,
  events, net displacement / path length in px.
- `tracks/creature.csv`: one row per frame (0–74). Columns:
  - `ref_x, ref_y`: **recommended reference point** (proxy for the body origin). ref_x = chest_front_x − 129 px
    (129 = median offset between the chest front and the mask centroid), ref_y = mask centroid y.
  - `cx_mask, cy_mask`: centroid of the full silhouette, including legs, tail and mane.
  - `chest_front_x`: median right edge of the trunk over rows 1290–1400. This is the smoothest feature
    (per-frame step 6.5 ± 0.9 px).
  - `rump_x`: median left edge of the trunk over the same rows (the tail base adds ±5 px noise).
    `nose_x` = bbox_x1 = tip of the muzzle.
  - bbox (x0,y0,x1,y1,w,h): full silhouette, including tail, mane top and hooves.
  - `body_len_nose_rump` = nose_x − rump_x (tail left out), `height_top_to_hoof` = bbox_h (top of the
    mane/horn to the hoof bottom), `trunk_len_band` = chest front to rump, `mask_len_main / mask_width_across`
    = PCA extents of the silhouette (tail included), `area_px`, `occluded` (always 0).
- `tracks/creature_raw.csv`: the raw measurement columns, including a "torso" blob from a 61-px morphological
  opening. That blob is noisy (it jumps when legs merge into it), so do not use it for motion.
- `bg_plate.png`: a clean background built from frame 0, with the creature's frame-0 area filled from frame 74.
- `scripts/`: background.py (plate + camera check), track.py (segmentation + raw track + overlays),
  analyse.py, finalize.py (final csv + json), zoom.py / grid_bg.py / check_overlay.py (visual checks), explore.py.

## Method
Each frame is differenced against the clean plate (Gaussian 5x5, threshold 30 on the summed |BGR| difference).
Rows below 1552 are cut off: they hold wet-road reflections and puddles. Thin horizontal contact-shadow lines
(≤ 10 px tall) near the ground are removed, the remaining pieces are combined with the main blob, and holes
are filled. I drew the overlays on frames 0, 10, 20, 30, 37, 45, 55, 65 and 74 and looked at them. The mask
covers the body, head, mane, tail and legs, and the reference path is a flat horizontal line through the trunk.

## Key numbers (px)
- ref point: (353.0, 1319.1) at frame 0 → (834.0, 1317.7) at frame 74. Net displacement 481 px, about
  6.5 px/frame on average. Motion is steady and walking-paced; there is no start or stop inside the clip.
- Path length: 481 px along x. Summing the 2D steps of (ref_x, ref_y) gives 497 px, but the extra 16 px is
  mostly ±1.7 px vertical centroid jitter, not real motion. So path length ≈ net displacement, because the
  motion is a straight line.
- Height (top of mane/horn to hoof): median 423 px (413–428). The highest point is the mane-crest or horn tip,
  not the head, because the curled mane rises above the head.
- Nose-to-rump length: median 344 (323–357). Full bbox width including tail: median 487 (409–519).
  Trunk (chest to rump): 270.
- Per-frame noise: chest_front_x ±0.9 px/frame; ref_y ±1.7; nose_x ±3 (head bobs); bbox_x0 ±9 (the tail swings).

## Events
- Frame 0 (t = 0): already walking right. Frame 74 (t = 2.467 s): still walking right.
- No bounces, impacts, contacts with other objects or direction changes. Hoof contacts follow the normal walk
  cycle and were not timed.

## Static objects (frame-0 plate, approximate ±10–20 px)
- Left pine: top (120, 365), trunk at x ≈ 80, visible down to y ≈ 1360.
- Right pine: top (1000, 410), canopy x 620–1080.
- Snowy mountain: peak (555, 605), base y ≈ 1400.
- White road centre line: from (665, 1480) to (420, 1920).
- Curved yellow line: (440, 1440)–(400, 1530).
- Bushes behind the creature: left x 0–370, y 1300–1560; right x 620–1080, y 1270–1540.
- Puddles: left foreground (0–500, 1720–1850), right (620–1080, 1660–1720), small centre (600–720, 1475–1500).

## Reliability and ambiguities
- The true rig origin (likely the pelvis or hips) is not visible. ref_x is a trunk-fixed point at the mask
  centroid, so it tracks the origin's horizontal motion to within about 1 px/frame. Its absolute position may be
  off from the true origin by a few tens of px; this does not matter for speeds or displacements.
- The tail and the far hind leg are low-contrast against the road and trees, so their mask parts are sometimes
  incomplete (e.g. the far hind leg near x 770 at frame 74). The bbox left edge and bbox_w are therefore the
  least reliable sizes.
- The wet road shows reflections and a contact shadow under the hooves. These were excluded. The hoof bottom
  is measured at about y 1547.
