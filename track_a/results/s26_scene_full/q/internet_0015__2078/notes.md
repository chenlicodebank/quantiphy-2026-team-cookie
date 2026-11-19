# Q2078: average speed of the motorcycle (m/s); prior: lane width = 3.66 m

- The motorcycle is the "cyclist" track in scene/ (a red/white two-wheeler in the upper lane, moving right to left, frames 0–136).
- **Scale** (measure.py): I took the median vertical brightness profile of the road over 4 frames × 4 x-windows and found the
  sub-pixel line peaks. The upper edge line is at y = 520.38, the double centre line at 565.33 / 573.30 and the lower edge line at 619.19.
  The upper (motorcycle's) lane, centre-to-centre of its lines, is 44.95 px; the lower lane is 45.89 px. Using 44.95 px for 3.66 m gives 0.0814 m/px.
  The lines are 2–3 px wide, so measuring between inner or outer line edges would shift this by about ±5%.
- **Pixel speed**: I checked the track by eye at f0 (centre x ≈ 1682 vs 1681 in the track) and f60 (≈ 955 vs 953).
  Linear fits: f0–136 gives 12.16 px/frame, f0–93 (sun) 12.04 and f94–136 (shade) 12.55. The mean of the per-frame differences is 12.26 px/frame
  (the same as the net displacement / frame count). Adopted value: 12.2 px/frame. dy is about 0.
- **Time base**: I used the file fps of 29.78. question_fps 30 would give a speed 0.7% higher, which makes no physical difference.
- Speed = 12.2 × 29.78 × 0.0814 = 29.6 m/s (≈106 km/h, the same as the cars it follows).
- **Second route**: sun-only displacement from f0 to f60 measured by eye: 727 px / 60 frames = 12.1 px/frame, which gives 29.4 m/s. This is consistent.
- **Confidence**: moderate–high. The main uncertainty is how the annotators defined lane width in pixels (about ±5%).
