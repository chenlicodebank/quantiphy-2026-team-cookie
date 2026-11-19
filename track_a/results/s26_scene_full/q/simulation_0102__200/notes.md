# Q200 — height of the shark (m); prior: shark acceleration = 1 m/s^2

2D video (side view; the shark swims left in the lower underwater panel). fps = question_fps = 24, so no re-timing.

## Scale from the prior (fit.py)
Quadratic fits of the shark's x(frame), frames 1–60 (fully visible, constant acceleration):
- mask centroid: 0.1502 px/frame^2 = 86.5 px/s^2 (rms 0.54 px); sub-windows 1–30: 83.4, 30–60: 85.8
- nose edge: 87.8 px/s^2 (sub-windows 88.4 / 88.0)
- tail edge: 86.7 px/s^2
Adopted a = 87.0 ± 1.5 px/s^2, so the scale is 1/87.0 = 0.01149 m/px.

## Shark pixel height (height.py)
Vertical extent of the shark mask (difference from the per-row background, threshold 25/40/60), checked every 4th frame from 0 to 60:
rows 852–955 → 104 px inclusive at all thresholds and stable in every frame. Allowing for antialiased edges,
the extent is about 103 px. The record's 101 px came from an opened mask, which trims the fin tips. On the zoomed
frame (frames/f24.png) the dorsal fin tip is at ~852 and the pectoral fin tip at ~955.

## Answer
Height = 103 px × 0.01149 = 1.18 m (range 1.16–1.21 depending on 101–104 px and 86–88 px/s^2).
Second route: the separate nose, tail and centroid acceleration fits agree within ±1.5%. Confidence: good (~3%).
