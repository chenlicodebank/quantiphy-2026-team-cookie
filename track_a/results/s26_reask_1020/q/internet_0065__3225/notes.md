# q3225 – ball displacement 0.20 s → 0.30 s

- question_fps = file fps = 30, so the interval is frames 6 → 9.
- Prior (g = 9.8 m/s²) gives no scale. The camera looks straight down and the basketball rolls horizontally across the
  floor, so there is no free fall to measure.
- Scale therefore comes from the standard object: a regulation size-7 basketball, diameter 0.24 m.
  - Its pixel diameter is the vertical (unblurred) bbox extent, median over frames 5–12 = 256 px. I checked this on the
    frame-8 crop (top ≈270, bottom ≈525).
  - Scale = 9.375e-4 m/px.
- Displacement of the centroid, frames 6 → 9:
  - Camera-stabilised (the scene/ track): 295.3 px. This is the main route.
  - Raw image: 294.1 px.
  - Second route, the mean of the leading-edge and trailing-edge bbox shifts: 294.5 px, which gives 0.276 m.
- Answer: 295.3 × 0.24 / 256 = **0.277 m**. The implied speed of about 2.8 m/s is plausible for a rolled ball.
- Confidence: moderate. The main uncertainty is the scale: the pixel diameter could be 256–275 px (the larger value
  includes motion blur), which would change the answer by up to about 7 %.
