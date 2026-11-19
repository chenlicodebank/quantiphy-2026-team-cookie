# Q164 – plane speed at 0.5 s (m/s)

2D simulation video, 24 fps (the file's fps equals question_fps). t = 0.5 s is frame 12. The prior is "car acceleration = 10 m/s^2", and it sets one metres-per-pixel scale for the whole scene.

## Car pixel acceleration (fit.py, from scene/tracks/car.csv)
I fitted a quadratic to x(frame) over frames 2–71:
- mask centroid: 0.5072 px/frame^2, which is 292.2 px/s^2 (rms 0.17 px). The sub-windows 2–36 and 36–71 give 292.2 and 291.0.
- bbox centre: 290.8; bbox front edge: 293.1.
- I adopted 292 px/s^2, so the scale is 10/292 = 0.03424 m/px.

## Plane pixel speed (plane_shift.py, my own template matching, frames 7–16)
- The plane moves at a constant rate, so the speed at frame 12 equals the steady value.
- Whole-plane template from frame i matched in frame i+1: shift 74.08 px/frame, the same in every frame. The middle section gives 74.3 and the rear section 73.7.
- The record's nose/tail line fits average 73.6, and the bbox centre averages 74.3 px/frame.
- I adopted 74.0 px/frame, which is 1776 px/s.

## Answer
1776 px/s x 0.03424 m/px = 60.8 m/s.

Second route: plane speed / car acceleration = 74.0 px/frame / 0.507 px/frame^2. This gives 145.9 frames, or 6.08 s; multiplied by 10 m/s^2 that is 60.8 m/s, the same value. The spread across the fits is about 60.3–61.4.

Confidence: good, within about 1.5%. The main uncertainty is which point on the plane is its origin, because of slight perspective (front 74.3, rear 73.7 px/frame).
