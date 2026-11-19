# q_2243 — displacement of the rolling ball, 0 s → 0.6 s (cm)

The file fps and question_fps are both 24. t=0 → frame 0, t=0.6 → frame round(14.4) = 14.

## Method (lab method card)
- f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Ball centre at frame 0: (545.0, 294.5). The ball is held on the board's top edge. This is the record's manual box,
  which I re-checked by eye on a 4x crop (edges at about 532.5–558.7 by 281.5–307.7, so the centre is about 545.6, 294.6).
- Ball centre at frame 14: (547.1, 354.2), from background-difference mask (`measure.py`, background = median of
  frames 36–48). The mask contour overlay is in frames/masks.png, and the record's value of 548.1, 354.2 agrees.
- Back-projection with the Euclidean depths from depth_info: 1.8180 m at t=0 and 1.7288 m at t=0.6 (`compute.py`).
  - p0 = (-0.224, -0.154, 1.798) m
  - p14 = (-0.209, -0.013, 1.716) m
  - Displacement = **16.4 cm**

## Checks
- Moving the frame-14 centre by ±2 px vertically gives 16.0–16.8 cm. If the depths are read as z instead of
  Euclidean distance, the result is 16.9 cm.
- Decomposition: the depth change is 8.9 cm, and the 60 px image motion at about 1.77 m is about 13.9 cm.
  sqrt(8.9² + 13.9²) ≈ 16.5 cm, which agrees.
- Ball diameter: 27 px at 1.818 m gives 6.4 cm, which is plausible.
- The acceleration prior (4.6 m/s²) is not needed, and a constant-acceleration check depends on the release frame
  (7–9), so I did not use it.

Confidence: good, within about ±5%.
