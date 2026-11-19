# Q505: height of the droplet (m)

- 2D sim, 60 fps (file fps = question fps). Prior: drop acceleration = 9.7 m/s^2 -> sets the m/px scale.
- Pixel acceleration (measure.py): quadratic fit of the mask centroid vs render index (the video frame 7 is a duplicate of
  frame 6 and render step 8 is missing, as scene/notes.md says; with that mapping the fit residual is < 0.4 px):
  a_y = 114090 px/s^2, a_x = -1684 px/s^2. Scalar-speed acceleration from the fit is 114103 px/s^2.
  Check: raw second differences over frames 0–6 give 111.7k–116.3k, mean ≈ 114.4k.
- Scale = 9.7 / 114100 = 8.50e-5 m/px.
- Drop height: the mask bbox height is 91–92 px in every clear frame (track, plus my own threshold sweep at 10/18/30 on
  frames 3, 4 and 6). A zoomed grid view of frame 4 gives about 955–1046, so 91 px. I used 91.5 px.
- Height = 91.5 × 8.50e-5 = 0.00778 m (≈7.8 mm, a plausible drop size).
- Confidence: good (about ±3%). The pixel height is uncertain by ±1 px and the acceleration fit by about 1%.
