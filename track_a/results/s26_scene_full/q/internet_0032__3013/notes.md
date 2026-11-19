# q3013 – boat distance traveled 0–2 s

- Prior: boat length 3.5 m. The camera is static (scene record shows a shift under 0.2 px). The boat moves right to left, side-on, with no reversal, so path length ≈ net displacement.
- Time base: file fps is 29.85 and question_fps is 30. Both give frame 60 for t = 2 s.
- I checked the hull tips on zoomed frames (view.py → frames/f0.png, f2.png) and they match scene/tracks/boat.csv. Frame 0: bow 761, stern 972. Frame 60: bow 673, stern 896.
- Displacement of the hull centre from frame 0 to frame 60 is 82.0 px. The mask centroid gives 83.0 px. A quadratic-smoothed path gives 84 px. The raw per-frame path equals the net displacement because the motion is monotonic.
- Scale (one factor, annotator convention): the hull length grows with perspective. A linear fit gives 214.6 px at frame 0, 219.3 px at frame 30 and 224 px at frame 60.
  - Frame 0 length: 82 × 3.5 / 214.6 = 1.34 m
  - Mid-interval length: 1.31 m
  - Per-frame scale integration (second route): 1.34 m
  - Clip-median length (232 px, outside the interval): 1.24 m. I did not use it.
- Answer: 1.33 m. Confidence: moderate-high (about ±4%). The main uncertainty is which frame's length the annotators used.
