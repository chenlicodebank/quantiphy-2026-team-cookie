# simulation_0192 — measurement record (pixels, seconds)

2D simulation (Blender), 120 fps, 200 frames (0–1.658 s), 1920x1080. t = frame/120. Pixel coordinates: x to the right, y **down**.
No metric scale is assumed anywhere here.

## Scene
Static camera looking straight at the rear of a white box truck in a grey warehouse. Two things move:
1. **cardboard_box**: a brown box (one lid flap sticking up at top-right) falls straight down from above the truck
   (centre x ≈ 946) and lands on the truck roof between two roof rails. It bounces a little and comes to rest.
2. **tail_lift_platform**: the dark metal tail-lift plate at the bottom of the rear door opening rotates upward
   about a horizontal hinge (y ≈ 1021–1027) and closes against the door. It is still closing slowly at the last frame.

Static items (pixel extents in scene.json): truck rear body (x 661–1227, y 533–1045), rear door opening
(x 820–1066, y 600–1021), two roof rails, red fire extinguisher, hazard stripes, "DOLL" labels, warehouse wall
(panel seams, pillars at x≈445/955/1465), four ceiling lamps, dark window/door panel at the left, and the
floor/wall boundary at y≈737.

## Files
- `scene.json`: inventory, static extents, pixel sizes, events, camera, caveats.
- `tracks/cardboard_box.csv` (every frame):
  - `cx_ref_px, cy_ref_px`: the **reference point**, i.e. the centre of the box's front face, used as a proxy
    for the box origin. Here cy = 159.35 (front-face centre at frame 0) + `tm_dy_px`. `tm_dy_px` is the vertical
    shift of a front-face-only template (frame 0, x 840–1050, y 75–245), matched with normalised cross-correlation
    and a parabolic sub-pixel peak (score ≥ 0.975). cx = midpoint of the sub-pixel side edges.
  - `face_top_y`: the top edge of the front face (saturation crossing, left of the flap). `mask_bottom_y`: the
    lowest box pixel; while the box is high this includes the visible underside. `face_left_x/face_right_x`: the
    side edges. `bbox_*` is the brown-mask bounding box (top includes the flap). `face_width_px` is about 280–282
    throughout.
  - `frozen_vs_prev = 1` means the box image did not change from the previous frame (see caveats).
- `tracks/tail_lift_platform.csv` (every frame):
  - `upper_edge_y`: the top boundary of the dark plate (sub-pixel, threshold 70 on the column-averaged intensity
    over x 860–1030). In frames 0–58 this is the hinge/far edge (constant at ≈1020.8). From frame 59 on it is the
    rising free edge.
  - `near_edge_y_below_hinge` (frames 0–58): the free edge of the plate while it still lies below the hinge (seen
    from above). It is below the image bottom in frames 0–3, enters at 1079 (frame 4) and rises to 1025 (frame 58).
  - `lower_visible_y`, `x_left/right_at_mid`, `width_at_mid_px`, `visible_height_px`: plate extents from frame 59 on.
    The bottom is ≈1026.5, the width ≈248 px and the height grows to 217.8 px at frame 199. `visible_height_px` in
    frames ≤58 = near edge − hinge.
- `tracks/camera.csv`: background shift against frame 0 (phase correlation of a wall patch). The largest shift is
  0.03 px, so the camera is static.
- `scripts/`: `track_final.py` makes all three CSVs and the overlays (this is the authoritative script).
  `track.py`, `refine.py` and `refine2.py` are earlier passes kept as history; their outputs were overwritten.
  `probe.py`, `dups.py`, `prof.py`, `boxprof.py`, `crops.py`, `show*.py` and `static.py` are inspection helpers.

## Key numbers (pixels)
- Box front face: width 281.6 px (sub-pixel edges; mask bbox 284 px), height ≈197 px (195 at frame 0, ≈200 at
  rest). The flap rises ≈17 px above the face. The box bbox at rest, including the flap, is x 804–1087, y 304–527.
- Box reference point: (946.4, 159.4) at frame 0 and (946.6, 423.8) at rest from frame 74. That is a vertical drop
  of 264.4 px with less than 0.5 px of horizontal drift. The motion is purely vertical.
- Box events:
  - Moving from the start (0.10 px by frame 1, 1.8 px by frame 5).
  - First contact with the roof/rails at frame 59–60 (t ≈ 0.49–0.50 s): cy goes 402.1 (frame 58), 410.5 (59), 419.1 (60).
  - Lowest point 423.1 at frames 62–63.
  - Small rebound to 421.15 at frames 67–69.
  - At rest at 423.8 from frame 74 (t = 0.617 s).
- Tail lift:
  - The plate moves through the whole clip.
  - It is edge-on at about frame 58–59 (t ≈ 0.49 s).
  - Upright free edge: 1018.6 (frame 59), 981.3 (frame 80), 940.0 (frame 100), 898.6 (frame 120),
    847.8 (frame 150), 808.7 (frame 199). It decelerates to about 0.3–0.5 px/frame at the end.
  - Plate width ≈248 px (about the door width, 246 px). Its projected length at frame 199 is 217.8 px.

## Reliability and ambiguities
- Box reference point: about ±1 px. The template drop (264.4 px) and the face-top-edge drop (259.5 px) disagree by
  ≈5 px. At rest a thin strip of the top face/flap shows above the front face, so the face-top edge reads high.
  The template value is preferred. The front-face centre stands in for the 3D centre, which is fine in this 2D
  frontal view.
- **Frozen frames:** the box position repeats exactly at frames 2, 8, 12, 16, 20, 24, 32, 35, 37, 40, 47 during the
  fall, and at 61 and 63. The tail lift keeps moving on those frames, so this is the simulation's update pattern,
  not duplicated video frames. One-frame differences of the box are therefore spiky; fit the fall over many frames.
- Box size: early in the fall the box is above eye level, so its underside is visible (y 257–297 at frame 0) and
  the mask is about 40 px taller than the front face. Use `face_width_px` (constant) or the ≈197 px face height.
- Tail lift: no visible centre or origin. The hinge line is clear (≈1021 before edge-on, ≈1026.5 after). The free
  edge is tracked to about ±1 px; the near edge before frame 58 is integer-pixel (±2 px). The plate is not yet fully
  vertical at the end, so 217.8 px is a lower bound on its projected length. Its rotation angle is not measured
  (the camera geometry is unknown).
- Static extents: ±3–4 px (partly visual). The camera is static.
- No motion blur problems. The only shadows are soft floor shadows at the lower left.
