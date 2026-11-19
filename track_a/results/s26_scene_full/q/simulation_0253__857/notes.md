# q857 – speed of the box at t = 1.5 s (frame 36), m/s

Prior: box width parallel to the slope = 0.611 m. No depth_info. fps = question_fps = 24, so frame 36 is used,
and speed = |p36 − p35| × 24.

## What the video shows
The camera looks at the box from the side. The large bright face is the box's side face, and its along-slope
extent is the 0.611 m width. The dark strip above it is the top face, seen at a slant. The box's end faces show
up at the ends of the path: the downhill end face early on, the uphill end face after about frame 26. So the
silhouette length (91–113 px) is **not** the width. The record's rect_len (~107 px) mixes in the end faces.

The scene has clear perspective. The side-face length drops steadily from 94.8 px (frame 15) to 79.4 px
(frame 44): a linear fit gives 93.9 − 0.0117·s px, rms 1.1 px. The ramp band also narrows, from 49.5 px to
46.5 px. The pixel acceleration falls from about 930 px/s² (frames 15–26) to about 685 px/s² (frames 28–44).
So a single m/px scale is wrong here, and the scale has to be taken at the box near frame 36.

## Measurements (scripts in this folder)
- `profile_b.py`: rotates each frame by 44.36° about the box centroid and takes the silhouette edges along the
  slope at 50 % of the b* (yellowness) rise against frame 0. Using b* keeps the shadow and the ramp band out;
  the 50 % point is also robust to motion blur.
- `sideface.py`: finds the boundary between the end face and the side face as the strongest luminance step
  inside the silhouette, then side-face length = boundary to far edge. Frames 24–28, 30, 32 and 33 are
  unreliable (no end face visible, or a duplicate frame) and are excluded.
  Frames 34–38 give 83.9, 84.0, 83.7, 82.5 and 83.5 px.
- Track point: the downhill silhouette edge, which is the near side face's leading edge from frame 21 on. It
  sits at the same depth as the side face, so pixel speed / side-face pixel length gives the true speed.
  Frame 27 is a misplaced duplicate (it shows frame 28's position) and is excluded.

## Routes
- **A (local):** quadratic fit of the edge over frames 28–44 gives a 35→36 pixel speed of 1279.7 px/s (the raw
  difference is 1300.5). Side length is 84.6 px from the linear fit, or 83.9 px measured at frames 35–36.
  That gives v = 9.25–9.33 m/s.
- **B (perspective model):** the edge track is fitted with a 1D projective map x = x0 + B·u/(1+C·u) of a
  constant-acceleration motion u = t² + k·t (rms 0.35 px). The metric scale comes from the side-face lengths.
  That gives v36 = 9.43 m/s and a = 7.0 m/s². The model's predicted shrink in scale from frame 22 to 36 (0.908)
  matches the measured side-length ratio (0.915).

## Answer
About 9.35 m/s (A and B averaged). They differ by about 2 %, coming from the side-face length and the
pixel-speed estimate. Confidence: about ±4 %. The main uncertainty is the end-face/side-face boundary under
motion blur.
