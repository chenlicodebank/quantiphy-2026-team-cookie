# simulation_0132 — measurement record

Video: Blender render, labelled **2D**, 1080x1920 portrait, 120 fps, 300 frames (2.5 s). t = frame/120.
Pixel coordinates: x right, y **down**, origin top-left. No metric scale is assumed anywhere.

## Scene
A kitchen. One apple (red-orange, ~61 px diameter) is the **only moving object**. It starts at rest on the
left part of the grey kitchen island at (689, 1072). It rolls left along the counter, rolls off the counter's
left edge (x≈352–370) at frame ≈141, falls to the floor and hits it at frame 192. It makes a small bounce
(apex frames 198–200, about 10 px), lands again at about frame 205, then rolls left along the floor. It touches the left image edge at frame 263
and is gone after frame 288. Everything else is static: island counter, diagonal cutting board, two fruits on a white plate (a red
peach and a yellow one; don't confuse them with the moving apple), a teal bowl, a pot, a milk jug and an "Allinson's" flour bag on a
black stool, a second stool with an egg carton, a glass pendant lamp, two wall ovens, a utensil rail and the floor.
Pixel boxes for all of these are in scene.json (estimated from zoomed gridded frames, ±3–5 px).

## Files
- `scene.json`: inventory, static-object pixel boxes, apple phases, events, camera.
- `tracks/apple.csv`: **the track to use**. One row per frame 0–299. `visible`; `ref_x, ref_y` is the apple centre
  (origin) from a least-squares circle fit to the upper ~70% of the mask outline. `bbox_*`, `width_px`, `height_px` give the box
  with any reflection trimmed. `fit_radius`; `len_major/len_minor` (min-area-rect of mask); `mask_cx/cy` (raw mask centroid);
  `reflection_trimmed`; `clipped_at_edge` = `occluded` (the apple is cut by the left image edge).
- `tracks/apple_raw.csv`: raw mask measurements before the correction (centroid, box, enclosing circle, circle fit).
- `scripts/track.py` builds the raw track. It uses the median-background difference (15 frames), an orange/red HSV gate,
  the largest blob near the previous position, and a circle fit. `scripts/refine.py` builds apple.csv. `scripts/overlay.py` draws the
  check tiles. `scripts/camera_check.py` checks for camera motion, and `camera_check.json` holds its result.

## How reliable
- Centre (frames 0–262): the circle fit is accurate to about ±0.5 px per frame. The apple is slightly lumpy and rotates, so
  per-frame differences jitter by about ±0.5 px. Smooth over a few frames before taking derivatives.
  Overlays at frames 0, 60, 120, 141, 160, 191, 192, 198, 204, 230 and 262 were checked by eye, and the circle sits on the apple.
- Reflections: the glossy counter (frames ~108–145) and the floor (~192–196) reflect the apple, which makes the raw mask taller
  at the bottom (up to 88 px). The circle fit and the trimmed box remove this. Shadows are grey and are not in the mask.
- Clipped frames 263–288: the apple is cut by the left edge. Here ref_x = bbox_x1 − 31.5 and ref_y = bbox_y0 + 31.5,
  which assumes a 64 px box. Treat ±2 px as the error. From frame 285 on the visible sliver is <15 px wide and ref_y is unreliable
  (it drifts to 1757). Frames 289–299: not detected (at most a few px left on screen).
- Apparent size: the circle-fit diameter is 60.6 px (median radius 30.3), and the tight mask box is median 62 x 65 px (it includes an anti-aliased rim).
  The size is constant through the clip (radius 30.5 on the counter, 30.0 on the floor), so there is no visible depth change.
  For a "diameter/size" prior use **~61–63 px** (61 = fitted circle, 62–63 = box width). The box height is 64–65 px because the apple is slightly taller than wide.
- Camera: static (phase-correlation shift <0.04 px over the whole clip). No pan, zoom or shake.
- Events (scene.json): the start of motion is gradual from frame ≈8, under 0.3 px/frame until ≈15. Leaving the counter edge is at frame 141
  ±1, impact is at frame 192 (contact between 191 and 192), the bounce apex is at 198–200, second contact at ≈205, the apple reaches the edge
  at 263, and it is last seen at 288.
- Motion summary (px/frame, for orientation only): on the counter, horizontal speed grows to ≈ −3.7 by frames 120–141.
  In the fall, horizontal speed stays ≈ −3.7 and vertical speed grows by ≈0.42 px/frame² (24 px/frame just before impact). On the floor,
  speed is ≈ −2.0 to −2.5 horizontal.
- Ambiguities: the moving fruit could be called an apple or a peach; it is the left, lone one, not the pair on the plate.
  The counter path is not perfectly level: the centre y goes from 1072 to ~1104 over frames 60–141, rolling slightly toward the
  camera/down the board. Under the 2D convention, use the in-plane pixel distance.
