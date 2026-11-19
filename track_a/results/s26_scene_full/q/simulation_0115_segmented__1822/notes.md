# Q1822 – length of the wooden dock (prior: boat acceleration = 3 m/s^2)

2D top-down render, 24 fps (file fps = question_fps, no re-timing). Scale from the boat's pixel acceleration.

- measure.py (own segmentation: non-white threshold, opening, connected components; dock = component above y 600):
  - boat centroid x(t) quadratic fit over all 37 frames: |a| = 138.5 px/s^2; slope of per-frame speed vs time 138.5 px/s^2
    (mean of noisy per-frame speed differences 133.9). fit.py: sub-windows 131–141, bbox edges 126–148 → 138.5 is robust.
  - dock length along its principal axis 574 px (bbox width 574 px, axis tilted ~1°), static. Visual check on frame 18:
    x ≈ 915–1487.
- scale = 3 / 138.5 = 0.02166 m/px → dock length = 574 × 0.02166 = **12.43 m**.
- Sanity: boat length 226 px → 4.9 m, width 89 px → 1.9 m – a plausible dinghy; dock width 97 px → 2.1 m.
- Second route: bbox-edge fits (136–139 px/s^2 over full clip) give 12.4–12.6 m.
Confidence: good (~3 %), limited by the acceleration fit.
