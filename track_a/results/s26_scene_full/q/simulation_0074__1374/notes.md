# q1374 – width of the white car (van), prior: length = 6 m

The "white car" is the white Chevrolet-Express-style cargo van (scene record calls it `van`). 3D Blender scene,
static camera, 24 fps (file fps = question fps).

## Camera calibration
- kerbs.py / calib.py: fitted 6 kerb edges (two road directions A, B), vanishing points
  A = (2683,-257), B = (-1305,-262), f = 1785 px assuming orthogonal roads, principal point at the image centre.
- poles.py: vertical VP from 3 poles = (1070, 4568). Independent f from vertical VP + horizon = 1794 px;
  from vertical VP + VP_A / VP_B = 1796 / 1791. The calibration is confirmed (hfov ~62 deg, tilt 24 deg).
- heights.py: with the given depths, origins of the pedestrian, taxi, van and cyclist come out ~8.5-8.9 m below the
  camera and feet/bottoms ~9.5-9.7 m below it, so the camera height is ~9.65 m. That is consistent.

## Van geometry (scale-free, from silhouette tangents)
- The van drives straight along road direction A (heading constant: near-wheel ground contacts at f71 give yaw
  -179.9 deg, and the f14/f38 depth positions keep the same lateral Y).
- azim.py: shadow-free silhouette per frame. A vertical world line has a constant ground azimuth, so the
  silhouette's max azimuth is the front-far footprint corner (the far end of the front bumper) and its min azimuth
  is the rear-near corner. Using the frames where both are clean (0-18, 67-71; other frames merge with the
  taxi or cyclist, or are cut by the signal pole):
  L = Yn*cot(az_min) - Yfar*cot(az_max) for every frame. This is linear and homogeneous, so the ratios come out
  without any scale (solve_az.py).
  Result: L = 0.5222 Yn, Yfar = 1.1842 Yn, so body W/L = 0.3528, which gives a body width of **2.12 m** with L = 6.
  (A real Express is 2.02/5.69 = 0.355, which matches.) Residual rms 0.0024. Frame subsets: 0.3495-0.3528.
  sim_bias.py: rounded plan-view corners (0.1-0.3 m) would bias the result by under 2%.
- Side mirrors (mirror.py, mirror_tri.py): the far mirror tip was triangulated from frames 2/4 vs 70/71, using the
  rear-near corner as the van-fixed reference. It sits 0.20-0.23 m beyond the far body side, 4.53 m ahead of the
  rear (A-pillar position, which is plausible). A mirror is also visible on the near side (symmetric model).
- Scale check: in the depth-derived metric frame (H = 9.65 m), the near body side is at Y ~11.15 m, giving
  L ~5.8 m, about 3% from the prior of 6 m. The given depth at f14 (31.28 m) is reproduced to ~0.5%.

## Answer
The world-space AABB width includes the mirrors: 2.117 + 2 x 0.212 = **2.54 m**.
Other reading: body width without mirrors = 2.12 m.
Confidence: the ratio measurement is good (+-3%). The main risk is whether the reference bounding box includes
the mirrors (I assumed yes, since a Blender object bbox includes all mesh parts).
