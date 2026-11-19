# Q169: speed of the plane at 0.3 s (m/s)

2D video, static camera, 24 fps (file fps = question_fps, so no re-timing). t = 0.3 s → frame round(7.2) = 7.

## Scale from prior (car acceleration = 10 m/s^2)
- Car x fitted with a quadratic over frames 1-40 (fit2.py, my own background-difference mask; background = frame 40 with
  the car region patched from frame 0):
  intensity-weighted centroid a = 0.3499 px/frame^2 (rms 0.07 px); bumper mid-point 0.3498; left/right bumpers
  0.352/0.347; sub-windows 1-20 and 15-40 give 0.350-0.353. The scene record's bbox centre gives 0.3494 (fit.py).
- a = 0.3499 × 24² = 201.5 px/s² → scale = 10 / 201.5 = 0.04962 m/px.

## Plane speed
- Pure horizontal translation at constant speed. Nose and tail edges, frames 2-10: 50, 51, 50, 51, 51, 50, 51, 51 px/frame
  → 50.5 px/frame (linear fit to nose edge 50.49). Backward difference at frame 7 is 51 px for both edges (integer-pixel
  edges, so ±0.5 px quantisation; the true constant step is 50.5).
- Speed = 50.5 × 24 × 0.04962 = 60.1 m/s (using the frame-7 integer step of 51 px would give 60.7).

## Checks
- Second route for the car acceleration: record bbox centre (0.3494) vs my centroid (0.3499): 0.15 % apart.
- Sanity with the scale: car length 114 px → 5.66 m (Cybertruck ≈ 5.7 m); plane length 750 px → 37.2 m (A320 ≈ 37.6 m).
  Both consistent with one scale, so the prior and the frame rate are physically plausible.

Confidence: high (~1-2 %).
