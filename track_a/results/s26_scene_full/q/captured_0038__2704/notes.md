# q_2704 — distance white cup ↔ pink bottle (cm)

Lab video, 24 fps (file rate = question_fps), 1280×720, camera static, f = 0.5959×1280 = 762.8 px, principal point (640, 360).
Both objects are static. Measured on frame 34 (t = 1.4 s → round(33.6) = 34) with `measure.py` (edge profiles).

- White cup (tumbler): x 723–794 at the rim, ~726–790 near the base; y 377–498 → bbox centre (758.5, 437.5) px.
- Pink bottle: x 643–688/690, y 329 (lid top) to ~478 (base, partly hidden by the card stand) → centre (666, 403.5) px.
  These agree with scene/scene.json (within 1 px).
- Back-projection, ray normalised and scaled to the given camera distances (cup 0.8740 m, bottle 0.9998 m):
  3D distance = **17.3 cm** (`compute.py`). Most of it is the depth difference (Δz ≈ 13.8 cm), plus Δx ≈ 9.9 cm and Δy ≈ 3 cm.

Checks:
- The sensitivity to ±2 px in u and ±3 px in v on each centre gives a range of 16.8–17.8 cm.
- Prior check: the dark credit card is 98 px long at 0.6867 m, which gives 88.2 mm against the 85.6 mm prior (+3%), so the lab focal length is consistent.
- Plausibility: the bottle is about 19.7 cm tall × 6.2 cm wide and the cup about 14 cm × 8 cm. Both are realistic.

Confidence: good (about ±5%). The depth values given in depth_info dominate the answer.
