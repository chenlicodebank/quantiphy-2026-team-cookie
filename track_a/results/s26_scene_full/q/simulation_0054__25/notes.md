# Q25: length of the orange car (m)

Prior: the orange car's acceleration is -2.86 m/s². The scene is 2D (static top-down camera, everything on the road plane), so I used one m/px scale taken from that acceleration.

## Acceleration in pixels (fit.py)
I fitted quadratics to the orange car's y position against frame number, using the full-view frames 16-90 from scene/tracks/orange_car.csv (track checked by eye on frame 50).
- bbox centre: -0.1811 (f16-90), -0.1767 (16-50), -0.1799 (50-90), -0.1825 (30-70) px/frame²
- mask centroid: -0.177 to -0.180; front edge y1: -0.165 to -0.180; rear edge y0: -0.180 to -0.193
- The deceleration is constant: the cubic term is negligible and the residuals have an rms of about 0.5 px.
- Adopted value: -0.179 px/frame², which is 161.1 px/s² at 30.003 fps. The file rate (30.003) and question_fps (30.0) differ by only 0.01 %, so the choice has no effect.

## Scale
2.86 / 161.1 = 0.01775 m/px

## Length in pixels
- I read the bumper-to-bumper extent along y on frame 50 (y 480 to 769, confirmed visually): about 290 px.
- The min-area-rect length is smallest (289.6-291) when the car is near the image centre (f40-60). It grows to 294-297 near the bottom edge because of slight perspective, and to 300+ near the top because of motion blur.
- Adopted value: 290.5 px.

## Answer
290.5 × 0.01775 = **5.16 m**. The spread is about 5.10-5.22 m from the range of acceleration fits and lengths.

## Checks
- Alternative inputs (acceleration from the mask centroid, 0.1772, with a 291 px length) give 5.20 m.
- The physical scale is plausible: the initial speed comes to about 10.4 m/s and the car width (124 px including mirrors) to about 2.2 m.

Confidence: good (about ±3 %).
