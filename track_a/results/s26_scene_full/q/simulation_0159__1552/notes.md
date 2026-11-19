# Q1552 — speed of the shark at t = 1 s (m/s)

Video: 3D Blender render, 24 fps (file and question_fps both 24), 41 frames, static camera. t = 1 s → frame 24;
speed = |p(24) − p(23)| × 24.

## Model
Both animals swim in a straight line with uniform acceleration from rest (turtle: fitted v0 = 0.006 m/s ≈ 0).
Position: P(t) = O0 + d · a t²/2, where O0 lies on the pixel ray of the origin at the given camera distance.
Pinhole camera, principal point (960, 540).

## Focal length (from the turtle prior a = 2.639 m/s² plus its depths 15.232 → 14.968 m)
- The scene/ core centroid of the turtle is noisy because of the flippers. Instead I chain-tracked the shell band
  frame to frame (NCC on background-subtracted images, `chain_turtle.py`). The track is smooth: −465…−472 px in x over f0–f40.
- I fitted the 3D model with f free, a fixed at 2.639, and the depth at 0.5 s constrained (`fit5.py`):
  f = 2528 / 2576 / 2561 px for the three band heights. With v0 free: f = 2531 and v0 ≈ 0.006. The rms is about 1 px.
  Shifting the origin ±40 px changes f by less than 1 %. **f ≈ 2550 px** (hfov ≈ 41°).
  The direction of motion is th ≈ −2.50 rad: (−0.80, 0, −0.60), i.e. leftward and toward the camera.
- The scene/ centroid track with the from-rest model (`fit3.py`) gave f = 2449 ± 49, which is consistent within about 4 %.

## Shark (route 1: fit to the shark's own track, `fit6.py`)
At f = 2550 I fitted the shark's start pixel, direction and acceleration to its pixel track. The depth
16.474 → 15.744 m at 0.5 s is enforced.
- Core centroid f20–37 (fully visible frames), from rest: a = 7.31, speed@1 s = **7.16** (rms 1.5 px). With v0 free: 7.23.
- Other tracks (full-mask centroid, bbox centre, core f0–37, f10–37, three chained body-patch tracks):
  the speed is 7.13–7.39 from rest. With v0 free the speeds run 7.2–7.7, with small negative v0 values that come from centroid artifacts.
- The shark's fitted direction (th ≈ −2.50…−2.53) is the same as the turtle's.
- For f between 2520 and 2580 the speed changes by only ±0.5 %.

## Route 2 (check, `fit7.py`)
I assumed the shark moves along the turtle's fitted direction from rest, and solved for a from the depth pair alone.
This gives a = 7.14–7.29 and speed@f24 = 7.00–7.13. The predicted f30 pixel x is 1094–1150 (measured core centroid: 1098).

## Answer
The shark accelerates uniformly from rest at a ≈ 7.3 m/s². The speed at frame 24 is a × 23.5/24 ≈ **7.15 m/s**.
Confidence: the routes agree to within about ±2–3 %.
The main uncertainty is that the mask centroid stands in for the shark's rig origin.
