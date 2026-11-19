# q_1663: width of the freestanding art display panel (m)

The file and the question both use 33 fps. Prior: person height 1.87 m. Depths: man 6.84 m at t=0 and 6.49 m at t=1;
nearest panel 11.042 m; sculpture and pedestal 5.085 m.

## Which panel
There are two panels, each a framed painting on a dark slab base, one on each side of the sculpture. The right one
(base x 656-784, frames 96 / t=2.909) is closer to the camera: its reconstructed centre is about 0.1 m nearer than the
left one's, and the left one is farther off-axis. Their pixel sizes are almost the same, and the left base gives the
same length to within about 2%.

## Camera (geom.py)
- Focal length: the man's pelvis is at (883,648) at frame 0 and (688.6,649.8) at frame 33. I assumed his
  forward depth stays constant (his apparent height is constant, 264-266 px with legs together). That gives
  f = 908 px and z_man = 6.36 m. Check: 1.87 m at that depth is 267 px, and a walking pose is slightly shorter, so this is consistent.
- Floor plane: the man's feet are on image row 786 at z = 6.36 m. I chose the camera height and a small pitch so that
  the right panel's origin (centre of the base footprint) lies exactly 11.042 m from the camera. The result is
  pitch about 1.2-1.5 deg downward and camera height 1.86-1.90 m. Check: the head top on row 521 is then about 1.85 m
  high and the pelvis about 0.99 m.
- Without pitch (h = 1.72 m), the panel centre would be 11.60 m away, which contradicts the given 11.042 m.
  I rejected that model.

## Panel measurement (bases.py, panels.py)
The silhouette of the base is a sloped parallelogram, so the panel is turned about 28 deg, with its right end
nearer the camera. I took the bottom front corners of the base at (657.5, 675.3) and (776.0, 685.5), and the back-right
corner at about (783, 680). I back-projected these onto the floor plane:
- front edge length (width across the face) = 1.431 m with the origin at mid-height, or 1.410 m with the origin at floor level;
- base depth about 0.4 m; world-x extent of the bounding box = 1.448 m or 1.427 m;
- the painting frame alone is narrower than the base, which is the widest part of the panel.

## Second route
With a plain pinhole scale at the panel (z about 10.8 m from the 11.042 m depth), the full base spans 128 px,
which is 1.52 m across the line of sight. Predicting that apparent width from the reconstruction
(L = 1.43, d = 0.40, about 17 deg relative turn) gives about 1.48 m. The two routes agree to within about 3%.

## Answer
The width is about 1.44 m. Both readings (face width and world-x bounding-box extent) give 1.41-1.45 m, and
1.44 m is in the middle of that range.
Confidence: moderate, about ±5%. The main uncertainties are where the panel's origin sits and the
pixel positions of the corners (±0.5 px moves the length by about 0.03 m).
