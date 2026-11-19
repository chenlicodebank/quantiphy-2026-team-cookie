# Q2413: width of the slope (cm)

Width means the horizontal extent across the face of the white ramp board. The file fps and question_fps are both 24.
The camera is static and the ramp does not move.

## Method
I used the lab pinhole camera: f = 0.5959 × 1280 = 763 px. The depth_info gives the distance to the far (top) edge
of the slope as 1.201 m and to the near (bottom) edge as 0.9555 m.
`measure_ramp.py` builds a white mask (min channel > 200, low chroma), keeps its largest component, and reads the
board's left and right x on every row. I ran it on frames 10, 40, 46 and 48, and all four agree within 1 px.
- Top edge: 145 px wide at y = 362. Extrapolating to the edge line at y ≈ 357 gives about 143.5 px; the rounded
  corners cut the very first rows.
- Bottom edge: 183 px wide at y = 476, extrapolating to about 184.5 px at y ≈ 480.
- The width changes linearly with y, at about 0.33 px per row, as expected for a rectangle in perspective.

## Results
- Route 1, far edge: 1.201 × 145 / 763 = 22.8 cm (22.6 cm with 143.5 px).
- Route 2, near edge: 0.9555 × 183 / 763 = 22.9 cm (23.1 cm with 184.5 px).
- Correcting distance to the optical-axis depth Z changes these to 22.5 and 22.8 cm.

All routes fall between 22.5 and 23.1 cm. **Answer: 22.8 cm.** Confidence: high, about ±2%.
