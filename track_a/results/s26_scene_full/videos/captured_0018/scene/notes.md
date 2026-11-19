# captured_0018 — measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

## Scene
Static camera (Orbbec, fx ≈ 763 px per the task conventions) looking into a room corner with grey cubicle-panel walls,
grey carpet and a wall-mounted TV at the top centre. Two people stand facing each other with arms extended and
**drop** objects simultaneously-ish:
- **Right person** (nearer the camera; black cap, dark grey shirt, black trousers): drops a **tennis_ball**
  (yellow-green, her left hand, image x≈771) and a **lemon_plush** (yellow plush lemon with two dark green leaves,
  her right hand, x≈881). Release ≈ frame 27 (both at once).
- **Left person** (farther; light top, dark green cargo trousers): drops a **white_box** (translucent white
  rectangular container with label, dark label patch at its lower end, red-orange end visible after landing; her right
  hand, x≈481) at ≈ frame 29, and a **soccer_ball** (black/white, her left hand, x≈541) at ≈ frame 29–30.
All four fall essentially vertically in the image (x drift < 15 px before impact).

## Files
- `scene.json` — inventory (with distinguishing features, frame-0 positions, pixel sizes), camera/perspective
  (horizon y≈342, left-wall vanishing point (1037,342), baseboard lines), events, apparent-size notes, anomalies.
- `tracks/<object>.csv` — one row per frame 0–48 for soccer_ball, white_box, tennis_ball, lemon_plush.
  Columns: `frame, t (=frame/24), phase (held|free), source (template|mask|manual), cx, cy` = reference point =
  visible centre = bbox centre (px); `mask_cx, mask_cy` = mask centroid (mask rows only); `bx0,by0,bx1,by1` bbox
  (x1/y1 exclusive); `bw, bh`; `len_major, len_minor, axis_deg` = PCA extents of the mask (major axis length, width
  across it, axis angle; for held rows the frame-0 extents are copied); `mask_area`; `occluded` (1 = hand overlaps);
  `notes` (hand occlusion, motion blur in px/frame).
- `scripts/` — `camshift.py` (camera-motion check), `track.py` (tracker), `finalize.py` (manual overrides + CSV),
  `overlay.py` / `montage.py` (visual checks), `blobs.py`, `sample_hsv.py`, `pts.py` (timestamps), `baseline.py`
  (perspective lines). `_raw_tracks.json`, `_masks.npz` are intermediate tracker output.

## How measured
- Camera: phase correlation of background regions vs frame 0: < 1.5 px (mostly < 0.5) → static; no correction.
- Held phase (frames 0 → release−1): template matching of the frame-0 patch (score ≥ 0.87); the hands drift a few px
  (tennis ball/lemon move ~7 px up-left over frames 0–26 as the right person's arms rise slightly).
- Free phase: |frame − frame0| > 28 (20 for tennis ball) gated by colour (tennis: H 22–45; lemon: yellow H 20–33 +
  dark-green leaves; ball: white + adjacent black patches; box: white, + red-orange end from frame 38), in fixed
  per-object regions with components assigned by x (box x<508 < ball). Bbox of merged components.
- Manual boxes (read from 3× zoom crops, ±2 px) where the object overlaps the hand/arm or the mask failed:
  soccer_ball frames 29–33, white_box frames 29–33 and 44–45.
- All tracks were drawn on frames and checked visually (boxes cover the right object and its full visible extent).

## Key numbers (px)
- Sizes at sharp frames: soccer ball Ø ≈ 44 (43–46); tennis ball Ø ≈ 23 (frame 0), 24–26 late; white box 23×57
  upright at frame 0, lying on its side at frames 47–48 ≈ 56×29 (long axis 57–58 in both poses); lemon plush with
  leaves 38×68 bbox at frame 0 (body ~27 wide × ~42 tall, leaves add ~22 on top).
- People: left person standing height ≈ 402 px (head top y 173 → soles y 575, frame 0); right person ≥ 622 px
  (head/cap top y≈98, feet cut by the image bottom at 720).
- Floor-contact image heights (bbox bottom): tennis ball 615 (x≈750), lemon 703 (x≈862), white box 598 (x≈485),
  soccer ball 565 (x≈535) — consistent with lemon/tennis (right person) being nearer the camera than the box/ball,
  and the lemon nearer than the tennis ball.

## Events (frame / t)
- 27 / 1.125 s: tennis ball and lemon released (±1 frame; 26 is last clearly-held frame).
- ≈29 / 1.208 s: white box released; ≈29–30 soccer ball released (frame 29 still at rest, 30 is 4–5 px lower).
- 36 / 1.50 s: tennis ball hits floor (lowest centre y 599) and rebounds; apex at frame 45 (centre y 423), falling again 46–48.
- 36 / 1.50 s: lemon hits floor (bottom y 703); bounces back/up and tumbles around (836–855, 596–640) through frame 48.
- 39 / 1.625 s: soccer ball hits floor (lowest centre y 541, bottom 565); rebounds, still rising at frame 48 (centre y 402.5) while drifting right ~+20 px.
- 39 / 1.625 s: white box lands upright (bottom 598), tips over leftward frames 40–46, lies on its side 47–48 at ~(423, 594).

## Reliability / ambiguities
- **Probable dropped frame between 35 and 36**: timestamps are uniform, but every falling object moves about twice
  its expected step 35→36 (ball 26→66→36 px, lemon 54→119 px, box 29→66→45 px), and frame-difference energy peaks
  there. Real elapsed time 35→36 is probably ~2/24 s. Impacts "at frame 36" may thus have happened between the two.
- **Motion blur** is heavy during the fall (10–55 px/frame): blurred objects are elongated vertically (e.g. ball bbox
  height up to 62 vs width 44; tennis ball 16×38). Use widths (across the motion) for size, and bbox centres for
  position; centres are good to ~±3 px in blurred frames, ±1–2 px in sharp ones. Blurred translucent box edges are faint.
- Release frames ±1 frame (hands occlude; objects start with ~zero speed).
- Lemon plush: tumbles after impact so its bbox/centre changes with orientation (leaves sometimes dark/hard to
  separate from shadows); a faint floor shadow sits below it after landing (not included).
- White box: translucent → mask may miss parts; red-orange end included from frame 38. Between frames 40–46 it
  rotates, so its centre shifts partly due to rotation.
- Tennis ball f27 bbox includes a little of the fingers; lemon f27 overlaps the hand.
- Depth: apparent sizes of ball (≈44 px) and box (≈57 px long) stay nearly constant → each falls at roughly constant
  depth; no metric scale is assumed here (use the given priors / depth_info with fx ≈ 763 px).
