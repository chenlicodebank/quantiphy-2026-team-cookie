# q_2738 — displacement of the white ball, 1.0 s → 1.5 s (cm)

Both the file and the question run at 24 fps, so t=1.0 s is frame 24 and t=1.5 s is frame 36.

Method (lab card): focal length f = 0.5959·1280 = 762.8 px, principal point (640, 360). I back-projected each
ball centre along its unit ray and scaled it by the given Euclidean camera distance (1.014 m at t=1.0, 0.737 m at t=1.5).
- Frame 24: centre (542.95, 458.47) px gives P = (-0.1269, 0.1288, 0.9977) m
- Frame 36: centre (497.33, 503.53) px gives P = (-0.1332, 0.1340, 0.7124) m
- Displacement = **28.55 cm**. Almost all of it is the change in depth: the ray-direction terms add only about 0.1 cm.

Centres come from the scene record's edge circle fits. I checked them by drawing the circles on 6× crops
(frames/c24.png, frames/c36.png), and they sit on the ball outline (±1–2 px). A 2 px error changes the answer by
less than 0.05 cm.

Second route (consistency): ball diameter = depth × pixel diameter / f. This gives 4.26 cm at frame 24 (32.1 px) and
4.38 cm at frame 36 (45.3 px), so the two depths agree with the change in image size to about 3%. The answer is
limited by the accuracy of the given depths. Confidence: high.

Script: check.py
