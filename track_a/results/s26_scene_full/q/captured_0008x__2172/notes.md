# q_2172 — basketball diameter (cm)

File fps = question_fps = 24, so t = frame/24. Lab camera: f = 0.5959*1280 = 763 px, pp (640,360).

## Method
- Primary frame: t = 1.5 s = frame 36 (first rebound apex, ball momentarily at rest, sharp outline),
  depth_info distance_ball_camera = 1.5225 m.
- Edge profiles in code (`profile.py`: darkness = 255 - min(BGR) on the white segmented background, crossing at
  level 60, through the ball centre; sharp 1-px edges). Overlay `frames/ov36.png` confirms the lines sit on the
  outline.
  - f35: W 114.5, H 112.3; f36: W 115.5, H 114.3; f37: W 114.5, H 115.9 px -> diameter ~114.5 px.
  - The scene record's circle fit (diameter_fit 107 px at f36) is too small: its saturation mask trims the pale,
    washed-out top-left of the ball. Corrected here to ~114.5 px (mask bbox 492-603/606 agrees).
- Naive card formula: D = 1.5225 * 114.5 / 763 = 22.85 cm.
- Exact sphere projection (ball centre 107 px off-axis, cos(theta)=0.990; tan(alpha)=b cos(theta)/f,
  r = d sin(alpha)): D = 22.5 cm.

## Second route
- t = 1.0 s (frame 24), depth 1.401 m: width 121.5 px horizontally (includes ~6 px horizontal motion blur
  while falling) -> naive 22.3 cm (21.6 cm after removing blur); exact-sphere ~21.2-21.9 cm.
- t = 1.2 s (frame 29), depth 1.564 m: width 105.5 px (heavy blur, segmentation edges less reliable) -> 21.6 cm.
- The blurred falling frames are less reliable; the clean apex frame is the main measurement.

## Answer
22.6 cm, between the naive (22.85) and exact-sphere (22.5) values at the apex. That fits a size-6 ball
(22.6-23 cm). Confidence: moderate-high, about ±4%.
