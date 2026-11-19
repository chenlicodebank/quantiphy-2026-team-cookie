# q_723: acceleration of the paper airplane at t = 1.25 s

- The file fps (24) and question_fps (24) agree, so t = 1.25 s is frame 30.
- 2D scene: the camera is static and the plane's pixel length is constant at about 140 px, so I used one metres-per-pixel
  scale.
- **Scale:** chalkboard = 5 m. I checked the board extents on frame 30 with a grid: the outer wooden frame is
  1372 px wide and the green surface is 1327 px. I took the whole object (with its frame), which gives
  5/1372 = 3.644e-3 m/px. The green-only scale would be about 3.4% larger.
- **Track:** `scene/tracks/paper_airplane.csv`, frames 13–36. These frames show the plane's full outline on the
  board, clean to ±1–2 px. I used the nose–tail midpoint (`ref_*`) and also the bbox centre.
- **Pixel speed:** about 76 px/frame up to f20, then it falls steadily: 62.3 px/frame at f29 and 61.2 at f30
  (frame-to-frame differences). That is about −1.3 to −1.5 px/frame².
- **Acceleration at f30** (`accel.py`), outer-frame scale:
  - Raw one-frame differences are noisy: −2.3 (ref) and −1.0 (bbox).
  - Polynomial fits of x(t) and y(t) (degree 2–4, windows ±6 to ±11 frames), then backward-difference speeds:
    −2.5 to −3.4, mostly about −3.0 to −3.3.
  - Linear fit of the speed series over ±3 to ±6 frames: −3.0 to −3.5.
  - The ref-point and bbox-centre routes agree within about 0.1.
- **Answer:** magnitude of the deceleration ≈ 3.1 m/s². The plane is slowing down; the question wants a positive
  number. With the green-only scale it would be about 3.2.
- **Confidence:** moderate, about ±10%. The spread comes from noise in the second derivative and from which board
  extent counts as its "length".
