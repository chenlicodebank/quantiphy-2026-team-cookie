# captured_0006s – measurement record (pixels, seconds; no metric scale)

Lab recording (Orbbec, 24 fps, 49 frames, 1280x720; per task f = 763 px, principal point ~(640,360)),
**segmented**: the real background and the thrower's hand/body were replaced by a static blue gradient
("Modified with Segment Anything 2 Demo" watermark, bottom-right, x>1020, y>685). Only two things remain:
a **yellow fruit** (the only moving object; elongated mango/lemon-like, a small green-ish stem/tip shows in frames 46-47)
and a **wooden table** (brown top, dark single central leg). t = frame/24.

## Story / events (scene.json "events")
- f0–18: fruit held (hand invisible) high above the table, centre ~(613, 221→237): nearly still, slow downward wind-up drift (~16 px).
- f19 (t=0.792 s): throw starts, the fruit moves up (±1 frame).
- f25 (t=1.042 s): highest point in the image (ref_y 137.6).
- It flies toward the camera: its apparent size grows ~1.6x by f28 and ~2.5x by the end.
- f32 (t=1.333 s): first impact on the table top (mask bottom y≈485). f33–35: small rebound with a shadow under it.
  f36–42: on the table near the front-left, rolling/sliding left.
- f43 (t=1.792 s): goes over the front-left corner (x<390) and falls. f46: reaches the bottom border. f48: out of frame.

## Files
- `scene.json`: inventory, table geometry, camera, events, apparent-size summary.
- `tracks/fruit.csv`: one row per frame (0–48). `ref_x, ref_y` = centroid of the filled mask (the visible centre, which
  is the lab convention). Also: bbox (`bx0..by1`, `bbox_w/h`, `bbox_cx/cy`), min-area-rect `len_major`, `wid_minor`,
  `major_angle_deg`, `area_px`, `eq_diam` (= diameter of a circle with the same area), `occluded`, `phase`, `flags`.
- `tracks/fruit_auto.csv`: the raw output of the automatic tracker (same numbers, no flags).
- `scripts/track2.py`: tracker = difference from the median background (`frames/bg.png`) plus a chroma test, table-shadow
  rejection (a uniformly darkened copy of the table is dropped), closing, hole filling, largest blob. Writes overlays
  `frames/ov2_*.png` and `frames/ov2_sheet.png`. I checked every frame's overlay by eye.
- `scripts/table.py`: table geometry and the per-frame camera-stability check. `scripts/view.py`: crop viewer.
  `scripts/finalize.py`: builds fruit.csv and scene.json. (`scripts/track.py` is the first, superseded tracker.)

## Reliability
- Camera: **static**. The table edges are identical to the pixel in all 49 frames.
- In the air (f0–31) centroids are good to ~1–2 px. The fruit's interior is drawn semi-transparent by the segmentation
  (often only a yellow rim is visible). The mask fills the outline, and the overlays confirm it covers the whole fruit.
- Motion blur: f29–31 and f44–46 are smeared along the fall direction (vertical), so `len_major`/`bbox_h` are inflated.
  Use `wid_minor` (≈71–74 px at f29–31) as the size there. The centroid is still the blur centre.
- On the table (f32–43) the bottom of the fruit is translucent and sits on its own shadow. The mask bottom is
  uncertain by about ±8 px (checked by hand at f32–35: auto bbox within ~10 px of the visible outline; f32 visible
  bottom ≈485 vs auto 475). The image y here partly reflects depth along the table top, not height.
- f46–47: cut off by the bottom border (by1 = 719), so the centre and size are truncated (occluded = 1).
- Shape is elongated, so the major and minor lengths depend on orientation, which tumbles. For a size reference use
  the held frames (f0–18: major ≈47, minor ≈42.5, eq_diam ≈46 px) or a frame with matching depth.

## Apparent size vs time (depth cue)
eq_diam ≈ 46 px (f0–18) → 58 (f24) → 64 (f26) → 78 (f28) → minor ≈72 (f29–31, blurred) → 80–100 on the table
(f33–42) → 108–121 while falling off (f43–44). The fruit gets much closer to the camera (roughly 2.5x nearer than where
it was held). Depth must come from the given depth_info. A rough pinhole check is Z ≈ 763·D/size_px.

## Table (static, from the median background)
Top back edge y = 434, x 513–816 (304 px). Top front edge y ≈ 514, x 390–976 (587 px). Front band y 515–541
(27 px thick). Leg x 672–715 (44 px wide) from y 542 down to the image border (cut off). The side edges converge at
about (645, 348), close to the principal point: the camera is a little above the table-top plane and looks roughly
horizontally, square to the front edge. Overall bbox [389, 434, 977, 719].

## Ambiguities
- The fruit type is not certain (yellow, elongated, with a stem; it looks like a mango or yellow pepper rather than
  a ball). The interior "ghost" and the missing hand are segmentation artefacts.
- Release frame ±1 (f19–20). The f22 mask is briefly rounder and larger than its neighbours.
