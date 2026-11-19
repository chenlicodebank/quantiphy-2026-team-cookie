# q_2490: ping pong ball distance travelled, 1.1 s to 1.3 s (cm)

- Time base: question_fps = file fps = 24. t=1.1 s is frame 26 and t=1.3 s is frame 31.
- Frame 26 is the first bounce on the table. It is blurred, and the streak contains both the descent and the rebound. Frames 27–31 are the rise towards the apex at frame 32. `view.py` writes `frames/montage.png`; I checked the masks and centres on it.
- Method (lab card): f = 0.5959 × 1280 = 762.8 px, principal point (640, 360). Each frame's centre in `scene/tracks/ball.csv` (mask centroid) is back-projected to 3D. The depth is a Euclidean distance, so it is applied along the normalised ray. Depth is interpolated linearly between the given values: f26 = 1.557 m and f31 = 1.4115 m. Path length = sum of the frame-to-frame 3D displacements (`measure.py`).
- Result: segments 4.75, 6.76, 5.58, 4.54, 3.55 cm, total **25.2 cm**.
- Checks:
  - Straight-line displacement f26→f31 = 24.7 cm, consistent because the path is nearly straight.
  - If the frame-26 centre is taken at the contact position (bottom of the streak minus the radius): 26.3 cm. If it is taken at the top of the streak: 23.8 cm. Spread is about ±5%.
  - Ball diameter from the pixel width and depth at f31/f32 is 4.24 / 4.29 cm, against the 4.0 cm prior. This confirms the scale to about 6%.
- Confidence: moderate-high. The main uncertainty is where the frame-26 centre is placed on the blurred bounce streak.
