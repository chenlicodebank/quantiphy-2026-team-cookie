# simulation_0058 – measurement record (pixels and seconds only, no metric scale)

3D Blender render, 2160x1080, 24 fps, 72 frames (t = frame/24). Static camera. Street crossroads:
the main road recedes from the camera to a vanishing point at (1253, 422.5). A cross street runs left–right across the view.
Movers: **yellow taxi**, **white van**, **cyclist**, **pedestrian**. Static: dark **Mercedes** (rear view, near), green
**BMW** (front view, far), traffic lights, lamps, trash bin, planters.
All coordinates are full-frame pixels (x right, y down, origin top-left).

## Files
- `scene.json` – inventory (descriptions, how to tell objects apart, visible frames, static boxes), camera/perspective, events.
- `tracks/taxi.csv`, `van.csv`, `cyclist.csv`, `pedestrian.csv` – final per-frame tracks. Common columns:
  `frame, time_s, ref_x, ref_y, x0, y0, x1, y1, bbox_w, bbox_h, ground_y, ..., occlusion, quality`.
  `ground_y` = image row of the ground contact (tyres / feet). It is the point to use with a ground plane or perspective.
  - taxi extra: `bottom_center_x`, mask centroid/area, `minrect_len/wid` (min-area rectangle of the mask),
    `y1_mask_incl_shadow` (mask bottom including the cast shadow), `paint_*` (box of the yellow paint only).
  - van extra: `rear_edge_row520` (most reliable per-frame position), `front_edge_measured`, `ground_source`.
  - cyclist extra: `template_scale`, `source`.
  - pedestrian extra: mask centroid/area.
- `tracks/_*.csv/json` – raw measurements: `_taxi_raw`, `_ped_raw` (mask stats), `_tm_van` (van window template,
  superseded by `_van_edges`), `_van_edges` (rear/front/roof edge profiles), `_cyc_raw` / `_cyc_upper`
  (cyclist template tracks), `_extra.json` (cyclist mask calibration, van wheel bottoms), `_static.json`
  (static boxes), `_vp.json` (curb lines, vanishing point).
- `background_final.png` – movers removed (temporal mode + manual fill of a taxi ghost on the road at x 570-960, y 596-720).
- `scripts/` – everything: s1-s3 background, s7/s9 van, s10/s11 cyclist, s13 taxi+pedestrian masks, s17 calibrations,
  s18 assembles final tracks, s19 overlay check, s20 static objects, s21 vanishing point, s22 event displacements,
  s4/s5/s6/s8/s14/s15/s16 inspection/debug helpers (s5 = abandoned watershed attempt).

## How measured, and reliability
- **Camera**: phase correlation of a static traffic light against frame 0 → max shift 0.01 px. Camera is static.
  **Frame 1 is an exact duplicate of frame 0.** Every object has zero displacement 0→1, and real motion starts 1→2.
  This matters for any speed at t = 1/24 s.
- **Taxi** (good): foreground = |frame − background| > 22, minus neutral cast shadows on road-grey background.
  The yellow paint (HSV h 12–32, s>40, v>185) gives a convex hull (roof sign → body), and the hull counts as taxi
  (the windows show the white van/sky behind and are not foreground). Added to it: foreground within a margin
  around the hull (bumpers, wheels, mirrors), minus van-white pixels, van brown windows and the cyclist box.
  - Sides and top are accurate to about ±2–3 px. The bottom `y1` = `ground_y` = tyre-contact line: per column, the darkest
    pixel under the paint (the contact shadow), taking the 90th percentile. It is checked visually and with
    profiles (frame 6: contact 670 px, frame 71: 848 px). The raw mask bottom (`y1_mask_incl_shadow`) includes
    the soft ground shadow and is 0–36 px lower: do not use it for height.
  - Frame-to-frame noise of the box centre is ±3–5 px; frames 19–22 and 32 jump by a few px where the box edge
    changes from mask detail. `mask_cx/cy` are smoother for motion.
  - Pixel length/width depend on the viewing angle: the taxi turns from side view (length 468–493 px, frames 0–12)
    to head-on (width 228 px at frame 44) and grows as it approaches (393 px wide, 263 px tall at frame 71).
    A "taxi length" prior is best matched to its side-view box (frames 0–~12). A width prior is best matched to the
    head-on box (frames ~44–71), where the box width ≈ car width plus mirrors.
- **Van** (position good, extents fair): it is white against a white sky/sidewalk and its lower half is behind
  the taxi for frames 0–47, so masks are unreliable.
  - Position = rear body edge on image row 520: the half-contrast crossing (diff ≥ 30) scanning right, sub-pixel.
    It is clean in all frames except 28–30, where the rear passes behind the static pedestrian-signal box: those
    are linearly interpolated (quality 'fair').
  - `x0` = rear edge − 7 px (rear bumper protrudes ~7 px, measured at frame 60).
  - `x1` = `x0` + length. Length was measured directly in frames 0–6 (front at row 560 + 8 px), 36–46 and 66–71
    (front bumper at row 600). Elsewhere it is linearly interpolated (`front_edge_measured` = no).
  - Measured lengths: 459 px (frames 0–6), 447–451 px (36–46), 462 → 479 px (66 → 71). The apparent length is
    larger far from the image centre (perspective), and at the right end part of the front face is visible.
  - `y0` = roof row from column profiles (471–477 px). `ground_y` = wheel bottom measured in frames 48–53 and
    66–71 (640–646 px); elsewhere roof + 169 px (median measured height).
  - The window-template track (`_tm_van.csv`) is wrong by up to 20–40 px in frames 19–28 and 68–71 (occlusion).
    Do not use it.
- **Cyclist** (good):
  - Masked colour template (TM_SQDIFF, rider+bike, frame 33) gives frames 12–71. An upper-body template is used
    for frames 0–11, where only head and torso show above the taxi, shifted to the full-template centre
    (frames 0–2 'poor', 3–11 'fair').
  - Image speed is very steady (17.2 → 18.6 px/frame from frame ~4). y is constant.
  - The box is the template box inset by a calibration from real masks in frames 29–38. The rider+bike extent is
    135 px long (tyre to tyre) × 138 px tall (head top to tyre contact). It is assumed constant (template scale
    ≈ 1.00 all clip), so the per-frame extents are not independent measurements.
- **Pedestrian** (good until frame 21, then cut by the image edge):
  - Mask = foreground in x < 300 minus taxi/van, components merged near the largest.
  - Feet bottom `y1` and head top `y0` are reliable from frame 3 (frame 2 misses the feet). Height 232 px at
    frame 0, 237–241 px at frames 4–16, 247–253 px at frames 20–32: he walks slightly towards the camera, and
    the height oscillates by about ±3 px with the gait.
  - The lamp post hides part of the body (arm/back) in frames ~0–13, so width is underestimated there.
  - From frame 22 `x0` = 0 (cut by the frame edge), so `ref_x`/width are biased right. `ref_y` = y1 − 0.47·height
    is an estimate of the pelvis row, not a measurement.
- **Static objects** (good, ±2 px): local-background thresholding in hand-placed boxes (s20).
  - Mercedes tyre contact y = 826 and BMW y = 589 are from brightness profiles (the mask boxes include shadow,
    to 857 / 591).
- **Perspective** (good):
  - Main-road curb lines are fitted on rows 450–580 (left curb rows 485–522 skipped: the BMW interrupts it).
    Vanishing point (1253.1, 422.5) = horizon row. Principal point assumed at the image centre (1080, 540).
  - Cross-street curbs are near-horizontal (rows 594–608), so the van and cyclist move along an almost
    constant-depth line, nearly parallel to the image x axis, and their pixel size barely changes (cyclist
    constant; van 447–479 px, mainly from off-axis perspective).
  - Taxi and pedestrian change depth: the taxi approaches strongly (height 118 → 263 px), the pedestrian slightly.

## Ambiguities / cautions
- The **reference point** for the simulation origin is approximated by the box centre (vehicles, cyclist) or an
  estimated pelvis (pedestrian). A vehicle root may sit at ground level: use `ground_y`/`bottom_center_x` if
  needed. For the taxi, the box centre moves relative to the car body as it turns, a few-px systematic effect in
  frames ~18–44.
- Depth ordering (image overlaps only, no physical contacts): taxi in front of the van and cyclist; cyclist in
  front of the van; Mercedes in front of the van's and cyclist's wheels; van and cyclist in front of the BMW.
- Shadows: soft ground shadows under all vehicles (light from behind/above). Masks of the taxi include them
  except at the bottom row definition above.
- No motion blur problems. Video compression gives faint halos around static poles when a mover passes behind;
  they were filtered (thin spikes ignored).
- Similar objects: two white-ish cars could be confused with the van only at a glance. The van is the only white
  vehicle, the taxi the only yellow one, the Mercedes the only dark car, and the BMW is far and green. There is
  only one pedestrian and one cyclist.
