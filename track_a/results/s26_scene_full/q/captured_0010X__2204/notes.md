# q_2204 — ball diameter (cm), captured_0010X (pendulum)

Prior (g = 9.8) gives no size; scale from depth_info + lab camera f = 0.5959*1280 = 762.8 px.
question_fps = file fps = 24, so times map to frames 7, 14, 22, 29, 36, 43.

## Key observation
Frames 0-11 show the real red ball. In frames 12-48 the ball is a flat pale-pink segmentation fill. That fill
is inflated relative to the ball:
- frame 7 shows a faint segmentation halo about 7 px beyond the red ball edge;
- the size jumps from about 30 px in red frame 11 to about 36 px in pale frame 12;
- the pale sizes at the given depths come out 5-15 % larger than the red-frame scale predicts.
So the size has to come from the red frames. scene/ball.csv equiv_diam (34 px at frame 7) includes blur and halo,
so I did not use it.

## Measurements (scripts: measure.py, halfmax.py, redwidth.py, profile.py)
- Frame 7 (t = 0.3 s, d = 1.706 m) moves mostly vertically, so I measured the horizontal chord:
  - sub-pixel half-level of darkness, which includes the shaded rim: 29.1 px -> D = 6.51 cm;
  - half-level of r-b: 27.9 px -> 6.24 cm.
- Red frames 1-7 all show a chord of about 29.1-30.1 px. Their phase-matched pale frames 29-36 have given depths of
  1.71-1.78 m (mean about 1.75 m), so D ≈ 1.75*29.2/763 = 6.7 cm.
- Frame 0 with the depth of the same-phase frame 29 (1.784 m): 30.2 px -> 7.06 cm. This is probably inflated by
  horizontal blur.
- The pale frames give D = d*px/f of 6.4-8.2 cm. They are upper bounds because the fill is inflated
  (frame 43: 6.36-6.76; frame 14: 7.2).

## Answer
D ≈ 6.6 cm, the centre of the red-frame routes (6.24-7.06). Confidence: moderate, about ±7 %. The ball is only
about 29 px across, and ±1 px is ±3.5 %.
