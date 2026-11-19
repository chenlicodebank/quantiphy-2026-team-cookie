# Q1805: height of the shark (m). Prior: shark acceleration = 1 m/s^2

This is a 2D side-view clip at 24 fps (file fps and question fps are the same). The camera is static. The scale comes from the shark's pixel acceleration.

## Acceleration (fit.py)
I fitted quadratics x(t) to frames 2–58, while the shark is fully in frame and moving left:
- scene template_dx: 85.2 px/s^2, stable across the windows 2–30, 30–58 and 10–58 (84.8–85.9).
- bbox nose x0: 86.7; bbox centre: 86.2; mask centroid: 85.8.
- My own re-mask from the video: nose x0 87.5, weighted centroid 87.8. Tail x1 gives 83.3, which is noisier because the tail flaps.
- Adopted value: 86 px/s^2 (spread about ±1.5%), so the scale is 1/86 = 0.01163 m/px.

## Height (height.py)
The shark's vertical extent (dorsal fin tip to pectoral fin tip) depends a little on the darkness threshold used to find its edge:
- threshold 5: 109 px; this includes the anti-aliasing halo.
- threshold 20: 105 px.
- thresholds 40 and 60: 104 px.
- The scene record gives 105 px (median, after a mask opening).

Adopted value: 104.5 px. The fins stay steady over frames 0–58.

## Answer
104.5 / 86 = 1.215 m, rounded to **1.22 m**.

## Check
The shark's length of 280 px gives 3.26 m at the same scale. That is a plausible shark, so the scale is consistent. Using the extreme acceleration estimates (85.2 or 87.8) changes the height by only ±1.5%.

Confidence: high (about 3%).
