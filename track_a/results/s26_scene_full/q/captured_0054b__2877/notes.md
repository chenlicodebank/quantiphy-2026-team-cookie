# q_2877 – distance green ball ↔ white ball at t = 1.0 s (frame 24)

- File fps = question_fps = 24, so frame 24.
- The "green ball" is the yellow-green tennis ball (called `yellow_ball` in scene/). The white ball is `white_ball`.
- Frame 24 (frames/crop24.png): both balls are motion-blurred streaks. The streak centroids from scene/tracks
  are green (325.3, 268.3) and white (377.1, 247.4). A visual check on a zoomed crop with a grid gives (326, 270)
  and (377, 247), which agrees.
- Camera: f = 0.5959·1280 = 762.8 px, c = (640, 360). Depths from depth_info: green 1.331 m, white 1.235 m.
- Back-projection as in the method card, X = d·((u−cx)/f, (v−cy)/f, 1): distance = 0.158 m (0.1575 with the
  visual centres).
- Alternative reading, with depth as the Euclidean ray length (normalised ray): 0.127 m. This reading is not
  used; I followed the card's formula.
- Most of the distance comes from the depth difference (0.096 m). The rest is the lateral offset, about 56 px,
  or roughly 0.09 m.
- Confidence: moderate. The two depth conventions differ by about 20 %.

Answer: 0.158 m
