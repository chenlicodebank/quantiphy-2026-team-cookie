# Q100 — speed of the yellow car at 1.0 s (m/s)

File fps = question_fps = 24, so t = 1.0 s -> frame 24; speed = |x(24) - x(23)| x 24.
2D top-down render, static camera; the yellow car drives left along a horizontal lane.

## Measurement (measure.py)
Yellow-chroma mask (R - B > 30, upper lane only, 5x5 closing, largest component) on frames 14–34.
- Length (x extent) = 270 px in every frame 14–31 (272 near frame 32+, from mild edge perspective).
- bbox centre x: f23 = 642.5, f24 = 632.5 -> 10.0 px/frame; front and rear edges also each move 10 px.
  Mean over frames 16–32 = 10.06 px/frame (constant velocity from frame 2, matching the scene record).

## Scale
Prior: yellow car length 5.67 m = 270 px -> 0.021 m/px.
Speed = 10.0 px/frame x 24 = 240 px/s x 0.021 = **5.04 m/s**.

## SAM 3 check
segment "yellow car" at f23 and f24: boxes x 507.4–777.1 and 497.1–767.6 (box widths 269.7 / 270.5 px, within
0.2 pct of my 270); box centres 642.25 -> 632.35 = 9.9 px/frame (1 pct from my 10.0, sub-pixel edge noise).
The overlay (frames/seg_00_f24.jpg) shows the mask covering the whole car without the shadow. No disagreement > 3 pct.

## Second route
Multi-frame average 16–32 gives 10.06 px/frame -> 5.07 m/s; agrees within 0.6 pct.
Confidence: high.
