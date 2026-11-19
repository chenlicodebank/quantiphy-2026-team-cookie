# q_456 – length of the box (simulation_0189, 2D)

Prior: box speed = 0.094 m/s. 2D planar scene, so one m/px scale comes from the box's own pixel speed.
fps = question_fps = 120, so no re-timing is needed.

Measurements (measure.py):
- Box pixel speed: I matched a template of the box body against frame 0 every 10 frames (sub-pixel parabola).
  The box moves straight up at a constant rate. A linear fit gives 19.192 px/s (residual std 0.05 px), and a
  quadratic fit gives essentially zero acceleration. This matches the scene record (0.160 px/frame, 63.95 px over 400 frames).
- Box length (horizontal extent): the brown mask (R−B > 40) gives x 530–937 = 408 px on rows 220/270/320. The
  sub-pixel half-level edges of the averaged profile are 529.31 and 937.73, so 408.4 px. This is the same at frame 200.
- Scale = 0.094 / 19.192 = 0.0048979 m/px.
- Length = 408.4 × 0.0048979 = 2.000 m.

Second route: the scene record's independent numbers (408 px, 63.95 px / 3.333 s = 19.19 px/s) give 1.998 m.
Height for comparison is 187 px, or 0.92 m.
Confidence: high (about ±1%).
