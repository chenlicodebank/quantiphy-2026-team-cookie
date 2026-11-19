# q3263 – speedboat velocity at 2.00 s (prior: 11 m/s at 1.00 s)

Internet video, side view, 2D. A single scale from the prior: v(2 s) = 11 m/s × v_px(f60) / v_px(f30).
Time base: 29.97 fps vs question_fps 30 → t=1 s is f30 and t=2 s is f60 at either rate (the difference is negligible).
The camera pans slowly to the right, so speeds are measured relative to the far bank (the background).

## Route 1 – scene record (speed.py)
Background-compensated forward differences (px/frame), averaged over ±2 frames:
- canopy_tm_x: 15.82 → 14.96, ratio 0.946 (a linear fit over f21-110 gives 0.946)
- bow_x: 15.85 → 14.83, ratio 0.935 (fit 0.946)
- ref_x (bbox centre): ratio 0.915 (fit 0.942); noisier because the stern flag flutters.
The raw image speeds without background compensation would be 15.4 → 14.0, a ratio of about 0.91 (about 10.0 m/s).

## Route 2 – independent check (check.py)
I matched my own whole-boat template (canopy and hull) and took the median of 4 far-bank patches as the background shift:
- boat minus background: 15.84 px/frame at f30 and 14.90 px/frame at f60, ratio 0.941.
- The background moves 0.4 px/frame at f30 and 0.8 px/frame at f60, which agrees with the record's camera shift.

## Answer
Ratio ≈ 0.943 → 11 × 0.943 ≈ 10.4 m/s. The boat slows in the image, partly because it turns slightly away from the camera.
Confidence: good (within about ±4 %). The main uncertainty is whether the annotators compensated for the pan; without it the answer is about 10.0.
