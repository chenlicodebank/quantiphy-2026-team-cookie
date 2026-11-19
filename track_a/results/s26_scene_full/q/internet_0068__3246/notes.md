# Q3246 – velocity of the acorn at 2.30 s (internet_0068)

Prior: acceleration of the acorn from 2.00 s to 2.30 s = 0.77 m/s^2. No depth_info. fps = question_fps = 30, so 2.00 s = frame 60 and 2.30 s = frame 69.

## Method (annotator convention: one planar scale from the prior)
- The acorn moves left to right horizontally at constant depth (its height stays ~420 px). It speeds up the whole time (steps grow from ~80 to ~145 px/frame).
- Positions: (a) stem x from the scene record (ref = stabilised, and raw); (b) bbox centre and trailing edge x_min from the record; (c) an independent template-matching track (cap+stem template from frame 64, sub-pixel peak) in `measure.py`. I checked the record's track against the sheet frames, and it is correct.
- Velocity is the forward difference (px/s). The pixel acceleration is (v(2.30) - v(2.00)) / 0.3. Scale = 0.77 / a_px, and the answer is v(2.30) × scale. Since that equals 0.77 × v69 / a_px, the answer only depends on the ratio of the pixel velocity to the pixel acceleration.
- Single-frame differences are noisy (±3 px per point gives about ±15 % in a over 9 frames), and frame 61 looks edited. So `fit.py` fits quadratic and cubic curves to the positions over frames 58/59–72 (leaving out frame 61) for every tracker.

## Key numbers
- v(2.30) ≈ 3830–3940 px/s; v(2.00) ≈ 2620–2770 px/s; a ≈ 3700–4400 px/s^2 (stem tracks ~3800–4000, template ~4100–4200, bbox centre ~4400).
- Scale ≈ 0.19–0.21 mm/px, which makes the 330 px acorn about 6.5 cm long. That is plausible for a toy acorn.
- Velocity estimates: stem 0.74–0.84, x_min 0.79–0.85, template 0.71–0.75, bbox centre 0.69. The median over all fits is 0.754 and the mean 0.759.
- Raw endpoint differences with no fit: ref stem 0.80, raw stem 0.78, template 0.72.

## Second route
The template-matching track is independent of the record's mask and gives 0.72–0.75. The record-based stem and edge tracks give 0.75–0.85. Both agree to within about ±7 %.

## Answer
0.76 m/s. Confidence: moderate, about ±8 %. The result is limited by how noisy the pixel acceleration over only 0.3 s is.
