# Q2076 — length of the black (dark) car, prior lane width = 3.66 m

Top-down static drone view, 2D planar scene. One scale from the prior (internet convention).

## Lane width in pixels (measure.py)
Vertical brightness profile (median over x 1000–1900, frame 0), line centroids:
upper edge line 521.6, centre double line 566.5 / 574.5, lower edge line 621.1.
- Upper lane (the one the car drives in), line centre to line centre: 44.9 px  <- used
- Lower lane: 46.6 px (mean of both lanes 45.75 px)
Scale = 3.66 / 44.9 = 0.0815 m/px.

## Car length in pixels
- Visual, ruled 8x crops (drawcar.py, frames/carz.png): f0 front bumper/headlights ≈ 861, rear ≈ 918 → 57 px;
  f10 ≈ 744.5 → 802.4 → 58 px.
- Code (carlen.py), half-max of |frame − median background| over f0–20: band y536–553 median 59.4 px
  (includes blur halo and some of the cast shadow at the front); lower band only 53.6 (misses the rounded ends);
  full band 64.2 (includes the shadow). scene/ record gives 60 px.
- Adopted 58 px bumper to bumper.

## Answer
58 × 0.0815 = 4.73 m. Range check: 57–60 px and lane 44.9–45.75 px → 4.56–4.89 m. Plausible sedan length.
Confidence: moderate (±4%).
