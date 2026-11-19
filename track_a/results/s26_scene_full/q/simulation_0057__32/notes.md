# Q32: width of the orange car (m)

The prior is the orange car's acceleration, -2.86 m/s^2. The scene is a 2D top-down view, so one metres-per-pixel scale applies.

## Time base
The file runs at 30.0033 fps and question_fps is 30. The difference is negligible: the acceleration changes by less than 0.03%.

## Pixel acceleration (fit.py)
Source: `cy_best_px` from scene/tracks, which comes from sub-pixel template matching.
- Quadratic fit of y(t): -163.9 px/s^2 over frames 7-90, -164.1 over 17-90, -163.1 over 7-50 and -163.8 over 50-90.
- Second route: a linear fit of the per-frame backward-difference speeds gives -163.8 to -164.2 px/s^2.
- The deceleration is uniform. I use a = 164.0 px/s^2, which gives a scale of 2.86 / 164.0 = 0.01744 m/px.

## Pixel width
- Orange HSV mask (width.py), frames 30-90: the column extent is 112 px, with row maxima of 112-114.
- The mask misses a dark-red rim on the right side. The raw RGB profiles (profile.py, frame 75) show the body edges at x about 294 and 407, so the body is about 113 px wide.
- A soft shadow lies beyond each side and is excluded. The mirrors are small and dark and are not included (the width is taken wheel to wheel).
- I take 113 px, with an uncertainty of about ±1.5 px.

## Answer
Width = 113 x 0.01744 = **1.97 m**. I report 1.96 because the 112 to 113 px range gives 1.95 to 1.97 m.

Sanity check: the length is 288 px x 0.01744 = 5.02 m, which is plausible for a sports car about 1.96 m wide.

Confidence: good, about ±3%. The scale is very consistent across frame windows. The main error is the edge definition of the width, about ±1.5 px.
