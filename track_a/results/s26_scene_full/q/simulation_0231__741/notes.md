# Q741 – acceleration of the paper airplane at t = 1 s (frame 24)

Time base: fps = question_fps = 24, so t = 1 s is frame 24. The scene is 2D: the wall is parallel to the image
and both objects move parallel to it, so one metres-per-pixel scale applies.

## Scale from the prior (cat speed 0.714 m/s)
The cat walks at a steady pace (record tracks in `cat.py`). Its mean pixel speed is 8.85–9.04 px/frame across
reference points (torso, dark centroid, bbox, mask, nose; both line fits and end-to-end) → 8.93 px/frame,
or 214.3 px/s. Scale = 0.714 / 214.3 = 0.003332 m/px.

## Airplane speed (`measure.py`)
I made my own mask (difference from the median background) on the board frames 15–32. Per-frame speeds near
frame 24 are about 76.5 px/frame (f16–20), then 73 (f22), 69.5–70.4 (f24), 65 (f27) and 61 (f30). The
airplane slows steadily after its climb. The one-frame difference of speed is noisy (±1 px), so I took the
slope of a local fit of speed against frame, evaluated at frame 24:
- mask centroid: −1.29 to −1.39 px/frame² (windows 18–30, 19–29, 20–28, 21–27)
- bbox centre: −1.39 to −1.50 px/frame²
- wider quadratic fit over 16–32: −1.20 / −1.27
Adopted value: −1.40 px/frame² × 576 = −806 px/s², × 0.003332 m/px = −2.69 m/s².

The airplane is slowing down; the answer is the magnitude, 2.69 m/s².

## Checks
- My track agrees with the record's `cx_best` (bbox centre) within 1–2 px. Speeds from the record give a
  slope of about −1.6 px/frame² over frames 20–28 (≈ 3.1 m/s²).
- Range across methods: 2.3–3.1 m/s².

Confidence: moderate, about ±12%. The main uncertainty is the local slope, because frame-level centre noise is
about 1 px.
