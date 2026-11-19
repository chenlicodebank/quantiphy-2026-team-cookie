# Q953 — length of the phoenix (m)

Prior: acceleration of the phoenix at 2.0 s = 2 m/s^2. 2D clip, static camera, fps 24 (= question_fps, no re-timing).

## Scale from the prior (fit.py)
Quadratic fits x(t) to the scene/ tracks (frames 2-71 and sub-windows):
- body_s_x: a = 282-285 px/s^2 (f2-71, f10-71), 260 (f24-71); cubic fit gives a(1 s)=285, a(2 s)=280 -> constant acceleration.
- body_x 286-288, head_x 294, centroid_x 284, bbox_x0 288, bbox_cx 282, bbox_x1 277 px/s^2 (f2-71).
- Fitted v(2 s) = -567 px/s, so v(0) = -567 + 2*283 ≈ 0: the bird starts from rest at t=0 and accelerates uniformly
  (x(f71) predicted 303 vs measured 315). Per-frame steps oscillate with the wingbeat (body bobbing), so the
  uniform-acceleration value of ~283 px/s^2 is used, not a one-frame difference.
- Scale = 2 / 283 = 0.00707 m/px.

## Length in pixels (widths.py, frames/f0.png)
Horizontal bbox (beak to tail-tip): frame 0 (rest, no motion blur) 566 px (x 1434-1999; beak tip ~1440, the faint
wisp in front of the beak is mostly outside the mask). Over the clip 536-624 px (tail plumes swing, motion blur),
median 591, mean 584.

## Answer
566 px x 0.00707 m/px = 4.00 m (mean-width reading: 584 px -> 4.13 m; range 3.79-4.41 m).
The round result at the rest frame supports 4.0 m. Confidence: good (~±5%).
