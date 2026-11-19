# Q1581 — typewriter speed at t = 0.333 s

question_fps = file fps = 24, so t = 0.333 s is frame 8. Speed = |p(8) - p(7)| x 24.

## Data
The fall track comes from scene/tracks/typewriter.csv (ref_y = bbox centre; frames 0-10 are in the air, impact between frames 10 and 11).
The camera is static and x stays at about 1240 px, so the typewriter drops nearly straight down.

## Method
- Quadratic fits of pixel y over frames (fit.py): the pixel acceleration is about 10-11 px/frame², and the fall starts at frame 0 (t0 between -0.35 and 0 frames).
- 3D drop model (fit3d_c.py): a pinhole camera pitched down by phi with focal length f. The origin starts at range 4.32 m (given, t=0) on the ray through
  the frame-0 pixel, then falls vertically with g = 9.8 (prior) from t0. The model is fitted to ref_y over frames 1-10 and is constrained so that the rest point
  (ref y = 609.5 px, frame 12 = t 0.5 s) is at the given range of 4.501 m.
  Result: f ≈ 2810 px (HFOV ≈ 41°), pitch ≈ 16° down, t0 ≈ 0 (-0.09 to +0.09 frames), rms 2.6-2.8 px.
  The modelled speed at frame 8 is 3.02-3.10 m/s across the different frame windows and with t0 free or fixed.
- A free fit without the range constraint is ill-conditioned (it gives an upward-looking camera), so it was rejected.

## Check
- Analytic check for a drop from rest at frame 0: v = g x (8² - 7²)/(2 x 24) = 9.8 x 7.5/24 = 3.0625 m/s. This agrees with the 3D fit.
- Scale check: the typewriter is about 290 px wide at 4.32 m with f = 2810, so it is about 0.45 m wide. That is a realistic size for a manual typewriter.

Answer: 3.06 m/s. Confidence: high (about ±3%). The main uncertainty is the exact release time (±0.1 frame gives ±1.3%).
