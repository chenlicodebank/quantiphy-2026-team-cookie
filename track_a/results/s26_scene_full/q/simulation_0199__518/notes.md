# q_518 – horizontal width of the "SKYNOVA" text on the bottle

Question: the horizontal width of the "SKYNOVA" text, in metres. Prior: the droplet's acceleration is 9.7 m/s². There is no depth_info. fps = question_fps = 60.

## Scale (2D, from the prior)
- The droplet centroid track (scene/tracks/droplet.csv, frames 0–10) is a clean parabola.
- Quadratic fit from frame 2 gives a = 31.33 px/frame²; from frame 3 it gives 31.26. The residuals are ≤1.2 px.
- The second differences range from 29.6 to 33.7 px/frame² and average about 31.3.
- So a = 31.3 × 3600 = 112,700 px/s², and the scale is 9.7 / 112,700 = 8.61e-5 m/px.
- Sanity check: the bottle body is 427 px wide, which gives 3.7 cm. That is plausible for a 30 ml bottle, so the scene looks like real scale.

## Text measurement (measure.py, edges.py)
- The text is printed vertically, reading bottom to top, on the bottle's front at x ≈ 1784–1823 and y ≈ 814–1141.
- The "horizontal width" is therefore the x-extent of the text, which is the cap height of the rotated letters.
- Route 1 (measure.py): a mask of white, low-saturation pixels on the amber label on frame 12 (checked in frames/textmask.png). It gives an x-extent of 1784–1823, i.e. 40 px.
- Route 2 (edges.py): subpixel half-level crossings in each row, averaged over frames 11–13.
  - Rows through full-height stems: 35.5 px wide.
  - Overall extent, including letter overshoot: 40.2 px.
- Adopted: 39 ± 2 px.
- Width = 39 × 8.61e-5 = **0.00336 m (about 3.4 mm)**. The range is 0.0031–0.0035 m.
- Alternative reading: if "width" meant the text's long run (its vertical extent, y 814–1141 = 327 px), it would be about 0.028 m. Not adopted, because the question says horizontal.

## Confidence
Medium. The assumption is that the droplet and the bottle front are at about the same depth (2D scale). The acceleration is known to about 1 %; the pixel width is uncertain by about ±5 %.
