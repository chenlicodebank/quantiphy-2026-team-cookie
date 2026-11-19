# q101 — speed of the black-and-white car at 1.0 s (m/s)

File fps = question_fps = 24 → t = 1.0 s is frame 24; speed = |p(24) − p(23)| × 24.

## Scale (2D, top-down, static camera)
Prior: yellow car length = 5.67 m. My background-subtraction mask (measure.py) gives the yellow car's x extent
= 270 px in every frame 18–30 (car near image centre, no edge perspective). SAM 3 segment at frame 24: horiz 267 px
(box 497.1–767.6), a 1.1 % difference (below 3 %); my mask's edges 498–767 agree with SAM's box, and SAM's mask
is slightly eroded at the bumpers. Using 270 px → 0.021 m/px.

## Black car motion
- My bbox centres (measure.py, my_tracks.csv): 1091.0 (f23) → 1105.0 (f24) = 14.0 px; neighbouring frames
  13.5–15 px (integer edges); mean over f14–34 = 14.03 px/frame, over f2–71 = 13.96.
- Sub-pixel column-profile cross-correlation (subpix.py): 14.07, 14.02 (f23→24), 14.08, 14.07 px/frame.
- SAM 3 track (tracks/black_and_white_car_0.csv): 1091.3 → 1105.2 = 13.9 px. All within 1 %.
Constant velocity (no acceleration), so 14.0 px/frame → 336 px/s.

## Answer
336 px/s × 5.67/270 m/px = 7.06 m/s (range 7.04–7.09 across routes).
Confidence: high (main uncertainty is the scale, ±1 %).
