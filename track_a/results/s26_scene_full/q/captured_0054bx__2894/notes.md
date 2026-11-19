# q2894: white ball diameter (cm)

The video and the question both use 24 fps. Depth of the white ball at t = 1.0 s (frame 24) is 1.235 m. The camera
focal length is f = 0.5959 × 1280 = 762.75 px.

## Method
- Frame 24 is SAM2-segmented, so the background is black. The white ball is motion-blurred into a stadium shape,
  and it touches the yellow/green ball at its trailing end.
- The mask is pixels with V > 40 and S < 70 near the track centre, then an opening.
- The diameter is the width across the blur axis, measured in 2-px slices through the central part of the mask.
  The blur axis was found by scanning angles for the one that gives the smallest width (`measure3.py`): -36°,
  which matches the track's motion direction of -40°.
- Results at f24: median width 43.4 px. Individual chords measured 43.4, 44.8 and 41.8 px; they are drawn in
  `frames/view24.png` and cover only the white ball. Frame 23 also gives 43.4 px, and frames 21-22 give 42-44 px.
- Size = 1.235 × 43.4 / 762.75 = 7.03 cm. The scene record's `wid_minor` of 48.5 px is inflated by the yellow ball's
  rim and the angle, and would give 7.85 cm.

## Checks
- The same method on the green/yellow ball at f24 gives 37.4 px. At its given depth of 1.331 m that is 6.52 cm, which
  fits a tennis ball (6.5-6.9 cm). If anything, the method reads about 2-3% low. Scaling up by that would give
  about 7.2 cm for the white ball.
- The white ball's width drops sharply from f24 (43 px) to f25 (36 px). A linear fit of 1/width against frame over
  f21-34 would give about 40 px at f24, or 6.5 cm. However, the same fit gives the tennis ball only 6.1 cm, which is
  too small, so I trust the direct measurement more.

## Answer
7.1 cm (from 7.0 measured and 7.2 corrected). Confidence: moderate, about ±7%.
