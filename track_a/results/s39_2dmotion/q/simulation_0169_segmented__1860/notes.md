# Q1860: speed of the astronaut at t = 1 s (2D, prior: astronaut height = 2.2 m)

File fps = question_fps = 24, so t = 1 s is frame 24. Speed is the backward difference from f23 to f24.

## Method (measure.py -> my_track.csv)
- Mask: pixels with min RGB below 225 on the white background, keeping the largest blob. Reference point is the mask centroid, at about hip level, as a proxy for the pelvis origin. The pose is rigid.
- Scale: the astronaut is nearly upright at f0 (axis 94 deg). Bbox height over f0-f4 is 90-91 px and the PCA main-axis length at f0 is 90.9 px, so I used 90.9 px = 2.2 m, which gives 0.02420 m/px.
- Speed: one-frame centroid steps near f24 are noisy (±0.5 px jitter): 4.09 (f22-23), 4.74 (f23-24), 4.47 (f24-25). A local quadratic fit of x(t) and y(t), with the derivative taken at frame 23.5 (the midpoint of the backward difference), gives 4.41 / 4.39 / 4.39 px/frame for windows of ±4, ±6 and ±8 frames.
- Speed = 4.40 px/frame x 24 x 0.02420 = **2.56 m/s**. The raw single difference would give 2.75 m/s, but that value is inflated by mask jitter.

## SAM 3 check
- f0 "astronaut": length 91.0 px, vert 90 px, centroid (1294.4, 520.2). Mine: 90.9 px, bbox h 90, centroid (1295.2, 519.1). They agree within 1%.
- f24: SAM centroid (1299.0, 455.7) vs mine (1298.8, 456.8), about 1 px apart. SAM length is 88.8 px vs mine about 91 (2.4%, under 3%). The scale comes from f0, where the two agree.
- f23: the text prompt found nothing. With a box prompt the mask outline is loose and picks up stray specks (extent 103 px, clearly too large in the overlay), so SAM was not used for the f23 extents. Its centroid (1298.3, 462.1) is still within 0.6 px of mine (1298.6, 461.5). The SAM centroid difference f23-f24 is about 6.4 px, which the bad f23 mask makes unreliable. My threshold mask is consistent from frame to frame and matches the figure on zoomed frames.

## Second route
Bbox-centre steps around f24 are 4.0, 4.1, 5.0, 4.5 and 4.0 px (mean about 4.3 px/frame, which gives 2.5 m/s). This agrees with the fitted 4.40.

Confidence: moderate to high. The main uncertainties are the height pixel extent (±1 px, about 1%) and the smoothing choice (fit 4.40 vs raw 4.74 px/frame).
