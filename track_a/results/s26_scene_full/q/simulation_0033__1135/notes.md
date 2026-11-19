# q1135: speed of the green car at t = 1.0 s (m/s)

The "green car" is the dark grey-green, motion-blurred car in the near lane. It is called grey_car in scene/ and drives right to left.
The time base is question_fps = 30, so t = 1 s is frame 30. The file runs at 30.0055 fps, which makes no difference here.

## Calibration (orange car, a check on the camera model)
- I fitted the orange car's wheel-centre tracks (scene/tracks/orange_car.csv, front wheel f10-31 and rear wheel f33-53) with one shared quadratic (orange_fit.py).
  The pixel acceleration is 471 px/s² (460 from the front wheel and 486 from the rear wheel alone).
  With the prior of -2.86 m/s² that gives k_o = 0.00607 m/px.
- Independent check from depth_info: d0² - d1² = k²[(u0-cx)² - (u1-cx)²], with the axle midpoint at u = 1509 (t=0) and 546 (t=1) and cx = 540.
  This gives k_o = 0.00615-0.0062. It agrees with the prior to within about 1.5%, so the pinhole model holds.
- The focal length is f = Z_o/k_o, with Z_o about 10.1-10.2 m, so f is about 1650 px (horizontal FOV about 36°).

## Green car (main route: depth_info plus the crossing time)
The car drives parallel to the image plane, so d(t)² = Z² + Y² + X(t)².
- At constant speed V, X0 = X1 + V, so d0² - d1² = V² + 2·V·X1. Equivalently V² = (d0² - d1²)/(2·t_c - 1), where t_c is the time the origin crosses the optical axis (X = 0, column 540).
- d0² - d1² = 13.077² - 4.630² = 149.57 m².
- The crossing time comes from cross540.py. It finds the green car's leading silhouette (f20-25) and trailing silhouette (f35-40) in the road rows y = 995-1015, using a difference against frames 19 and 44, and fits each with a line.
  At column 540, depth does not affect the projection, so the time an edge passes x = 540 is exact.
  - The front crosses at f25.01, 24.77 and 24.57, and the rear at f35.26, 35.55 and 35.68 (rows 995, 1005, 1015).
  - The midpoints are f30.14, 30.16 and 30.12, so t_c = 30.14/30 = 1.0047 s.
- V = sqrt(149.57/(2·1.0047 - 1)) = 12.17 m/s, with X1 = 0.06 m. The result is insensitive to t_c: ±0.5 frame changes it by about ±0.2 m/s.
- Check: the front-to-rear passage takes about 10.3-11.1 frames, which at 12.17 m/s is a 4.2-4.5 m car (at those rows). That is plausible.

## Constant-speed check
- The silhouette speeds are flat within each window: lead 114 px/frame (f20-25) and trail 120-126 px/frame (f35-40).
- Template tracks of features on the car body are also flat: about 139 px/frame at y≈1015 over f27-32 and about 163 px/frame at y≈1070 over f30-37 (tmpl.py). Both may be reflections.
- There is no deceleration trend. The small jump between the lead and trail windows (about 5%) could be a slight acceleration (up to about 1 m/s², which would give about 12.7 m/s), or just the shape of the silhouette. I used constant speed.

## Second route (pixel speed times depth over f), which is weaker
- The silhouettes move about 117 px/frame. With f = 1650, the far side of the car at Z of about 5.3-5.7 m gives V of about 11.3-12.2 m/s.
- This depends on the camera height, the origin height and the car's width, which are all unknown. It is consistent with the main route to within about 7%.

Answer: 12.17 m/s. Confidence is moderate, about ±5%. The main risk is the car not moving at constant speed between t = 0 and 0.67 s, when it is off-screen.
