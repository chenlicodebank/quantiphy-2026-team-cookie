# simulation_0158 — measurement record (pixels, seconds)

2D Blender underwater scene, 1920x1080, 24 fps, 48 frames (t = frame/24). Static camera. Two moving
animals, both swimming right-to-left: a **shark** in the upper band (body centre y ≈ 140) and a **sea turtle**
lower down (carapace centre y ≈ 550). Background: blue water with faint static light rays, and a pale sandy
seabed (bottom ~25 % of the image) with animated turquoise caustic spots. There are no other objects.

## Files
- `scene.json`: inventory, sizes, events, camera, reference-point definitions.
- `tracks/shark.csv`, `tracks/turtle.csv`: one row per frame 0-47. Columns:
  - `frame, t`
  - `ref_x, ref_y`: **use these as the object position**. They come from rigid template matching (see below).
  - `shift_x, shift_y` (shark) / `shell_shift_x, shell_shift_y` (turtle): template translation relative to the reference frame
    (shark: frame 30; turtle: frame 40). `ref = reference centre + shift`.
  - `x0,y0,x1,y1,bbox_w,bbox_h`: bounding box of the background-difference mask (whole visible animal incl. fins/flippers).
  - `cx_bbox, cy_bbox, cx_mask, cy_mask`: bbox centre and mask centroid (biased by edge clipping and fin/flipper pose; do not use for motion).
  - `len_axis, width_axis, axis_deg`: PCA extents of the mask (length along main axis, width across it).
  - `area`, `clipped` (L/R/T = mask touches that image edge), `occluded` (1 = cut by an image edge; there is no inter-object occlusion).
  - shark only: `snout_x_est` (= 670 + shift_x, snout tip x), `match_patch` (head / mid / rear template, or mask_tail_tip), `match_rmse`, `shifts_all` (all patch results).
  - turtle only: `core_x, core_y` (centroid of the eroded mask, flipper-biased, for reference only), `shell_rmse`, `shell_vis_frac`, `shell_shifts_alt`.
- `bg_median.jpg`: median background (has ghosts at the right edge; the tracking used frame 47 patched with frame 0 instead).
- `scripts/`: `bg.py` (median bg + camera check), `track.py` (masks, bbox, PCA extents; run first),
  `track2.py` (template-matched reference points; run second), `sizes.py` (sizes), `probe.py` (diagnostic).

## How measured
- Masks: max-channel |frame − background| > 10, open/close, connected components split by centroid y (< 360 shark,
  ≥ 360 turtle), holes filled; seabed rows y ≥ 785 excluded. Background = frame 47 with the turtle region taken from
  frame 0 and the left-top corner (frame-47 tail tip) from frame 0. Overlays were checked by eye at frames
  0, 8, 10, 20, 30, 36, 40, 47.
- Shark position: the shark's shading changes strongly with the light rays, so matching uses high-pass, locally
  contrast-normalised grey images. Three patches cut from frame 30 (head x 672-1000, mid-body+dorsal fin x 1000-1300,
  rear body x 1300-1440). Head used for frames 0-38 (in frames 0-12 partly off-screen to the right, still fine),
  mid for 39-43, rear for 44, and the mask tail-tip x1 (− 1579) for 45-47. Reference centre at frame 30:
  (1124.5, 140) = midpoint of snout tip (x 670, checked visually) and tail tip (x 1579).
  Per-frame noise ~±3-5 px in x (e.g. frames 11-12, 23-24, 35); frames 44-47 rely on the flexing tail (±5-8 px).
  ref_y in frames 44-47 less reliable (frame 44 shows 146 instead of ~141).
- Turtle position: carapace template from frame 40 (x 1110-1370, y 495-555) used for frames 26-47 (very clean);
  a template from frame 26 (same carapace, darker lighting) for frames 10-25, chained to frame-40 coordinates
  (agrees with the frame-40 template within 0-6 px over frames 26-30); a head+front-shell template from frame 12
  for frames 0-9 (most of the shell is off-screen right). Reference centre at frame 40: (1240, 550).
  In frames 0-21 ref_x exceeds 1919 (centre off-screen) — expected; it is extrapolated from the visible part.
- Camera: phase correlation on the seabed band — no shift (≤ 0.12 px).

## Sizes (px)
- Shark: snout-tip to tail-tip length **911** (range 908-916, frames 26-37). Body depth at gills ~157 (y 58-215).
  Total height not measurable: the dorsal fin is cut by the top edge whenever it is in view (visible bbox y 0-~257,
  pectoral/pelvic fins lowest ~255). Mask bbox width in frames 26-37 is ~860-919 because the faint snout tip is
  often missed by the mask — use 911 or `x1 − snout_x_est + 1`.
- Turtle: head-to-rear-flipper bbox length ~305-333 (median ~320; 312 at frame 40); carapace length ~260;
  height 108-132 when flippers trail (frames 38-47), up to ~235 when front flippers point down (frames 15-25).
  Turtle bbox values in frames 0-21 are cut by the right edge.
- Seabed (static): crest of the rear dune y ≈ 792-800 at x 1000-1150; front dune edge y ≈ 900-985 at x 240-960.

## Motion and events
- Both animals start (almost) at rest at frame 0 and accelerate steadily leftward through the whole clip; vertical
  position stays constant (shark y 140±3, turtle y 550±2). Per-frame ref_x steps: shark −2 → about −107 px/frame,
  turtle −1 → about −43 px/frame, both growing roughly linearly (no fitted model given here).
- Shark: snout in view from frame 0 (x 1782); whole body in view frames 26-37; snout leaves the left edge at frame 38;
  only the tail tip remains at frame 47.
- Turtle: in view from frame 0 (head at x ~1775), fully in frame from frame 22; front flippers down ~5-25, sweep back ~26-40.
- No contact or occlusion between the animals (shark above, gap ~235 px).

## Ambiguities
- The rig origins are not visible; the reference points are fixed body points (body/carapace centres), so
  displacements, speeds and accelerations are exact up to tracking noise, but absolute positions/distances between
  the two animals carry ~±20 px uncertainty about where each origin lies.
- If a prior gives a size: the shark's length is clean (911 px); its height is not (clipped fin). Turtle length
  depends on whether flippers/head are included (carapace ~260, whole animal ~320).
- No shadows on the seabed from the animals; motion blur is small.
