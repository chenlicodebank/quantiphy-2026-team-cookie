# q_2695 – height of the glass jar (cm)

Lab video, 1280x720, 24 fps (file fps = question fps). Lab method card: f = 0.5959 x 1280 = 763 px, depth of the jar at t=1.0 s = 1.008 m.
The jar is static (scene record: camera static, jar does not move).

## Measurement (jar_measure.py, zoom.py)
- I used the median of frames 2, 5 and 24 (and 40, 44, 48 for the zoom views) so the ball doesn't get in the way.
- Top of the lid against the black background: the first row brighter than 60 is y = 408 in the middle columns
  (409–411 at the rounded corners). The lid's top ellipse is very thin (about 3 px). The cup rim ellipse is also almost flat, so the camera is close to lid height.
- Bottom: the dark outer bottom edge of the glass against the table is at y ≈ 484–485 (zoomed, contrast-stretched view jar2.png).
- Pixel height (bbox) ≈ 76 px (±1.5). Width ≈ 57 px, which gives a diameter of ≈ 7.5 cm, a plausible jar.

## Result
H = 1.008 m x 76 / 763 = 0.1004 m ≈ **10.0 cm**.

## Checks
- Front-to-front reading: lid front edge ≈ 411 to bottom 484 is 73.5 px. With the front-surface depth (≈0.97 m) that gives ≈ 9.4 cm.
  With the centre depth, as the method card says, it gives 9.7 cm. Answer kept at the bbox/method-card value.
- Scale check with the ping-pong ball at t=1.0 s (frame 24): the predicted diameter is 0.04 x 763 / 1.055 = 28.9 px. Measured: bbox about 30 px
  (with some blur), minor axis 24.6 px. That agrees within about 10%, so the f / depth scale holds.
- Confidence: moderate-high. The edges are uncertain by ±1–2 px, which is ±2–3% of the height. The ambiguity in the reading (silhouette vs front edge) is ~4%.
