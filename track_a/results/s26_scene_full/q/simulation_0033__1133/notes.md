# Q1133: height of the streetlight (m). Answer: 4.12 m

Question fps is 30 and the file fps is 30.005. I used frame indices throughout (t=1 s is frame 30).

## Lamp pixel height (measure_lamp.py + a direct pixel dump)
The lamp is static. The finial tip is at y ≈ 327.7 (x 195-198) and the base bottom at y ≈ 891.5 (pole x ≈ 192.5). That gives a height of **563.8 px**, which matches the record's 565 px.

## Focal length (from the orange car: prior + depth_info)
- Car speed comes from masked template matching (orange pixels only, track_tm2.py, tm2_shifts.csv). The pixel speed falls linearly: 37.2 px/frame at f3 and 12.0 at f53.
  The acceleration is 0.509 px/frame² both at f3-25 and at f41-53, so it is constant: 463 px/s².
  The prior of 2.86 m/s² then gives **s_car = 0.00617 m/px** (route A).
- Position: I integrated the shifts and anchored them on the Hough axle midpoints (frames where both wheels are found). This gives u(f0) ≈ 1480 (off-screen) and u(f30) ≈ 540.
  The car's depth is constant, so d0² − d30² = s²(dx0² − dx30²). That gives **s = 0.00632-0.00641** (route B), with the range set by the origin x: axle midpoint or bbox centre.
- f = Z/s, with Z = sqrt(d30² − s²(dx30² + dy²)) ≈ 10.05-10.24 m.
  Route B gives f ≈ 1566-1619 and route A gives 1631-1659. The two scales differ by 2-4%. I adopted **f ≈ 1615 ± 35**.
  The pedestrian route is ill-conditioned (its depth changes by only 0.13 m), so I did not use it.
  As a sanity check, the pedestrian's height with f ≈ 1600 comes out at about 1.8 m.

## Height (height.py)
H = h_px · Z_l / f, with Z_l = d_l / sqrt(1 + ((u−cx)² + (v−cy)²)/f²) and d_l = 12.325.
- Origin at the lamp base (y 891.5): Z_l = 11.78, giving **H = 4.13 m (f 1610)** and 4.08 m (f 1630). The range over f 1566-1660 is 4.01-4.23.
- Origin at the bbox centre: Z_l = 12.04, giving H = 4.22 m (f 1610).

The base origin is favoured, by two checks:
- The hydrant (d 12.565) and lamp base rows are consistent under the base-origin hypothesis: predicted 2.4 px, observed about 1 px. Under the centre hypothesis the sign is wrong (predicted −2.6 px).
- The curb and sidewalk geometry points to a lamp depth below 12.

The answer is 4.12 m. The centre-origin reading would give about 4.2 m, which is within 2.5%.

## Confidence
Moderate to high: the expected error is about 3%. The main uncertainties are f, where the two routes differ by 2-4%, and the location of the lamp's origin (about 2%).
