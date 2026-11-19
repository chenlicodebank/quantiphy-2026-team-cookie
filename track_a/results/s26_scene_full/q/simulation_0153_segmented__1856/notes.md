# q_1856 — speed of the blue car at t = 1.5 s

The question's rate and the file's rate are both 24 fps, so t = 1.5 s is frame 36. Speed is the one-frame backward difference, frame 35 → 36.
The prior is a tyre diameter of 0.369 m. The scene is planar 2D with a static camera, so I used one m/px scale taken from the near-side front tyre.

## Pixel speed (from scene/tracks/cart.csv; template tracks, ±0.5 px)
Shift from frame 35 to frame 36:
- front hub: 47.54 px
- rear hub: 47.96 px
- sill marker: 48.08 px

Mean: 47.86 px/frame. The car is rigid and does not rotate, so every point on it gives the same shift.

## Tyre diameter in pixels (my measurement)
- `circfit.py`: casts rays from the front hub, finds the outer tyre boundary and fits a circle. It uses only the free bottom and right edges, because the fender hides the top.
  - Frames 35–41 (rms 0.5–0.9 px): D = 109.2, 109.6, 108.6, 108.1, 108.2, 109.3, 109.6 px. At frame 36 it is 109.6 px.
  - From the fitted centre, the bottom edge is about 54.8 px away (D ≈ 109.6).
- `tire.py`: the horizontal width of the dark rubber through the hub row is 112–113 px. That is slightly wider because the tread shows in perspective and there may be a little motion blur.
- I used D ≈ 109.3 px, which gives a scale of 0.369 / 109.3 = 0.003376 m/px.

## Answer
47.86 px/frame × 0.003376 m/px × 24 fps = **3.88 m/s**. I answered **3.87 m/s**.

## Check
- The hub-only and marker-only shifts give 3.85–3.90 m/s.
- Using the wider horizontal width (112.5 px) gives 3.77 m/s, which bounds the answer at about −3 %.

Confidence: good, about ±3 %. The main uncertainty is the tyre's pixel diameter.
