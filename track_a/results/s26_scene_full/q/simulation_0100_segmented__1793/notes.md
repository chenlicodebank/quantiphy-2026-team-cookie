# q_1793 — average speed of the shark (m/s)

- 2D segmentation video, static camera, 24 fps (file fps = question_fps; no re-timing).
- Scale: boat length = 10 m. measure.py (frame 57 mask) gives the boat x extent 666–1521 = 856 px (stern hull to bow tip), which matches the scene record. So the scale is 0.011682 m/px.
- Shark motion: pure leftward translation. I tracked the left and right mask edges in every frame (measure.py):
  - Mean per-frame shift over frames 0→57: 10.58 / 10.54 px/frame. This includes the identical frames 0–1, when the shark is at rest.
  - Excluding that first step: 10.75 / 10.73 px/frame.
  - The scene record's template track gives 10.76 px/frame (excluding the first step), which agrees.
- Speed = px/frame × 24 × 0.011682:
  - 2.96 m/s including the rest step.
  - 3.02 m/s excluding it.
  - Answer: 3.0 m/s, which is within 1% of both conventions.
- Second route: the net reference-point travel of 602.4 px over 57 frames gives the same 10.57 px/frame, which agrees with the edge tracks.
- Confidence: high. The main uncertainty is the boat-length convention (bbox including the rudder fragment), about ±1%.
