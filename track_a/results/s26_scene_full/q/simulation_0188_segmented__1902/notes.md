# q1902 – width of the truck (m)

Prior: acceleration = 10.757 m/s^2. depth_info: origin–camera 22.532 m at t=0.5 s (frame 15) and 19.525 m at t=1 s (frame 30).
The file and the question both use 30 fps.

## Method
1. Motion model (`recon.py`): the truck translates without rotating along a fixed direction u, so P(t) = Q0 + s(t)·u with
   s = ½·a·t². A free t0 fits to −0.001 s, so the truck starts from rest at frame 0. I used the scene tracks (hubs, the far
   bumper corner, the rear box edge, the stair top, the front-tyre ground contact) plus my own silhouette tracks (`silh.py`):
   x-only tracks for the far cab front corner and the far mirror's outer edge. I fit all of these jointly at each candidate
   f (rms 1.2 px). The prior a sets the metric scale. The motion alone does not determine f, as expected.
2. Focal length: I took the origin to be the bbox centre (length midpoint from bumper to box rear, lateral midpoint,
   height midpoint from ground to stair top) and solved for its camera distances (`solve_f.py`). f ≈ 2680 px gives
   22.51 / 19.49 m, against the given 22.532 / 19.525 m, so both values are reproduced.
   Independent check: the second vanishing point from horizontal lines on the cab front face (`vp2.py`, frame 15),
   combined with the length-direction VP at x ≈ −3100 on the horizon, gives f ≈ 2600–2870. This agrees.
3. Lateral extents (`klt3d.py`): I KLT-tracked 120 features from frame 15 over frames 5–27 and triangulated each with the
   motion model at f = 2680. The lateral coordinates are:
   - near side of the cab and box: about 12.76 (box rear edge 12.68–12.81)
   - near mirror outer edge: 12.47
   - far cab front corner: 14.81
   - far mirror outer edge: 15.205
4. Widths at f = 2680:
   - body (cab/box side to side): about 2.07 m
   - mirror to mirror (full world AABB lateral extent): about 2.75 m
   A change of ±100 px in f moves these by only about ±0.03 m.

## Answer
Under the AABB convention the mirrors count, because they are part of the rendered truck. Answer: **2.76 m**.
The alternative reading (body only, no mirrors) gives about 2.07 m.

## Confidence
The geometry is consistent: both depths are reproduced and the two focal-length routes agree. The main uncertainty is
whether the reference bbox includes the mirrors. The near mirror sticks out 0.29 m and the far one 0.39 m, so the two
sides are not symmetric.
