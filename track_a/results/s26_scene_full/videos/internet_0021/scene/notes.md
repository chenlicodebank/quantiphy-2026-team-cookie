# internet_0021 – measurement record

Units: pixels (3840x2160 frame) and seconds. fps = 29.553957, 107 frames (0–106), t = frame / fps.
No metric scale is assumed. Following the internet-video convention, an answering session should take ONE scale =
prior world value / prior pixel value (e.g. airplane length in m / airplane pixel length) and apply it to everything.

## Scene
Sunset sky above a row of city buildings. One airliner (narrow-body twin-jet, B737-like side silhouette, gear down)
flies left→right in side view, at y≈820–870 px, and leaves through the right edge. It is the only moving object
(no birds, cars or people detected). Hand-held camera, slow smooth pan right + tilt up, no zoom.

## Files
- `scene.json` – inventory (airplane + static buildings, red "M" metro sign, trees, sky), events, camera summary.
- `tracks/airplane.csv` – one row per frame 0–106 (`visible`=0 at 106). Columns:
  `cx_bbox,cy_bbox` bbox centre (reference point = visible centre); `cx_mask,cy_mask` mask centroid;
  `x0,y0,x1,y1` bbox (x0 = rear-most point: tail fin / stabiliser tip; x1 = nose tip);
  `bbox_w` = nose-to-tail horizontal pixel length (the "length along the motion direction");
  `bbox_h` = height incl. near wing tip and landing gear; `axis_len, axis_wid, axis_angle_deg` = extents along / across the
  mask's principal axis (axis a few degrees from horizontal while fully visible, so axis_len ≈ bbox_w; meaningless once cut by the edge); `area` mask pixels;
  `cut_by_edge`=1 when the plane touches the right image edge (frames 89–105; then bbox_w, cx, cy are of the visible part only);
  `cam_dx,cam_dy` background shift; `*_bgcomp` = position minus background shift (motion relative to the buildings).
- `tracks/camera_shift.csv` – per-frame background shift vs frame 0: `bg_dx_px,bg_dy_px` (phase correlation on the
  building region y 1300–2100, half resolution ×2) and an independent ORB similarity fit (`orb_scale, orb_rot_deg,
  orb_tx_px, orb_ty_px`, inliers).
- `static_measure.json` – automatic skyline heights and a partial red-sign box at frame 30 (sign box there covers only
  the right half; use the by-eye box in scene.json).
- `scripts/measure.py` (tracking + camera), `scripts/static.py` (static objects + bg-compensated columns),
  `scripts/summary.py` (printout).

## Method
Plane mask = pixels ≥40 grey levels darker than the per-row median of the sky (rows y<1150), closed 5×5, largest
component near the previous position plus nearby fragments. Overlays (frames 0, 15, …, 90, 95, 98, 100, 102) were
checked by eye: the mask covers the full silhouette (fuselage, fin, stabiliser, near wing, engine, gear); edges are
anti-aliased so extents are ±1–2 px.

## Key numbers
- Airplane fully in frame 0–88. bbox_w: 328 px (f0) → 349 (f30) → 364 (f45) → 379 (f60) → 406 (f88), growing smoothly
  (~0.9 px/frame) – the plane gets closer during the pass, so a single scale is an approximation (annotator convention
  is still one scale; the prior's pixel length is most likely measured at a single frame – use the frame the question
  implies, otherwise early/mid frames ~330–365 px).
- Raw image motion of bbox centre: x 1757.5 → 3602.5 px over frames 0–88 (≈17.5 px/frame at start, ≈24.5 at end:
  apparent acceleration is partly perspective growth); y 866 → 837 (slightly up in the image).
- Relative to background (bgcomp): additional +62 px in x and −23 px in y by frame 88.
- Events: nose touches right edge f89 (t=3.011 s); last visible (tail only) f105 (t=3.553 s); gone f106 (t=3.587 s).
  No other events (no landing, no direction change).
- Camera: background moves smoothly to dx −67.5 px, dy +18…+27 px by the end (camera panning right, tilting up,
  following the plane slightly); ORB scale 0.998–1.000 (no zoom), rotation ≤0.26°. Per-frame jitter ~1–2 px.

## Static objects (frame 30, ±5–10 px; buildings extend below frame/trees, so only widths & rooflines are meaningful)
Left grey building x 374–902 (roof ≈1339, antennas to 1217); dark glass apartment block x 902–1930 (roof ≈1425);
low pale houses x 1930–2678 (pitched roof peak ≈1660); right building with lattice tower x 2678–3840 (roof ≈1508,
tower top ≈1301); red "M" metro sign bbox (3242,1660)–(3357,1773), 115×113 px, on a dark pole x≈3290–3305;
far-left brick tower x 0–180 from y≈1615; trees along the bottom (y>2000).

## Reliability / ambiguities
- Plane bbox and tail/nose points: good (±1–2 px). Mask centroid differs from bbox centre by ~10–20 px (wing/gear
  mass); the "visible centre" convention suggests bbox centre. After f88 only x0 (tail) is a valid full-object point.
- x0 switches between horizontal-stabiliser tip and fin tip depending on attitude (few px).
- No motion blur problems; no occlusion except leaving the frame. Plane is far away, so apparent wing span / height
  include the near wing drawn up and the gear; there is no top view (no real wingspan visible).
- Camera shift: phase-correlation and ORB agree within ~3–6 px in x (ORB includes a small rotation term about the
  image origin); phase correlation response drops to ~0.3 late in the clip but values are smooth and consistent.
