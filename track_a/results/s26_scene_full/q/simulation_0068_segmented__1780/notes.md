# q1780 – length of the turning yellow (beige) car

2D top-down video; fps 24 = question_fps, so no re-timing.

Scale from the prior (white van acceleration = 4 m/s²): a quadratic fit to the van's vertical position y(t) (`fit.py`, scene tracks, checked).
- Centroid cy, frames 3–71: 160.8 px/s². Frames 10–71: 160.9; frames 3–39: 159.9; frames 30–71: 162.0. Rotated-rect centre: 159.3–161.5. Bbox edges: 156–167, noisier.
- Value used: 160.8 px/s², so the scale is 4 / 160.8 = 0.02488 m/px.

Length of the turning (beige/yellow) car:
- From the record: the median rotated-rectangle length over all frames is 223.1 px (10–90 % range 220–226).
- Second route (`len.py`): extents measured on the raw frames while the car is axis-aligned.
  - Frames 0–1 (car at rest): 223 px (mask), or 219–221 px with a half-max threshold.
  - Frames 68–71: 217–220 px.
- Value used: about 221.5 px, giving 221.5 × 0.02488 ≈ 5.51 m. The range across routes is 5.40–5.55 m.
- Sanity check: the van's length of 240 px comes out at 5.97 m, a plausible ratio to the car.

Answer: 5.52 m. Confidence is good, with an error of about ±3 %.
