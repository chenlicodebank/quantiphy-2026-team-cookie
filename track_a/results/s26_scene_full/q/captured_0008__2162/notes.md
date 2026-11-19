# q_2162 — basketball diameter (cm), captured_0008 (lab, 24 fps; file fps = question fps = 24)

Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Ball depths from depth_info:
t=1.0 s (frame 24) 1.401 m, t=1.2 s (frame 29) 1.564 m, t=1.5 s (frame 36, first-bounce apex) 1.5225 m.
D = 2 d sin(alpha). alpha is the half-angle of the cone of tangent rays, fitted to the edge points
(`edgefit.py`, so the off-axis position is handled). It is also checked as the angle between the left/right and
top/bottom edge rays (`hwidth.py`).

Edge definition: the SAM2 edit blurs the background, which leaves a soft orange halo of several px outside the
ball. A half-max on saturation (`radial.py`) or the steepest drop in S puts the edge in this halo
(frame 36: 116-117 px, too large). The steepest drop of Lab a*+b* follows the sharp boundary of the ball.
`overlay.py` draws circles of 104, 110 and 116 px on frame 36: the 110 px circle sits on the ball edge and the
116 px circle sits on the halo.

Key measurements (a*+b* edge):
- Frame 36 (clean, near zero motion): circle fit 109.4 px, giving 21.5 cm (cone fit). W/H = 111.6/110.0 px gives 21.9/21.7 cm.
  The overlay reads ~110-111 px.
- Frame 24 (vertical motion blur): the horizontal extent of ~118-121 px gives 20.6-21.1 cm. The circle-fit cone gives 20.5-21.0 cm.
- Frame 29 (heavy blur): circle 106.5 px gives 21.1 cm. The horizontal width of 99 px gives 21.8 cm.
- Second-route check: the scene/ record's diameters (fits A and B) are 107.7 px at frame 36 (21.5 cm), 114.5 px
  at frame 24 (about 20.3 cm with the off-axis correction) and 102.5 px at frame 29 (21.0 cm).

Answer: 21.5 cm. The value mainly comes from the clean frame 36; the blurred frames are consistent with it.
Confidence: moderate, ±4 %. The main uncertainty is where the blurred-halo edge lies. The prior (g = 9.8) does not
affect the size.
