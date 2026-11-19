# q_1708 — length of the eagle (m)

File rate 25 fps, question_fps 24 (frame = round(t*24)); scene/ track frame columns used.

## Scale
- Prior: person speed 1.3 m/s. Person's depth_info is ~constant (139.95 -> 139.98 m) although the body walks:
  origin static, so it gives no direction. Image speed of the person = 1.34 px/frame = 32.2 px/s (human.py).
  If that were all lateral, f = 32.2*140/1.3 = 3470 px -> person height 73 px * 140 / 3470 = 2.9 m (impossible),
  so the person also walks toward the camera (image moves down, consistent with an elevated camera; the height
  trend over the clip, +0.4 +- 1.2 px, is too noisy to resolve the ~1.7 px expected growth).
- Focal from the standard object: person bbox height 73 px median (max 77-78; head top may be 1-3 px higher) at
  140 m, height 1.75-1.8 m -> f ~ 5700-6000 px. With f = 5700 the person's lateral speed is 0.77 m/s and its
  toward-camera speed 1.05 m/s (fits the 1.3 m/s prior).
- An attempt to get f from the boat's vertical image motion + ground plane (boat.py) is ill-conditioned
  (f 8000 to 40000 depending on the boat reference point) and was discarded.
- Check: eagle wingspan peaks (bbox_w at f5-6, 17-18, 31-32, 42-43) x depth (interpolated from depth_info,
  0.396 m/frame toward the camera) ~ 9450 px*m -> apparent span 1.6-1.8 m at f=5700: realistic for an eagle
  with partly curved wings (full span ~1.9-2.0 m). Eagle 3D speed t=1->2 s ~11.7 m/s: realistic.

## Length
The eagle flies mostly toward the camera (depth 139.76 -> 130.25 m in 1 s) and is seen almost head-on in every
frame (frames/bird_big.png): only wings are visible, the body/tail extent along the flight direction cannot be
measured in pixels. Length therefore taken from the measured wingspan scale and eagle proportions
(length/wingspan ~0.42-0.45, real eagles 0.7-1.0 m, typical ~0.85 m): ~0.8-0.9 m.

Answer: 0.85 m. Confidence: low-moderate (not directly measurable; based on scale-consistent wingspan and
standard eagle proportions).
