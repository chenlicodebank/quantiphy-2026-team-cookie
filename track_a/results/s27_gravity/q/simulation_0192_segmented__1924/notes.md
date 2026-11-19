# q_1924 — speed of the box at t = 0.4 s

The file and the question both run at 120 fps, so t = 0.4 s is frame 48.
This is a 2D clip: the box falls straight down at constant depth (its width stays constant).

## Method (fit.py)
- I used the box's `front_top_y` track from scene/tracks/box.csv. It is a sub-pixel edge that I checked against the record's notes. Only vertical motion matters, and a constant offset from the origin cancels.
- The per-frame steps are irregular (stalls followed by double steps), so one-frame differences of the raw track are noise. I fitted a parabola to frames 5–60 instead. Contact with the roof happens at about frame 61.
  - Pixel acceleration: 2050 px/s². Vertex (release) at t0 = 0.0056 s, so the box effectively falls from rest at t ≈ 0. Fit rms is 2.5 px.
  - Scale from the prior (g = 9.8 m/s²): 9.8 / 2050 = 0.00478 m/px.
  - Speed at 0.4 s: 3.865 m/s from the fit derivative, or 3.824 m/s as the one-frame backward difference 47→48 on the fit.
- Other frame windows (10–60, 20–60, 5–50) give 3.86–3.93 m/s.
- Second route: a fit with the box released from rest and only t0 free gives t0 = 0.0055 s and 9.8 × (0.4 − t0) = 3.866 m/s.
- Sanity check: the box comes out 1.34 m wide and the truck rear (566 px) 2.7 m wide. Both are plausible, so the prior gives a sensible real-world scale.
- The raw backward difference at frame 48 (6.39 px → 3.67 m/s) is affected by the step jitter, so I did not use it.

## Answer
3.85 m/s: between the instantaneous fit value (3.865) and the backward-difference value (3.824).
Confidence is good, about ±3 %.
