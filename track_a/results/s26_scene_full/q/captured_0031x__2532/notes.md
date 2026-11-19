# q2532 — diameter of the white ball (cm)

Prior: tennis ball diameter 6.7 cm. depth_info at t=1.6 s (frame round(1.6*24)=38): tennis 1.190 m, white 0.994 m.
File fps = question fps = 24. Lab camera f = 0.5959*1280 = 763 px.

## Measurement (measure.py, overlay frames/fit38.png)
Circle fit to the upper/side mask contour (bottom shaded/reflection unreliable), frames 34-42:
- frame 38: yellow 52.9 px (bbox width 56 incl. outline), white 24.3 px (bbox width 25; edge with outline ~25-26 px).
- scene/ record: white 25 px, yellow 54 px at frame 38 — consistent.

## The depth_info labels look swapped
- Method card as given: tennis = 1.19*52.9/763 = 8.25 cm, 23 % off the exact prior 6.7 -> inconsistent.
- In the image the white ball's table contact point (v~456) is higher than the yellow ball's (v~479), so the
  white ball is FARTHER from the camera than the yellow, opposite to the labels. Ground-plane ratio
  (479-360)/(456-360) = 1.24 ~ 1.19/0.994 = 1.20.
- Swapped: tennis = 0.994*52.9/763 = 6.89 cm (3 % off 6.7, good); white = 1.19*25/763 = 3.90 cm
  (25.5 px edge -> 3.98 cm). Scaled by the prior: 6.7*(25/52.9)*(1.19/0.994) = 3.79 cm.
- Labels as given: white = 0.994*25/763 = 3.26 cm, or via prior ratio 2.64 cm — these two routes disagree by 20 %,
  while the swapped reading is self-consistent and matches a standard 40 mm table-tennis ball.

## Answer
4.0 cm (swapped-depth reading; range 3.8-4.0 across routes). Alternative under literal labels: 3.26 cm.
Confidence: moderate-good.
