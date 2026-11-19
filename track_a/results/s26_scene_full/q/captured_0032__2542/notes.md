# q_2542: distance between the white ball and the tennis ball at 1.5 s (cm)

- t = 1.5 s gives frame round(1.5 x 24) = 36. The file rate and question_fps are both 24. The record notes a dropped
  frame between frames 35 and 36. That doesn't matter here because only the position at frame 36 is needed.
- Camera: lab card f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Centres at frame 36 (measure.py, HSV masks, overlay in ov36.png):
  - tennis ball: (583.6, 433.6)
  - white ball: (721.1, 430.9)
  - The scene record has (582.3, 434.7) and (721.1, 430.1), which agrees.
- Back-projection: each centre's pixel ray, normalised and scaled to the Euclidean depth_info distance (tennis
  1.183 m, ping-pong 1.353 m). The 3D distance between the two points is **28.3 cm**.
- Second route: bounding-box midpoints give 28.29 cm and the record's centroids give 28.47 cm. Shifting the white
  centre about 1.5 px down, for the shaded underside its mask leaves out, changes the result by less than 0.2 cm.
- Scale check: at 1.183 m a 6.7 cm ball should be 43.2 px across. The measured mask is 40 px tall and 48 px wide
  (horizontal motion blur), which is consistent.
- Confidence: high, about ±1 cm. The result depends mostly on the given depth difference (17 cm) and the horizontal
  separation (about 137 px, about 22 cm).
