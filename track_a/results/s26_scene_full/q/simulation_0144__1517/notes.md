# Q1517 – rocket acceleration at t = 1 s (frame 24)

The file and question_fps are both 24 fps. The 3D Blender scene has a static camera at 1920x1080. One rocket leaves the HIMARS pod
and flies up-left along a straight image line.
Prior: rocket length is 2.9 m. Depths: 43.064 m at frame 0 (at rest in the tube) and 41.127 m at frame 12.

## Geometry (scripts: model3d.py, scanf.py, podedges.py, vp.py, solve.py, final.py, blurfit.py)
- Image track: I used scene/tracks/missile.csv. Origin = nose/tail midpoint for frames 13-30 and nose − L/2 for frames 3-12.
  I checked it on crops. A 1-D fit of the image track shows the rocket at rest until about frame 0.5, with the nose just inside
  the tube mouth.
- 3D direction: it comes from the vanishing point of the pod's long edges (the tubes are parallel to the rocket).
  I fitted the edges with sub-pixel lines (rms 0.1-0.4 px). Pairwise intersections fall at (3706-3833, 3418-3559) and I
  used (3770, 3500). The flight line passes within about 30 px of this point.
  At f = 2400, the direction found independently from the two depths (with the rest position in the tube) gives a
  vanishing point of (3690, 3435), so the two routes agree. The rocket climbs about 30 degrees toward the camera.
- Focal length: it comes from the 2.9 m length. I fitted the measured length over frames 13-30 as
  α·(model projected length) + β·(image speed); the β term is motion blur, about 0.19 of a frame.
  This gives f ≈ 2430-2440 px. Without the blur correction, frames 13-14 alone would give f ≈ 2510.
  With the vanishing-point direction, the depth at the fitted rest position comes out at 42.98 m, against the given 43.064.
  This is consistent, but it hardly depends on f, so f rests on the length.
- 3D positions: each frame's ray is intersected with the 3D line through P12 = 41.127·ray(frame-12 origin) along that
  direction.

## Kinematics
- The 3D path s(t) does NOT fit constant acceleration well (rms 0.11 m, and the start time comes out at −0.2 s, which
  contradicts the rest seen in frames 0-2).
- It fits a Blender Bezier ease (smoothstep s = S(3x² − 2x³)) very well (rms 0.03 m). The fit starts at t0 = 0.03 s with a
  duration T ≈ 2.84 s (about 68-69 frames), which looks like keyframes at frame 1 and frame ~70.
- Reference definition: a = (v24 − v23)·24, with one-frame differences of the fitted curve:
  - free smoothstep at f = 2440: a ≈ 10.6 m/s²
  - smoothstep with T fixed at 69 frames: a ≈ 9.8 m/s²
  - local quadratic or cubic fits of the raw 3D track over frames 16-30 or 18-30 (f = 2400): 10.0-10.3 m/s²
- Sensitivity: f ± 100 px changes a by ∓0.6. The vanishing-point uncertainty changes a by ±0.2.

## Second-route check
- The direction from the depths agrees with the direction from the pod's vanishing point.
- The local polynomial fits agree with the smoothstep model to within about 5%.

## Caveats
- The rocket's edge-to-edge width grows 17-19% between frames 18 and 30. The straight-line model predicts 12%.
  The dark-side width grows 11%, so the extra growth is probably edge bias where the lit side meets the sky.
  If it were real, the approach would be stronger.

## Answer
10.3 m/s². Confidence: moderate, roughly ±10%.
