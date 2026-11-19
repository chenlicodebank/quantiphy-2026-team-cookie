# q_1899 — truck tyre diameter (m)

Prior: truck acceleration 10.757 m/s^2. depth_info: centre-to-camera 22.532 m at t=0.5 s (frame 15), 19.525 m at
t=1.0 s (frame 30). File fps = question_fps = 30. 3D Blender scene, segmentation (white background), static level camera.

## Method
1. `fit.py`: front-hub pixel track (frames 0-46, scene/tracks) fitted with a straight-line, constant-acceleration
   projective model u,v = (A + B s)/(1 + C s), s = 0.5 a t^2 (truck starts from rest at frame 0; a free fit with
   t0, v0 gives the same, RMS 0.13 px). C = -0.02787 /m = Dz/Z0 gives the hub's metric depth once f is known.
   Vanishing point of travel (B/C, F/C) = (-3164, 538) -> camera level (VP row = image centre row).
2. `recon.py` / `solve_f.py`: metric 3D truck model for a given f (near-side plane through the hub; front of cab,
   rear of box, top of platform, tyre bottom) -> bbox centre (+ unknown width W/2 laterally). Solving both given
   distances for (f, W): f = 2616 px, W = 2.56 m (plausible truck width), length 7.86 m, height 3.42 m; both
   distances reproduced exactly. Longitudinal centre uncertainty +-0.5 m -> f 2502..2730.
   (Width read from the cab front face corners gives ~2.85 m at this f; fixing W = 2.2..2.8 gives f = 2598..2641.)
3. `tyre_diam.py`: front tyre per frame 20-46: rim-ring centre (bright pixels), tyre bottom (mask bottom row), tyre
   top (dark gap under the fender -> tyre edge, sub-pixel midpoint) along the column through the rim centre.
   Diameter = (bottom - top) px x Z_hub / f, with Z_hub from the motion fit.
   Note: scene/ record's hub y is ~3 px above the rim centre, so its hub-to-ground "radius" overstates (gives ~0.815 m).

## Results (f = 2616)
- top-to-bottom route: 0.764 m median, sd 0.003 over 27 frames (constant as the truck approaches -> depth model consistent;
  e.g. frame 40: 142.2 px at Z = 14.10 m).
- 2 x (bottom - rim centre): 0.786 m (rim centroid sits ~1.5 px above the midpoint of the tyre outline).
- f range 2502 / 2730 -> 0.774 / 0.755 m.

Answer: 0.766 m (top-bottom route, nudged slightly toward the rim route). Confidence: about +-3%.
