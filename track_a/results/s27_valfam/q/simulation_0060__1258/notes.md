# q_1258 – speed of the yellow car (taxi) at t = 2.5 s (frame 60, question_fps = file fps = 24)

Answer: **4.1 m/s**

## Camera
- Principal point (1080, 540). Horizon row taken from the far-road vanishing point (1207.5, -41.7) from scene/. Two
  hand checks with the lamp rows (top line ∩ base line): -38 (left row) and -34 (right row). I used a horizon of about -40.
- Focal length from the prior (white van a = 4 m/s²), in `calib.py` / `taxi_speed.py`:
  - Route A: put the van wheel-midpoint track on the 3D line through its depth points at frames 14 and 38, then fit a
    quadratic to the path. This gives f ≈ 2276–2300 px for the windows 2–71, 2–27 and 28–71.
  - Route B: intersect the van track with its constant-height plane, anchored by only one depth. This gives f ≈ 2274–2317.
  - So f ≈ 2290 px. The van length is then 661 px·21.5/2290 ≈ 6.2 m, which is plausible.
  - In the image, motion starts at about frame -1, not at frame 1 (frames 0 and 1 are duplicates), so I used the full
    fits rather than "from rest at frame 1".
- Height consistency for objects with two given depths (`plane.py`): the heights agree for f ≈ 2000–2600.
  Ground ≈ 5.2 m below the camera, taxi roof sign 3.45 m below it, taxi centre ≈ 4.2 m below it.

## Taxi speed (main route, `sign_track.py`)
- I re-tracked the taxi's roof sign (rear face) myself in frames 52–71 with a sub-pixel scale+translation template
  (correlation ≥ 0.99). The scene/ "ref" blends a side-face point and a rear-face point, so its x drifts the wrong way
  in frames 57–71 and it gave 3.8–4.0 m/s.
- The sign's height plane comes from the given depths at frames 14 and 38: h = -3.456 / -3.435 m, which agree.
- I intersected the sign rays with that plane. The sign's distance at frame 60 is 31.9 m.
  - Cross-check: the taxi's rear-tyre ground contact (y ≈ 333) on the ground plane lies 1.3 m further back, as expected.
- Per-frame speeds are about 3.7–4.5 (noisy) and the speed is nearly constant. Linear or quadratic fits evaluated at
  frames 59→60 over several windows give 4.06–4.17 m/s at a horizon of -41.7. The result hardly depends on f
  (2233–2370 → ±0.01).
- Sensitivity to the horizon row (`vp_sens.py`): -30 → 4.30, -41.7 → 4.07, -55 → 3.84. It is insensitive to cy.
  With the horizon at about -40 (curb lines plus lamp check), the speed is ≈ 4.1.

## Second route (radial / apparent scale, `taxi_scale*.py`)
- Under pure translation along the road, image points scale about the vanishing point by Z0/Z.
- Sign: v-VP ratio over frames 57→71 = 1.0748, i.e. dlnZ/dt = 0.124 /s. With Z_opt ≈ 31.5 m and the road z-component
  0.968, that is ≈ 4.0 m/s.
- Body-template scale rates are noisier (isotropic 0.140 /s gives ≈ 4.2–4.3; anisotropic sx/sy spread 0.10–0.16).
  This is consistent but low precision.

Confidence: moderate-good, about ±5% (dominated by the horizon row and the depth/plane height).
