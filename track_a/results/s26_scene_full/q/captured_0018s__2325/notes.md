# q2325: distance box ↔ soccer ball at t = 3.0 s (cm)

**Main problem:** the clip has only 49 frames (0–2.04 s, file fps 24 = question_fps). t = 3.0 s is frame 72, which
is not in the video, so the positions at f72 are extrapolated from the end of the clip (f39–48).

## Measurements (scene/ tracks checked against crops in frames/strip.png)
- Box (white_carton): lands f39, tips over to the left, and is lying on its side by f47–48. At f48 its centre is (419, 594)
  and its bottom row is 610. It is still sliding left at about 9 px/frame, so I assume it stops a few frames later at
  cx ≈ 405 (range 400–419).
- Soccer ball: bounces at f39 (bottom row 577, centre row ≈554). A parabola fitted to f40–48 puts the apex at f48.7
  (cy 403) and the next ground contact at about f58. With the observed restitution (rebound height ratio ≈0.52), the next
  contacts are at about f71 and f81, so at f72 the ball is near the ground (cy ≈550). It drifts right at a steady 2.1 px/frame,
  which gives cx ≈595 at f72.
- Ball fall g in pixels (f30–35) is 4.96 px/f², which implies Z ≈2.6 m. That is consistent with depth 2.8 m.

## Scale and geometry (dist.py)
- f = 763 px, pp (640, 360). The ball centre at its bounce is back-projected with D = 2.8 m: Z = 2.69 m, radius 0.081 m,
  so the ground is 0.765 m below the camera.
- Level camera: the people's feet (near person: row 716 at 2.0 m; far person: row 577 at 3.13 m) give the same ground
  height, about 0.845 m, so the camera is level. The ball's 2.8 m sets the absolute scale.
- Box depth comes from where its bottom meets the ground (row 610): Z = 0.765·763/250 = 2.33 m, which puts the box
  centre at (−0.72, 0.72, 2.33) m and its depth at about 2.55 m.
- Ball centre at f72 is (−0.16, 0.67, 2.69) m.

## Result
- Extrapolated case: distance = 0.665 m.
- Sensitivity: ball x 580 → 0.62; box not sliding further → 0.63; ball 41 px above ground → 0.69. A tilted-camera ground
  model (fitted to the near person and the ball) gives box Z 2.41 → about 0.65. If the ball were at the far person's depth
  scale (box Z 2.58, ball 2.69) → about 0.65.
- Answer: **65 cm**.
- If the frame-48 positions are used without extrapolation, the distance is 0.75 m.

Confidence: low to moderate, because t = 3.0 s is outside the clip. The geometry routes agree within ±5%. The main risk is
where the ball is by f72.
