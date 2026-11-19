# q3250 – acorn displacement 2.30 s → 2.40 s (cm)

Time base: file fps = question_fps = 30, so frames 69 → 72. The prior interval 2.00–2.30 s is frames 60 → 69.

Reference point: the stem knob x position, which is sharp and doesn't stretch with motion blur. The bbox centre is
biased because the bbox grows with blur (329 → 367 px), which inflates the apparent acceleration to about 4200–5000 px/s², so I didn't use it.

Measurements:
- scene record, ref (stabilised) stem x: forward velocities v60 = 90.4 and v69 = 127.0 px/frame, so
  a = (127.0 − 90.4)/9 × 900 = 3660 px/s². A quadratic fit over frames 60–70 gives 3420 px/s².
- my own stem tracker (stem.py: dark-pixel centroid in rows 545–585, raw frames): v60 = 89.5 and v69 = 129.0,
  so a = 3949 px/s². The fit gives 3708 px/s². The raw stem x from the record gives 3840 (endpoint) and 3547 (fit).
- The estimates have a spread of about ±7%. Their mean is 3690 px/s², so the scale is 0.77 / 3690 = 2.09e-4 m/px.
- Displacement from frame 69 to 72: ref stem 410.0 px, my raw stem 409.9 px, record raw 411.9 px. The camera drift is
  negligible here.
- Result: 410 px × 2.09e-4 = 8.56 cm. Across the individual acceleration estimates the result ranges from 8.0 to 9.2 cm.

Second check: the displacement is consistent across three tracks (within ±1 px). The answer is limited by the uncertainty in the pixel acceleration.
Sanity check: the acorn length of about 330 px works out to about 6.9 cm, which is plausible for a toy acorn.

Answer: 8.6 cm. Confidence is moderate (about ±7%).
