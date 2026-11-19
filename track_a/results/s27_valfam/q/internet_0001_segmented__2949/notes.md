# q_2949: speed of the black car (m/s), prior: lane width = 3.66 m

The file runs at 24 fps but question_fps is 30. Camera is static (checked in scene/). The car is scene's dark_car in the lane y 436-538, moving +x.

## Scale
- The lane dashes bounding the car's lane sit at y ≈ 435.5 and ≈ 537.5. I measured them in static_objects.json and checked them on the frame-12 crop (frames/f12.png). That gives a lane width of 102.2 px, so the scale is 3.66 / 102.2 = 0.0358 m/px.
- The other lanes are 102-110 px (mean about 106). Using the mean instead would lower the answer by about 4 %.

## Pixel speed (speed.py, scene/tracks/dark_car.csv, frames 0-29 fully visible)
- File frames 4, 11, 18, 25 and 32 are exact duplicates. hyp.py shows that the distinct content advances at about 20.6 frames per 24 file frames.
- Step between distinct frames: 40.54 px for the centre, 40.58 for the front and 40.50 for the rear. The fit is linear (constant velocity).
- Mean step per file frame including the duplicates: 34.64 px.

## Candidate conventions
- (A) Distinct-frame forward difference × 30 (original 30 fps, every frame distinct): 1216 px/s → **43.6 m/s**.
- (B) Mean per-frame step including duplicates × 30: 1039 px/s → **37.2 m/s**.
- (C) Real-time average at the file's 24 fps: 831 px/s → **29.8 m/s**.

The three routes agree on the pixel track (centre, front and rear give the same step within 0.1 px). The only difference between them is how frames map to time. A single non-duplicate forward difference at 30 fps gives (A) under most hypotheses about the source, but (B) is plausible if the annotator averaged over frames.

## Answer
**39.5 m/s.** I chose this between (A) and (B), which minimises the expected error: within about 9 % of A and 6 % of B.

## Confidence
- The pixel speed and scale are reliable to about 3 %.
- The main uncertainty is the frame-timing convention (±10-15 %).
