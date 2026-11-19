# captured_0029x – measurement notes

Lab video (24 fps, 49 frames, 1280x720, 3D), background replaced by black (SAM2 "Modified with Segment Anything 2 Demo"
watermark bottom-right). Content: a hand (masked out) holds a yellow tennis ball near the camera just right of the
front-right corner of a wooden table, throws/tosses it away from the camera onto the far part of the table, and the
ball then rolls leftwards along the back part of the table top, slightly toward the camera, until the clip ends.
Camera is static. Only moving object: the ball. Time t = frame/24.

## Files
- `scene.json` – inventory (ball, hand, table, pedestal), phases, events, camera / perspective info, table pixel geometry.
- `tracks/ball.csv` – final ball track, every frame 0-48: `cx, cy` (visible centre, px), `diam_px` (fitted circle
  diameter, px), `diam_med5` (5-frame running median of diam within phases 0-17 / 18-24 / 25-48, for depth-from-size
  use), `centre_method`, bbox, mask extents (`mask_len_major`/`mask_width_minor` = PCA extents of the mask,
  `mask_height` = bbox height), mask area, `equiv_diam` (=2*sqrt(area/pi)), `occluded` flag and note.
- `tracks/ball_raw.csv` – all raw per-frame alternatives (centroid, min-enclosing circle, full LSQ circle, robust
  circle + inlier fraction, upper-arc circle).
- `table_measure.json` – table silhouette hull / bbox / column extents at frame 45 and per-frame camera shift.
- `scripts/` – `track_ball.py` (HSV mask H 21-45, S>=50, V>=50, circle fits) → `finalize_ball.py` (best estimate
  per frame) ; `table2.py` (table + camera check); `overlay.py`, `draw_track.py`, `view.py` (visual checks);
  `table.py`, `hsvprobe.py` (early exploration).

## Method and reliability
- Ball centre = centre of a least-squares circle fitted to the yellow-mask contour (frames 0-22), a robust
  (outlier-trimmed) circle fit for frames 23-48, and an upper-arc fit for frames 31-32 where a contact-shadow blob
  joined the mask. Overlays checked visually on many frames (circles sit on the ball).
- Frames 0-17 (held): ball's lower part is shadowed and partly hidden by the masked-out hand; the mask is somewhat
  irregular but the circle fit gives a steady ~98-99 px diameter (frames 0-11), centre ±2 px. bbox_w ≈ 110 includes a
  bump at the right side, so prefer diam_px (≈99) over bbox for the held-ball size.
- Frames 18-21: heavy motion blur (ball smeared, plus skin remnants at frame 18) → centre ±5 px, diameter ±10 px
  (frame 18's 106.7 px is inflated by blur). Frames 22-24: mild blur, ±2-3 px.
- Frames 25-48: sharp; centre ±1 px, diameter ±1-1.5 px. The bottom of the ball merges with a dark contact shadow
  on the table's back edge; bbox heights of 54-58 px in frames 31-34, 38, 46 are shadow artefacts – use diam_px.
- Apparent diameter: 99 px (held) → 64 (f22) → 50 (f25) → min ≈41.4 (f29-32, farthest) → 46 (f40) → 51 (f48).
  With the benchmark intrinsics (f = 0.5959·1280 = 762.8 px, principal point ≈ (640,360)), depth ∝ 1/diam_px:
  Z = f·D_real/diam_px for a known ball diameter D_real (not assumed here).
- Camera static: background strip phase correlation shift < 0.3 px for all frames.

## Events (frame / time)
- 0-11 (0-0.458 s): ball held still. 12 (0.5 s): throw motion begins. Release between 17 and 18 (≈0.73-0.75 s).
- 18-24: fast travel up-left in the image / away from the camera; largest per-frame displacement ≈74 px at frame 19.
- ≈25 (1.04 s): ball is on the far part of the table top (no visible bounce; landing moment is ambiguous, ±2 frames).
- ≈30 (1.25 s): farthest from camera (min diameter, frames 29-32); after that the ball rolls left (~10.5 px/frame)
  and slightly toward the camera; still moving at frame 48 (2.0 s).
- Frames 35→36: a 20 px step vs ~10.5 px neighbours – likely a dropped frame in the recording; keep in mind when
  differencing.

## Static objects (frame 45, px)
- Table top (wood): corners back-left (453,450), back-right (915,468, rounded), front-right top (1130,585), front-left
  top (209,540); front-edge bottom corners (210,565) and (1140,623). Front edge ≈922 px long, back edge ≈462, left side
  ≈260, right side ≈245; front edge thickness 25 px (left) – 37 px (right). Silhouette bbox [208,450,1141,623].
- Perspective: side edges converge to ≈(711,355); front/back edges nearly horizontal → table-plane horizon ≈ y 355.
- Pedestal: dark column under the table, bbox [620,613,695,719], ≈60 px wide, cut by the image bottom.

## Ambiguities
- The hand is invisible (segmented out); no hand track. "Release" time is inferred from the jump in ball motion.
- Whether the ball bounced on landing cannot be seen (it arrives at the far edge region where its image y hardly
  changes); the image-y reversal near frame 30 could be the landing/settling or the end of its recession.
- Segmentation artefacts: black notch in the table's near-right corner at frames 18-20; small yellowish shadow blobs
  under the ball on the table.
