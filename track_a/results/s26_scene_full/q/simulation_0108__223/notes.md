# q_223 – distance between the two viruses at t = 2.0 s (frame 48), prior: left virus speed 1.7393 m/s

fps = question_fps = 24, so t = 2.0 s is frame 48. No depth_info.

## What the scene really is
- Right virus B: constant pixel velocity (13.781, -0.685) px/frame. Its speed is flat to within 0.06% over frames 2–30, so it stays at a constant depth.
- Left virus A (the prior object) is not moving in a fronto-parallel plane. Its body grows by about 4–5% over frames 1–27, its
  pixel speed rises from 11.48 to 13.0 px/frame, and its slight leftward x-drift (-0.35 px/frame) points away from the image
  centre. That drift pattern is perspective expansion, so A is approaching the camera.
- A's track (sub-pixel flow from scene/scripts/flow.json) fits a constant-3D-velocity projective model
  u = cx+(a+bk)/(1+gk), v = cy+(c+dk)/(1+gk) with rms 0.086 px (fitf.py). Fitted values: g = -0.001413/frame,
  d = -11.55 px/frame, b ≈ 0. So A moves straight up in the world, with Vx = 0, and at the same time comes closer. This is what
  you get from a camera pitched down while the object moves vertically. A second estimate of g from the x-drift alone (assuming
  cx = 960 and Vx = 0) is -0.00148, which agrees. Body-size growth gives about -0.0016 to -0.0019, but that is noisier because the
  lumpy body rotates and the size jumps at a rotation event at frame 10→11.

## Scale and distance (answer.py)
- I work in pixel-equivalents at A's starting depth. A's velocity is (b, d, f·g). Its 3D speed sets the metres-per-unit scale
  through the 1.7393 m/s prior.
- B's depth: H1 puts B in the same world plane as A's motion (pitched camera). This gives Z_B/Z_A0 = 1.0017.
  H2 puts B at the same starting depth as A. The two differ by less than 0.2%.
- Positions at frame 48: A = (703.8, -10.9) from the model (flow-cumulative gives (703.3, -10.5)). B = (1953.4, 582.4), from
  constant velocity. The scene track gives 1951.7, but notes.md marks the 13.62–13.72 px/frame dip as a clipping artefact.
- The focal length cannot be measured precisely here. The off-axis stretch of B's body gives f ≈ 3460 ± 290 px, with systematic
  error from rotation. Blender's default 50 mm lens gives 2667 px.

| f (px) | camera pitch | distance (m) |
|---|---|---|
| 2000 | 13.7° | 8.29 |
| 2667 | 18.1° | 8.15 |
| 3000 | 20.2° | 8.07 |
| 3461 | 22.9° | 7.94 |
| 4000 | 26.1° | 7.78 |

  The answer is 8.05 m, taking f ≈ 3000 between the two estimates.
- Check against naive 2D (pixel distance 1383 px, scaled by A's pixel speed): 8.73 m using frame 2 and 7.71 m using frame 48.
  The 3D answer lies between these, as it should.

## Confidence
Moderate. The answer moves by about ±4% for f anywhere from 2000 to 4000 px. The main assumptions are that A's speed is
constant in 3D and that B sits at the same depth as A (in its plane).
