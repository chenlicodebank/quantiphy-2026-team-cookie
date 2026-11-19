# Q30: length of the orange car (m)

Prior: the orange car's acceleration is -2.86 m/s². The scene is a 2D top-down view, so I used one metres-per-pixel scale for the whole frame.

## Pixel acceleration (fit.py)
I fitted a quadratic to cy_best_px from scene/tracks/orange_car.csv against t = frame/fps.
- Frames 7–90 give -163.95 px/s² (rms 0.09 px). Frames 17–90 give -164.17, frames 7–48 give -163.02, frames 48–90 give -163.89 and frames 60–90 give -163.88. The cubic term is about 0, so the deceleration is uniform.
- Second route: the mean of the per-frame speed differences over frames 8–90 is -165.2 px/s².
- I used -164.0 px/s².
- fps: the file says 30.0033 and the question says 30. The difference is 0.02%, which is negligible.

Scale = 2.86 / 164.0 = 0.017439 m/px.

## Pixel length (length.py, independent of the record)
I took the profile of R−B (orange-ness) along columns near the car's axis and found the bumper edges with half-max subpixel interpolation.
- Frames 40, 60, 75, 87 and 90 give 285–289 px. The 279 px values come from an off-axis column at x=320, where the rounded nose is shorter.
- The record's mask median is 288 px. I used 287.5 px.

## Answer
Length = 287.5 × 0.017439 = 5.01 m. If I use the second-route acceleration (-165.2 px/s²) instead, the length is 4.98 m. A sports car about 5 m long is plausible.

Confidence: high, to within about 2%.
