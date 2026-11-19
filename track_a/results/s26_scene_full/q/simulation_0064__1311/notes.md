# q1311 — height of the turning yellow car (taxi), simulation_0064

Answer: **1.67 m**. This is the world vertical extent of the taxi's bounding box, from the tyre contact up to the top of the roof sign.
Time base: question_fps = file fps = 24, so t = 0.58 s is frame 14 and t = 1.58 s is frame 38.

## Camera model (cam.py)
Pinhole with principal point (1080, 540), pitch only (roll 0, yaw about 0; the street vanishing point x is about 1060–1087).
- Horizon row v_h = −121, from the curb vanishing points in scene.json. The bike's two depths fit an
  origin at constant height for v_h ≈ −130, which is consistent (horizon.py).
- **Focal length f ≈ 2180 px** (ped_f.py). The pedestrian walks parallel to the image x-axis at constant
  depth: feet row 298–300 and head row about 195 stay constant. Its x track is very linear (slope −3.06 px/frame,
  rms 1.4 px; fitted over f34–71). That gives x(f14) = 406 (extrapolated; it is hidden behind the signal head) and x(f38) = 333,
  with the pelvis at row 245. With Y and Z constant, d² = Z²(1 + ((u−cx)²+(v−cy)²)/f²), and the two given
  depths (38.347 and 38.722 m) solve to f = 2170–2210 (Z = 36.3 m, walking speed 1.21 m/s).
  Sensitivity: about 16 px of f per px of x14.
- Camera height h = 6.74 m. It is fixed by the taxi's own depth at f38 (33.008 m): the origin at the footprint centre is
  scaled to that distance. Using the bounding-box centre instead changes H by +0.5 %.

## Taxi height (taxi_h.py, taxi_multi.py, pick.py)
Side-on frames. pick.py measures the near front and rear tyre bottoms (the dark-to-cobble transition at the
wheel-centre columns) and the top of the roof sign (the first orange row) in code:
- f32: tyres (650.5, 371.3) and (826.5, 346.6); sign top (728.5, 234.0)
- f38: tyres (559.5, 375.6) and (757.5, 357.8); sign top (670.5, 240.0)
- f44: tyres (471, 378.2) and (683, 367.2); sign top (605, 245.0)

Method:
1. Back-project the tyre contacts onto the ground plane. This gives the heading and a wheelbase of 2.90 m.
2. Shift the line between them inward by half the outer tyre spacing (0.85–0.92 m) to get the car's vertical centre plane.
3. Intersect the ray through the sign-top pixel with that plane. The height of that point above the ground is H.

This method accounts for the camera looking down: the roof is further away than the near tyres.

Results at f = 2180 and v_h = −121: H = 1.682/1.667 (f32: 1.698/1.682, f44: 1.676/1.662) for a half-spacing of 0.85/0.92 m.
The three frames agree within 1 %.
Over v_h −150…−95: ±0.5 %. H scales about as 1/f: f = 2120 gives 1.72, f = 2240 gives 1.62.

## Checks
- With the camera fixed by the taxi's depth (h = 6.74), the pedestrian at f38 (feet row 299, pelvis row 245)
  comes out at 38.706 m from the camera; the given value is 38.722 m (0.04 % off). Its pelvis height is 0.91 m and its height while walking is 1.71 m.
- The bike's distances, using a rough origin guess, are within ±1.5 % of the given values.
- Real-world sanity check: the wheelbase of 2.90 m at f = 2180 matches a Crown Victoria taxi (2.91 m), and 1.67 m is plausible
  for a sedan of about 1.47 m plus the roof sign. The van's paint width is about 1.94 m.
- The record in scene/ was used for tracks only; all values the answer depends on were re-measured.

Confidence: moderate to good, about ±4 %. The main uncertainty is f (pedestrian route, ±2–3 %, supported by
the wheelbase sanity check).
