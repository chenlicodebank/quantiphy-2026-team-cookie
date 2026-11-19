# internet_0040 — measurement notes

Video: 2160x3840 portrait, 28 frames, 24.406118 fps (t = frame/fps). Internet footage, labelled 2D.
Content: a hand pushes a red credit card up and to the left across a pink wall lit by a circular spotlight;
the card decelerates and stops. Camera is static.

## Files
- `scene.json` – inventory, pixel sizes, motion summary, events, camera.
- `tracks/red_card.csv` – every frame 0-27: `cx_mask,cy_mask` (mask centroid), `cx_bbox,cy_bbox` (bbox centre,
  recommended reference point = visible card centre), bbox `x0,y0,x1,y1,w,h`, `minrect_length/width` and
  `long_axis_angle_deg` (cv2.minAreaRect of the mask contour), `median_row_width` / `median_col_height`
  (robust widths, reduced by the thumb notch — prefer bbox_w/bbox_h for size), `area_px`, `visible`.
- `tracks/card_shadow.csv` – bbox of the visible part of the card's shadow (left edge = true shadow left edge).
- `tracks/spotlight.csv` – spotlight disc centroid/bbox per frame (camera-motion check).
- `scripts/track.py` (all tracking + overlays), `scripts/summarize.py` (steps/net/path), `scripts/montage.py`,
  `scripts/probe.py`.

## Method
Card mask = HSV red (S>135, V>150, H<=6 or >=172), open/close, largest component, holes filled (text, chip).
Overlays of every frame were checked: mask covers the card, top/left/bottom edges hit the card edges, the
thumb cuts a notch in the right end but the bottom-right corner remains visible so bbox_x1 ≈ card right edge.

## Key numbers (pixels)
- Card length (long side, horizontal): ~473 px (mean bbox_w frames 18-27, sharp frames; range 450-489).
  Short side: ~298 px (frames 9-27). Aspect 1.59 ≈ standard credit card 85.6x54 mm (if a question gives the card
  length as the prior, use ~473 px; the annotator likely measured the card's length in a clear late frame).
  Frames 0-2 the card looks shorter (388-414 px) and taller (324 px): it is tilted/closer to the camera and blurred.
- Motion of bbox centre: (1491.5,2605.5) at f0 -> (1166.5,2053.5) at f27; net 640.6 px, path 654.5 px,
  direction up-left (dx -325, dy -552). Per-frame steps fall from ~58 px (f1-2) to ~45 (f5) ~25 (f9-11)
  ~17 (f14-17) ~7 (f20-23) ~2-5 (f24-27): roughly steady deceleration, at rest by ~f24 (t≈0.98 s).
  Top-left-corner track gives net 654.6 px and the mask centroid 651.3 px (consistent within ~2%).

## Reliability / ambiguities
- Positions ±3 px in sharp frames, ±8 px in blurred frames 0-8 (blur stretches edges along the motion).
- Card is not strictly planar-motion: its shadow offset halves (200 -> 100 px), so it also moves toward the wall,
  and its apparent height shrinks 324 -> 298 px (~8%) over frames 0-9. Single-scale (planar) conversion is
  the benchmark convention anyway.
- Slight in-plane rotation (-2° -> +2°).
- Camera static: spotlight disc fixed to within a few px (small drift is occlusion by hand, not camera motion).
- Only one card, one hand; no other moving objects.
