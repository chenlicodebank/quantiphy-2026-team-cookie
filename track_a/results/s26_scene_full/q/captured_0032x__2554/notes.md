# q_2554 — distance white ball ↔ tennis ball at t = 1.5 s (cm)

- t = 1.5 s → frame 36 at question_fps 24 (file is 24 fps too). Lab camera: f = 0.5959·1280 = 762.8 px, (cx,cy) = (640,360).
- Ball centres measured in code (measure.py): HSV mask, circle fitted to the upper contour (the lower rim is shaded).
  Frame 36: tennis (yellow) (583.2, 435.0), diameter 42.4 px; white (721.4, 433.6), diameter 23.9 px. The overlay
  (frames/overlay36.png) sits on both balls. A second centre estimate (minimum enclosing circle) gives the same distance.
- Back-projected along the pixel ray, normalised to the given Euclidean depths (tennis 1.183 m, ping-pong 1.353 m):
  **distance = 28.4 cm** (enclosing-circle centres give 28.36 cm, fitted-circle centres 28.38 cm).
- Checks: the tennis ball's pixel diameter of 42.4 px at 1.183 m gives 6.6 cm, close to the 6.7 cm prior; the prior predicts 43.2 px.
  The white ball's diameter gives a depth of 1.28 m if it is a 40 mm ping-pong ball (the given depth is 1.353 m; its mask is
  slightly blurred). Neighbouring frames give 22.9 cm (frame 35) and 31.3 cm (frame 37). The distance changes fast because
  the balls are moving apart, and the scene record notes a likely dropped frame between 35 and 36. A 5-frame smoothing
  would give about 27.5–28 cm. A 2 px error in a centre moves the result by about 0.3 cm.
- Most of the distance is the given depth difference (≈17 cm) plus about 23 cm of sideways separation, so the result is not very sensitive to the pixel measurements.
- Confidence: good (±1 cm), mostly limited by how the reference handled timing and smoothing.
