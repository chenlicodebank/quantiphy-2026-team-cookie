# q3195: width of the acorn (cm). Prior: g = 9.8 m/s^2

## Geometry / time base
- The clip is rotated. Image +x is "down": the toy is released from the hand at frame 38/39 and accelerates in +x
  (per-frame steps 42 -> 92 -> 142 -> 168 -> 196 -> 231 -> 264 px) until it lands on the backrest/rail at frame 45.
  So the chair has been tipped onto its back, and frames 39-45 are free fall in the image plane.
- fps: the file is 30.013 and question_fps is 30, a negligible difference. I used 30.

## Pixel acceleration (measure_fall.py)
- On a central row band I found the 50% crossings of the blurred profile: the dome's leading edge (R), the
  cap/dome junction (L) and their midpoint, for frames 38-46.
- Quadratic fits give: mid 30.9-32.6 px/frame^2, L 33.0-35.8 and R 28-32 (windows 39-45, 40-45 and 41-45).
  Adopted value: 32.5 px/frame^2 = 29250 px/s^2.
- Scale = 9.8 / 29250 = 3.35e-4 m/px (0.0335 cm/px).

## Pixel width (view_crops.py, measure_width.py; the record's scene/tracks/ball.csv was used for frame 0)
- The width is the diameter across the toy axis. The toy axis is horizontal while it falls, so the width is the
  image-y extent. That extent has no motion blur, because the motion is along x.
- The toy moves away from the camera while it falls, so its apparent size shrinks:
  - Dome/cap junction: about 255 px (frame 38), 245 (40), 225 (42), about 215 (44).
  - The whole toy including the cap is about 5% wider: 268 px at frame 0 in the record, 266-270 px in held
    frames 30-38 by silhouette.
  - On the seat afterwards it is about 210-220 px.
- I used one scale, following the annotators' planar convention, and measured the width in the middle of the fall
  window, where the acceleration was measured: whole toy about 238 px at frames 41-42.

## Answer
238 px x 0.0335 cm/px = 7.97 cm, rounded to **8.0 cm**.

The answer depends on which frame's pixel width is used:
- Held frame 0 (268 px): 9.0 cm.
- End of the fall or on the seat (215-220 px): 7.2-7.4 cm.
- Mid-fall (adopted): 8.0 cm. This is within about 12% of both extremes.

## Checks
- A perspective-corrected route uses position in units of the toy's own width, (x - cx) / s, frame by frame. It
  gives about 0.185 widths/frame^2, i.e. width ≈ 5.9 cm. It is very sensitive to the noisy size readings and to the
  toy tilting, so I did not use it.
- Real-world check: an Apple Watch case at frame 115 is about 101 px tall (40-45 mm) near seat depth. That suggests
  about 0.42 mm/px there, i.e. a toy about 9 cm wide. This is somewhat larger than the gravity scale gives.
- Confidence: moderate. The main uncertainty is which pixel width the annotators used (about ±12%), plus about ±5%
  on the pixel acceleration.
