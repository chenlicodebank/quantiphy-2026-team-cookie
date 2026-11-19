# q1526 – width of the yellow car (simulation_0150, 3D Blender, 24 fps = question_fps)

Answer: **2.12 m** (body width across the car, the shorter horizontal extent of the bounding box).

## Scale / camera
- The camera is static and level, with the principal point taken as (960, 540) (vanishing point and horizon).
- Tyre (tire.py): in the vertical profile through the near wheel the rim runs from y 731 to 853 (centre y 792), and the tyre's
  bottom edge meets the floor at y 884. That gives a tyre outer diameter of 2 x 91.7 = 183.4 px. The value is the same at
  frame 12 (t = 0.5 s) and in frames 22-27, so the depth is the same during the side-on pass.
- Pinhole fit to prior D = 0.764 m and the depth to the left-front tyre at t = 0.5 s (11.38 m; the wheel is at pixel (1660, 792)):
  f ≈ 2603 px, forward depth of the tyre centre Zt = 10.94 m (the silhouette is taken about 0.1 m nearer, at the tyre's outer side).
- The left-front tyre faces the camera, because the car drives towards image-left. Camera height = 344 px x 10.84 / 2603 ≈ 1.43 m.
  The B1 check is only rough: the back-wall/floor line (~y 700-705, hard to see) gives a wall depth of 22.6-23.4 m, against the
  given 23.44 m.

## Width measurement (main route: depth ratios from rigid side-on translation)
The car's far side is never seen directly. It is measured from the rear wing's two end plates, which sit at the same
longitudinal position and height on the near and far sides of the car (lobes2.py, rows 592-604, sub-pixel yellow edges).
- For a point at depth Z, the image x satisfies u - cx = (Z_rim / Z)(u_rim - cx + D). Here u_rim is the near rear-wheel centre;
  rim.py re-measured it from the rim's horizontal extents, which agree with the scene record to ±1.5 px. Frames where it is
  missing are filled by the scene track scaled by 1.0158 (fit rms 0.6 px).
- Joint fit (joint.py) of the near and far plates' rear edges (frames 21-27 and 31-37, either side of the image centre) with one
  shared offset D: s_near = 0.9717 ± 0.0012 and s_far = 0.8599 ± 0.0010, with D = 243.4 px.
  Fitted separately, the two plates give D = 243.8 and 241.8 px, so the rigid model holds.
- Independent per-frame check: Z_far/Z_near = (u_n - cx)/(u_f - cx) = 1.128-1.132 (frames 22-25) and 1.121-1.124 (frames 35-37).
  The slope fit gives 1.130, which agrees.
- Rim face ≈ 0.105 m nearer than the tyre centre, so Z_rim ≈ 10.84 m. This gives near plate 11.15 m, far plate 12.60 m
  (wing span 1.45 m) and centreline Zc = 11.88 m.
- Width = 2 x (Zc - near body side), with the body side ≈ rim face plus 0.02 m (tyre sidewall or fender bulge): W = 2.12 m.
  Varying the assumptions (rim inset 0.08-0.13 m, body side 0-0.04 m beyond the rim) gives 2.08-2.16 m.
- The side mirror is a small stub (mirror.py). Its slope against the rim is 0.986, which puts it about 0.15 m inboard of the rim
  face, so it does not widen the bounding box.

## Second route (sanity check)
The car resembles a Mazda RX-7 FD (real width 1.76 m, wheelbase 2.425 m, tyre ≈ 0.63 m). Measured here, the wheelbase is
711 px x 10.84 / 2603 = 2.96 m (scale 1.22), and the tyre ratio 0.764 / 0.631 gives scale 1.21. Width ≈ 1.76 x 1.21-1.22 =
2.13-2.14 m, which agrees with 2.12 m.

## Confidence
Moderate to good, about ±4 %. The main uncertainty is how far the near body side sits from the rim face (±0.04 m on the width).

## Corrections to the scene record
- The rim centres in the record are good for frames 14-26 (front wheel) and 22-33 (rear wheel). The record's rear values at
  frames 34-35 are less reliable.
- x_wheelmid follows body patches that move about 1.6 % slower than the rims (the upper body is set back from the wheels), so
  it is not at the depth of the tyre centre.
