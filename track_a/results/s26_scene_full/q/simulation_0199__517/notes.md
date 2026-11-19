# Q517: diameter of the bottle's body (m)

Prior: the droplet's acceleration is 9.7 m/s². No depth_info is given. fps = question_fps = 60, so no re-timing is needed.
I treat the scene as 2D, with one metres-per-pixel scale taken from the droplet's pixel acceleration.

## Droplet pixel acceleration (`acc.py`, using scene/tracks/droplet.csv)
I checked the centroid track from the record against the frames. The droplet is the only moving object and the camera is static.
- **Second differences of the centroid y (frames 0–10):** 31.2, 32.7, 30.5, 33.7, 30.8, 31.0, 29.6, 33.2, 31.2 px/frame².
- **Quadratic fits:** 31.33–31.80 px/frame² for the centroid and 31.69–31.77 for the bbox centre, across the windows 0–10, 2–10, 1–7 and 2–7.
- **Value used:** a = 31.6 px/frame² = 113,760 px/s². The horizontal acceleration is negligible (−0.4 px/frame²).
- **Scale:** 9.7 / 113,760 = 8.53e-5 m/px.

## Bottle body width (`bottle.py`, frame 13, row profiles)
- **Edges:** the strongest gradient on the left is at x = 1701–1707 and on the right at x = 2128–2132.
- **Clean rows:** at y = 900, 950, 1100, 1150 and 1200 the width is 425–427 px. Rows with label text are excluded.
- **Zoomed crop:** confirms the outer silhouette runs from about 1702 to 2130. Width = 427 px (±4).

## Result
Diameter = 427 × 8.53e-5 = **0.0364 m**, about 3.6 cm.

## Check
- **Second route:** the fits over frames 2–10 and over frames 1–7 give 0.0365 and 0.0360 m, a spread of about ±1%.
- **Plausibility:** the label says "30ml". A real 30 ml bottle is about 3.2–3.5 cm across, so 3.6 cm is consistent with the scale.

## Confidence
Moderate to high. The main risk is a depth difference between the droplet's fall plane and the bottle, which a 2D single scale ignores.
