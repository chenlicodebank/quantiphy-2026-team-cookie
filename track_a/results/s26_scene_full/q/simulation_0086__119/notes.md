# q_119 – width of the car (m)

Prior: car acceleration = 4.03 m/s². 2D top-down scene, 24 fps (file fps = question_fps), so no re-timing.

## Scale from the acceleration (fit.py)
- I tracked the front bumper edge (sharp; the rear edge is motion-blurred) to sub-pixel precision against the empty frame 71, using rows y=620–690, for frames 0–56.
- Quadratic fits of x(frame) give: frames 2–56: 0.5475 px/frame²; 1–56: 0.5466; 5–50: 0.5415; 10–56: 0.556; 2–30: 0.521.
  The per-frame steps grow linearly from about 1 px to about 31.5 px, so the acceleration is constant.
- I adopted a = 0.5475 px/frame² = 315.4 px/s², so the scale is 4.03 / 315.4 = 0.01278 m/px.
- Sanity check: the car length of 438 px comes to 5.60 m, close to a real Cybertruck (5.68 m).

## Width (frame 0, at rest)
- Mask extent across the motion axis, including the mirrors: y 558–746 = **189 px**, which gives **2.415 m**. This is the world-space AABB reading, since the mesh includes the mirrors.
- Body without the mirrors is ≈155 px (1.98 m). Across the front wheel arches it is ≈170 px (2.17 m).
- I answer with the AABB, mirrors included: 2.41 m. Its ratio to the length (0.43) matches a real Cybertruck with mirrors extended (95"/224").

## Check / confidence
- The other frame windows of the fit change a by ±1.5%, which moves the width between 2.38 and 2.44 m.
- The main uncertainty is whether the mirrors count. If they don't, the answer would be ≈1.98 m.
