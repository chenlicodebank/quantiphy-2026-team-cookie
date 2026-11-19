# Q1086 – height of the bench seat (m)

Answer: **0.535 m** (bench total height, floor to top of cushions = world bbox vertical extent).

## Scene
- The image is rolled 90°: world up = image +x. The "sofa" + "rug" in scene/ is really the **bench**:
  a thick base plate on the floor (front-bottom edge at x≈113), a twisted support, a seat slab
  (front face x 255–298), and 4 cushions (front-top edge x≈327, back-top silhouette x≈382).
  Checked on an upright-rotated view (rot.py / rotzoom.py, frames/rot50.png, rz.png).
- The camera is level: the world-vertical shelf divider edges keep a constant image y (166, 1027) from x=720 to x=1040
  (tilt.py), so the pitch is below 0.3°. Receding floor-tile and bench-end lines converge at about (540, 541),
  which puts the principal point at the image centre.
- The file runs at 33.039 fps and the question at 33.0 fps. I used frame numbers: t=1 s is frame 33.

## Scale (solve.py)
- Person (origin = pelvis, image x≈540): I assumed the walk stays at constant camera-z.
  - Route A: the depths 5.424/4.886 at pelvis y 20/263.7 give f=871 px and Z=4.657 m. The implied speed is 1.303 m/s,
    which reproduces the 1.3 m/s prior.
  - Route B: the speed prior plus the pixel speed over frames 5–100 gives f=882 px and Z=4.662 m.
  - I used f=876 px and Z_person=4.66 m.
- Camera height comes from the stance-foot sole at x≈350.5 (frames 8, 11, 15): h_c = 189.5·4.66/876 = 1.008 m.
- Bench base: the floor-contact edge at x=113 gives Z_front=2.068 m. Its thickness is 0.071 m and its back top edge
  (x≈225) is at Z=2.61 m, so the base is 0.54 m deep.
- Cushion top: Z_front = u·876/213 and Z_back = u·876/158, where u = h_c − H.

## Results by route
1. Seat centred over the base (twisted pedestal design): H = **0.524 m**. The seat is 0.69 m deep, Z 1.99–2.68.
2. Origin distance 2.267 m taken as the centre of the cushion top: H = **0.548 m**.
3. Origin taken as the seat centre at half height: H = 0.563 m. This route forces the seat well in front of the base,
   which is less plausible.
- With the route-1 geometry, the bbox centre would be 2.45 m from the camera, not 2.267 m. So the bench origin is
  probably not at its bbox centre. The person-based scale is well confirmed (two independent routes and the speed
  prior), so I trust the floor geometry more than any assumption about where the origin is.
- Final answer: 0.535, between routes 1 and 2.
- Naming: "bench seat" is read as the bench object, floor to the cushion top. The seat-slab top alone, under the
  cushions, would be about 0.46 m.

## Confidence
Moderate: about ±5%. Most of the uncertainty is the depth of the cushions (where the seat sits relative to the base).
The second-largest source is the camera height (which foot is the stance foot, ±2%).
