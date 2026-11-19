# simulation_0304 – measurement record (pixels, seconds)

Video: Blender render, 3D scene, 2560x1440, 24 fps, 72 frames (t = frame/24, frame 0 = 0 s, last frame 71 = 2.958 s).

## Scene content
- **Only one object: a whale** (dark blue, humpback-like with long pectoral fins), seen from below / the side against a
  featureless underwater blue gradient. Head at upper left (around x 1000-1450, y 300-700), body runs diagonally
  down-right to the tail fluke. It swims with tail strokes: the tail sweeps down (fluke clipped by the bottom edge in
  frames 8-38) and then rises up to the right (frames 50-71, where the tail is above the body line and the second
  pectoral fin shows under the body).
- No other animals, props, ground, seabed, surface or markings. No static objects to measure.
- A pale semi-transparent patch at the top-left of the head (about x 1000-1100, y 400-560 at frame 0) is part of the
  whale render (light on the snout/jaw). It is included in the mask.

## Files
- `scene.json` – inventory, camera, events, summary values at frames 0/71, path lengths in px.
- `tracks/whale.csv` – merged per-frame track (all 72 frames):
  `ref_x, ref_y` = 2D mask centroid (proxy for the rig origin; the origin itself is not visible);
  `head_x, head_y` = centre of a tracked head/front-body patch (450x310 px box at frame 0, centred at (1225,545));
  `head_scale_vs_f0` = apparent size of that patch relative to frame 0; `head_rot_deg_vs_f0` = its in-plane rotation;
  bbox (x0,y0,x1,y1,w,h, inclusive px); `mask_len_main_axis` / `mask_width_across` = mask extent along / across the
  PCA main axis; `main_axis_angle_deg` (image coords, y down); `area_px`; `occluded_or_clipped` = 1 when the mask
  touches the image border (only the tail, at the bottom edge, frames 8-38).
- `tracks/whale_mask.csv`, `tracks/whale_head.csv` – the raw outputs that the merged file combines.
- `scripts/segment.py` (mask: per-frame cubic background fit, |RGB - bg| > 40, morphology, components > 2000 px),
  `scripts/head_track.py` (multi-scale/rotation NCC template matching at half resolution, frame-0 template, coarse-to-fine),
  `scripts/check_head.py`, `scripts/merge.py`, `scripts/probe.py`. Overlay checks: `../frames/ov_*.png`, `../frames/headcheck.png`.

## Key numbers (px)
- Frame 0: mask bbox x 954-2446, y 390-1302 (1493 x 913); main-axis length 1606, across 743 (axis 27.5° down-right; the
  across value includes the spread pectoral fin); centroid (1511, 810); head (1225, 545).
- Frame 71: bbox x 773-1993, y 297-909 (1221 x 613); main-axis length 1257, across 589 (axis -6.5°); centroid (1214, 533); head (1042, 432).
- The whole-body extents change a lot because the body bends (tail strokes) – they are not a rigid size. For a rigid
  size cue use the head patch scale. Full unclipped body extent only in frames 0-7 and 39-71.
- Head motion: steady drift up-left, ~3-4 px/frame, path 222 px, net 215 px over 71 frames (smooth, near-uniform).
  Centroid path 497 px (net 407 px) – includes tail-flex wobble and the bottom-edge clipping bias in frames 8-38.

## Camera / perspective
- Camera static: background gradient pixel values identical in frames 0, 20, 71; no features shift. Nothing to subtract.
- No ground plane, horizon or vanishing points. Only depth cue: the whale's apparent size.
- Head patch scale: 1.00 (f0), ~0.96 (f20), ~0.945 (f24), ~0.93 (f36), ~0.92 (f48), ~0.90 (f55), ~0.89 (f62), 0.88 (f71).
  So the whale moves away from the camera (if scale ~ 1/depth, depth grows about 13% over the clip), while drifting
  up-left in the image. Frame-to-frame scale noise about ±0.01 (the head rolls slightly, so the template is not
  perfectly rigid; see the ~-2° rotation drift).

## Events
- Frames 0 and 1 are identical; motion visible from frame 2 (t = 0.083 s). The whale swims the whole clip (no stop).
- Tail fluke clipped by bottom edge frames 8-38 (t 0.333-1.583 s).
- Centroid y peaks at frame 12 (t 0.5 s), then rises; centroid x stalls around frames 26-31; tail lifts above the body
  line from about frame 50-55 (bbox bottom then stays at ~ y 910-918, set by the pectoral fin).

## Reliability / ambiguity
- Mask: clean (high contrast against background); edges ±2 px. Mask is the full whale incl. fins.
- The rig origin of the whale is unknown; the mask centroid is shifted by tail bending and clipping. The head track is
  smoother and better for questions about the whale's motion if the origin is near the front/middle of the body.
  For depth-based questions, combine the given depth_info with the image position (choose head or centroid) and
  the focal length estimated from the given prior.
- Only one object, so there is no ambiguity about which object a question means.
