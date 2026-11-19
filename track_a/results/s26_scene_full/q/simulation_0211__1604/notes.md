# Q1604 — black cat to camera distance at t = 1.5 s (frame 36)

File fps = question_fps = 24, so t=1.5 s -> frame 36.

## Route 1: constant-velocity straight line (prior + depth_info only)
p(t)=p0+vt, |p0|=4.199, |p0+v|=4.481, |v|=0.94 m/s
-> d(t)^2 = d0^2 + t(d1^2-d0^2-s^2) + t^2 s^2 -> d(1.5) = 4.687 m.

## Route 2: pinhole back-projection (fit.py)
Cat torso centre track (scene/tracks/cat.csv, 5-frame smoothed), principal point (960,540).
Focal chosen so that the 3D chord between f0 (depth 4.199) and f24 (depth 4.481) equals 0.94 m:
f = 2028 px (HFOV ≈ 51°). Rays at frames 12, 30, 36, 42, 49 all meet the line P0->P24 within
≤1.3 cm, at line parameter k ≈ t (0.476@0.5 s, 1.517@1.5 s, 2.028@2.04 s): motion is straight
and uniform, validating route 1. Depth at frame 36 = 4.694 m.

## Answer
4.69 m (routes agree within 0.2%). Confidence high.
