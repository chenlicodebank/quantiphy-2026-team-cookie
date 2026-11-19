# Q1541: width of the blue car (light-blue utility cart), metres. Round 2 (verification of round 1)

**Answer: 0.845 m.** Round 1 proposed 0.845 m (decision "new"). I reproduced its fault proof with my own code and get W = 0.84 ± 0.03 m, so the change stands.

## Setup
- The file and question_fps are both 24 fps, so t = 1 s is frame 24.
- Blender 3D scene with a static, level camera. Horizon / vanishing point at (959.3, 539.1).
- The cart drives parallel to the image plane at constant depth. Its right side faces the camera.
- Width (bounding box) = near front tyre outer face to far front tyre outer face, all along the viewing axis:
  W = Z_no·(1/k − 1), with k = Z_no/Z_fo.
  - The body (roof, headlights) lies inside the tyres (C1, C3 and round 1 measured this; I did not re-measure it).
- **Crux:** k. Round 1 has 0.915 (W 0.845). C1 and C2 have 0.923 (W 0.75). The two values differ by about 2.7 px in where the far tyre's centre sits.

## Measurements (my scripts: rowedge.py, nearedge.py, uroute.py, overlay.py, yellow2.py)
1. **Far front tyre outer-face circle** (`rowedge.py`, frames 14-24).
   - Per-row right silhouette: the outermost crossing of the half level between the local background and the tyre (or its tread highlight). Then circle fits, free radius and fixed radius 48-49.8 px.
   - Overlays are in `frames/ov1.png` and `frames/ov2.png`.
   - Frames 19, 23 and 24 are contaminated and were excluded:
     - frame 19 has a bright bulge on the edge at rows 865-875;
     - frames 23-24 have background clutter, with rms 1.3 px.
   - Clean frames 16-18 and 20-22:
     - rows 840-900: centre rows 862.0-863.6, mean about 862.8;
     - rows 840-910: centre rows 863.2-864.7, mean about 864.0.
   - Rows below about v_c + 37 are where the far tyre's inner-face circle takes over the silhouette. I computed the crossover from the tyre-width parallax. Including those rows pushes v_c down (larger row), so 862.8-864.0 is an upper bound on the true centre row.
2. **Near front tyre outer-face circle** (`nearedge.py`, frames 33-41, right arc rows 856-935).
   - Centre row 893.0-893.1 (frame-to-frame sd 0.3), free radius 52.7-53.6 px, rms 0.12-0.24 px.
   - This agrees with round 1 (893.0, r 53.3).
3. **V route (vertical).** k = (v_far − 539.1)/(v_near − 539.1):
   - v_far 862.8 gives k 0.9145; v_far 864.0 gives k 0.918.
   - **W = 0.81-0.85 m.**
   - C1's k = 0.923 would need v_far = 865.8. No clean frame gives that.
4. **U route (horizontal, independent of v).** Both tyres sit on the same axle, so u_far − 960 = k·(u_near − 960).
   - Regressing the far circle's centre u on the record's front-hub u over frames 15-18 and 20-22 gives slope 0.912-0.914, whatever radius I assume (48-49.8 px). The intercept is −1.6 to −4 px, which comes from the assumed radius and the edge bias.
   - **W = 0.86-0.88 m.**
   - Per-frame ratios with no intercept give 0.917-0.920 (W 0.79-0.82). They depend on the radius I assume, so the slope is the robust value.
5. **Scale.**
   - depth_info 9.312 m to the near-front tyre centre at frame 24, at pixel (623.3, 893.0).
   - Near radius 53.3 px for the 0.369 m tyre gives f ≈ 2625 px and Z_centre = 9.155 m.
   - Z_no = 9.085 m (tyre width 0.14 ± 0.05 m; ±0.3 % on W). Z hardly depends on f.
6. **Result.** k ≈ 0.915 (V 0.9145-0.918, U 0.912-0.914) gives W = 9.085 × (1/0.915 − 1) = **0.844 m**. Range 0.81-0.88.

## Rechecks
- **a. Closure** (`yellow2.py`): the yellow car's near front tyre, fitted on its lower arcs plus its bottom against the floor in frames 22-26.
  - Bottom row 895.7. The radius is poorly constrained by the lower arcs (93-99 px); with the centre at the hub row 797 it is 98.7 px.
  - Ground-contact depth ratio: Z_y/Z_no = (946.35 − 539.1)/(895.7 − 539.1) = 1.142.
  - Yellow tyre diameter = 0.369 × (r_y/53.3) × 1.142:
    - r_y = 98.7 px gives 0.780 m (**+2.1 %** against the 0.764 prior);
    - r_y = 93.4 px gives 0.739 m (−3.3 %).
  - Either way within 5 %. Round 1 got +3.4 %. This closure tests the scale, not k.
- **b. Plausibility.**
  - Cart: length about 1.9 m, height about 1.7 m, width 0.84 m. That is a narrow utility cart with width/length 0.44, which is plausible.
  - Camera height about 1.41 m.
  - Yellow car: length about 4.5 m.
  - No people in view.
- **c. Units and time base:** metres. Frame 24 = t 1 s at 24 fps (the file rate is the same).
- **d. Fault proof.**
  - **C1 (0.753) and C2 (0.755):** they used k = 0.923, which needs the far centre at row 865.8 and a horizontal slope of 0.923. I measure 862.8-864.0 and 0.912-0.914. Their far edge was taken at rows 892-906, 28-43 px below the far centre. From about +37 px down, that part of the silhouette belongs to the inner face, which is nearer the camera and so biases k up.
  - **C3 (0.73):** it fitted the far tyre with a 55 px radius; the true radius is about 48.8 px. Its roof width is not the bounding box.
  - **C4 (0.66):** a guessed tyre width on SAM centres. I could not reproduce it.
  - **C5-C7 (0.95-1.10):** front-face widths read by eye. They lie outside both my routes.
  - **C8 (0.85):** close in value but not a measurement.
  - **Submitted 0.7906:** a blend whose component A = 0.753 carries the k fault above.

## Decision
- I verified round 1's change: the fault is reproduced and my own value (0.84) agrees with 0.845 within 1 %.
- Answer **0.845 m**, decision "new" (no candidate's method followed), confidence medium.
- The remaining uncertainty is about ±0.03 m. It comes from ±1 px in the far-tyre centre row and the 0.912-0.918 spread in k between routes.
