# q988 – whale displacement 0.5 s → 1.0 s

- fps 24 = question_fps → frames 12 → 24. 2D scene, static camera (scene record).
- Scale from prior: whale length 19.17 m. Whale straight and fully in frame at frames 47–53: mask length ~3450 px
  (bbox_w / principal axis); the mask stops ~10–20 px short of the snout tip → true length ~3465 px.
  Scale = 19.17 / 3465 = 0.005532 m/px.
- Head translation frames 12→24 (`tm.py`):
  - record jaw_front_x: raw −137.9 px, quadratic fit (f 6–30) −139.9 px
  - front_x_780_880: −136.1 / −135.9 px; snout_x: −144 / −140.4 px
  - second route, template matching of the head region (700×400 template): −142.4, −142.4, −141.1, −142.5 px for
    pairs (12,24), (11,23), (13,25), (10,22). Smaller templates and ones further back on the body sometimes lock onto the background, so I dropped those.
  - vertical motion < 1 px (head_cy is level).
- Adopted: 140 px × 0.005532 = 0.775 m.
- Confidence: good (±3%). The whale is assumed to be rigid at the head, so the rig origin moves with it. Tail bending
  shifts the whole-body centroid, but that is a mask artifact, not origin motion.
