# q1798 boat length (m)
2D clip, 24 fps (file = question fps). Scale from prior: shark acceleration 1 m/s^2.
- measure.py: segmented non-white mask (thr 12), shark = components below y=740, boat above.
- Shark x quadratic fits (frames 1-72): snout -86.0, tail -85.8, centroid -86.0, bbox centre -85.9 px/s^2;
  half-window fits 82-86 px/s^2. Use 86.0 px/s^2 -> 0.01163 m/px.
- Boat full horizontal extent (bow tip to stern incl. antenna), frames 26-72 fully in view: 856-862, median 859 px.
- Length = 859/86.0 = 9.99 m. (Hull only 831 px would give 9.66 m; AABB includes all parts so use 859.)
Second route: half-window acceleration fits (82-86) give 10.0-10.5 m; full-fit consistent across 4 reference points.
Confidence: high (~2-3%).
