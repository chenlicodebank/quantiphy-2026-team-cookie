# q_424 — displacement of the elephant (m)

Prior: elephant speed = 1.424 m/s. No depth_info. 2D scene, camera static, fps = question_fps = 24, 60 frames (t 0 → 59/24 = 2.458 s).

## Method
- Used the record's elephant track (`scene/tracks/elephant.csv`, ref point = torso centre via template tracking), re-checked with `check.py`.
- Motion is purely horizontal and nearly constant: per-frame steps 3.53 ± 0.21 px; net displacement f0→f59 = 208.15 px, path 208.43 px.
- Scale from prior (speed taken as mean per-frame speed): 3.533 px/frame × 24 = 84.78 px/s ↔ 1.424 m/s → 0.01680 m/px.
- Displacement = 208.15 px × 0.01680 = 3.496 m.

## Second route
- Constant speed assumption: 1.424 m/s × 59/24 s = 3.501 m.
- Independent reference point: rump edge moved 208.0 px (linear fit slope 3.42 px/frame); with the ref-point linear-fit slope 3.50 px/frame the ratio net/rate is the same within ~1 %.

## Answer
3.50 m. Confidence high (scale ratio cancels pixel errors; only depends on the prior being the average/constant walking speed).
