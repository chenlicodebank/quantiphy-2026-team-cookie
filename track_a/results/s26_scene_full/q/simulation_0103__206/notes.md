# q_206 — shark height (m), prior: shark acceleration = 1 m/s^2

2D video, static camera, 24 fps (file fps = question_fps). One metres-per-pixel scale comes from the shark's own pixel acceleration.

## Acceleration (fit.py)
Quadratic fits of x(t) for frames 1–53 or 2–53 (from frame 10 for the check):
- Centroid cx: a = 87.3 / 87.5 px/s² (from frame 10: 88.8), residual rms 0.47 px.
- Tail edge x1: a = 86.1 / 86.0 px/s² (87.1), rms 0.48 px.
- Bbox centre: 86.3–88.6 px/s². Nose edge x0: 86.5–90.0 px/s² (this edge is noisier).
- Adopted value: a ≈ 87.0 px/s², so the scale is 1/87.0 m/px.

## Height
The bbox height runs from the dorsal-fin tip to the pectoral-fin tip: median 105 px over all frames (range 104–106). I checked this visually on a zoomed crop of frame 24 (fin tip at y ≈ 851, pectoral tip at y ≈ 956).

Height = 105 / 87.0 = 1.207 m.

## Check by a second route
The tail-edge track gives 105/86.1 = 1.22 m. The centroid track gives 105/87.4 = 1.20 m. The two routes agree within 1.5%.

The length is 260 px, which gives 2.99 m. A 3 m shark with 1.2 m fin-to-fin height is plausible.

Confidence: good (±3%).
