# q_2444 — velocity of the book at t = 1.0 s (frame 24, question_fps = file fps = 24)

## Method (measure.py)
- Book centre per frame from scene/tracks/teal_book.csv (full mask) and teal_book_cover_only.csv (cover only). I checked
  the record: the static camera, the motion onset between frames 18 and 19, and the ramp phase over frames 19-28.
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- 3D: P24 = 1.0685 m x ray(frame 24) and P29 = 0.977 m x ray(frame 29) (t = 1.2 s -> frame 29). The book slides along a
  straight ramp, so each frame's 3D centre is the closest point between its pixel ray and the line P24-P29. This
  reproduces both given depths exactly.
- Per-frame 3D speeds (m/s, backward difference ending at frame k): 22: 0.36, 23: 0.46, 24: 0.52, 25: 0.66, 26: 0.73, 27: 0.76, 28: 0.84.
  - Linear fit over frames 20-28: a ≈ 2.1 m/s², v(frame 24) = 0.57, v(24.5) = 0.61.
  - Forward difference smoothed over 5 frames (the reference convention): 0.625. The cover-only track gives 0.627.
- Taking the prior a = 2.8 m/s² from rest at onset frame ~18.7: v = 2.8 x (24 - 18.7)/24 ≈ 0.62 m/s, which agrees.

## Second route (route2.py)
- Ramp direction from the slope far/near depths (1.243 / 0.99 m) at the ramp edge midpoints gives a ramp length of 0.37 m.
  - v(24) = 0.62 and the 5-frame forward mean = 0.68.
  - But this route predicts a depth of 0.955 m at 1.2 s (given: 0.977), so it overestimates slightly. Route 1 is preferred.

## Answer
v ≈ 0.61 m/s = **61 cm/s**. Plausible range 57-66. The measured acceleration (2.1-2.2) is lower than the prior's 2.8, so
there is some scale uncertainty. Confidence: moderate.
