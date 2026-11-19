# Q2965 — ball velocity at t = 2.00 s (cm/s)

Prior: basketball size = 24 cm. 2D internet clip (segmented, white background), static camera assumed
(no background to check; player's feet are steady). File fps 30.0003, question_fps 30 -> t = 2.00 s is frame 60,
in free flight (release frame 46, apex ~66, rim contact 83).

## Measurement (measure.py, fit.py, fit_sam.py)
- My ball centre per frame 46-82: connected component of dark pixels (255 - min channel > 40), plus a soft-weighted
  centroid. SAM 3 track ("basketball", tracks/basketball_0.csv) agrees with it within ~0.5 px on every flight frame
  (except 80, a known elongated-mask artifact, excluded).
- Raw centres around frame 60 are noisy (y: 59 310.2, 60 305.6, 61 304.4, 62 306.7, 63 298.1 — non-monotonic,
  segmentation/compression jitter of ~2 px), so the raw one-frame forward difference (248 px/s) is unreliable.
  Used a fit: x linear, y quadratic over the clean flight, velocity = forward difference of fitted positions 60->61:
  frames 46-79: 313 px/s; 50-70: 306 px/s; 54-66: 300 px/s (my centroids and SAM give identical values).
  Chosen 306 px/s (vx ~9.5 px/frame, vy ~ -4.1 px/frame).
- Ball diameter: my mask on clean frames median bbox 17 x 16, equal-area 16.7 px; SAM mask at frame 52: box
  16.5 x 16.4, equal-area 16.85 px (frame 60 mask is squashed, 14 x 16, not used for size). Agree within 3%.
  Used 16.8 px -> scale 24/16.8 = 1.429 cm/px.

## Answer
306 px/s x 1.429 cm/px = 437 cm/s -> answer 435 cm/s (range over fit windows / diameter 16.7-17: 420-450).

## Check
Vertical acceleration of the fit = 0.69 px/frame^2 = 621 px/s^2 -> 887 cm/s^2 with this scale, close to g (981),
so the ball scale is physically plausible (g-scale would give ~10% higher speed, ~480 cm/s; the reference uses the
ball scale, so kept 435). Confidence: moderate (±5-8%).
