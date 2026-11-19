# q_2531 — distance white ball ↔ tennis ball at t=1.6 s (cm)

- t=1.6 s × 24 fps (question fps = file fps) → frame 38.
- Lab method card: f = 0.5959×1280 = 762.8 px, principal point (640,360).
- Centres in frame 38 (my measurements in code, `measure.py`, `white.py`):
  - tennis (yellow) ball: upper-arc circle fit (739.9, 452.7), enclosing circle (740.5, 453.5); scene record says (738.8, 452.0). I used (739.5, 452.5).
  - white ball: circle fit to the left/right edges of its low-saturation mask, (662.2, 443.7), diam 27.7 px; scene record says (662.4, 445.0).
- Back-projection P = ((u−cx)/f, (v−cy)/f, 1) × depth, with depth 1.19 m (tennis) and 0.994 m (white).
  - Distance = 23.58 cm with my centres, 23.47 cm with the scene-record centres.
  - If I treat depth as the Euclidean range along the ray instead, I get 22.4 cm (a −5% alternative). I answer with the method card's convention.
- The depth difference (19.6 cm) dominates, and the lateral separation is about 10 cm, so the answer is set mainly by depth_info.
- Sanity check: the tennis ball's pixel diameter (~52–55 px) and the prior of 6.7 cm imply a depth of about 0.93–0.98 m, not 1.19 m. So depth_info does not quite match the image sizes, but the reference was built from the measured depths, so I used them as given.
- Answer: 23.5 cm. Confidence: moderate (depends on the depth convention).
