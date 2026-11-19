# q_2943 – length of the white box (cm)

The object is the small static printed white carton (scene/ `small_white_box`), lying on the floor near (517,496) px.
Depth at t=1.4 s (frame 34): 2.082 m. File fps = question fps = 24. f = 0.5959*1280 = 763 px, principal point (640,360).

## Pixel outline (boxmask.py)
I thresholded the crop and took the convex hull. The hull hexagon is identical in frames 10, 34 and 47 (the box is static):
far top corners A(521,465), B(541,470); near top-left F(492,505); near bottom E(494,521), D(512,527);
inner near top-right G = F + (D-E) = (510,511). The brown near-end face is F-G-D-E.
Top-face long edges: A-F 49.4 px and B-G 51.4 px. The long axis points diagonally away from the camera, so it is foreshortened.

## Naive method card
pixel length * depth / f = 13.5-14.0 cm. This ignores the foreshortening of the long axis, which runs into depth.

## Floor-plane correction (floor.py, vel.py, boxlen.py)
- I took the floor normal from the vanishing points of the moving board's quad (frames 20-32, which are consistent, with about 85-88 deg
  between the two vanishing directions): n ≈ (0.08..0.18, -0.83, -0.54).
- Check against the prior: with n = (0.08,-0.83,-0.54) and the board at 2.815 m at frame 34, the 5-frame mean of the per-frame
  speeds over frames 32-36 is 1.93 m/s, against the prior of 1.9339 m/s. Note that this window includes the dropped-frame double step at 35->36.
- I back-projected the box corners onto the plane parallel to the floor that passes through the box top, at the box centre (2.082 m) + H/2.
  Results: height H (F-E) ≈ 5.7 cm, width ≈ 5.0-5.9 cm, length A-F 16.7-17.2 cm and B-G 17.1-17.8 cm across the plausible
  normals and offsets.
- Answer: length ≈ 17.0 cm. The box is about 17 x 5.5 x 5.7 cm, a plausible carton.

## Confidence
Moderate. The main uncertainties are the floor-normal estimate (about ±3%) and the ±1 px corner positions (about ±2-3%).
The naive no-foreshortening value is 13.7 cm.
The depth_info points (bin, bag, toy) do not fit a single floor plane, so I did not use them for the floor orientation.
