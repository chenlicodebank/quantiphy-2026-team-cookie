# q1344 — height of the green car (m)

The file and the question both run at 24 fps, so t = 0.58 s is f14 and t = 1.58 s is f38. The green car is parked (static), so I measured it on f0.

## Camera calibration (pinhole, principal point at the image centre, no roll)
- Vanishing points come from least-squares Hough lines on scene/bg.png (`lines.py`, `vp.py`):
  road A at (623, 76), road B at (3127, 76) (the far-sidewalk back edge gives the same point, (3124, 77)), and the vertical VP of the poles at (1069, 2058).
  The horizon is level at v = 76.
- Focal length: perpendicular roads give f = 849 px. The vertical VP with the horizon gives f = 839 px.
  Check against the depths: the pedestrian's 3D displacement between f14 and f38 (rays × the given depths) is parallel to road B only near f ≈ 850
  (it is 0.3° off at 854 and 2–3.5° off at 800 or 900; `dircheck.py`). I used f = 848 px, which makes the pitch 28.7°.
- The depth_info alone constrains f only weakly (`calib.py`, `check.py`).
- Camera height above the ground, from the pedestrian at f38: the pelvis pixel (365, 439) back-projected with depth 21.349 m, and the feet at v = 479 directly below it,
  give a pelvis height of 0.84 m and a camera height H = 6.95 m (`ground.py`).
  Check: for the van, the taxi and the cyclist, the ground point under their lowest pixel lies 2.6 m, 2.5 m and about 1 m short of the origin's horizontal range from the depths.
  That matches about half a vehicle length (`sens.py`), so H is consistent.
- Prior check: the van's acceleration from centroid tracks on the ground plane comes out 4.5 m/s² against 4 in the prior.
  The centroid is a biased proxy for the origin and this check depends only weakly on f, so I treat it as a rough check only.

## Green car (`pairs.py`, `sens.py`, `profile.py`)
- The near-side tyre contacts at pixels (1518, 414) and (1597, 397.5) are projected onto the ground plane.
  The wheelbase comes out 2.77 m, and the car's axis is parallel to road B within 0.4°.
- Width: I took the near headlight outer edge to lie in the body-side plane, 0.10 m outboard of the contact line. Pairing it with the far headlight gives an outer-headlight width of 1.52 m.
  The car's centreline therefore lies 0.66 m beyond the near contact line.
- Route 1: the two top corners of the windshield form a lateral pair, (1558, 349) and (1514, 339.5), whose midpoint lies on the centreline. This gives a header height of 1.38–1.39 m.
- Route 2: the far top edge of the roof at (1536, 333.5), taken at the far-roof lateral offset, gives 1.40–1.41 m.
- Sensitivity: ±1 px at the tyre contact changes the height by ±0.02 m, ±0.1 m in H by ±0.02 m, and f = 839–848 px by less than 0.01 m.
- Sanity check: the car looks like a BMW E24 (real height 1.35 m, wheelbase 2.63 m). Scaled by the wheelbase ratio, that gives about 1.42 m.

Answer: the height (the vertical extent of the bounding box, up to the highest point of the roof) is about **1.41 m**. Confidence: moderate, roughly ±5 %.
