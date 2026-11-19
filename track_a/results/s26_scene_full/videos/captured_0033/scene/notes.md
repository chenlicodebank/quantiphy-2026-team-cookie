# captured_0033 — measurement record

Lab recording, 1280x720, 24 fps, 49 frames (t = frame/24, 0 to 2.000 s). Static camera. Lab intrinsics convention: f = 763 px, principal point ≈ (640, 360).

## Scene
A person in blue denim overalls (face blurred) stands at the left behind a light-brown wooden table that has a single dark central leg. Their right arm is extended and holds a **small white ball** (ping-pong-ball-like) at about (625, 229) px. Over frames 4–8 the hand lifts the ball (centre y goes 217 → 172) and lets go at about frame 9. The ball falls and bounces on the back part of the table top (impact between frames 14 and 15). It rises to an apex at frame 20 (616, 310), bounces again at frame 25 (599, 434), then makes small hops and rolls toward the camera and to the left. It leaves the table's front edge at about frame 35 (457, 495), falls past the front of the table close to the camera (frames 36–37, large and blurred), and leaves the bottom of the image after frame 38. Frames 39–48 contain no ball.

The ball is the only object that moves. The person's arm is nearly still after the release. A "Modified with Segment Anything 2 Demo" watermark is present: the background is blurred and the ball stays sharp.

## Files
- `scene.json`: inventory (ball, table, person, tripod, monitor, walls, left stand), table corner pixels, camera, events.
- `tracks/ball.csv`: one row per frame (0–48). Columns:
  - `visible`, `occluded` (fingers in frames 0–10; bottom border at frame 38), `motion_blur`, `phase`
  - centroid `cx, cy` (the reference point = visible centre)
  - bbox, `area_px`, `eq_diam_px` (diameter of a circle with the same area)
  - `len_main_px` / `width_across_px`: PCA extents along and across the main axis; along ≈ motion direction when blurred
  - `main_axis_deg`, `touches_frame_edge`
- `scripts/`: `common.py` (frame decoder), `track_ball.py` (tracker + overlay), `static_table.py` (table polygon + camera-shift check), `crops.py` (inspection montages).

## Method
- **Ball mask:** pixels that differ from a ball-free background (median of frames 41–48) by more than 30 and have grey level above 140. The mask is limited to a window around rough hand-picked guide positions so the arm cannot be picked up. In frames 0–11 only near-white pixels are kept (B > 150, R − B < 35), which rejects skin. The largest blob is taken. The overlays (`frames/ball_overlay.png`) were checked by eye: the mask covers the ball in every frame.
- **Table:** brown-colour mask on frame 46, approximated by a polygon. The back-left corner was corrected by eye to (462, 430), because the blurred person beside it distorts the mask.
- **Camera:** phase correlation of the wall region against frame 0 gives shifts under 0.15 px, so the camera is static.

## Reliability and ambiguities
- **Ball centre**
  - Frames 15–21 and 25–35 (round, sharp): about ±1 px.
  - Blurred frames 12–14, 22–24 and 36–37: the centroid of the streak is the mid-exposure position, about ±2–3 px. Along-motion length includes the blur, so use `width_across_px` for size.
  - Frames 0–10: the lower part of the ball is hidden by the fingers. The centre is biased upward by a few px and the size is underestimated (17–25 px).
- **Ball apparent diameter:** take `width_across_px`. The mask misses about 2–4 px of soft halo and, in some frames, the shadowed lower rim. Typical values:
  - About 31–34 px near the apex after bounce 1 (frames 17–20).
  - 34–38 px on the table after bounce 2.
  - About 45 px at the front edge (frame 35).
  - About 52–55 px while falling off (frames 36–37).
  - The ball grows because it moves toward the camera. With a given ball size D, depth ≈ 763·D/d_px.
- **Event timing:**
  - Bounce 1 lies between frames 14 and 15. The lowest measured centre (y 404) is at blurred frame 14.
  - Bounce 2 is at frame 25, ±1 frame.
  - Release is at about frame 9, ±1 frame. The highest hand-held position is frame 8.
  - Leaving the table edge is at frame 35–36.
- **Table and perspective:** the table top is a trapezoid. Its front edge (309, 514)–(901, 534) is 592 px long; its back edge (462, 430)–(771, 440) is 309 px. The front face is about 26–31 px thick. Image y on the table maps to depth, so pixel displacements of the ball on the table are strongly foreshortened. 3D positions need depths (back-projection with f = 763).
- **No metric scale is assumed anywhere.**
