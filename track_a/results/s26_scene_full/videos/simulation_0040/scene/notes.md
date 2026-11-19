# simulation_0040 — measurement record (pixels, seconds)

Scene: Blender render, 3D, 1080x1080, 24 fps, 72 frames (3.0 s). Aerial view looking (nearly) straight down on a
sandy beach point with green sea below/right and a rocky outcrop at the top right. One man (white T-shirt, grey
trousers) walks slowly toward the bottom of the image; one large black bird flies left-to-right across the whole
frame, low over him, and leaves at the right edge after frame 67. Both cast long shadows toward the up-right (low sun).
Camera is static (background phase-correlation shift < 0.03 px all frames). t = frame/24.

**Frame 1 is an exact duplicate of frame 0** (every object identical). Any one-frame speed at frame 1 is 0 in the
raw video; real motion starts between frames 1 and 2.

## Files
- `scene.json` — inventory, camera, events, apparent-size summaries.
- `tracks/walker.csv` — every frame 0-71. `pelvis_torso_x/y` = recommended pelvis point: shirt (bright torso pixels)
  centroid + constant offset (+2.6, +8.8) px (smooth). `pelvis_x/y` = point at 0.48 of the head-top→feet span (noisier,
  ±2 px from leg swing). Also body-mask centroid, shirt centroid, bbox, vertical body length (head top to lowest foot),
  width, area, occlusion flag (frame 24 = bird overlapping the feet).
- `tracks/walker_shadow.csv` — shadow mask (person-group mask minus body): centroid, bbox, main-axis length/width/angle.
  Frames 6-8 and 23-24 merged with the bird / bird shadow: those values are distorted (flag column).
- `tracks/bird.csv` — frames 0-67: mask centroid `cx,cy` (reference point), bbox centre, bbox, bbox w/h,
  main-axis length (≈ projected wingspan/body length, PCA extent), width across, axis angle, area,
  merged flag (23-24), edge flag (0-2, 67: partly outside the image, centroid biased to the visible part).
- `tracks/bird_shadow.csv` — frames 0-38 (37-38 weak, over water), same columns; merged 6-8.
- `bg_median_half.jpg` — median (object-free) background at half resolution (540x540) for a quick look at static features.
- `scripts/` — `bg.py` (camera check), `blobs.py` (median background → frames/bg_full.npy scratch),
  `comp_all.py` (components, shirt centroid), `seg.py` (pixel classes), `track.py` (tracks + overlays),
  `zoom_check.py` (bbox overlays for visual checks), `static_and_stats.py` (static regions, summary numbers),
  `summ.py`, `probe.py` (inspection).

## Method
Median background over all 72 frames (camera static); moving mask = max channel |frame − bg| > 28. The walker group
(body + attached shadow) is the component containing the bright shirt. Walker body = pixels in a 33x64 px column
around the shirt that are not "darkened sand" colour (R/B > 1.4 and darker than bg), plus everything in the column
above the shirt (brown hair). Bird and bird shadow are separate components except in merge frames, where an
interpolated bbox from neighbouring frames isolates them (bird = dark pixels V<60 inside it). Overlays were checked
visually at frames 0, 7, 12, 23, 24, 36, 40, 50, 66, 71: masks cover the right objects and their full extents.

## Key numbers (pixels)
- Walker: moves ~(+0.1, +1.5) px/frame (direction ~86° = down the image), steady, never stops or turns; total shirt
  displacement frame 0→71 ≈ (8.2, 106.6) px. Apparent vertical body length 39-50 px (median 45.5), width 17-24 px;
  no size trend → roughly constant camera distance. Because the view is near top-down, the "body length" is a
  foreshortened standing height, NOT a true height in pixels; use it with care.
- Bird: ~16-17.5 px/frame in x and +2..+6 px/frame in y; heading wavers 7°-27° below +x in a ~12-frame rhythm
  (no sharp turns). Path from (5.6, 360) at frame 0 to (1074.7, 655) at frame 67 (edge-cut endpoints).
  Main-axis length oscillates with wing beats: min 35.9 px (frame 22), max 62.8 px (frame 54); peaks ≈ frames 5, 31,
  54; troughs ≈ 11, 22-24, 47. Largest bbox 39x59 px. Peak size slightly larger late in the clip (57→58→63).
  The bird looks about as large as the standing man although it is much smaller in reality → it is much closer to
  the camera (high above the ground); its shadow lands ~360 px away on the sand.
- Bird shadow: offset from bird ~(+360, −45) px at frame 0, ~(+380, −55) at frame 24; blurry; main-axis 32-82 px.
- Static: dry-sand x-range at y=380: 0-841; y=490: 0-739; y=600: 56-627; y=700: 171-527; sand tip near
  (395-430, 720-760) merging into shallow water. Rock outcrop approx x 500-1000, y 0-215 (dark rocks x 702-990),
  white patch at its top around x 520-700, y 0-110. Pale curved wet-sand bands follow the shore.

## Reliability / ambiguity
- Walker reference: pelvis is not directly visible from above; pelvis_torso is a torso-based proxy (±2 px absolute,
  much better frame-to-frame). Leg swing makes bbox/body length vary ±5 px with the gait.
- Bird centroid: ±1-2 px; it shifts with wing pose (mask centroid ≠ body origin by a few px when wings move).
  Frames 0-2 and 67 are cut by the image edge; frames 23-24 overlap the walker's shadow (bird mask may include a few
  shadow pixels or lose some).
- Over dark water (frames ~45-67) the black bird has lower contrast; faint wing-tip edges may be lost (lengths there
  may be ~1-3 px short).
- Bird-shadow detections after frame 34 (water) are weak/partial; frame 37 detection is tiny.
- 3D: no ground horizon or vanishing points; the scene is essentially a top view, so image displacements of the
  walker are ground displacements (one scale at his depth). The bird is at a different (smaller) depth; do not use
  the walker's scale for the bird without depth information.
