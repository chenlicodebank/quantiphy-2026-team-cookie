# q_2163: maximum rebound height of the basketball above the desk (cm)

The file and the question are both 24 fps. Lab camera: f = 763 px, principal point (640, 360).
Depth is the Euclidean distance along the pixel ray.

## Time mapping
t=1.0 is frame 24 (ball just released), t=1.2 is frame 29 (one frame before the first impact), and t=1.5 is frame 36
(apex of the first rebound). The apex is confirmed by an image-y parabola fit over frames 32-40, which puts it at
frame 35.56. Frames 35-36 have cy of about 305; checked on a zoomed crop, the centre is about (550, 303).

## Measurements (scripts: measure.py, table2.py, height.py, timing.py)
- **Ball diameter:** from the given depths and the pixel diameters, D = 0.209 m (frame 29) and 0.213 m (frame 36).
  The radius used is 0.1065 m.
- **Desk top:** the four edges were fitted in code on the mean of frames 0-15 (gradient along normals, robust line
  fit, residual 0.3-0.6 px).
  - Corners: NL (430.9, 604.7), LB (478.2, 415.8), FR (690.8, 375.3), NR (756.7, 540.7).
  - The two vanishing directions are 89.8 deg apart, as expected for a rectangle, which validates the fit.
  - Desk normal (up) in camera coordinates: (-0.163, -0.914, -0.371). The camera is pitched about 22 deg down.
  - Desk centre (diagonal intersection) is at pixel (588.8, 465.4). Back-projected with the given 1.725 m, the plane
    through it gives a desk top of 77.3 x 58.4 cm, which is plausible.
- **Ball at apex:** frame 36, back-projected with 1.5225 m to (-0.179, -0.109, 1.508) m.
  - Centre height above the desk plane: **39.8 cm**.
  - Bottom of the ball above the desk: 29.2 cm.

## Second route (gravity prior, timing only)
Image-y parabolas fitted to the fall, the first rebound and the second rebound give impacts at frames 29.71 and 41.26.
That is a flight time of 0.4815 s, so the rise is g T^2/8 = 28.4 cm (27.7-29.2 from the apex to either impact).
The ball centre is then 28.4 + 10.65 = 39.0 cm above the desk. This agrees with the geometry route (29.2 / 39.8),
which confirms the desk depth and the plane.

The ball depth from its pixel diameter at the impact frames (shadow merge and blur, about 102 px) would put the
centre about 5 cm higher. That conflicts with both routes, so it was not used.

## Readings
- Ball centre (the reference convention for positions) above the desk, true vertical: 39.0-39.8 cm.
  - The 3D distance from the ball centre to the desk-centre point is 40.2 cm.
  - The difference in camera Y only (no tilt correction) is 34.4 cm.
- Rise of the ball, i.e. its bottom above the desk: 28.4-29.2 cm.

**Answer: 38.5 cm.** The centre-height reading is taken because the reference positions are clicked object
centres and the question supplies the desk distance. The value is shaded slightly toward the uncorrected-tilt
variant.

Confidence: moderate. The measurement is solid, about ±1 cm within each reading; the main uncertainty is which
reading was intended.
