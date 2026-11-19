# simulation_0279 – measurement record

2D Blender render, 2560x1440, 24 fps, 72 frames (t = frame/24, 0–2.958 s). Everything is in
full-resolution pixels (x right, y down) and seconds. No metric scale was assumed.

## Scene
- **whale** (only moving object): grey humpback-like whale, seen side-on, head LEFT, long
  pectoral flipper hanging down, tail/flukes RIGHT. Swims horizontally to the left at a
  uniform rate. Its tail beats: it is cut off by the right image edge in frames 0–34 and 37–46,
  sweeps down to its lowest around frames 27–29 (bbox bottom 1099 px at the right edge), and
  then rises continuously from frame ~47 to the end (tail tip y 733 → 132 px).
- **whale_shadow**: soft dark shadow on the floor (y ≈ 1000–1440), moves with the whale.
- **floor/backdrop**: seamless light-grey studio cyclorama with a spotlight, dark vignette
  corners, no texture or markings. Nothing else in the scene.
- **Camera**: static (see camera_check.csv). Apparent whale size is constant (2D scene).

## Files
- `scene.json` – inventory, sizes, events, camera summary.
- `tracks/whale.csv` – one row per frame (0–71):
  - `head_chain_x, head_chain_y` – **recommended reference point**: the frame-0 snout tip,
    carried forward by frame-to-frame template matching of the rigid head (snout…eye, 520x160
    px), sub-pixel. Per-step x displacement −8.02 px (std ≈ 0.1), y constant at 542–544. Best
    proxy for the rig origin's motion (the head moves rigidly; the origin isn't visible).
  - `snout_sub_x, snout_y` – sub-pixel snout-tip edge (independent check; ±0.3 px per frame).
    `snout_x` = integer leftmost outline pixel.
  - `head_x, head_y, head_score` – match against the fixed frame-0 template. OK to frame ~62;
    it degrades after that as the head pitches. Prefer the chain columns.
  - `bbox_x0..y1, bbox_w, bbox_h, bbox_cx, bbox_cy` – box around the whale outline (includes
    the flippers and flukes). While `cut_by_right_edge = 1` the box is truncated at x = 2559
    (`occluded` = same flag: part of the whale is outside the frame).
  - `mask_cx, mask_cy, mask_area_px, mask_method` – silhouette centroid/area. `fill` = closed
    outline flood-filled (good). `colspan` = outline gaps, so each column is filled between its
    top and bottom outline pixels: this fills the gap between flipper and belly, and leaves
    a few narrow unfilled strips where the faint back outline is missing. Area ±3%,
    centroid ±15 px. Truncated masks while cut.
  - `tail_tip_x/y` – rightmost outline point (the fluke tip, valid only when cut = 0).
    `top_x`, `bottom_x` – x of the top-most and bottom-most outline point.
  - `axis_len_px, axis_width_px, axis_angle_deg` – PCA extents/angle of the mask (the body
    is curved, so treat as approximate; angle positive = tail lower).
  - `frame_diff_prev` – mean |frame − previous frame|. Frame 1 = frame 0 (0.06), so the
    first rendered frame is duplicated.
- `tracks/shadow.csv` – shadow blob (blurred image < 70 grey, y > 1000): bbox, leftmost
  point, centroid. Its edges are soft and depend on the threshold (±10 px). The left end
  leaves the frame at about frame 57–60.
- `tracks/camera_check.csv` – vignette-crossing rows at x = 150 and x = 2450 and two
  background patch means per frame.
- `scripts/` – `segment_track.py` (outline, mask, bbox, fixed head template),
  `refine_head.py` (sub-pixel snout, chained head track, duplicate-frame check), `extras.py`
  (shadow, camera), `summarize.py` (numbers quoted here). Viewers/probes: `look.py`,
  `gradviz.py`, `edgeviz*.py`, `probe.py`. `background.py` was a failed attempt at a
  background model and isn't used: the whale and shadow cover the same pixels in most frames.

## Method
The background is a smooth, static gradient and the shadow is very blurred, so the whale is
segmented from its **sharp outline**. An edge pixel must pass two tests: Sobel magnitude
(σ = 1 blur) > 15, and more than 1.6× the σ = 4 gradient. Blurred shadow edges fail the
second test. Small fragments are dropped, along with dark-neighbourhood edges in the
fluke-shadow area (x > 2100, y > 950) and everything below y = 1200. Overlays (outline, mask,
bbox, centroid, head point, tail tip) were checked visually on frames 0, 7, 14, 21, 24, 28,
35, 42, 49, 53, 56, 57, 63, 70 and 71. They hit the whale and its full extent.

## Key numbers (px)
- Head/snout: x 614.4 at frames 0–1 → 53.0 at frame 71. Uniform −8.02 px/frame from frame
  1→2 to 70→71, with no start or stop inside the clip. y ≈ 543 throughout.
- Whale length (whole whale in frame, frames 47–71): bbox_w 2312 (f47), **2319 (f52, body
  almost straight: tail tip y 574 vs snout y 543, PCA angle 0°)**, 2290 (f60), 2246 (f66),
  2217 (f71, tail raised). The straight snout-to-fluke-tip distance is 2318–2319 px at frames
  47–52 and 2253 px at frame 71. Frames 0–46 give only lower bounds (tail cut).
- Height (bbox_h, flipper included): 533 (f47, min) to 869 (f71, max, tail up). In the cut
  frames it is 536–687 (tail at the edge). Body depth without the flipper is ≈ 350 px (back
  y ≈ 394, belly ≈ 745 near the flipper root).
- Head snout→eye ≈ 512 px (frame 0: snout (614,544), eye ≈ (1125,525)). Pectoral flipper
  root→tip ≈ 600 ± 40 px (frame 0).

## Reliability and ambiguities
- Head track and snout: ±0.3 px. These are the most reliable items. A question's "position"
  of the whale (its origin) probably moves like the head, because the rig translates
  uniformly while the tail bends. bbox and mask centres also move with the tail beat (e.g.
  bbox_cy 702 → 555), so do not use them for whale speed.
- bbox top: ±2 px. bbox bottom: ±20 px in frames ~20–35 and ~40–71. In those frames the
  fluke tip or flipper tip meets the tip of its own shadow, and the shadow edge turns sharp
  there. Bottom extents in frames 0–19 are clean.
- The far-side (left) flipper is slightly blurred and sometimes has no detectable outline.
  It lies inside the bbox, so it only affects mask area and centroid.
- No occlusion by other objects. The only "occlusion" is the tail outside the right image
  edge (flag).
- Camera: the vignette crossings are fixed to ±1 px (the right column changes ~2 px when the
  tail passes nearby). The background has no texture, so a tiny pan can't be strictly
  excluded, but none is indicated.
