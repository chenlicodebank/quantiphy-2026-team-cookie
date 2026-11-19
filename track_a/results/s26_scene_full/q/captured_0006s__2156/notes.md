# q2156 – height of the toy (cm)

The toy is the yellow toy fruit, the only moving object; depth_info calls it the "ball". The file and question_fps are both 24 fps.
Lab card: f = 0.5959 x 1280 = 762.8 px.

## Main route: f24 (t = 1.0 s, Z = 1.402 m)
`measure.py`: I made a background-difference mask (median of f0/f10/f40) and checked its overlay in `frames/m24.png`, where the box
fits the visible outline. Bbox at f24: w = 60 px, h = 56 px (vertical extent; the robust value is also 56).
H = 1.402 x 56 / 762.8 = **10.29 cm**. (Horizontal width 57–60 px gives 10.5–11.0 cm. The major axis from the record, 58 px,
gives 10.66 cm.)

## Check: f29 (t = 1.2 s, Z = 1.065 m)
This frame is motion-blurred vertically, so the bbox height (94 px) is inflated. The record's minor axis across the blur is
72.6 px, which gives 1.065 x 72.6 / 762.8 = 10.13 cm. This agrees with the main route to within about 2%.

## Answer
10.3 cm. The object is nearly round (aspect ratio about 1.05–1.07), so the result barely depends on how it is oriented.
The estimated spread is about ±4%.
