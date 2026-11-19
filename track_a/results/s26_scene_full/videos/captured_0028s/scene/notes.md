# captured_0028s — measurement record (pixels, seconds)

Lab video (Orbbec Femto Mega, 1280x720, 24 fps, 49 frames, 0–2.000 s), background replaced by
Segment-Anything-2 (blue sky; watermark bottom-right). 3D scene. Camera static (phase correlation of the
table region vs frame 0: < 0.15 px horizontally, < 0.55 px vertically). Benchmark intrinsics: f = 763 px,
principal point ≈ (640, 360).

## Objects
- **ball** – small white ball, the only moving object, visible in every frame, never occluded.
  Held still (invisible hand) f0–11 at ≈(718, 312); lifted slowly f12–20 to y≈291; released ≈f21 (t 0.875 s);
  falls and bounces on the table top three times (f26, f36, f47) while drifting right (x 719→766) and
  toward the camera (apparent diameter ≈18 px → ≈27 px).
- **table** – tan wooden top on one pedestal, static. Frame-0 pixels: top surface trapezoid, far edge y≈427,
  x 574–847 (274 px); near edge y≈489, x 464–951 (≈488 px); front face (slab + underside) y≈489–505 (left) to
  517 (right), 498 px wide at y 500. bbox (464,426)–(961,517).
- **table_column** – dark-grey pedestal, x 708–747 (39 px wide), from y≈515 to the image bottom (cut off);
  a darker bracket/shadow x≈650–799, y≈505–515 sits under the top.

## Files
- `scene.json` – inventory, static geometry, camera, events (frame + time).
- `tracks/ball.csv` – every frame: mask centroid (`mask_cx, mask_cy` = reference point, visible centre),
  bbox centre, bbox (x0,y0,x1,y1,w,h), principal-axis length/width and angle, area, equivalent-circle
  diameter, `occluded` (always 0), `overlaps_table_image` (ball's bottom at/below table far edge y 426:
  f26, f36, f37, f46, f47).
- `scripts/track_ball.py` – background subtraction (per-pixel median of all frames in crop x600–900,
  y200–560; |diff|>30, morphology, gated nearest component, holes filled); writes the csv and
  `frames/ball_check.png` (mask overlays, all frames, checked visually: masks cover the whole ball).
- `scripts/static_objects.py` – table/column colour masks at frame 0 and camera-shift check.
- `scripts/probe_colors.py` – colour probe used to reject a simple whiteness threshold (table highlights
  are also low-saturation).

## Events (nearest frame)
| event | frame | t (s) | centre y px |
|---|---|---|---|
| held still | 0–11 | 0–0.458 | ≈312 |
| slow lift (hand) | 12–20 | 0.5–0.833 | 310→291 |
| release / top of first fall | ≈21 (between 20–22) | 0.875 | 291 |
| bounce 1 | 26 | 1.083 | 409 (bottom 426) |
| apex 1 | 32 | 1.333 | 301 |
| bounce 2 | 36 (impact f36–37) | 1.5 | 414 (bottom 436) |
| apex 2 | 42 | 1.75 | 313 |
| bounce 3 | 47 | 1.958 | 436 (bottom 457) |
| end (rising) | 48 | 2.0 | 400 |
Free-fall frame-to-frame centre drops f22–25: 7, 15, 24, 34 px (≈9 px/frame² in image at the start depth).

## Reliability / ambiguities
- Centroid accuracy ≈0.5 px in slow frames (f0–22, apexes), ≈1–2 px in fast frames: motion blur stretches
  the ball vertically (bbox_h / len_major up to 54 px). Use `bbox_w` / `width_minor` as the diameter in
  blurred frames; best unblurred sizes: f0–21 ≈18 px (bbox 19–20 × 16–18), f32 ≈22.5 px, f42 ≈26.6 px.
- f47: the mask is 37 px wide (vs ≈28 neighbours) – the ball on the table picks up a little table/shadow
  difference; centroid x ok to ~1 px, width there is unreliable.
- Bounce frames are the nearest sampled frames; true impact lies between frames (24 fps).
- Ball depth decreases through the clip (size ∝ 1/depth): depth at f42 ≈ 0.68 × depth at f0. The vertical
  pixel motion therefore mixes height change with approach; for metric work use given depth_info and
  back-project with f = 763 px.
- f0–20 motion is caused by an invisible (segmented-out) hand, not free flight.
- No metric scale assumed anywhere.
