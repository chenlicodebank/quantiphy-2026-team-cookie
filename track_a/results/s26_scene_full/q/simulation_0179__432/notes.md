# Q432 — height of the entrance gate (incl. frame), prior: cart acceleration = 1.507 m/s²

Time base: fps 24 = question_fps, no re-timing.

## Cart acceleration in pixels (accel.py)
Quadratic fit of the record's track (scene/tracks/shopping_cart.csv, checked: one cart, frames 0-59, pure +x motion):
bbox_cx a = 295.8 / 294.8 / 295.5 px/s² (fits from frames 2/10/20), wheels_cx 294–295, rms 0.5 px; motion starts at t≈0.
Handle-tip / front edges give 288 / 302 (the visible extent grows by perspective); use 295.3 px/s².
→ 1.507/295.3 = 0.005103 m/px at the cart's depth.

## Perspective (lines.py, vp.py, model.py)
The "2D" scene has clear perspective, and the gate is at a different depth: its near post stands on the floor at y=957 and its far post at y=775, while the cart's wheels are at y≈866–884.
- LSD line segments. The receding floor lines (142 of them) meet at (959.8, 212.9), so the horizon is y_h = 212.5 and the principal point x is 960.
  Long verticals (34 gate/door edges) meet at y ≈ 22300 below the image.
- Level camera with zero roll and yaw, pitched down: f = sqrt((540-212.5)(22300-540)) = 2670 px (hfov ≈ 39.6°), pitch 7.0°.
- Camera height h = 1 for the reconstruction. The cart origin is at the cart's mid-depth ground row (≈875, between near wheels 884 and far wheels ≈866) and half the cart height above the floor.
  Its camera depth Zc gives m/px = Zc/f, which fixes h = 3.37 m (the cart then has height 1.24 m).
- Gate: the front-left vertical edge of the near wooden post runs from floor (222, 957) to frame top (193, 51), giving H = **4.076 m**.
  Independent check on the far post, floor y=775 to beam top y=93: **4.069 m**. The two agree to 0.2%, which supports the horizon and pitch.

## Sensitivity
- Vertical VP from 21000 to 23500 (f 2589–2742): ±0.003 m.
- Cart ground row from 866 to 884: 4.02–4.13 m.
- Origin at the cart's base instead of its centre: −0.02 m.
- a_px ±1%: ±0.04 m.

A naive single 2D scale (906 px × 0.005103) would give 4.63 m. That is rejected because the gate post is clearly nearer the camera than the cart.

Answer: 4.07 m (confidence moderate, about ±4%).
