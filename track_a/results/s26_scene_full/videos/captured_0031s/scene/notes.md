# captured_0031s — measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

## Scene
A real recording (Orbbec camera, f = 763 px, principal point ~ (640,360)). The background has been replaced
(SAM2 demo watermark at bottom right), so only the **table top**, its **pedestal** and **two balls** are real.
- **yellow_ball**: larger yellow tennis-type ball. Rests at the far right of the table top (frames 0–14), rolls toward
  the camera and slightly left from frame ~15, reaches the front edge at frame 41, drops off at frame 42, and falls in
  front of the pedestal (frames 43–47, motion-blurred). It is out of view at frame 48.
- **white_ball**: small white/grey ball, left of the yellow one. Rests at frames 0–14, then rolls toward the camera and
  left from frame ~15. It is still rolling on the table at the last frame (48) and never reaches the edge.
- **table_top** (static): brown wood, seen obliquely. **pedestal** (static): dark column, about 40 px wide, cut off by the bottom border.
- No people or other props.

## Files
- `scene.json`: inventory, rest positions, static extents (table corners, edge lengths, front-face thickness,
  front-edge line y(x), pedestal bbox), events, camera check, perspective cues, apparent-size series.
- `tracks/yellow_ball.csv`, `tracks/white_ball.csv` (final): frame, t, cx, cy (visible centre of the sphere, px),
  diam_px, bbox, len_main/width_across/height (for a sphere all = diameter; while falling, len_main = height =
  the blurred vertical streak and width = the horizontal diameter), raw mask extents, occluded flag, state, method, note.
- `tracks/*_v2.csv`: mask-based first estimates. `tracks/*_fit.csv`: edge-circle fits with a score (intermediate files).
- `static_raw.json`: raw static measurements and the per-frame camera-shift check.
- `scripts/`: probe.py and track.py (first attempts), track2.py (masks with a clean background), refine.py (circle fit
  to colour gradients), static.py, assemble.py (final CSVs and overrides), write_scene.py, crops.py (viewer).

## Method and reliability
- Masks: the yellow ball is found by hue and saturation. The white ball is found by difference from a clean background
  made from frames 0–10 (left of x=665) and frame 48 (right of it). The glossy table shows reflections under both
  balls, so the bottom of each mask is unreliable. I refined each centre and diameter by fitting a circle to the
  image edges, using only the upper 300° of the circle. I checked the overlays in all frames, and the circles match
  the ball outlines.
- Accuracy on the table: centre about ±0.5–1 px, diameter about ±1 px. The yellow diameter grows smoothly from 33 to
  57 px; the white one from 20 to 32 px. In frames 0–1 the white ball's centre y reads 1–2 px low
  (exposure/encoding change at the start; it is actually at rest).
- White frame 40: the edge fit failed, so that row is interpolated from frames 39 and 41 (flagged in `method`).
- Yellow frames 43–47: vertical motion blur. The centre is the midpoint of the blurred mask (±3–5 px vertically), and
  the diameter is the mask width (56–61 px, slightly inflated by blur). Frame 47 is cut by the bottom border
  (`occluded`=1), so its cy is uncertain. Frame 42 is the moment the ball drops off the edge (top slightly blurred).
- Motion onset is frame 15 ±1 for both balls; it is clearly visible by frames 16–17. What started the motion is not
  visible (no hand appears; both balls start together, which suggests a tilt or push outside the frame).
- Both balls get closer to the camera as they roll (diameter increases), so the motion is mostly in depth. Use the
  given depth_info and/or the size prior together with f = 763 px: Z ≈ f·D_real/diam_px, and
  X = (cx−640)·Z/f, Y = (cy−360)·Z/f. The ratio of apparent diameters gives relative depth (yellow depth falls to
  about 0.58× its start value by frame 41; white to about 0.62× by frame 48).
- Camera: static. Phase correlation of table patches shows ≤0.15 px variation.
- Perspective: the table top is the only real plane. Extending its side edges gives a vanishing point near (706,354),
  so the horizon is about y=354 if the table is level. The far edge is 271 px long and the near edge 498 px.
  The front face is about 20 px thick.
- Ambiguities: reflections and shadows under the balls (not counted in the sizes); the pale background next to the
  white ball's top edge; blur during the fall. The "white" ball is greyish in shadow.
