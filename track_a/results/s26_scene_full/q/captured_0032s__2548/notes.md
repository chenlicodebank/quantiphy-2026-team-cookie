# q_2548 — distance white ball ↔ tennis ball at t = 1.5 s (cm)

- t = 1.5 s → frame 36 (question_fps 24 = file fps). (scene/ notes a probable dropped frame between 35 and 36; the frame index is still 36.)
- Camera: lab method card, f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Centres at frame 36 (measure.py → crop36.png at 5x, plus scene tracks): tennis (yellow) ≈ (583–584, 434–435) px,
  white ≈ (722.3, 433–436) px. Apparent sizes: tennis ≈ 44 px tall (50 px wide incl. horizontal blur), white ≈ 22 px tall
  (25 px wide incl. blur); these agree with the depths: 6.7 cm at 1.183 m → 43.2 px expected; 4 cm ping-pong ball at 1.353 m → 22.5 px.
- Back-projection P = ((u−cx)/f, (v−cy)/f, 1) × depth (compute.py), depths 1.1830 m (tennis), 1.3530 m (white):
  distance = 28.9–29.0 cm across the three centre estimates; treating depth as Euclidean range along the ray gives 28.4–28.5 cm.
- Answer: 28.9 cm (method-card convention). Second route (Euclidean-range reading and different centre estimates) within 2 %.
- Confidence: good; the result is dominated by the given depth difference (17 cm) and the 139 px lateral separation (~22.7 cm).
