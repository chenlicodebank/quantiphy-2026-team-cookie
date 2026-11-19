# q_1465: length (front to back) of the red car

Answer: **4.37 m**

The file and the question both run at 24 fps, so frame = round(t*24). This is a 3D Blender render with a static camera.

## Focal length (fitf.py, fitf2.py, par.py)
- Image positions are the scene/ track reference points (amodal bbox centres). Each 3D point = depth x unit ray, with the principal point at the image centre.
- Forklift prior: a = 2 m/s^2, starting from rest near t = 0. Both vehicles are at rest in frames 0 and 1.
  - Displacement between t=1 and t=2 with the given depths: 3.0 m gives f = 3329 px; 2.917 m (t0 = 1/24) gives f = 3577 px.
  - Full-track fit: intersect each frame's ray with the 3D line, fit s(t) = s0 + a/2 (t-t0)^2 and require a = 2. This gives f = 3290-3680 px, depending on the frame window and on which centre is used, with fitted t0 = 0.00-0.04 s.
- Chosen f = 3450 px (HFOV about 41 deg), uncertainty about ±5%.
- Cross-check: with this f the car's fitted acceleration is 5.04 m/s^2, which looks like a round design value of 5. The car and forklift 3D paths come out nearly parallel (<1 deg apart).

## Car geometry by motion triangulation (track.py/track2.py, tri.py, tri2.py)
- Car axes:
  - u = heading, from the car origins back-projected at t=1 and t=2.
  - n = up, assuming a camera with zero roll.
  - w = n x u.
- Method: track car features by template matching from frame 24 across frames 14-43. Since the car translates along u by the fitted s(t), each feature's depth is triangulated from that motion. Reprojection rms is about 1-2 px.
- Consistency checks:
  - The two left wheel hubs share the same b and c, so u is right.
  - The two corner tail lights have the same c, so n is right.
  - The hubs reproject onto the wheel centres in the drawn overlays.
- **Wheelbase = 2.48 m** (2.45-2.54 for f = 3300-3600). This is insensitive to f.
- Rear (f = 3450, a measured from the frame-24 reference):
  - plate a = -1.97, centre light -1.94, corner tail lights -1.78, exhausts -1.78/-1.79, grey diffuser panels -1.82.
  - Rear-most is about **-1.99** (rear hub at -1.21).
- Front:
  - The front-left corner frontier point (silhouette tangent from the heading vanishing point) is at a = 1.96-1.98, about 0.5 m above the ground (front hub at +1.29).
  - The nose centre (centre plane b ≈ 0.17, from the plate and the symmetric light/exhaust pairs) is hidden behind the hood contour.
  - Silhouette upper bounds (nosebound.py): a <= 2.50 / 2.36 / 2.19 for nose heights c = 0.1 / 0.2 / 0.3. The ground is at c ≈ -0.13 (hub c 0.18, wheel radius about 0.31 m).
  - The hood contour on the centre plane lies at a ≈ 2.2-2.3.
  - Front-most is about **2.33 ± 0.12**.
- Measured length: 2.33 + 1.99 ≈ **4.32 m** (range about 4.17-4.45).

## Second route (sanity check)
- The model is a LaFerrari. Its measured proportions match the real car scaled by about 0.94: wheelbase 2.48, track about 1.68 at the hub caps, tail-light height about 0.68 m.
- Real length / wheelbase = 4.702 / 2.650 = 1.774, so 2.48 x 1.774 = **4.40 m**.

## Answer
- The direct measurement (4.32) and the proportion route (4.40) agree within 2%, so the answer is 4.37 m.
- Main uncertainties: the hidden nose position (±0.1 m), and whether the world AABB is aligned with the car's heading (assumed yes).
- Confidence: moderate-good, about ±4%.
