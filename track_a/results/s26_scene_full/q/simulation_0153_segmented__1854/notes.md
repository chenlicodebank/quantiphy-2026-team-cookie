# q_1854 — speed of the blue car at t = 1 s (m/s)

Prior: the blue car's tire diameter is 0.369 m. No depth_info. fps = question_fps = 24, so t = 1 s is frame 24.
The scene is 2D: a side view with constant depth (the wheelbase changes only 1.6 % over frames 20–41). I use one m/px scale.

## Motion (from the scene/tracks/cart.csv template tracks, which are drift-free and checked)
x displacement from frame 23 to frame 24: front hub 47.72 px, rear hub 47.71 px, sill marker 48.05 px.
Neighbouring frames change smoothly (about 47.0 at frame 23 and 48.5 at frame 25), so I use 47.8 px/frame.
No vertical motion.

## Tire pixel diameter (my scripts: tire.py, tire_w.py, tire_rad.py)
- Front tire (the rear tire is cluttered by the body). I found the dark-pixel boundary along rays from the hub, then
  did an algebraic circle fit over the lower arc (20–160°). Over frames 30–38 the fit gives 103–110 px, mean ≈107.
- Checks:
  - Right edge to hub: ≈55 px.
  - Hub to bottom: ≈52.5 px.
  - Zoomed frame 34: right edge x≈1167, bottom y≈948, hub ≈(1113,895). This gives D ≈106–110.
- Perspective correction to frame 24: wheelbase 339.3 px at frame 24 against ≈336.2 over frames 30–38
  (×1.009), so D ≈108 px at frame 24.
- Scale: 0.369 / 108 = 3.42e-3 m/px.

## Result
v = 47.8 px/frame × 24 × 0.369 / 108 = **3.92 m/s**.
Second route: the circle fit done directly on frames 22–26 gives a mean of 106.6 px, which means 3.97 m/s.
Plausible range: 3.85–4.05.
Confidence: moderate-good. The main uncertainty is the tire's pixel diameter (±3 %). Its top is hidden by the
fender and its bottom looks slightly flattened.
