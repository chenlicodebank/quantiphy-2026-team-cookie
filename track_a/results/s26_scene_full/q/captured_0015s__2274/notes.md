# q_2274 — shoulder breadth of the person (cm)

Prior: gravity 9.8 m/s^2; depth_info: none. Both the file and the question use 24 fps.
Approach: get a planar metres-per-pixel scale from the toy's free-fall acceleration, then convert the shoulder width in pixels.

## Scale from gravity (fit_g.py, fit_scene.py, tmatch.py, tmatch2.py)
- Free-flight frames: toss 1 is frames 17–21 and toss 2 is frames 53–58 (the toy is clearly off the hands).
- Mask-edge and bbox fits (from the scene record and my own mask) disagree: the top edge gives 3100–4400 px/s^2, the bottom
  edge 1900–2600 and the centroid 2700–3650. The toy's outline changes shape (tail, small rotation), and in toss 2 the
  bottom edge is contaminated by a background seam. I did not use these fits.
- Template matching (normalised cross-correlation of the toy's head and of its whole body, sub-pixel peak) gives fit
  residuals of about 0.1 px:
  - toss 1: a = 2646–2653 px/s^2 for every reference frame, and the head and body templates agree.
  - toss 2: a = 2810–2884 px/s^2 (2789–2869 without frame 58; frame 58 as the reference is an outlier at 3070).
  - Mean: a ≈ 2740 px/s^2, so the scale is 9.8 / 2740 = 3.58 mm/px. Toss 1 alone gives 3.70 mm/px and toss 2 alone 3.46 mm/px.

## Shoulder width in pixels (shoulder.py, frames/mask5.png)
- Person mask = |frame − bg| > 60, taking the run of pixels through the body centre on each row.
- Frames used: 0, 3, 5, 8, 32, 36, 40, 43, 66, 70, 72 (arms down).
- Across the shoulders and upper arms (deltoid level, y = 240–255) the width is 108–112 px; I use **110 px**. Below
  y ≈ 265 the arms widen it. The shoulder curve tops out at y ≈ 230–235 (100–104 px).

## Answer
- 110 px × 3.58 mm/px = **39.3 cm** (outer shoulder width across the deltoids).
- Toss 1 alone gives 40.7 cm and toss 2 alone 38.1 cm.
- Other reading: shoulder points only (acromion), about 100 px → about 36 cm.

## Checks and confidence
- Lab camera (f = 763 px): 3.58 mm/px puts the person about 2.7 m away and makes the person about 1.82 m tall (508 px).
  That is on the tall side, so the scale may be somewhat high.
- The toy is held a little in front of the person's body. That would make the scale on the person's plane slightly larger
  still, which I did not correct for.
- 39 cm is a typical shoulder breadth for an adult woman.
- Confidence: moderate, about ±10%. The two tosses disagree by 7%.
