# captured_0038s — measurement record (pixels, seconds; no metric scale)

Lab video (24 fps, 49 frames, 1280x720, 3D). The real background was replaced with green by Segment Anything 2
(watermark bottom-right). Camera static (phase correlation shift <= 0.13 px in every frame). Per benchmark: fx ~ 763 px,
principal point ~ (640, 360). t = frame/24.

## Scene
A square wooden table on a black pedestal, seen obliquely. On it (static): pink bottle, white cup, a card tent
(two leaning playing cards) with flat cards in front of it, and a dark blue card with a yellow sticker near the front
edge. The only moving object is a **white ball** (ping-pong-like). It rests on the far-left corner of the table, is
launched rightwards between frames 11 and 12 (the striker was removed by the segmentation and is not visible), slows
quickly over frames 12-16, then rolls at a roughly steady ~16 px/frame across the table. It passes **in front of** the
card tent/flat cards (f29-34) and the white cup (f34-37), and is still rolling at frame 48. There is no bounce or impact.

## Files
- `scene.json`: inventory, static object boxes, camera/perspective notes, events.
- `tracks/ball.csv`: one row per frame (0-48). Columns: `cx, cy` = visible ball centre (bbox centre of the mask:
  pixels brighter than the median background by >10 grey levels, so the dark contact shadow is excluded);
  `cx_tm, cy_tm` = template-matching centre (smoothest frame-to-frame, but ~3 px **above** the true centre because the
  template centre was the bright upper part; add ~+3 px to y for absolute use); `cx_centroid, cy_centroid`; bbox;
  `width_px` (horizontal = motion direction, includes motion blur), `height_px` and `max_col_height` (vertical,
  blur-free → apparent diameter); `occluded` (always 0: the ball is never behind anything); `mask_unreliable` + `note`.
- `tracks/ball_raw.csv`: first-pass mask (bright + differs from background); its centroid is biased up, kept for reference.
- `scripts/`: probe.py (background + camera check), track_ball.py (first pass), refine_tm.py (template matching),
  build_track.py (final track), static_objects.py, view.py / check_overlay.py / profile.py (visual checks).
  Scripts write scratch to `frames/` (bg.png and tm.npy are needed by later scripts).

## Ball numbers (pixels)
- Rest position f0-4: centre ~(277, 492). Frames 5-10: small shift ~3 px left and back (pre-launch contact), f11 ~(276.5, 491.5).
- Per-frame centre step (template track): f11→12 ~47-52 (heavy blur), then 33, 29, 25, 20, then ~16 ± 0.5 px/frame from f16 to f48.
  f35→36 is ~33 px (twice normal) in both trackers — most likely a **dropped frame** in the recording; treat with care
  (an answer using per-frame speeds there may need to split it over two intervals).
- Path: x 277 → 968, y 492 → 511 (moves right and slightly down in the image, i.e. slightly toward the camera).
- Apparent diameter (vertical): ~40-41 px at rest (rest mask clipped on the left by a segmentation artefact),
  37-38 px for f15-28, 35-36 px for f38-48 → ball slowly moves away from the camera in depth while crossing (or apparent size
  drops ~7%); horizontal extent ~53 px while moving because of blur.

## Static objects (median background image, ball removed), bbox x0,y0,x1,y1
pink bottle 636,332,687,477 (52x146); white cup 724,378,794,497 (71x120); card tent ~655,415,712,498 (~57x83, hand-corrected);
flat cards 645,495,743,515 (99x21); dark card 519,533,619,551 (101x19); table top 208,450,1141,623 with corners ≈
back-left (455,450), back-right (915,465), front-left (210,540), front-right (1140,590); edge thickness ~22-30 px;
pedestal 605,590,719,719 (column ~57 px wide).

## Reliability
- Ball centre: ±1 px in clean frames (f0-5, f15-28, f38-48). f12-14: heavy blur, ±3 px. f29-37: ball over white
  cards/cup, mask edges merge (height_px up to 44 there is wrong); use cx_tm/cy_tm (+3 px in y), ±2 px.
  f6-10: mask leaked into the table, box copied from frame 0 shifted by the template shift.
- Static boxes ±2-3 px; card tent and table back edge are hand-adjusted from the grid view.
- Ambiguities: green background is synthetic (no shadows/scale there); segmentation artefacts at the ball's left at rest
  and around the table corner during launch (f12-14); probable dropped frame at f35-36.
