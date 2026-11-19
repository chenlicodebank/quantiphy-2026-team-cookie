# simulation_0091 — measurement record (2D simulation, 24 fps, 30 frames, 1920x1080)

## Scene
Plain blue sky, static camera, no ground/horizon/features. Two birds seen side-on:
- **eagle**: bald eagle (white head pointing left, white tail, dark wings), large. Starts at body centre ~(742, 586),
  flies LEFT ~128 px/frame, fully visible frames 0-6, cut by the left edge at frame 7, gone from frame 8.
- **crow**: small all-black bird, head pointing right. Starts at ~(1154, 590), flies RIGHT ~78-80 px/frame,
  fully visible frames 0-10, cut by the right edge at frame 11, gone from frame 12.
Frames 0 and 1 are pixel-identical (birds frozen); motion starts between frame 1 and 2. Frames 12-29 are empty sky.
Both birds fly nearly horizontally (eagle body y 586-588; crow body y 590-597), essentially constant speed.

## Files
- `scene.json`: inventory, visibility, per-frame sizes and displacements, events, camera.
- `tracks/eagle.csv`, `tracks/crow.csv`: per frame: `frame, time`, `body_cx, body_cy` (recommended origin proxy:
  x = midpoint of the beak-to-tail extent on the body line, y = mean mask y within ±15 px of that line),
  `centroid_x/y` (mask centroid, pulled upward by raised wings), `bbox_*` (x0,y0,x1,y1 inclusive, w,h),
  `body_len_px` (beak-to-tail horizontal extent on the body band), `area_px`, `truncated_by_edge`, `occluded` (always 0).
- `scripts/measure.py` (segmentation + tracks), `scripts/overlay.py` (check image), `scripts/probe.py` (first look).

## Method
Background = per-pixel median of frames 14,18,22,26,29 (empty). Mask = RGB distance from background > 15, 3x3 opening,
components assigned to eagle/crow by expected x. Overlays (bbox, body point, centroid) checked visually on frames
0,2,4,5,6,7,9,10: boxes cover the full bird incl. white head, tail and feet.

## Key numbers (px)
- Eagle beak-to-tail length 150 (static frame 0), 149 while moving (frames 2-5) — most reliable size. Bbox height
  changes with wing beat: 162 (f0, wing up) -> 155,139,114,80 -> 37 (f6, wings level). Per-frame dx of body_cx:
  -128.5, -128, -128, -128, -125 (frames 2..6). dy ≈ 0.
- Crow beak-to-tail 89 (frame 0), 88-90 in most frames; 73-78 in frames 2-5 where the thin tail/beak is faint.
  Bbox height 72 (f0), min 28 (f3), max 77 (f9). Per-frame dx centroid: 81,78,78,76,75,79,77,80,80 (mean ≈ 78.4);
  body_cx dx: 82.5,80.5,80,72.5,77,78,78,78,78.5.
- Frame 0 separation: body_cx 411.5 px apart (crow right of eagle), dy ≈ 4 px.

## Reliability / ambiguities
- Origins are not visible; body_cx is ±2-3 px, body_cy ±3 px (crow y wobble 590-597 is probably wing-beat
  segmentation, the origin likely moves even less). Centroid y is biased by the wings — prefer body_cy.
- Motion blur (~128 px/frame for eagle) makes head/tail faint in moving frames; threshold 15 recovers them
  (threshold 40 lost ~10 px of eagle length).
- Side view: no true wingspan visible; bbox width ≈ body length; bbox height reflects wing raise only.
- Edge frames (eagle 7, crow 11) are truncated — do not use their positions/sizes.
- One-frame speeds: the first moving step is frame 1->2; the speed at frame 1 is 0 (identical frames).
- 2D scene: single m/px scale from the prior object applies to both birds (same depth plane assumed; no perspective cues).
