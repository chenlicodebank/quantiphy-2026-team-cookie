# q438: speed of the box at t = 1.5 s (frame 36), round 2

Prior: box acceleration at 0.75 s (frame 18) = 2.338 m/s². No depth_info. File fps = question_fps = 24, so frame 36 = round(1.5 × 24).
Scene: 2D-labelled Blender render. A carton falls (frames 0–7), lands on a blue ramp (28.8° in the image), slides
down it, and passes behind the China Food crates from about frame 32. Static camera.

## Crux
Two inputs, both depending on how the box centre is tracked while the box yaws: (1) the pixel acceleration at
frame 18 that sets the scale (C1 594, round 1 625, DeepSeek 700–736 px/s²); (2) the pixel centre speed at frame 36
(C1 1056, C2 881, C3 980, C4 1133, round 1 960 px/s).

## My measurements (own code: track.py, fit.py, fall.py)
- `track.py`: box mask = (brown HSV AND |frame − background| > 25) OR diff > 60. The background is frame 0, with the
  frame-0 box region taken from frame 39. The crate occluder comes from frame 0. Extents along the ramp (u) and
  across it (n). The overlays (frames/mask34.png, mask36.png) show the mask covers the box exactly. The leading
  corner touches the crate top at frame 36, so umax is truncated from 36 on.
- Silhouette length along u: 312 → 281 over frames 12–20 (the box settles in yaw; a right side face is visible),
  281 ± 2 over frames 20–29, then 286, 294, 299, 305, 312, 320 over frames 30–35 (left side face appears, yaw)
  = +6.5 px/frame. Height across u: 184–187, rising to 190–192 at frames 33–36.
- Pixel acceleration (quadratic fits):
  - clean window 20–29 (constant length): midpoint 633, trailing edge 618, leading edge 648 px/s².
  - Trailing edge over windows containing frame 18: 588–624.
  - Midpoint over 14–22: 730–810, biased by the yaw/perspective change of the side face (rejected; see gravity).
  - Adopted a(18) = 620 ± 15 px/s² → scale 3.77 mm/px.
- Free fall (fall.py, template tracking of the box face over frames 0–7, pure translation, rms 0.07 px):
  2552 px/s². Taking this as g gives 3.844 mm/px.
- Centre at frame 36 = trailing edge (never occluded) + half the silhouette length. Trailing-edge steps for frames
  34/35/36 are 35.5/36.2/36.9 px. Length extrapolated linearly or quadratically from frames 30–35 (326–327 at
  frame 36). Centre step at frame 36 = 40.1–40.5 px/frame. Cross-check: midpoint quadratic over 29–35 / 30–35
  gives 40.7 / 40.8, and the directly measured step at 35 is 40.1.
  → v36 = 970 ± 15 px/s (round 1: 960 ± 30, so reproduced).
- Speed: prior scale 970 × 2.338/620 = 3.66 m/s; gravity scale 970 × 3.844e-3 = 3.73 m/s. **Answer 3.68 m/s.**
  If the height growth of 2.7 % over frames 29–36 is approach toward the camera, it changes the speed by under 1 %.

## Rechecks
a. Closure: at the gravity scale (3.844 mm/px) the clean-window slide acceleration of 620–633 px/s² gives
   2.38–2.43 m/s², against the prior 2.338: +2 to +4 %. In reverse, the prior scale gives g = 2552 × 3.77e-3
   = 9.62 m/s² (−1.9 %). The DeepSeek scale (2.338/720) would give g = 8.3 m/s² (−16 %): ruled out.
b. Plausibility: the box is 281 × 186 px = 1.06 × 0.70 m, a large carton, plausible. Friction μ ≈ 0.28. Speed
   3.7 m/s after a ~1.2 s slide at 2.34 m/s² from ~0.9 m/s at landing is consistent (0.9 + 2.34 × 1.2 ≈ 3.7 under
   constant acceleration; the measured centre slows slightly after frame 29).
c. Units: m/s. t = 1.5 s → frame 36 at question_fps 24 (the same as the file fps).
d. Faults:
   - C1 (4.15): its v36 = 1056 px/s comes from front-face texture translation with a constant-acceleration line.
     The measured centre step at 36 is 40.1–40.8 px (963–979 px/s). For 44 px the silhouette would have to grow
     14 px/frame; it grows 6.5. Its a = 594 is close to correct. Its error is +9 % in v36.
   - C2 (2.94): its scale a = 700 px/s² comes from a 12–29 centroid quadratic. My midpoint over 14–29 gives 733,
     but the clean window gives 620–633, and gravity closure rejects 700+. Its v36 of 881 (constant rigid shift)
     is below the measured 963–979.
   - C3 (3.2): its a = 736 has the same bias. Its v36 = 980 agrees with mine.
   - C4 (3.64): a = 728 (biased) and v36 = 1133 (constant-acceleration extrapolation). The errors cancel.
   - Submitted 3.839: a blend of C1 and the DeepSeek median, both with proven faults. It is 4 % above my value.
   - Round 1 (3.6): its fault proof is reproduced (v36 960 vs my 970; a 625 vs my 620). Its value is 2 % below
     mine; it used the prior scale only.

## Decision
The round-1 change is verified. The submitted blend rests on two faulty inputs. My value is 3.68 m/s (prior scale
3.66, gravity scale 3.73). Decision "new" (close to round 1, but no listed candidate's method). Confidence:
medium-high.
