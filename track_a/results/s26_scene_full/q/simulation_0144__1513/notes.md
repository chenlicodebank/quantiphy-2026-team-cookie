# Q1513 – tire diameter (simulation_0144)

Prior: rocket length 2.9 m. depth_info: rocket origin at 43.064 m (t=0, f0) and 41.127 m (t=0.5 s, f12).
File fps = question fps = 24, so the frame numbers are the same.

## 1. Focal length (fitf.py)
- Rocket origin in the image: f0 = nose back-extrapolated to s=-449 on the flight line, minus half the length
  (1333,763); f12 = (1239,656) from scene/ (nose minus 72.8 px). Back-projecting with the two given distances
  gives P0 and P12 for any f, and so the rocket's 3D flight line (the rocket flies along its own axis).
- For frames 18-30 (sky background) I measured the blur-free rocket length as the distance between the 50 %
  points of the end ramps of an along-axis difference profile (blur.py). The tail ramp grows as about 0.5 x the
  per-frame image speed (Blender motion blur), so the scene/ mask lengths include blur. Lengths:
  141.5 px at f18, rising to 177.5 px at f30.
- The predicted image length of a 2.9 m segment on the 3D line at each frame's origin was fitted to these
  lengths: **f = 2118 px** (HFOV 48.8 deg). The fit follows the whole growth curve within about 2 px (f18-23
  alone give 2142, f25-30 give 2101). It is insensitive to the f0/f12 origin estimates (±5 px gives ±5 px in f).
  Check: the width ratio 13.4/15.4 (f14→f30) gives a depth ratio of 0.87; the model gives 0.855.

## 2. Tire pixel size (tire2.py, tire3.py; frame 0)
Measured the vertical extent of the light-grey tire sidewall through the hub column (threshold sweep, plus visual
check on 8x crops): front 76.5 px, middle 69.5 px, rear 68.5 px (±1 px). Hub centres are (1177,996.5),
(1347.5,968.5) and (1400.5,961).

## 3. Wheel depths (geom.py)
- Assumptions: camera roll 0; the wheel-centre line is horizontal; the pod (rocket axis) lies in the truck's
  vertical mid-plane; the near-side wheel plane is offset by delta = 1.0 m toward the camera.
- Solving for the camera pitch that makes the rocket axis line up with the heading gives three roots. The only
  physical one is pitch -0.6 deg (horizon at y≈562, which matches the visible skyline at y≈600-660; the other
  roots put the horizon off-frame or give a 37 m wheelbase).
- At this root: wheel distances 39.5 / 42.5 / 43.5 m; axle spacings 4.4 m and 1.5 m (plausible for a 6x6 truck);
  hub 3.9 m below the rocket centre.
- D = pixel extent / (projected vertical extent of a 1 m circle with its axle along the lateral axis):
  **front 1.373, middle 1.333, rear 1.342 m**.

## Second-route / sensitivity
- The three wheels give independent estimates at very different depths, and they agree within 3 %. This is a
  check on the recovered heading.
- If the pitch comes from the visible skyline instead (-3 deg), the wheels give 1.331 / 1.315 / 1.332.
- delta from 0.6 to 1.2 m changes D by ±1 %.
- Main error sources: f (±2 %), the tire pixel extents (±1.5 %) and the pod-in-mid-plane assumption.

Answer: **1.34 m** (estimates span 1.32-1.37). Confidence: moderate-good (about ±4 %).
