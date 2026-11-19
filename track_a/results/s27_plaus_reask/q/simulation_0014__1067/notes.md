# q_1067 – height of the house's door (simulation_0014)

File fps = question fps = 24. Static camera, 1920x1954, principal point taken as image centre (960, 977).

## Pixel measurements (frame 72, door_px.py: row brightness profiles)
- Doorway opening (dark): y 948.5 -> 1175.5 = **227 px**; the open door leaf (left): y ~950 -> ~1173 = 223 px.
- Barrels at the barn front (same depth as the door): top rim y ~1097, bottom ~1190 = **93 px**. Ratio door/barrel = 2.44.
- Cart wheel (cart distance 27.562 m): vertical diameter ~186 px (y 1062-1248).
- Horizon from the ground-plane relation (cart ground 1248 at 27.56 m, barn base 1183 at ~55 m): y_h ~1110-1118; camera height x f ~ 3550 px·m.

## Scale: the gravity route vs real-world sizes
- The falling object is a twig bird nest (the "nest" of depth_info), a soft body that sags and slides off the branch from about frame 20, then falls and lands at frame 49-50.
- Fits of the fall (fit_fall.py, fit2-4.py; the landing depth is pinned from the ground plane at Z ~4.6 m) only constrain a·f ~ 18,400 px·m/s². Taking a = 9.8 m/s² gives
  f ~ 1,900 px. That would make the door ~6 m, the barrels ~2.6 m, the cart wheel ~2.7 m, the nest ~0.8 m wide and the leaves 15-20 cm: every object would be ~2.7x
  its real size. The nest's distance change from t=0 to t=1 (-0.031 m) fits either f (it depends on how much the nest moves toward the camera).
- Per the benchmark rule (an everyday object off by more than 40 pct means the geometry is wrong), I take the scale from standard objects instead. The soft-body nest
  evidently falls at ~0.4 g in world units (soft-body damping/goal), so its fall gives no usable scale.
- Standard objects (consistent with each other at f ~ 5,000-5,300 px):
  * Barrels ~0.9-0.95 m tall -> door = 2.44 x barrel = 2.20-2.32 m (independent of depth and focal length).
  * Cart wheel ~1.0 m at 27.3 m -> f ~ 5,000; door front wall at ~52.5 m (house origin 55.77 m minus about half the house depth) -> door ~2.3-2.4 m.
  * At f = 5,300: the nest is 0.29 m, the wheel 0.96 m, the barn front 5.4 m wide and 6.1 m to the apex, and the camera 0.67 m high. All plausible.
- Answer: door height ~ **2.25 m** (opening 227 px x 52.5 m / 5,300 px).

## Confidence
Moderate. The scale rests on typical object sizes (barrel/wheel), not on the gravity prior. If the scene were truly built so that the nest falls at 9.8 m/s², the answer
would be ~6 m instead. Reading the question as the door leaf instead of the opening changes the result by only ~2 pct.
