# q 3145 – height of the person riding the scooter (m)

Prior: average speed of rider = 4.9 m/s. 2D internet video, 30 fps (file fps = question_fps; no re-timing).

## Method (annotator convention: one scale = prior world value / prior pixel value)
- Pixel speed from scene/tracks/rider_scooter.csv (per-frame |dx| mean x 30), checked against frames:
  bbox centre raw 486.7, torso raw 488.6, bbox centre stabilised 496.8, torso stabilised 498.7,
  front axle stabilised 497.6 px/s. Camera drifts slowly (+0.34 px/frame), so raw vs stabilised differ by ~2 %;
  I used the mean of the raw and stabilised values, 492.7 px/s -> scale 0.00994 m/px.
- Person height = cap top to shoe sole on the deck, read on zoomed grid frames: frame 0 ~279 px
  (818 -> ~1097), frame 45 ~287 px (816 -> ~1103), frame 93 ~292 px (from the record). Mean 286 px.
- Height = 286 x 0.00994 = 2.84 m.

## Checks
- Stabilised-only scale: 286 x 4.9/498 = 2.81 m. Raw-only: 2.87 m. Frame-0-only height: 2.77 m.
- Sanity: 2.8 m is too tall for a real person (the scooter would come out at ~1.85 m long), so the given speed
  is high for this footage (a real 1.65 m person would mean ~2.9 m/s). The prior is taken as exact, as the task says.
- Other reading: rider + scooter, cap top to tyre bottom (~313 px), gives 3.11 m. Not used.

Confidence: moderate. About ±3 % from the measurement itself; the remaining doubt is how the annotator measured it.
