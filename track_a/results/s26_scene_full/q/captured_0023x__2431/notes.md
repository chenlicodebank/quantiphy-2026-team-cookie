# q_2431 — width of the slope (cm)

The slope is the white board that leans back on the table. Its width is the horizontal extent across its face (left edge to right edge).
The file rate and question_fps are both 24.

## Method (lab method card)
- f = 0.5959 × 1280 = 763 px, principal point (640, 360).
- `measure.py` makes a white mask (S < 40, V > 180) on frames 0 and 48 and takes the longest white run in each row.
  - **Top (far) edge, row 358 (frame 48):** x 517–659, so 143 px. The centre is at (588, 358).
  - **Bottom (near) edge, rows 472–478:** x 494–676, so 183 px. The centre is at (585, 477).
  - Frames 0 and 48 agree to within 1 px. On frame 0 the book covers the top rows.
- depth_info gives Euclidean distances, which I converted to Z along each edge-centre ray:
  - far: Z = 1.201 / 1.0023 = 1.198 m;
  - near: Z = 0.9555 / 1.0143 = 0.942 m.
- **Route 1 (far edge):** 143 × 1.198 / 763 = 0.2246 m.
- **Route 2 (near edge):** 183 × 0.942 / 763 = 0.2260 m.
- The two independent edge/depth pairs agree to within 0.6%.

## Answer
The width is about 22.5 cm. Confidence is good, within about ±3%. The main uncertainty is the edge pixels at the matting boundary (±1–2 px) and whether
the depth points lie exactly on the edges.
