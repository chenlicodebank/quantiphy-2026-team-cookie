# Q1201: diameter of the moving bicycle's wheel. Answer: 0.65 m

The video and the question both use 33 fps. Frame f is at t = f/33, so t=1 is f33 and t=2 is f66.
Prior: bike speed 4.87 m/s. Bike depth is 14.1134 m at t=1 and 18.9543 m at t=2.

## Geometry of the scene
- The camera is static and level. The bike rides almost straight away from the camera, so its wheels are
  seen edge-on. The rear wheel's vertical extent is its diameter. That extent runs from the tyre ground contact to
  the tyre top, which sits just under the white rear-rack plate at the top of the blue rear mudguard.
- The tyre-contact row fits v = vh + K/(frame + c) with rms 0.8 px: vh = 537.2, K = 20023, c = 57.51 (`depth_fit.py`).
  - The bike's depth rate is (18.9543 - 14.1134)/33 = 0.14669 m/frame, so the contact depth is
    Z_c = 0.14669 (frame + c).
  - The origin depth extrapolates to 0.14669 (frame + 63.2), so the rear contact is about 0.84 m nearer than the
    bike origin. The pixel-height ratio of the rider agrees.
  - Wheel size: D = D_px · Z_c / f.

## Focal length: manhole cover (`manhole_model.py`)
- A flat circle on a level ground plane gives f = (v_mid - vh) · W / H.
- I fitted a blurred-step model to the cover, averaged over frames 20-98.
  - Inner disc: H/W = 27.5/174.4 = 0.158.
  - Outer ring: 33.4/207.2 = 0.161.
  - Middle row: 840.0.
- Results: f = 1921 (inner) or 1872 (outer) with vh = 537.2. With vh = 533 they are 1948 and 1904.
  Best estimate f ≈ 1900 ± 50 px (horizontal field of view about 54°).
- Real-world sanity check:
  - Camera height h = K · 0.14669 / f ≈ 1.5 m.
  - The cyclist's head top is about 1.65 m above the ground, and the pedestrian is about 1.7-1.85 m tall. Both are plausible.
- Rejected route: if the 4.87 m/s were exact constant 3D speed along a straight line, the small extra over the
  4.841 m/s radial rate would force f ≈ 900 px. That gives a rider about 3.5 m tall, and it contradicts the manhole
  value. Because the motion is almost entirely radial, that route is very sensitive to 0.5 % speed noise, so I did
  not use it.
- The human depth_info (19.04 m and 20.27 m) does not match the image: the pedestrian's feet are on the same image
  row as the bike's tyre, so the two are at about the same depth. It looks like an offset rig origin, so I did not
  use it.

## Wheel pixel size (`fender_prof.py`, `plate_prof.py`, `strut_end.py`)
- Tyre top = bottom edge of the white rack plate:
  | frame | plate bottom row | ground row | D_px |
  |---|---|---|---|
  | f0 | 738.5 | 885 | 146.5 |
  | f2 | 731.5 | 874 | 142.5 |
  | f4 | 725.3 | 863 | 137.7 |
  | f6 | 719.7 | 853 | 133.3 |
  | f10 | 709.5 | 834 | 124.5 |
  | f20 | 688.3 | 795 | 106.7 |
  | f30 | 671.0 | 767 | 96.0 |
  | f40 | 657.6 | 743 | 85.4 |
- D_px · (frame + 57.51) is about 8370 (range 8240-8480).
- Check by a second route, from the axle: the rack struts end at the rear axle (about 811 at f0 and 802 at f2).
  Doubling the axle height gives 2 × 74 = 148 px at f0 and 144 px at f2, so D_px · (frame + c) ≈ 8510-8570.
- The top of the saturated blue mudguard gives 8130, a lower bound.
- Combined value: D_px · (frame + c) ≈ 8400 ± 150.

## Result
- D = 8400 × 0.14669 / 1895 = 0.650 m with vh = 537.2.
- With vh = 533 (c = 59.24, f = 1925) D = 0.655. With vh = 530, D = 0.66.
- Using only the inner-disc f gives 0.64; only the outer-ring f gives 0.66.
- **Answer 0.65 m.** Confidence: moderate, about ±5 %. The main uncertainties are the focal length (±2.5 %) and
  where exactly the tyre top sits under the rack and mudguard (±2 %).
