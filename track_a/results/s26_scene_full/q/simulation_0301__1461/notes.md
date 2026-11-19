# Q1461 — forklift width (left wheel to right wheel), simulation_0301

Answer: **1.43 m**

## Inputs
- Prior: forklift acceleration = 2 m/s^2 (from rest). Depths: forklift 16.7953 m at t=1 s (frame 24), 19.0980 m at t=2 s (frame 48).
  question_fps = file fps = 24.
- Motion onset: phase-correlation shifts of the forklift region vs frame 0 for frames 2,3,4,5 = 0.75, 1.73, 3.36, 5.41 px
  -> ratio ~4:9:16:25, i.e. s = 0.5*a*t^2 with t0 = 0 (frame 1 shift ~0.2 px, lost in compression) (`onset.py`).

## Focal length (fit_track.py, fit_track2.py, fit_alpha.py)
- 3D model: origin P(t) = P0 + t^2 * d (a = 2), straight line; fitted f, P0, d to the image track of the forklift
  (frames 13-71) plus the two given depths (reproduced to <0.2 mm).
- The origin's image point is unknown: tried bbox centre (alpha=0) to bbox bottom-centre (alpha=1).
  f = 3348 (alpha 0), 3467 (0.5), 3527 (0.75), 3587 (1.0) px.
- Evidence for alpha ~0.7-0.75 (origin = vehicle root at ground level): (i) a fit with the acceleration free gives
  a = 1.91-1.97 for alpha 0.75-1, but 1.54 for alpha 0 (the prior says 2); (ii) the far-tire silhouette fit has
  rms 1.1 px for alpha 0.75 and 3.5 px for alpha 0; (iii) for alpha~0.7 the origin comes out at ground height
  (rear hub 0.33 m = tire radius above it).
- Camera roll assumed zero: up = the vector perpendicular to the motion direction d in the camera y-z plane;
  lateral axis L = d x up. The camera pitches down ~20 deg.

## Width (track_feat.py, hub3d.py, edges.py, nearfit.py, multi.py)
- Tracked the near rear wheel hub across frames 13-71 (template matching) and placed it in 3D as a fixed offset from
  the origin: hub depth Z ≈ 15.59 m at frame 24 (~1 m nearer than the origin).
- Foreground mask = |frame - clean background| > 40. Near rear tire: fitted the outer-sidewall circle (axes d and
  up, radius R) to its left and bottom silhouette -> R = 0.33-0.34 m, rms 1.7 px. Far rear tire: its right silhouette
  edge (the only visible part) fitted with the same circle shifted by W*L -> W = outer face to outer face.
- Results (alpha 0.75 / 1.0 / 0):
  - frame 16: 1.429 / 1.389 / failed
  - frame 24: 1.428 / 1.389 / 1.552 (rms 3.5)
  - frame 28: 1.428 / 1.390 / 1.549
  - frame 32: 1.424 / 1.387 / 1.542
  (The frame 20 fit failed to converge because of a bad starting point; it was not used.)
- Second route: frames 16, 28 and 32 give the same value as frame 24 to within 0.3%. An independent rough
  linear estimate (near hub to far-tire extreme, 189 px/m along L) gave ~1.35-1.38 m before the perspective and
  radius corrections.

## Answer and confidence
W ≈ 1.43 m (alpha 0.7-0.75; 1.39 if the origin is at the bbox bottom; 1.55 if it is at the body centre, which the
kinematics argue against). Main uncertainty is the focal length / origin choice: about ±4%.
