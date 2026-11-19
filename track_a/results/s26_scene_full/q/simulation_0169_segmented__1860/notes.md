# Q1860: astronaut speed at t = 1 s

- This is a 2D segmentation video at 24 fps (file and question rates agree). t = 1 s is frame 24.
- Scale comes from the prior (height 2.2 m). The figure is nearly upright (axis 94-98°). I re-segmented frames 10-40 with `measure.py` (min RGB < 225, largest blob). The bbox height is 90-91 px (mean 90.4), and the scene record gives a mean axis length of 91.4 px. Faint edge pixels may be lost, so I used about 91 px, which gives 0.02418 m/px.
- Speed: I fitted a local quadratic to the mask centroid x(t) and y(t) around f24 and took the derivative at f23.5, which matches the one-frame backward difference p(24) - p(23). Windows of ±4, ±6 and ±8 frames give 4.41, 4.39 and 4.39 px/frame. That is 4.39 x 24 x 2.2/91 = 2.55 m/s (2.57 m/s if H = 90.4 px).
- The raw one-frame difference f23→f24 is 4.75 px. It is noisy (centroid jitter about ±0.5 px), and the neighbouring steps are 4.0-4.5 px, so I used the smoothed value.
- Second route: the bbox-centre track gives 2.56-2.57 m/s, which agrees.
- Answer: 2.55 m/s. Confidence is good (about ±3%). The main uncertainty is the pixel height that corresponds to 2.2 m.
