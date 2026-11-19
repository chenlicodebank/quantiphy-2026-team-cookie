# q_791 – speed of the front horse (m/s)

Prior: speed of the horse at the back = 0.874 m/s. 2D simulation, 24 fps (file fps = question_fps, no re-timing).

* Horses walk left→right side-on along the house wall, hooves on the same ground line (y≈1041-1050) → same depth,
  one px→m scale. "Front" (leading, right-hand) horse = horse_tan; "back" (trailing) horse = horse_brown.
* Answer = 0.874 × (tan px speed / brown px speed). Brown uses frames 0-48 (frame 49 is a loop reset).

Measurements (px/frame):
1. scene/ tracks, linear fits (measure.py): tan 5.93-6.02, brown 3.16-3.26 → ratio 1.84-1.85 (bbox_x1 1.90).
   Track endpoints: torso_x0 tan 5.94 / brown 3.10 = 1.91; ref_x 6.30 / 3.15 = 2.0 (noisy single-frame endpoints).
2. Independent route (chain.py): frame-to-frame sub-pixel template tracking of three barrel patches per horse:
   tan 6.04-6.17, brown 3.18-3.25 → ratio 1.86-1.91. Tan speed oscillates with gait (~33 frame cycle);
   mean over one full cycle (frames 7-39) 5.96 px/frame, consistent.
3. 8-frame windowed template matching (check_tm.py): tan 6.1-6.3, brown 3.1 → ratio ~1.97-2.0 (noisier, upper bound).

Adopted: tan ≈ 6.02, brown ≈ 3.18 px/frame → ratio ≈ 1.89 → 0.874 × 1.89 ≈ 1.65 m/s.
(Scale check: 0.874/(3.18×24) = 0.01145 m/px → tan horse ~2.6 m long, brown ~2.1 m; plausible.)
Confidence: ±4 % (spread of ratios 1.84-1.93 from gait-induced speed oscillation).
