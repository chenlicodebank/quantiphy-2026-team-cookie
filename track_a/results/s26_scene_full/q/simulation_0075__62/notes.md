# q62 – side length of the square earthen platform

2D top-down scene, 24 fps (file fps = question_fps). Scale from prior: white car (the only white vehicle, the van) = 6 m.

- Van length: zoomed crop at f71 (frames/van.png) shows the body from y≈82 to y≈317, so 235–236 px. The record gives 236 px at thr25 for f0 and f71,
  and 233 at f36. My column-profile script (van_len.py) reads 231–246 px; the larger values include the rear shadow. I used 236 px,
  so the scale is 6/236 = 0.02542 m/px.
- Earthen platforms are the three brown squares (NW, SW, SE). measure.py takes connected components that differ from the sidewalk by more than 20:
  sqrt(area) = 83.2, 83.4 and 82.0 px; bbox 85×83, 85×83 and 84×83; half-max widths 83, 81, 81 and 79. The record gives 80–83. Best estimate is 82.5 px.
- Side = 82.5 × 0.02542 = 2.10 m.
- Second route: the record's static bbox (≈82 px) with the van at 233–236 px gives 2.09–2.11 m. The squares and the van are both near
  the camera's centre band, and the record found no scale change with image position.
Confidence: moderate-high, about ±4% from the edge definitions.
