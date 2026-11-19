# q_2263 - length of the slope (cm)
The slope is the white board the ball rolls down (back-middle of the table). The file and question_fps are both 24.
Method (lab card): f = 0.5959*1280 = 762.8 px, principal point (640,360). I back-projected the midpoint of the board's far (top)
edge and near (bottom) edge with the given depths (slope_far 1.854 m, slope_near 1.701 m) and took the 3D distance.
- I found the edges in code from intensity profiles on frame 43 (measure.py): top edge at x=548 has a dark line at y=306-307,
  and the bottom edge at x=559 ends at y=416-417, where the shadow line starts at 418. Points used: far (548,306), near (559,417).
- Far point = (-0.221,-0.130,1.836) m, near point = (-0.179,0.126,1.687) m, so the length is 0.2994 m.
- Sensitivity: 1 px of edge error changes the length by about 0.2 cm.
Checks:
- The depths are consistent with each other: the board width measured at the top edge (far depth) is 22.5 cm and at the bottom edge
  (near depth) is 22.5 cm. These match, as they should for a rectangle; a 22.5 x 30 cm board is clipboard-sized.
- Kinematics: the prior is a = 4.6 m/s^2. The ball starts moving at frame ~8.5 and reaches the board's front edge at frame ~17,
  so the run is about 0.354 s and s = 0.5*4.6*0.354^2 = 0.29 m. That agrees with the length to within about 4%.
Answer: 29.9 cm. Confidence: good (about 5%).
