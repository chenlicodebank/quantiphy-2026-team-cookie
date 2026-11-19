# Q255 — side length of the table (m)

Prior: chess piece speed = 0.04 m/s. 2D top-down video with no visible perspective (the board squares have an even 33.6 px pitch), so one metres-per-pixel scale comes from the piece's pixel speed.

- Piece speed (scene track circ_cy, a circle-fit centre; checked in measure.py): a linear fit over frames 0–36 gives 1.3982 px/frame
  (residual 0.18 px). The mean of the per-frame steps over 1–36 is 1.3986 px/frame, and net/36 is 1.3969 px/frame. Motion is uniform.
- fps: 24.012 (file) and 24.0 (question) differ by only 0.05 %, which is negligible. I used 24.012, so the speed is 33.58 px/s.
- Scale = 0.04 / 33.58 = 1.1911e-3 m/px.
- Table top (measure.py, gradient edges along 11 rows and 11 columns away from the rounded corners): x 111.5–776.5 and
  y 211.5–876.5, so 665 × 665 px (square). This matches the scene record. Columns 500–600 hit the tray, not the table edge, and are ignored.
- Side = 665 × 1.1911e-3 = **0.792 m**.

Check: the board is 336 px, which gives 0.40 m, or 4 cm squares. A 0.79 m coffee table is plausible.
The piece origin may sit a little above the table plane, which would add a small perspective bias. That bias can't be measured (the focal length is unknown) and is ignored, as in the 2D convention.
Confidence: high (±2 %).
