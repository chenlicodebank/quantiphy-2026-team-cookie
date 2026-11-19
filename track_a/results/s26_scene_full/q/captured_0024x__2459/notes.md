# q_2459 — length of the slope (cm)

File fps = question fps = 24. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Method
- Slope = white ramp board. Its outline was segmented in code at frame 48 (low saturation, high value; `board.py`,
  overlay `frames/board.png`). Corners: top (748,361)-(860,361), bottom on table (609,466)-(~706,491).
- Far end = top-edge midpoint (804, 361), depth 1.243 m; near end = bottom-edge midpoint (657.5, 478.5), depth 0.990 m
  (depth_info, treated as Euclidean camera-to-point distance). Back-projected both (`calc.py`).
- 3D distance = **0.3687 m = 36.9 cm**.

## Checks
- Left edge 35.6 cm, right edge 38.0 cm (same end depths applied to the corners), so the midline value of 36.9 sits between them.
- If the depths are read as Z instead of ray distance: 38.3 cm (+4%).
- Book check: back-projected book centres at t=1.0 (frame 24, 1.0685 m) and t=1.2 (frame 29, 0.977 m) are 16.1 cm apart.
  The prior a = 2.8 m/s^2 with the start at frame 19 predicts 18.2 cm. That is roughly consistent, given the ±1 frame
  uncertainty in the start frame.

Confidence: moderate-high (about ±5%). The main uncertainty is which exact points the end depths refer to.
