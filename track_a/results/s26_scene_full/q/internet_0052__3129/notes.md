# Q3129 — height of the person riding the scooter (m)

Prior: average speed = 2.91 m/s. This is a 2D side view of internet footage, so I used one planar scale, following the annotators' convention.

## Pixel speed
- Rider and scooter move right to left at a uniform speed (from scene/tracks/rider_scooter.csv, frames 0–55).
- Front edge of the scooter, raw pixels: 18.50 px/frame. After stabilisation: 18.67 px/frame. The camera drifts by only ~9 px over the whole clip.
- Rider's body centre: 18.3–18.5 px/frame.
- Value used: 18.6 px/frame × 30 fps = 558 px/s. The file fps and question_fps are both 30.
- Scale = 2.91 / 558 = 0.005215 m/px.

## Rider height in pixels
Measured from the top of the cap to the shoe soles on the deck, on zoomed frames (frames/head*.png, frames/feet*.png):
- frame 0: cap top ≈ 701, soles ≈ 1012 → 311 px
- frame 48: cap top ≈ 683, soles ≈ 1001 → 319 px. The rider stands slightly more upright late in the clip; the record's person_top_y goes from 698 to 685.
- The record's visual value is ≈ 305 px.
- Value used: ≈ 313 px.

## Answer
313 × 0.005215 = **1.63 m**. Across the frames the value ranges from 1.59 to 1.66 m.

## Other reading
If the scooter is included (wheel bottom to cap top, 333–345 px), the value would be 1.74–1.80 m. The question asks for the person's height, so I did not use this reading.

## Confidence
Moderate. The speed and scale are solid, to about 1%. The main uncertainty is the rider's posture, about ±3%.
