# simulation_0114 — measurement record (pixels, seconds)

Video: 1080x1920 portrait, 80 frames, fps 24.002401, simulation (Blender), **2D** scene. t = frame / fps.
Scene: top-down view of a snowy mountain slope (static photo-like backdrop). One moving object: a **yellow
aeroplane** (seen from above: straight main wing, small tail stabiliser at the top, nose pointing down the image).
It starts at rest at frame 0 near the top (ref ≈ (671, 160.5) px) and moves **straight down the image (+y)**,
speeding up steadily the whole clip. Its nose reaches the bottom edge at frame 76, only the tail shows at frame 77,
and it has gone from frame 78 on. There is no turning, bounce or other moving object.

## Files
- `scene.json`: inventory, rest sizes, events, camera.
- `tracks/plane.csv`: one row per frame from 0 to 77. Columns:
  - `ref_x, ref_y`: **recommended origin**. This is the blur-corrected bbox centre: `ref_y = wing_y - 18.0`, where
    18.0 px is the offset from the wing row to the bbox centre at frame 0, before any blur. `ref_x = cx_bbox`.
    Frame 77 has no ref (plane mostly out of frame).
  - `cx_bbox, cy_bbox`: centre of the HSV yellow-mask bbox. `bbox_*`: that mask's box. The mask loses the faint
    blurred tail in later frames, so cy_bbox is biased by a few px. Prefer ref_y.
  - `cx_diff, cy_diff`: centroid weighted by the background difference (background = frame 79, the empty scene).
    It does not depend on blur, but it is the visible mass centroid, about 7 px below the bbox centre.
  - `wing_y`: mean row of the main wing bar (mask rows ≥100 px wide). `tail_y`: the tail stabiliser row (NaN after
    frame 51, where the blurred tail falls below the colour threshold).
  - `lowthr_*`: box of the background-difference blob, which includes the blur smear.
  - `wingspan_rest_px` = 168, `length_rest_px` = 108 (constants measured at frame 0); `occluded_or_cut` = 1 at frames 76–77.
- `tracks/camera_shift.csv`: background shift per frame from phase correlation. It is ≤0.1 px throughout, so the
  **camera is static**.
- `scripts/`: probe.py, track.py (HSV mask, camera shift), track2.py (difference centroid, wing/tail rows,
  low-threshold box), finalize.py (ref columns, scene.json, overlay), overlay.py and diffview.py (visual checks).

## Plane size (pixels, frame 0, sharp)
- Wingspan (image x): **168 px** (bbox x 587–755). Nose-to-tail length (image y): **108 px** (y 106–214).
- Tail stabiliser span is about 92 px. The wing bar is about 24 px thick (y ≈ 166–190).
- Later frames: the width stays at 168 px. The height of the background-difference box grows with motion blur (about
  112 px at frames 70–75), and the yellow mask height shrinks (98–104 px) because the blurred tail fades. Use the
  frame-0 values for size. In a 2D scene the apparent size should not change, and the measured width confirms that.

## Motion facts (raw, no model fitted for the record)
- x stays at 671 ± 1.5 px (the difference centroid wanders by ±4 px because of blur and background, which is noise).
- Per-frame Δref_y (px) rises roughly linearly, from 0 at frames 0–1 to about 44–45 at frames 74–76. Values are
  quantised to 0.5 px. A quadratic fit over frames 2–40 puts zero velocity at frame −0.04, which means it starts
  from rest at frame 0. This looks like uniform acceleration, but answering sessions should fit it themselves.
- Positions: ref_y = 160.5 at frame 0, 430.5 at frame 30, 1235.5 at frame 60, 1840.5 at frame 75.

## Events
- Motion start (from rest): frame 0, t = 0.
- Nose touches the bottom edge: frame 76 (t = 3.166 s). At frame 77 only the tail is visible, and from frame 78
  (t = 3.250 s) the plane is out of frame.

## Static objects (approximate boxes, x0 y0 x1 y1 px)
- Large dark rock outcrop at top-centre: [516, 220, 840, 550]. The plane flies over it at frames 0–35.
- Small dark rock spire on the right: [860, 570, 980, 770].
- Blue crevasses at lower left/centre: [170, 1640, 680, 1920].
- Bright snow cornice edge running diagonally across the middle (y ≈ 960–1000 at left).
- Pale grey angular backdrop at the top, y < ~200.
These are only scenery and are not measured precisely.

## Reliability / ambiguities
- ref_y is good to about ±1 px. The 18 px offset from the wing row assumes the plane's origin is its bbox centre; the
  true Blender origin may be off by a few px along the fuselage. That is a constant offset, so it does not affect
  speeds or displacements.
- There is strong vertical motion blur later on (up to about 45 px/frame), so sizes should be taken from frame 0.
- There is no shadow and no other moving object.
- 2D convention: a single metres-per-pixel scale from the prior (e.g. wingspan 168 px or length 108 px).
