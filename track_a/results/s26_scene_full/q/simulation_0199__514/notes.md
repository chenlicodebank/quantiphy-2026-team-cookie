# Q514: height of the droplet (m)

- 2D render, 60 fps (file fps = question_fps, so no re-timing). The prior gives the droplet's acceleration as 9.7 m/s^2, and that sets the scale.
- `measure2.py`: the mask is the RGB max-abs difference against frame 13 (no drop in view), at thresholds 8, 12 and 18, cleaned with open and close, keeping the largest component, for frames 0–10.
  - I fitted a quadratic to the vertical position, using both the centroid and the bbox centre and three frame windows: a = 31.5–31.8 px/frame^2, median about 31.65.
  - That is 31.65 × 3600 = 113,940 px/s^2.
  - Scale = 9.7 / 113,940 = 8.51e-5 m/px.
- Droplet bbox height: 90–91 px at threshold 18, 90–93 at threshold 12, steady over frames 0–9. A zoomed crop of frame 5 (`frames/f5.png`) shows y of about 1100–1190, i.e. 90 px. I used 90.5 px.
- Height = 90.5 × 8.51e-5 = 0.00770 m.
- Second route: the scene record's centroid steps give a mean step increment of (301.0 − 17.1) / 9 = 31.54 px/frame^2 and a box height of 89–90 px. That gives 0.0076–0.0077 m, which agrees.
- Confidence: high, about ±3%.
