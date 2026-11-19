# Q31: distance between the two black lamps (m)

Prior: the orange car's acceleration is -2.86 m/s^2. No depth_info. The file fps is 30.0033 and question_fps is 30. Using either rate changes the fitted acceleration by less than 0.03 %.

## Scale (from the car)
- The track is `scene/tracks/orange_car.csv`, cy_best: sub-pixel template matching on the front 136 px of the car (hood and windshield), frames 7-90.
- A quadratic fit of cy(t) over frames 7-90 gives a = -163.9 px/s^2.
  - Frames 7-48 give -163.0 and frames 48-90 give -163.9.
  - A linear fit of the per-frame speeds gives -163.8.
  - The deceleration is uniform. (`measure.py`)
- Scale at the car's tracked surface: 2.86 / 163.9 = 0.017450 m/px. The car then measures 288 x 110 px, about 5.0 x 1.9 m, which is plausible.

## Lamp positions (`discfit.py`, `poles.py`, `overlay.py`)
- The view is top-down with clear perspective.
- Each lamp has a hexagonal head joined by a dark "arm" to a round disc. The head-to-disc direction points exactly away from the image centre (540, 540): the angle mismatch is 0.3 deg for lamp A and 1.2 deg for lamp B.
- The offset ratio k = |head - c| / |disc - c| - 1 is the same for both lamps: 0.200 and 0.196.
- So the "arm" is the vertical pole seen in perspective, the hexagon is the lantern at the top, and the disc is the base on the ground.
- Base discs, from circle fits to the edge facing the image centre (stable over frames 0, 45 and 90): A at (251.6, 465.1), B at (251.9, 909.0), r 11.7 px. They are 443.9 px apart.
- Second route: the head-to-head distance divided by (1+k), 530.2 / 1.198 = 442.6 px. This agrees within 0.3 %.
- The poles are vertical, so the world horizontal distance between the lamps does not depend on where each lamp's origin sits along its pole.

## Perspective correction (car surface vs ground)
- The car template tracks a surface about 0.95 m above the ground: the hood and windshield of a low sports car.
- The scale on the ground plane is therefore larger by H/(H - z_s), where H is the camera height.
- Estimating H:
  - The lamp top is at z/H = k/(1+k) = 0.165.
  - The fire hydrant's dome is displaced radially by about 19 px at 503 px from the centre, so z/H is about 0.036.
  - A typical decorative lamp of about 3.4 m, or a hydrant about 0.75 m tall, both give H of about 21 m (horizontal field of view about 50 deg, which is plausible).
- Correction: about 1.047 for H = 21 m. The range is 1.03-1.065 for H between 18 and 30 m and z_s between 0.8 and 1.1 m.
- Distance = 443.9 px x 0.017450 m/px x (1.03 to 1.065) = 7.96 to 8.25 m. Without the correction (a pure 2D single scale) it would be 7.75 m.

Answer: 8.08 m, a value inside the 7.96-8.25 m range.
Confidence: moderate-high. The pixel measurements are good to under 0.5 %. The main uncertainty is the perspective correction, about ±2 %.
