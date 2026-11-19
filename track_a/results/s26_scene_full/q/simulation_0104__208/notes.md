# q_208 – diagonal length of the phone (m)

Prior: lifting speed of the charging post = 0.2 m/s. fps = question_fps = 24 (no re-timing).
2D-type scene, static camera; the phone rides on the post head and moves with it.

## Scale (measure.py)
Sub-pixel top edge of the phone, every frame: at rest in frames 0-1, then a constant rise frames 1→27,
mean 23.950 px/frame (std 0.14; total 622.7 px over 26 frames), at rest after that. The post head moves exactly
with it (scene record: head band 1011→389 over the same frames).
574.8 px/s ↔ 0.2 m/s → 3.4795e-4 m/px.

## Phone extent
Horizontal silhouette extent, sub-pixel, on rows through the middle of the phone: x 688.8 → 1256.4 = **567.6 px**
(the same within ±0.1 px in all 31 frames). Thickness 23 px (constant along the length, so no measurable
perspective).
The silhouette has two faces. x 688.8–789.5 (100.7 px) is darker and shows the bottom end of the phone (jack, USB
port, mic, speaker). x 789.5–1256.4 (466.9 px) is the long side with the buttons. So the phone is turned about the
vertical axis and both faces are in view.
For a rectangle L × W turned by θ, the projected length is L cosθ + W sinθ, which is at most the diagonal
sqrt(L²+W²). It reaches that maximum when the view is square-on to the diagonal; then side/end = L²/W². Here the
ratio is 466.9/100.7 = 4.64, so L/W = 2.15, a normal phone shape. That gives L = 514.8 px (0.179 m),
W = 239.1 px (0.083 m) and D = 567.6 px.
Robustness: if the true L/W is anywhere from 1.8 to 2.3, solving L cosθ = 466.9 and W sinθ = 100.7 gives
D = 568–573 px. So the answer depends very little on the assumed shape.

## Answer
D = 567.6 px × 3.4795e-4 = **0.1975 m** (with the 8 mm thickness, the 3D box diagonal is 0.1977 m, a negligible
difference).

## Checks / confidence
- The scale is consistent frame to frame (per-frame rise std 0.6%). The extent is stable over all frames.
- One point does not fit: at this low resolution the jack hole on the end face looks round rather than squashed.
  The geometry above (both faces in view, constant thickness) still requires a turned phone.
- Confidence: good (likely within about 3-5%).
