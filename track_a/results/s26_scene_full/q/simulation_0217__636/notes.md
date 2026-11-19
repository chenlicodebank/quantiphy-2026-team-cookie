# q_636 — width of the white sofa (m)

Prior: black cat speed = 0.94 m/s. There is no depth_info. The scene is a 2D top-down render at 24 fps (file fps =
question_fps = 24, so no re-timing).

## Scale (measure.py)
- I re-tracked the black cat on all 50 frames (mask max(BGR) < 60).
  - Front-edge steps are 10–12 px/frame, with a mean of 10.98 px/frame.
  - The whole-mask centroid moves 10.92 px/frame (net) and 10.93 px/frame (mean step).
  - Its speed is constant, so I used 10.95 px/frame = 262.8 px/s.
- Scale = 0.94 / 262.8 = **0.003577 m/px**.

## Sofa extent (sofa3.py, frame 0, overlay frames/sofa_edges.png)
- I scanned each column for the edge between the sofa (grey level about 120–135) and the carpet (65–95), threshold
  108. Columns where the sofa meets the sunlit floor were excluded.
  - Top of the left arm: y = 519. Top of the right arm: y = 520.
  - Bottom of the back: y = 996, at x ≈ 970–1030.
  - Horizontal extent: from x ≈ 567 (the edge at the rug, found from row profiles) to 1450.
- The axis-aligned box is about 883 px (x) by 477 px (y).
- Width is the shorter horizontal extent, which is the front-to-back depth: 477 px, giving **1.706 m**. The length
  would be 883 px, giving 3.16 m.

## Perspective check
- The camera is a perspective camera looking straight down. The tops of the walls sit about 1.065 times further from
  the image centre than the floor edges: left edge 158 → 100, right edge 1745 → 1790, top edge 122 → 99.
- So the walls reach h_w ≈ 0.06 H, where H is the camera height. With real-scale walls of about 2.5–3 m, H is about
  40–50 m.
- The sofa's lower outline (top of the back, about 0.75 m high) lies about 456 px from the image centre. That makes it
  look about 1–3 % larger than it would in the cat's plane (cat origin about 0.2 m high).
- The arms' top edge is near the image centre (y ≈ 520 vs cy ≈ 540), so its position is barely affected.
- I applied a correction of about 1 %: 1.706 → **1.69 m**.

## Second route
- The sofa's real-world proportions look sensible at this scale. The cat's body without the tail is
  152 px × 0.003577 = 0.54 m, a normal cat. The rug is 1.74 m across and the room is 5.7 m wide.
- Using the cat's front-edge speed alone (10.98 px/frame) gives 1.701 m before the perspective correction, about
  0.3 % different.

Confidence: moderate-high. The main uncertainty is the perspective height correction (0–4 %).
