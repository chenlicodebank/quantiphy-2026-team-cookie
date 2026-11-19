# q_2041 — average speed of the white car (prior: lane width = 3.66 m)

## Scale (road.py)
I segmented the asphalt by low saturation across the road in about 45 row bands, on frames 20, 150 and 280.
- Road width: median 78–79 px, so one lane is about 39.2 px. Measured separately, centre line to left edge is 38–39 px
  and centre line to right edge is 39–40 px.
- I checked this on a 6× zoomed crop: asphalt runs from x≈522 to ≈600, with the centre line at ≈561.
- (scene/notes.md says the road is 71 px wide. That figure is too narrow: it is the track region, not the asphalt edge.)
- Scale = 3.66 / 39.2 = 0.0934 m/px.
- Sanity check: by this scale the car is 63 px ≈ 5.9 m long, so the real lane is probably narrower than 3.66 m. The prior
  is exact by convention, so I used it anyway.

## Motion
- Camera: nearly static (drift ≤13 px). I used raw pixels, as the annotators did.
- White car, fully in frame 99–290:
  - scene track, raw: net 9.68 px/frame; mean per-frame step 9.75 (inflated by jitter); stabilised net 9.63.
  - independent check (check.py): bright-blob bbox and centroid every 10 frames from 100 to 290. Net 9.687 px/frame,
    linear-fit slope 9.73.
- The car decelerates gently (≈10.4 → 8.9 px/frame), so the average over the visible span is what is asked.
- Value used: 9.67 px/frame.
- Rate: 30 fps (question_fps); the file's 29.94 differs by only 0.2 %.

## Answer
9.67 px/frame × 30 = 290 px/s; × 0.0934 = **27.1 m/s** (≈97 km/h).

Confidence: moderate. The main uncertainty is how the annotators measured the lane in pixels (±1–2 px of 39 is ±3–5 %).
