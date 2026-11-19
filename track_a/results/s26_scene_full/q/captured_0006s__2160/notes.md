# q2160 – speed of the toy (yellow fruit) at first impact with the desk

File fps = question fps = 24. Camera f = 0.5959*1280 = 763 px, (cx,cy) = (640,360).
Depth_info: f24 (t=1.0) distance 1.402 m, f29 (t=1.2) distance 1.065 m.

## Events (checked on frames/seq.png, f26–35)
Released f19, apex f24–25, falls toward the camera, first contact with the table top between f31 and f32
(f32 is already sitting on the table, centroid v≈425). Free flight f20–31.

## Route 1 (main): ballistic 3D fit (fit.py, fit2.py)
I fitted X,Z linear in time and Y quadratic (g fixed at 9.8 or left free) to the scene/ centroids (u,v) of f21–31
(also tried other windows), with the two depth_info distances as constraints.
Pixel rms is 2–4 px and the depth residuals are ≤2.5 cm. Velocity ≈ (vx −0.1, vz −1.4…−1.6 toward the camera,
vy growing downward).
- With g free (it comes out as 8.5–9.1): speed 3.0–3.1 at f31 and 3.32–3.45 at f32.
- With g = 9.8: speed 3.16–3.19 at f31 and 3.53–3.56 at f32.
Contact: the centre at f32 sits on the table (Y≈0.075 m). The fitted Y is ≈0.015 at f31 and ≈0.13–0.145 at f32,
so contact happens about halfway between the two frames. Speed at that moment ≈ 3.25 (g free) to 3.36 (g = 9.8).

## Route 2 (check): depth from apparent size (route2.py)
Depth = f*D/size, with D calibrated at f24/f29, then the centroids back-projected. This is noisy because the elongated
fruit tumbles. A local fit over f26–31 gives speed at f31 = 2.7 (minor width) or 3.2 (eq_diam). It is consistent but
less reliable.
Simple check: the vertical pixel step f30→f31 at Z≈1 m gives vy≈2.6–3.0 m/s near contact. Combined with vz≈1.5,
that gives ≈3.0–3.4.

## Answer
3.3 m/s (the speed just before the first impact). Confidence: moderate, about ±10%. The reference may have used a
smoothed difference near the impact frame, which would give a somewhat lower value.
