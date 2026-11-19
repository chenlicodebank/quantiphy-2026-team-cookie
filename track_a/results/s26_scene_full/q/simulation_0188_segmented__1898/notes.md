# q_1898 — height of the truck (m)

Prior: a = 10.757 m/s^2. depth_info: D(t=0.5 s, frame 15) = 22.532 m, D(t=1 s, frame 30) = 19.525 m.
question_fps = file fps = 30. Truck starts at rest at frame 0 (pixel steps 0.56, 1.66, 2.59, ... ≈ 1:3:5), so the
path length along its straight heading is s(t) = 0.5·a·t².

## Method (3D, pinhole, level camera, cx,cy = 960,540)
1. Heading vanishing point re-measured from the straight image trajectories of 6 tracked points
   (`vpfit.py`): (-3141, 539) (record's edge-based value -3030 was a bit off; leave-one-out range -3122…-3158).
   Horizon row 539 → camera level.
2. `fit3d.py`: for a trial f, each tracked point X(t) = X0 + s(t)·m (m = heading from VP and f); X0 solved by linear
   least squares from its pixel track (rms 0.6–4 px). Known metric s(t) fixes the scale through perspective.
3. `depthfit.py` / `final.py`: truck centre = midpoint bumper↔box rear along heading, mid height
   (or ground level), half width (2.3–2.7 m) behind the visible side. f solved so that the centre distance
   reproduces D15 and D30: f15 ≈ 2635–2683, f30 ≈ 2630–2688 (both depths reproduced by the same f, within 0.01 m).
4. Height = world vertical extent from top of the platform railing (bbox top) to bottom of the front tyre
   (bbox bottom), each back-projected at its own fitted depth, frames 34–43 (truck fully in view):
   H = 3.416–3.436 m (frame-to-frame std 0.004 m); track-point version (stairs_top → front hub + wheel radius) 3.413–3.433.

## Second route (independent focal length)
Lateral vanishing point from the cab-front grille top/bottom edges at frame 43 (`lateral_vp.py`, slopes −0.238/−0.303)
with orthogonality to the heading VP → f = 2633 / 2650 px, matching the depth route (≈2660). At f = 2640 the height is
≈ 3.43 m.

## Sensitivity
dH/df ≈ −0.0004 m/px; heading-VP uncertainty ±40 px → ±0.02 m. Other outputs: length ≈ 8.0 m, wheel radius 0.41 m
(plausible catering truck).

Answer: 3.42 m. Confidence: good (≈ ±3%).
