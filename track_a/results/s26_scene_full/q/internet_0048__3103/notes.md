# q3103: width of a single wall pad (cm). Prior: g = 9.8 m/s^2

Time base: the file and the question both run at 30 fps. At 30 fps the ball's arc gives a plausible ball size
(see below), so 30 fps is used.

## Scale from gravity (fit_g.py)
The ball's centre y from scene/tracks/ball.csv was checked against frames (scene/notes.md: clean mask, ±1 px).
A quadratic fit of y(t) over the free flight between release and bounce (frames 36–60) gives:
- raw pixels: 3729 px/s^2 (rms 0.6 px);
- camera-compensated (bg0): 3713 px/s^2;
- sub-windows: 3694–3787 px/s^2;
- mean of the second differences: 3772 px/s^2.

Adopted value: 3720 px/s^2, so scale = 9.8 / 3720 = 2.634 mm/px.

## Pad width (seams.py)
Dark seams were located in code from intensity profiles at several heights, in frames 0 and 20. The 8 panels span
x ≈ 99 → 1824 at y = 550, which is 215.6 px per panel. The average is 213.8 px at y = 250 and 216.6 px at
y = 700, and single panels range from 210 to 222 px. Adopted width: 215 px.

Width = 215 × 2.634 mm = 56.6 cm.

## Checks
- Ball diameter 94 px × 2.634 mm = 24.8 cm, against a real basketball's 24.3 cm. The gravity scale is
  consistent, so the ball flies close to the wall plane.
- Second route, using the real ball size as the scale: 215 / 94 × 24.3 = 55.6 cm.
- Real gym wall pads are often 2 ft (61 cm) wide, so the result is plausible.

Confidence: about ±4 %.
