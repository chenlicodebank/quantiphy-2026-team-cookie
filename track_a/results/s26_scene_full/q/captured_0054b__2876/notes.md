# Q2876 – distance between the orange ball (basketball) and the soccer ball at t = 1.0 s (frame 24)

question_fps = file fps = 24, so t = 1.0 s is frame 24. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
depth_info values are Euclidean camera-to-centre distances, so they scale the unit ray, not Z.

## Measurements
- Orange ball = basketball. At frame 24 the track centre is (537.8, 385.9), a clean round mask (diameter 62.9 px).
  depth_info gives 1.81 m -> P_b = (-0.240, 0.061, 1.793) m.
- Soccer ball, frame 24: this is its release frame. It is vertically blurred, and its right side is hidden by the crouching
  person's hand. From the free left and top outline (crops `frames/soc.png`, `frames/soccer_fit.png`), its
  left edge is about x 895 and it spans y about 575-640, so the centre is about (924, 607). The scene track gives
  (915.8, 599.9), biased left/up by the occlusion.
- The soccer depth is only given at t = 2.0 s (3.254 m). I carried it to frame 24 with the apparent diameter,
  measured by circle fits to the outline in `soccer_fit.py`:
  - frames 46-48 (grey disc): 53.5 (poor fit), 46.9, 46.7, so about 46.5 px at frame 48. Frames 44-45 give 47.5 and 45.1.
    The record's 37-39 px under-segments the low-contrast disc.
  - frames 25-28: 61.6, 67 (blurred), 61.7, 60.7, so about 62 px at frame 24.
  - Soccer distance at frame 24 = 3.254 x 46.5 / 62 = 2.44 m -> P_s = (0.815, 0.709, 2.189) m.
- Distance |P_s - P_b| = **1.30 m**.

## Sensitivity / checks
- Using the track centre instead: 1.28 m. Diameter at frame 24 of 60 / 64 px gives 1.36 / 1.25 m. Diameter at frame 48 of 44 px gives 1.21 m.
- Physical sanity check: the implied soccer-ball diameter is 3.254 x 46.5 / 763 = 0.198 m, which is plausible (size 4-5).
  The basketball at t = 0.5 s gives 2.24 x 75.4 / 763 = 0.22 m, also plausible. The prior (2.21 m/s at 0.5 s) is roughly
  reproduced: about 1.9-2.3 m/s from pixel steps and the size-based depth change around frames 10-15. That window includes
  a skipped capture at frame 11->12.
- The basketball's given 1.0 s depth (1.81 m) is low compared with its apparent size (62 px would give 0.147 m).
  A second route uses that depth plus a real-size ratio to place the soccer ball (0.22 / 0.243). It gives a soccer distance of
  1.66 m and a separation of 0.95 m. I did not adopt it, because it relies on assumed real ball sizes rather than the soccer
  ball's own given depth.
- Confidence: moderate. The main uncertainty is the soccer depth at 1.0 s, which is not given directly (about ±7 %).
