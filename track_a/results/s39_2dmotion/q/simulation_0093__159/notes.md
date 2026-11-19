# q159 — speed of the car at t = 1.0 s (prior: car length = 5.67 m)

2D video, file fps = question_fps = 24, so t = 1.0 s is frame 24. Speed = |p(24) − p(23)| × 24.

## Scale (car length in pixels)
- `measure_car.py` (threshold |RGB−bg| > 18, largest component under y=580): bbox length 91 px over frames 0–11
  (car near the image centre), growing to 95 px at frame 24 and 98 px at frame 37.
- `edges.py`: sub-pixel column-profile edges. At frame 4 (car centred at x = 960) the length is 92.4 / 91.4 / 90.2 px at
  thresholds 15 / 30 / 60 (plateau contrast ~105 at the rear, ~137 at the nose, so the half-max reading is ≈ 90.5–91).
  Frames 0, 2, 6, 8 give the same.
- Why it grows: off-centre, the perspective camera also shows the car's rear end face. At frame 24 the left-edge profile
  has a low-contrast ramp (31, 48, 62 …), which is that face. So near the centre the box is the true side length:
  **L = 91 px**, which gives 5.67/91 = 0.0623 m/px.
- SAM 3 ("white car"), frame 4: box 914.5–1007.0 (92.5 px), horiz_px 94. That is 1.6–3% more than my 91 px. On the
  zoomed frame, and in the profile, SAM takes in the faint anti-aliased pixels at the pointed nose (profile 47, 14 at
  1005–1006). Frame 24 SAM: 96.3 px box, the same as my threshold-15 value of 96.4. Both are below the 3% limit, and I kept 91 px
  (the half-contrast edges).

## Motion
- Constant velocity from frame 2 on (frames 0–1 are at rest). Bbox-centre steps average 20.125 px/frame, and a linear fit over
  frames 2–37 gives 20.108. Mask centroid: mean 20.176, fit 20.149. Step 23→24: 20.0 (bbox centre), 20.36 (centroid),
  20.4 (SAM centroids 1341.7 → 1362.1).
- I used 20.13 px/frame, which is 483.1 px/s.

## Result
v = 20.13 × 24 × 5.67 / 91 = **30.1 m/s**.

## Second-route check
- Using the raw single step at frame 24 (20.0 to 20.4 px) gives 29.9 to 30.5 m/s.
- Other scale readings: the SAM length 92.5 px gives 29.6 m/s. The frame-24 bbox length of 95 px, which includes the end face, gives 28.8 m/s.
  (Using the plane instead is not possible, because its size is not given.)

Confidence: high that the answer is within about 3%. The main uncertainty is which edge to take for the pixel length (91 to 92.5 px).
