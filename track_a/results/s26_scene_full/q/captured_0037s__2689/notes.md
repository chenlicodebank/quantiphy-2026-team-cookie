# q 2689 – height of the glass jar (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). Static camera, f = 0.5959*1280 = 763 px, c = (640,360).
Jar depth (depth_info, t=1.0 s): 1.008 m. The jar is static.

## Scale check (prior)
Ball (4 cm) at frame 24 (apex, no vertical blur), depth 1.055 m: expected 763*0.04/1.055 = 28.9 px.
Measured vertical extent in code (ball_view.py) is ~29 px (rows 338-367). So f = 763 and the depths agree.
(The ball sizes in scene/tracks/ball.csv, ~25 px, are too small: that mask threshold drops the shaded lower edge.)

## Jar pixel measurements (jar_width.py, jar_profile.py; median/clean frames 0-6)
- Top of lid (half-max against the green): row 407.6 (same in 4 columns).
- Front bottom edge (dark contact band 478-485, table from ~487): row 484.5 (range 483.5-486).
- Width (half-max against the green, rows 416-449): 56 px, so R = 1.008*28/763 = 3.70 cm. (The scene.json box,
  64 px wide, is too wide.)
- Raw vertical extent = 77 px, so the naive card value is 1.008*77/763 = 10.16 cm (10.36 if the bottom is at 486).

## Perspective correction (jar_model.py)
The camera looks down on the jar. The image top is therefore the BACK rim of the lid, and the image bottom is the
FRONT rim of the base, so the raw extent includes half of each end ellipse. I modelled a pinhole cylinder: centre at
1.008 m on its pixel ray, axis along the table normal, and the camera pitched down onto the table by t. I solved for H
so that the projected top and bottom rows match the measurements.
- Tilt t, from three estimates: card->tape 3D vector from the depth_info gives 3.7-4.9 deg; the white cup's thin rim
  ellipse gives ~2 deg; the visible lid-top ellipse (~6-8 px) gives ~2.5-4 deg (the model predicts 5.8/6.9/7.9 px for
  2/3/4 deg).
- H = 8.81 / 8.71 / 8.61 cm for t = 2/3/4 deg (bottom row 484.5), and 9.00 / 8.89 / 8.79 cm with bottom row 486.
- Rounded lid edge and heel (effective rim radius smaller than R) add ~+0.1-0.2 cm.

## Answer
H ≈ 9.0 cm (route range 8.6-9.2). The uncorrected card value is 10.2 cm. I answer with the geometrically corrected
value, because the reference is a ruler measurement of the real jar (7.4 cm diameter x 9 cm is a plausible jam jar).
Confidence: moderate. The main uncertainty is the end-ellipse correction (~±0.3 cm), plus ±1 px on the edges.
