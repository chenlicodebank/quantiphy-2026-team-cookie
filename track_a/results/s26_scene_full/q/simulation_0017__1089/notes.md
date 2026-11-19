# q1089 – height of the freestanding art display panel (simulation_0017)

Answer: **2.0 m** (range 1.95–2.05 m).

## Scene
- The video is rolled 90°: world up = original image +x. When rotated upright it shows a gallery atrium: a bench in the
  foreground (2.27 m), a person walking left→right at about 4.66 m, the central sculpture on its pedestal (5.96 m), and
  two identical freestanding art display panels (framed canvas on a stepped base) standing on the floor by the back
  colonnade on either side of the pedestal (original y≈300–400 and y≈655–770).
- Timing: the file runs at 33.039 fps and the question at 33.0 fps. Frames were used as round(t·33).
- Camera pitch is about 0. Clean vertical structure edges at horizontal offsets from −375 to +490 px have slopes
  |dy/dx| < 0.0015 (`pitch.py`), so the horizon is the image centre (539.5).

## Measurements (code: profiles.py, edges.py, height.py; crops from crop_rot.py)
- Panel in original x (up axis), measured on both panels, which match: frame top edge 614.5 and lowest base edge
  464.5 (the base's lower edge runs from 464.5 to 468.5 along its length). That is 150 px, centred on the horizon
  (75 px above, 75–71 px below).
- Walker: I fitted the pelvis track (scene/tracks/human.csv, checked) with a line: about 7.54 px/frame and u(f33) = −285 px.
  - Constant-Z walk (head size constant) + the given depths 5.424 / 4.886 + 1.3 m in 1 s gives Z = 4.655 m,
    f ≈ 893 px (hfov ≈ 62°) and Z/f = 0.00520 m/px.
  - The pixel rate alone gives Z/f = 1.3/(7.54·33) = 0.00522, so the two routes agree.
  - The range over different fit windows is 0.00505–0.00532.
- Planted sole lowest edge is at x = 348.5 (frames 2, 8, 14), which is 191 px below the horizon. Camera height h = 191·0.00521 =
  0.996 m. This is consistent with the pelvis sitting exactly at the horizon, and it gives a walker height of 1.89 m.

## Height
- The panel's base is on the floor at d_b px below the horizon, so Z_p/f = h/d_b and Z_p ≈ 11.9 m. The top is d_t = 75 px
  above the horizon, so H = h(1 + d_t/d_b).
  - Lowest edge 464.5: H = 1.99 m.
  - Mid edge 466.5: H = 2.02 m.
  - 468.5: H = 2.05 m.
  - If the base's front edge sits about 0.2 m in front of the panel plane, add about 0.02 m.
- Second check: the 1.89 m walker and the panel top both sit about 1.9–2.0 m above the floor in the same geometry. The canvas
  comes out at about 1.5 m tall and 1.2 m wide, which is plausible.

## Conflict with depth_info (important)
- depth_info gives the panel distance as 4.223 m. With f ≈ 893 that would make the panel only 150·4.14/893 ≈ **0.70 m** tall,
  floating about 0.65 m above the floor.
- That is impossible in the image. Both panels stand on the floor behind the sculpture pedestal (5.96 m). Their floor contact
  is only 75 px below the horizon, while the walker's feet at 4.66 m are 191 px below. This puts the panels about 12 m away.
- So the 4.223 m value most likely refers to an object origin that is not at the mesh. The bounding-box height comes from
  the geometry, so I answer from the floor geometry: 2.0 m.
- Alternative under the depth_info reading: 0.70 m.

Confidence: moderate-high that the answer is about 2.0 m (±4% from the bottom edge and walker scale), with the depth_info
conflict as the main risk.
