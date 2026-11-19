# q_2553 — white (ping-pong) ball velocity at 1.5 s (frame 36), cm/s

File fps = question fps = 24, so t = 1.5 s is frame 36. Camera: f = 0.5959 x 1280 = 763 px, principal point (640,360).
Depth given at frame 36: ping-pong ball 1.353 m, tennis ball 1.183 m.

## Checks
- Track `scene/tracks/white_ball.csv` is on the right ball (crops in frames/crops.png and frames/crops2.png). Frames 33–35 are motion-blurred and the ball moves
  about 9–11 px/frame. From 36 on it is sharp and moves about 5.8 px/frame. The 35→36 step is 14.5 px (the record flags a possible dropped frame. Yellow also jumps there).
  Another possibility is real slide-to-roll deceleration after the impact: a hollow ball's rolling speed is 3/5 of its sliding speed, roughly 100 → 60 cm/s.
- The apparent size checks the given depth: the vertical extent at frame 36 is about 22.5 px, and 763 x 0.04 / 22.5 = 1.36 m (matches 1.353).
- The ball is rolling mostly TOWARD the camera. Its apparent width grows from about 24.5 to 31.8 px over frames 36–48, so depth falls by about 22%.
  The table-plane model (ball centre at fixed height, horizon v≈354, H≈0.141 m below the camera, solved from the two given depths) gives the same depth ratio.
  The back-projected Y stays constant (≈0.130 m), which is consistent with rolling on a level table.

## Per-frame depth (two routes)
Z_plane = f·H/(v − 354) (vel3.py); Z_diam = 1.339·d36/d(i) from a linear fit of the apparent diameter (vel.py). Both go from 1.339 m at frame 36 to about 1.04 m at frame 48.

## Velocity candidates (3D, cm/s)
- Sharp region only (forward from 36): linear fit 36–42 gives 57 (plane) and 69 (diam). Quadratic fit 36–48 at 36 gives 57 / 77. The mean speed over 36–48 is about 61.
- Centred 5-frame smoothing of the forward differences (= (P39 − P34)/5·fps), which is how I read the reference's "forward difference smoothed over ≥5 frames":
  84 (diam), 96 (plane), 88 (mixed depth). This window includes the faster frames 34–35 and the 35→36 jump.
- 1-frame forward 36→37: 79 (diam), noisy for the plane route.

## Answer
The reference convention is centred smoothing of forward differences over ≥5 frames, which gives about 84–96. Smoothing that leans forward gives about 60–75.
I answer 80 cm/s, weighted toward the centred reading.
Confidence: moderate-low. The ambiguity in the window and the 35→36 jump dominate (about ±20%).
