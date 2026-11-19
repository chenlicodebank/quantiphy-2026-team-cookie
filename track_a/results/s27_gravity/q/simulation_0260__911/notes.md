# Q911: width (longer side) of the AC

The scene is 2D, so a single metres-per-pixel scale comes from the prior (the mug's free-fall acceleration is 9.8 m/s^2). The file fps and question_fps are both 30.

## Scale (fit_acc.py)
I fitted a quadratic to the mug track from scene/tracks/mug.csv over the free-fall frames, before impact at frame 16:
- ref_y, frames 5-15: a = 6155 px/s^2, rms 0.48 px, release time t0 ≈ 0. This is the value I used.
- bottom y1, frames 3-15: a = 6198 px/s^2.
- ref_y, frames 7-15: a = 6118 px/s^2.
- top rim, frames 5-15: a = 6080 px/s^2. This one is noisier because the apparent height changes with perspective.

Scale = 9.8 / 6155 = 0.001592 m/px. The spread between routes is about ±1 pct.

## AC width (ac_measure.py, frame 30, plus 6x zoomed crops of both top corners)
- The left edge of the white LG outdoor unit is at x ≈ 131.5 and the right edge at x ≈ 637.5.
- Rows 820 and 860 give gradient edges at 131 and 637, and the white mask spans 132-636.
- Width = 506 px, which matches the record's 506 px.
- Width = 506 × 0.001592 = 0.806 m. The other acceleration routes give 0.800 to 0.811 m.

## Plausibility check
- The resting mug is 56 px tall and its body is 48 px wide, which comes to 8.9 cm and 7.6 cm: a realistic mug.
- 0.81 m is within the typical width of an LG outdoor unit (about 0.77-0.87 m).
- The AC sits slightly in front of the table, but the 2D convention uses one scale.

Answer: 0.806 m. Confidence: good, about ±3 pct.
