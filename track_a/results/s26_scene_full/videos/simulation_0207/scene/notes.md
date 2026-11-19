# simulation_0207 — measurement record

2D simulation (Blender render), 24 fps, 30 frames (1.25 s), 2124x1080. t = frame/24.
All values in pixels (x right, y down, original resolution). No metric scale assumed.

## Scene
A still-life desk (lamp, books, letter, alarm clock, photo frame, telephone, pen, papers, two
blurred chairs behind, teal wall). A black vintage typewriter starts high in the air (frame 0,
centre ~(981, 258)), falls straight down, hits the desk between frames 10 and 11, tips up onto
its front edge (max at frame 15), falls back with a small yaw turn, rocks and is at rest from
frame 24 (centre ~(1034.5, 940)). It is the only moving object; nothing else is knocked over.
Camera is static (no shift).

## Files
- scene.json — inventory, camera, events, static-object boxes, typewriter key extents.
- tracks/typewriter.csv — one row per frame 0-29: frame, time, bbox_cx/bbox_cy (bbox centre =
  reference point / origin estimate), centroid_x/y (mask pixel mean), bbox x0,y0,x1,y1, bbox_w,
  bbox_h, minrect_len/wid/angle (min-area rectangle of the mask), area_px, occluded (always 0).
- scripts/: diff.py (background check), diffviz.py (difference images), track.py (the tracker,
  writes the csv and frames/overlay.png), landing_sheet.py (zoomed check of frames 9-24),
  thr_test.py (threshold test for the post-landing mask).

## Method
Background = frame 29 above y=550 + frame 0 below y=550 (the typewriter is absent from each
part in that frame). Mask = max-channel |frame - background| > 30, morphological close/open,
connected components inside a window around the previous box, holes filled. After landing,
the alarm-clock face and the white card to the right change shading (typewriter shadow), so they
are masked out (ellipse at (1216,912) and x>1212 below y=960). Overlays were inspected: box
hugs the typewriter in every frame.

## Reliability
- Fall (frames 0-10): very good, ±1-2 px. Width is constant 289-292 px → constant depth, so one
  px scale applies (prior "typewriter width/length" ↔ 291 px). Box height grows 113→167 px
  because the view changes from underside to top as it drops (not depth). Use bbox_cy (or the
  mean of y0/y1) for vertical motion; the pixel centroid in frames 0-5 is biased (mask misses
  part of the top-right carriage, which is close to the wall colour) — prefer bbox centre.
- Free-fall: bbox top, bottom and centre all have nearly constant second differences through
  frames 1-9; frame 10 shows slightly less increment (possibly perspective/edge effects), worth
  excluding when fitting gravity-like acceleration.
- Release: the object is already moving at frame 0 (0→1: +8 px), i.e. released at/just before t=0.
- After impact (11-23) the typewriter tumbles in 3D; the bbox centre is only a rough proxy of the
  true origin (±10-20 px). Right edge in frames 17-22 hits the 1211 clip limit (true edge ~1204).
- After landing (11-29) the mask's right edge overshoots by ~10-15 px (desk/clock shadow);
  subtract that from bbox_w if a size is needed then. Rest (24-29): mask box
  [860,854,1209,1026] (350x173); zoomed visual reading [867,850,1195,1022] (~328x172).
  For size questions prefer the fall-phase width 291 px (clean silhouette against the wall).
- Static object boxes in scene.json: read from a grid overlay, ±10 px.
- Ambiguities: shadows on the desk and clock change during landing; eyeglasses on the desk are
  hidden behind the typewriter after landing; chairs are blurred background.
