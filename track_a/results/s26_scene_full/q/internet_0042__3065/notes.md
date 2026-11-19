# q3065 – average speed of the white car (m/s)

Prior: white car length = 4.572 m. Internet convention: one planar scale = prior / pixel length.

- Pixel length (bumper to bumper, frames 11-17 when fully visible): 457 px (scene record; checked on a zoomed
  frame 14: rear ~105, front ~559). Scale = 4.572/457 = 0.01000 m/px.
- Reference point = front bumper (visible in all 44 frames): y 152 (f0) -> 1498 (f43), straight motion in y
  (x drifts only 14 px). Mean per-frame displacement = 1346/43 = 31.30 px/frame.
  Second route: rear bumper f11->f43: 1051/32 = 32.84 px/frame; centre 241->1281: 32.5 px/frame (later frames
  are faster: apparent speed rises 28 -> 35 px/frame). My own edge detector (measure.py) reproduces the record's
  rear-edge positions exactly. Camera-stabilised (zoom-out 2.4 % after f24) values are ~2 % lower; the annotator
  convention uses raw pixels, so raw is used.
- Frame rate: file 28.70 fps, question_fps 30. Both give plausible car speeds (9.0 vs 9.4 m/s), so physics cannot
  decide; the clip appears re-timed from 30 fps original footage, and the reference follows the original -> 30 fps.
- Speed = 31.30 px/frame x 0.01000 m/px x 30 = 9.39 m/s (at 28.70 fps it would be 8.99 m/s).

Confidence: moderate; ±4 % from fps choice and reference point.
