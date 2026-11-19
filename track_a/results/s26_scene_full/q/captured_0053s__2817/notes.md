# q_2817 – diameter of the white cup's rim (cm)

The shell/Python tool was denied in this session, so I could not run new measurement code. The answer comes from the
pre-existing scene record (scene/static_objects.json, a polynomial-background mask that is accurate to ±1–2 px) and a
visual check of scene/bg_median.png.

- The cup is a small white tumbler with a dark lid, standing upright and static at (564, 424). Its mask bbox is x 552–579,
  so it is 28 px wide (min-rect width 27 px). The lid/rim is at the top and is the widest part, so rim diameter ≈ 27–28 px.
- Lab camera: f = 0.5959 × 1280 = 762.8 px. depth_info: distance_white_cup_camera = 2.516 m (the cup is static).
- Diameter = 2.516 × 27.5 / 762.8 = 0.0907 m ≈ 9.1 cm (9.2 cm at 28 px, 8.9 cm at 27 px).

Second-route check: the same mask method gives the basketball 65.5 px at 2.925 m, which is 25.1 cm, against a real
size-7 ball of about 24 cm. So the masks may be about 1 px wide, which is why I used 27.5 px instead of 28 px.

Confidence: moderate (±5%). The prior (the trashbin's velocity) isn't needed, because the size uses depth_info and the
known focal length.
