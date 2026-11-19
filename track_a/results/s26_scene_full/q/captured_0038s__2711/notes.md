# q2711 — distance white cup ↔ pink bottle (cm)

Lab video, 24 fps (file and question fps agree), 1280x720, static camera; both objects are static.
Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Centres = bbox centres of colour masks
(measure.py, frame 20, ball far away), back-projected along the pixel ray with depth_info as the Euclidean camera distance.

- Pink bottle mask bbox 638,332–687,476 → centre (662.5, 404.0); depth 0.9998 m (bottom ~2 px hidden by card tent; negligible).
- White cup mask bbox 724,379–794,496 → centre (759.0, 437.5); depth 0.8740 m.
- Overlay frames/masks.png confirms both boxes.
- 3D distance = **17.6 cm** (depth difference ~12.6 cm, lateral ~12 cm).

Checks: treating depth as z instead of ray length gives 16.8 cm; mask centroids instead of bbox centres change the
result by <0.3 cm. Scene-record boxes (636,332,687,477 / 724,378,794,497) agree within 1-2 px.
Card sanity check: dark card ~101 px wide at 0.6867 m → ~9.1 cm vs 8.56 cm prior (oblique view), consistent scale.
Confidence: moderate-high; main uncertainty is where annotators clicked the centres (±1 cm).
