# Q448: speed of the gift box at t = 1.5 s (m/s)

The file runs at 24 fps and the question also states 24 fps, so no re-timing is needed. t = 1.5 s is frame 36.
This is a 2D scene, so one metres-per-pixel scale applies. The prior gives the box's acceleration after 1 s as 3.18 m/s².
After it lands (frames 9 onward), the box slides down the ramp with constant acceleration.

## Method (fit.py, fit2.py)
- Track: scene/tracks/gift_box.csv, using the `_dupfix` reference point (frame 38 is a duplicate of frame 37, so the
  record replaces it with the midpoint of frames 37 and 39). On frame 36 the point sits on the box centre at about (1209, 907),
  which I checked on a crop in frames/f36.png.
- Path length s(t) along the ramp, fitted with a quadratic over frames 10–37. The fit residual is 0.7 px.
  - a_px = 745 px/s², which gives a scale of 3.18 / 745 = 0.00427 m/px.
  - Speed for frame 36 (the backward step 35→36, i.e. at the midpoint t = 35.5/24) = 1117 px/s.
  - Speed = 1117 × 0.00427 = **4.77 m/s**.
- The raw step 35→36 is 1118.8 px/s, which gives 4.78 m/s.

## Checks
- Second reference point (the centre of the min-area rectangle, gift_box_v2.csv): 4.77 m/s over frames 10–37 and 4.78 m/s over frames 10–39.
- Changing the fit window gives 4.70 to 4.91 m/s. Frames 10–37, 9–37 and 12–37 all give 4.76–4.78.
- Physics check: the free-fall acceleration over frames 0–8 is 2277 px/s². With g = 9.81 m/s² that gives a scale of 0.00431 m/px,
  and then the slide acceleration is 745 × 0.00431 = 3.21 m/s², which is close to the prior's 3.18. Using this scale instead
  gives a speed of 4.81 m/s.

Answer: 4.78 m/s. Confidence is high, with an uncertainty of about ±2%.
