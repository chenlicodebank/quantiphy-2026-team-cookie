# q3110 — height of the person riding the scooter (m)

Prior: average speed of the rider = 3.8 m/s. The video is internet footage at 30 fps (file and question rates match). The rider moves left→right, parallel to the image plane: their apparent size stays constant across the frame.

## Scale (from the prior)
- I used the torso-centroid track from scene/tracks/rider_scooter.csv. It is background-relative (`x_bg_px`, camera drift removed), and I kept only unflagged frames 143–259 (`speed.py`).
- Average pixel speed:
  - net/frames over 143–258: 31.30 px/frame
  - linear-fit slope: 31.7
  - mean of the per-frame speeds after 9-frame smoothing: 31.43
  - I took ≈31.4 px/frame = 942 px/s.
- The rider speeds up, from about 26 px/frame early in the pass to 33 px/frame late. The average depends a little on the window: 30.3–31.7 for windows covering most of the pass.
- Scale = 3.8 / 942 = 0.00403 m/px.

## Height in pixels
- Frame 190 (f190.png, the clearest full view), read on the gridded zoom: cap top ≈ 1058, shoe sole ≈ 1480, so about 422 px. This matches the scene record's 420 px (cap top → shoe sole).
- Height ≈ 421 px × 0.00403 = **1.70 m**.
- Other reading: cap top → ground under the wheels is 450 px, which gives 1.81 m (rider plus scooter deck). The question asks for the person, so I answered with the person's own extent.

## Check
Using the same scale on the scooter:
- length 263 px → 1.06 m (a typical e-kick-scooter is about 1.08 m)
- wheel diameter 55 px → 0.22 m (typical 8.5" wheel = 0.216 m)

Both are plausible, which supports the scale. Confidence: moderate-high, about ±5 %. The main uncertainty is which window the annotators used to average the speed.
