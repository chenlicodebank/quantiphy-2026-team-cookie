# q_2673 — ping pong ball displacement 0.9 s → 1.4 s (cm)

- question_fps = file fps = 24. t=0.9 → frame round(21.6)=22; t=1.4 → frame round(33.6)=34.
- Camera: f = 0.5959·1280 = 762.8 px, principal point (640,360). Static camera.
- Ball centres (scene/tracks/ball.csv, checked on 6× zoomed crops `frames/crop_22.png`, `crop_34.png`, script `crops.py`):
  - frame 22: (569.3, 453.4); by eye from crop: (569, 456.5)
  - frame 34: (838.5, 513.1); by eye from crop: (839, 514)
- Depths from depth_info: 1.010 m (t=0.9), 0.716 m (t=1.4).
- Back-projection (`compute.py`):
  - depth treated as Euclidean range along the ray: 41.7 cm
  - depth treated as z (method-card formula (u-cx)/f,(v-cy)/f,1)×d): 40.7 cm
  - 3-frame averaged centres (21–23, 33–35): 41.6 cm (second route, agrees)
- Displacement is dominated by the 29.4 cm depth change; the centre-pixel uncertainty (±3 px) changes it by <0.2 cm.
- Answer: 41.2 cm (midpoint of the two depth readings, both within 1.3 %). Confidence: good, ±5 %.
