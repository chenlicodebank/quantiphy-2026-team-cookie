# q_3162: height of the person (m). Prior: g = 9.8 m/s^2

The time base is 30 fps. File rate and question_fps agree, and the result is a plausible human height.

## Scale from gravity (fitg.py)
I fitted a quadratic to the ball's vertical pixel position (scene/tracks/ball.csv; bg-fixed and raw both checked):
- Shot flight, frames 55–95, excluding the degraded frames 73–77: 1855 px/s² (bg) and 1849 (raw). Residuals are about 1.5 px.
- Halves of the shot: 1897 (55–72) and 1802 (79–95).
- Bounce arcs: 1884–1894 (99–133), 1840–1852 (137–162) and 1885 (166–185).
- Using the main shot gives g_px ≈ 1855 px/s², so scale = 9.8/1855 = 5.28 mm/px. Across all arcs the
  range is 1840–1894, which is ±1.5 %.

## Person height
The person stands still in frames 0–38. Pixel height, cap top to sole: median 322 px (record), range 316–325.
I checked by eye on a zoomed crop at t = 0.5 s: the top is at ≈580 and the soles at ≈900, so ≈320 px.
Height = 322 × 0.005283 = 1.70 m.

## Check
With the same scale, the ball's free-flight diameter of 46 px gives 0.243 m. A real basketball is 0.24 m, so the
scale is consistent. The person and the ball are at about the same depth.

Answer: 1.70 m. Confidence is good, about ±4 %. The spread in g and the head outline (cap or blurred face) are the
main uncertainties.
