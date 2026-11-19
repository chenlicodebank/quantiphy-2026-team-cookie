# q_1421 – side length of the orange floor tiles (simulation_0180)

The prior is the trolley's acceleration, 1.507 m/s² (constant, starting from rest). The depth_info gives the trolley's distance from the camera: 12.589 m at t=0 and 12.513 m at t=0.5 s. The file and question_fps are both 24 fps.

## Method
1. `tiles.py`: I made a background from the median of frames 0, 30 and 59, which removes the cart. I masked the orange tiles (HSV) and found each tile's 4 corners with approxPolyDP. Overlay: `frames/blobs.png`.
2. `calib.py`: I took the 12 orange tiles in the near U-shaped border, gave each one its grid coordinate (row tiles 76..84 = (0..7,0); column tiles 81,85,87 = (0,-1..-3); tile 86 = (7,-1)) and fitted a full pinhole camera. The fit had the rotation, the translation, the focal length f and a grout fraction g as free parameters, with the principal point fixed at the image centre. World units are one tile pitch.
   - Result: f = 2623 ± 30 px, g = 0.098, RMS error 1.4 px.
   - With the tile aspect ratio also left free: aspect = 1.007 ± 0.012 and f = 2637. So the tiles really are square and f is stable.
   - Camera centre: (7.39, -22.07, 6.48) tile pitches.
3. `cart.py`: I back-projected the cart's wheel-bottom track (scene/tracks/cart.csv, columns bottom_cx/bottom_y and wheels_cx/bottom_y) onto the floor plane.
   - The cart moves straight along the tile-row direction, with less than 0.04 pitch of sideways drift.
   - Fitting s = s0 + v0·t + ½·a·t² gives a = 2.946 to 2.969 pitch/s². The cart starts from rest at frame 0 (v0 ≈ 0), and the RMS error is 0.005 to 0.012 pitch.
   - Scale: 1.507 / a = 0.508 to 0.511 m per pitch. The total displacement over frames 0 to 59 is 8.96 pitch against ½·1.507·(59/24)² = 4.554 m, which gives 0.508 m/pitch.

## Second route (depth_info)
- At t=0 the cart's origin is about 24.0 to 24.7 pitch from the camera. The range depends on where the origin sits: at the bbox-centre height, somewhere between the near wheel line and 0.6 pitch inward. With the given 12.589 m this gives 0.510 to 0.524 m/pitch, which agrees with the acceleration route.
- The ratio of the distances at t=0.5 s and t=0 is 0.9944 predicted against 0.9940 given.

## Answer
The tile side, taken as the grid pitch (centre to centre, grout included), is **0.509 m**.
- If the grout line is excluded, the orange area alone is about (1 − 0.098) × 0.509 ≈ 0.46 m. The grout fraction comes from the colour mask and is probably overestimated.
- The answer uses the pitch.
- Confidence: about ±3% on the pitch.
