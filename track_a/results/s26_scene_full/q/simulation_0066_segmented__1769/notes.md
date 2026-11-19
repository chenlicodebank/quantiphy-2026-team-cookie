# q1769 — width of the turning yellow car (taxi), simulation_0066_segmented

The file runs at 24 fps and question_fps is also 24. t=0.58 s is frame 14 and t=1.58 s is frame 38.
The yellow car is the "taxi" in scene/ and the white car is the "van". I checked both tracks against the frames.

## Focal length (unknown; principal point taken at the image centre 1080,540)
1. **White van, a = 4 m/s² (prior) plus the given depths at frames 14 and 38** (focal_van*.py, f_disp.py).
   - The van moves on a straight 3D line. I back-projected its mask centroid at each frame onto the line defined by the two depth points.
   - A free quadratic fit over frames 0–50 gives a = 4.0 with the start of motion at frame ≈0 when f ≈ 870. Frames after 55 are biased by the near-field centroid.
   - The displacement from frame 14 to 38, assuming a start from rest at t=0 (4.33 m), gives f ≈ 845 with the centroid as the origin proxy, 920 with a lower-body point, and 990 with the bottom centre.
   - So f falls in 850–1000, depending on where the van's origin is.
2. **Vanishing points** (vp_van.py, vp_sedan.py, vp_solve.py). The van's body edges at frame 71 give a vanishing point near (635, 69). The parked purple sedan's edges and wheel line give one near (3240–4000, 40 to −110). If the two directions are orthogonal, f ≈ 900–1000.
3. **FOV limit:** the stated horizontal FOV of at most about 100° implies f ≳ 906.

**Adopted: f ≈ 920–930 px (about ±7%).** The camera pitch is ≈27°, taken from the horizon through the van's vanishing point. This agrees with the pitch implied by the van's and the cyclist's depth pairs (pitch.py).

## Width (taxi_width.py)
- At frame 14 (t=0.58 s, given depth 19.6514 m) the taxi is seen almost nose-on: the front fascia spans the full silhouette and only a sliver of side is visible.
- The mask (taxi_rows.py, frames/taxi_mask_14.png) has a maximum horizontal extent of **104 px** (x 824–927), at rows 418–450 (front fenders).
- **Origin:** depth × the ray through the mask centroid (875, 416).
- **Ground plane:** pitch 27°, no roll.
- **Length from frame 71:** the bumper extremes (96, 632) and (567, 536), intersected with the origin-height plane, give L ≈ 5.3 m. The ratio L/W ≈ 2.8 is car-like.
- **Fitting W:** the widest points are modelled as the front corners (0.4 L ahead of the origin, 0.1–0.2 m above it). W is solved so that their projections are 104 px apart.
- **Result at f=930 with yaw 0–5°:** W = 1.87–1.90 m.
  - Varying the corner position and height changes W by ±3%.
  - Taking the heading from the centroid path tangent instead (yaw 23°, contradicted by the near-frontal look) would give 2.02 m.
- **Range over f:** W scales roughly as 1/f, giving 2.05 m at f=850 and 1.75 m at f=1000.

**Answer: 1.9 m.** Mirrors are not wider than the fender line in the silhouette.

## Check
- The box-model reprojection at frames 38/50/60/71 (check38.py) only gives an upper bound: a box over-predicts a rounded car's silhouette. It is consistent with W ≤ 2 m.
- The L/W ratio (≈2.8) is plausible for this sedan.

**Confidence:** moderate (about ±8%). The dominant uncertainty is the focal length, which hinges on where the van's origin is.
