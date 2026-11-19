# captured_0038 — measurement record (pixels, seconds; no metric scale)

Lab video, 3D, 24 fps, 49 frames (t = 0 … 2.000 s), 1280×720. The frame has a "Modified with Segment
Anything 2 Demo" watermark: the person's face is an opaque skin-coloured blob and the room background is
blurred. The camera is **static**. Lab convention: f ≈ 0.5959 × 1280 = 763 px, principal point ≈ (640, 360).

## Scene
A white ping-pong-like **ball** starts at rest at the back-left of a wooden table, next to the seated
person's face (x≈278, y≈490). At t≈0.48 s (between frames 11 and 12) the person launches it with a finger
flick (the hand shows at the table edge in frames 12–16; it could also be a blow). The ball rolls to the
right. It passes in front of the card stand, the lying card and the base of the white tumbler without
touching them (frames 29–35). It is still rolling at the last frame, at (968, 514). Nothing else moves except
the person (small head motion, hand raised to the face around frames 24–36).

## Files
- `scene.json`: inventory (ball, person, pink_bottle, white_tumbler, card_stand, lying_card,
  dark_card, table, background) with pixel extents, camera and perspective cues, events.
- `tracks/ball.csv`: one row per frame (0–48).
  - `cx_best, cy_best`: the **recommended reference point** (the ball's visible centre).
  - `cx, cy`: raw tracker values. `tm_cx, tm_cy`: template-match cross-check (frames 14–48).
  - `top_y`: sub-pixel top edge (the most reliable edge). `left_x, right_x, width_incl_blur`: horizontal
    50 % edges, which include motion blur. `shadow_y`: the row of the darkest contact shadow under the ball,
    which approximates the table contact line and sits about 0–8 px below the ball's bottom.
  - `bbox_*`: left_x … right_x × top_y … top_y+38. `blob_h`: height of the bright-pixel blob, which
    understates the size because the ball's bottom is shaded. `occlusion`: notes for each frame.
- `scripts/`: `track_ball2.py` is the tracker and writes ball.csv. `tmatch.py` is the template cross-check.
  `finalize_ball.py` merges the two into cx_best/cy_best; run it after track_ball2.py. `pts.py` checks the
  timestamps and camera shift. `static_edges.py` measures static-object edges from profiles of the median
  frame. `draw_static.py` draws the overlay check. `crops.py` and `profile.py` are viewers. `probe.py` and
  `track_ball.py` are earlier attempts, kept for the record; track_ball.py writes `tracks/ball_raw.csv`, a
  superseded mask that includes the shadow and halo, so do not use it.

## How it was measured
Background is the per-pixel median over all frames; the ball is at rest for only 12 of 49 frames, so the
median contains no ball. The ball is the pixels brighter than the background (signed difference), so its
dark contact shadow is excluded. Vertical size comes from column profiles: top edge to the bottom of the
shaded ball is about **38 px (37–39)** at rest (frame 3), mid-clip (frame 20) and at the end (frame 45).
The centre y is therefore top_y + 19. The centre x is the midpoint of the 50 % left/right edges; motion blur
is roughly symmetric, so this does not bias the centre. The overlays (frames/ball2_*.png) were checked by
eye: the box and centre sit on the ball in every frame.

## Motion summary (pixels; for orientation only, no model fitted)
- At rest, frames 0–11. It jitters by ≤2.5 px in frames 5–11; the left edge is hidden by the face blob,
  so here x = right_x − 18.5.
- Launch between frames 11 and 12. The x steps are 48.5, 32.4, 28.6, 24.0, 20.1, 16.5 px/frame for frames
  12–17, i.e. fast at first and quickly slowing.
- Frames 17–48: a steady ~16.2 px/frame in x and +0.6 px/frame in y (moving right and slightly down).
- **Anomaly: the step from frame 35 to 36 is 31.4 px, twice the steady step.** The tracker and the template
  match agree, and the file timestamps are regular, so one capture frame was most likely dropped
  between 35 and 36. Reference annotations clicked frame by frame would contain this jump too.
  Path-length or speed questions spanning frames 35–36 can show a single doubled step; mention it.
- Apparent size: the vertical diameter stays at about 38 px throughout. The blurred width grows from ~41
  (frames 16–28) to ~43.7 px (frames 39–48), and y and shadow_y increase. Together these suggest the ball
  comes slightly closer to the camera as it rolls right. The table's right side is also closer, since the
  table band is taller there.

## Reliability
- Ball centre in frames 14–28 and 36–48: ±0.5–1 px (tracker and template agree within ~1.5 px).
- Frames 29–35 (in front of the white cards and the tumbler base): ±2 px in x. The tracker's top edge
  failed in frame 35, so that frame uses the template y.
- Frames 12–13: heavy motion blur next to the face blob, ±2–3 px.
- Frames 0–11: x ±1 px (left side occluded); y is fine.
- The 38 px diameter is ±1.5 px (the bottom edge is soft and shaded). With a known ball diameter, use
  the vertical size, not the blurred width. At rest the visible width is 36 px, cut by the face.
- Static extents are from gradient profiles of the median frame, ±2 px. The pink bottle's base is partly
  hidden by the card stand. The table's back edge is soft (±5 px); its left part is near or behind the
  person.

## Ambiguities
- Similar objects: the ball, the white tumbler and the white cards are all white. The ball is the only
  small sphere and the only object that moves.
- The launch mechanism (finger flick or blow) is not certain. The motion starts between frames 11 and 12.
- Shadow: a dark contact shadow lies directly under the ball (shadow_y). It is excluded from the ball
  extents.
- The halo around the resting ball in frames 0–11 is an artefact of the editing; it is not part of the ball.
