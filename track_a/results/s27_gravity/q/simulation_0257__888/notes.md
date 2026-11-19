# Q888 – speed of the plant at t = 0.2 s (m/s)

- The video is a 2D Blender scene: the pot and plant fall straight down from frame 0 and land at frame 15.
- Time base: question_fps = 30, but the file says 24 fps. As instructed, I used 30 fps throughout: t = 0.2 s → frame 6,
  and the speed is the backward difference between frames 5 and 6, times 30.
- Scale comes from the prior (g = 9.8 m/s² before 0.5 s). I fitted a quadratic to the vertical position in frames 0–14
  (fit.py, using the scene/ tracks). I checked three position measures: the mask centroid, the bbox centre and the
  bottom edge.
  - Mask centroid: a = 6.93–6.95 px/frame², release at frame 0.00 ± 0.01, fit residual 0.28 px.
  - Bbox centre: a ≈ 6.97–7.00 px/frame².
  - Bottom edge: a ≈ 7.00–7.09 px/frame² (noisier, residual 0.6–0.9 px).
- Scale: m/px = 9.8 / (a × 30²). Speed at frame 6 = d6 × 30 × m/px = 9.8 × d6 / (30 × a).
  - With the fitted d6 = a × 5.5 (release at frame 0), this gives 9.8 × 5.5 / 30 = 1.797 m/s.
  - The fits give 1.73–1.80 m/s. The cleanest track (centroid) gives 1.80.
  - Raw differences: centroid d6 = 37.4 px → 1.76 m/s; bottom edge 36 px → 1.71 m/s.
- Second route: the release time from the fit is ≈ 0, so the backward difference must be g × 5.5 / 30 = 1.797 m/s.
  This does not depend on the pixel scale, and it agrees.
- If the reference had used 24 fps instead, the answer would be about 2.25 m/s.
- Answer: 1.80 m/s. Confidence: good, given the 30 fps convention.
