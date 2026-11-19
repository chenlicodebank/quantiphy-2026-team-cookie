# Q1440 – height of the truck (simulation_0188)

Prior: acceleration 10.757 m/s^2. depth_info: origin distance 22.532 m at t=0.5 s (frame 15) and 19.525 m at t=1 s (frame 30).
question_fps = file fps = 30.

## Method
1. Kinematics (`fit_kin.py`): the image track of the front hub along its straight image line was fit with a projective
   (Möbius) map of s(t) = 0.5·a·(t−t0)². Result: t0 = 0.000 s, rms 0.06 px. The other keypoints give the same. So the
   truck starts from rest at frame 0 with constant a, and s(t) = 0.5·10.757·t² m is known for every frame.
2. 3D hub trajectory for a trial focal f (`solve_f.py`): the hub rays are scaled by Z0(1+C·s) so that the hub moves on a
   straight line at unit speed per metre of s. Level camera, principal point at the image centre. The along-axis lengths
   do not depend on f: wheelbase 4.16 m, rear box edge to bumper 8.95 m, bbox centre 2.54 m behind the front hub.
3. Focal length from depth_info (`solve_fW.py`): the origin = front hub − L·u + W·lateral + height. The two given
   distances are solved for (f, W) at a chosen L:
   - L = 2.54 (bbox centre): f = 2743 px and W = 0.87–1.05 m. That matches half of the measured cab width
     (1.87 m / 2 = 0.94 m), so this case is self-consistent and is the one adopted.
   - L = 2.08 (middle of the wheelbase): f = 2850.
   - L = 3.0: f = 2638.
   The origin height has almost no effect on f.
4. Height (`railtop.py`, `final.py`): the top of the truck is the top of the near-side railing post above the cab
   (y = 332 px at frame 40). It was found in code as the top of the background-difference mask, for frames 28–46.
   That point is intersected with the near-side vertical plane through the hub line. The box top front and rear come
   out at the same height (3.10/3.10 at f = 2650), which confirms the plane. The ground is the tyre bottom straight below
   the hub, from column intensity profiles: tyre radius 72.7 px at frame 40 (63 px at frame 30, 79 px at frame 44).
   The scene record's value of 68 px was too small.
   - Top above the hub: 3.007 m, the same in every frame 28–46 (±0.004).
   - Tyre radius: 0.386 m.
   - Height = 3.39 m (frames 30/36/40/44: 3.395, 3.386, 3.391, 3.389).

## Checks / sensitivity
- Second route: the frame-by-frame repeat across frames 28–46 agrees within 0.3%. The box top is level along the
  near-side plane.
- Origin placement (L = 2.08 → 3.0 m) changes the answer only from 3.35 to 3.43 m (±1.2%). Any f from 2400 to 3100
  gives 3.23–3.49 m.
- Some error remains from the assumption that the near-side railing post lies in the wheel-face plane (±0.1 m lateral,
  which is about 0.6%).

Answer: **3.39 m** (confidence: good, about ±3%).
