# q1310 – length of the turning yellow car (taxi), simulation_0064

Answer: **5.05 m** (range from the model variants: 4.9–5.19 m).

The file's frame rate and question_fps are both 24, so no time conversion was needed. 3D Blender scene with a static camera.

## Camera (scripts: focal_ped.py, cam.py, height.py)
- Principal point (1080,540). The horizon is at y = -121 (street vanishing point and horizontal cross-street curbs, from scene/), so pitch = atan(661/f).
- **Focal length from the pedestrian.** He walks along the cross street, whose image lines are horizontal, so he moves along the camera X axis at constant camera Y and Z. That gives
  d14² - d38² = (Z/f)²[(u14-cx)² - (u38-cx)²], and then d38² = (Z/f)²[(u-cx)² + (v-cy)² + f²].
  - Inputs: given pelvis depths 38.3473 m and 38.7220 m. ref_x comes from a linear fit over f35–71 (≈ -3.07 px/frame). He is hidden at f14, so u14 = 407 is extrapolated; u38 = 333 and pelvis v = 244.
  - Result: **f ≈ 2185 px** (2163–2201 over the fit windows), about 53° horizontal field of view.
- **Camera height h = 6.74 m**, from the pedestrian's pelvis 3D point and his feet row (y = 299). Sanity check: the same numbers give the person a height of 1.74 m and a pelvis height of 0.92 m.

## Taxi length (taxi_round.py, run_all.py)
- **Box model.** The near-side tyre contact points are back-projected onto the ground plane, which gives the heading and the near-side line. The car's centre line is 0.9 m further in, and the width is 2.0 m.
- **Fit.** A rounded-rectangle footprint (corner radius r) at heights 0.3 m and 0.75 m is projected into the image. Length L and a fore/aft offset are fitted so that the projected silhouette matches the measured left/right image extents.
- **Extents and contacts.** These come from zoomed crops (crop.py) plus background differencing against frame 0 (extents.py). The pole occludes the front end from f41 to f55, so those frames are not used. f71 is not used because the signal hides the rear.

| frame | tyre contacts (front, rear) | x extent |
|---|---|---|
| 38 | (559,371), (761,357.5) | 476–839 |
| 40 | (526,373.75), (733.5,358.75) | 457–818 |
| 56 | (313.7,375.5), (526,374.5) | 251–635 |
| 60 | (263.7,376), (475.6,375) | 202–589 |

- **Results.** L by frame (f = 2185, r = 0.25): 5.10, 5.04, 5.10, 5.10. Varying r from 0 to 0.4 gives 4.99–5.14, and varying f from 2163 to 2200 moves the result by about ±1%. Removing 2 px of motion blur from each end lowers it by about 0.06 m.
- **Depth check (second route).** At t = 1.58 s the box model puts the taxi origin at 33.16 m (origin 0.5 m above the ground) or 33.26 m (origin at ground level). The given depth is 33.008 m, a 0.5% match, which confirms f and h with an independent object. Scaling to the given depth multiplies L by 0.995.
- **Also consistent:** the wheelbase comes out at 2.9–3.0 m. The four frames (two oblique at a heading of about -161°, two side-on at about -179°) agree to within ±1.5%.

## Confidence
About ±4%. The main uncertainties are the rounded-corner and silhouette modelling of the car ends, plus motion blur. Note that a real Crown Victoria is 5.39 m long, but this render's model has larger wheels and is not the real car, so I used only the measurement.
