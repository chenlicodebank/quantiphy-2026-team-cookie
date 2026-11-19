# q2319 – height of the yellow toy (cm)

File fps 24 = question_fps 24. Lab camera: f = 0.5959 x 1280 = 763 px.

Object: a yellow corn-like plush with a dark green leafy top. The near (right) person holds it in her hand next to her body and drops it at f27.
Depth: no depth is given for the toy itself, so I used distance_near_person_camera = 2.002 m (she is holding it).
Cross-check: the toy's lowest ground contact (y≈698 at f36) is at the same image row as her shoes (700–716), so it is at about her depth.

Pixel height (measure.py: HSV yellow + dark-green mask, PCA long axis):
- f26, held upright, leaves up: vertical extent 58 px (y 217–274).
- f0 held: 54 px tall, but the mask picks up part of the arm and the hand covers some of the toy.
- After the bounce, sharp frames f41/f42/f46: long axis 52–53 px. The mask misses about 1 px of blended edge on each side, so about 54–55 px.
  The toy is tumbling here, so its axis may be tilted away from the image plane.
- Falling frames f30–35 have vertical motion blur, so I did not use them for size.
- Adopted: 57 px (upright with leaves, between the two routes).

Height = 2.002 m x 57 / 763 = 0.1496 m ≈ 15.0 cm (range 14.4–15.2 cm for 55–58 px).

Gravity check (accel.py): fitting the pixel acceleration to g gives inconsistent depths, for example 1.87 m for the soccer ball,
which really is at 2.8 m. That is because of a dropped or irregular frame near f35–36, so the gravity prior was not used for scale.
Confidence: moderate. The main uncertainties are the toy's exact depth and whether the leaves count in the height.
