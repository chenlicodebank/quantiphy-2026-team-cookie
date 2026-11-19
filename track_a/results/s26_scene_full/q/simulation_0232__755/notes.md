# Q755 – length of black cat incl. tail (m)

2D scene (cat walks left→right on desk top, parallel to image plane, static camera). fps = question_fps = 24.

Scale from prior (cat speed 0.714 m/s):
- Pixel speed (all 50 frames): torso centroid net 9.11 px/frame, linear fit 8.96; mask front edge fit 8.89,
  rear edge net 9.04 → adopted 9.0 px/frame = 216 px/s → 0.714/216 = 0.00331 m/px.

Length (horizontal bbox extent, tail tip → nose), measure.py:
- Scene record's mask (bbox median 199.5) and my threshold-25 mask (188) lose the light face (diff only ~20 grey levels).
- Threshold 12 on |frame − median background|, rows above y=728 (excludes contact shadows/desk), connected components:
  median 201 px (197–210 over 50 frames). Frame 24 read by eye on a grid: tail tip x≈371, nose x≈574 → 203 px.
- Length = 201 × 0.00331 = 0.664 m (with 9.11 px/frame: 0.657 m).

Answer: 0.66 m. Confidence: moderate-high (~±4%, dominated by gait-induced speed variation and edge blur).
