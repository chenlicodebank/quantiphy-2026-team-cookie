# Q2283 – soccer ball speed at t = 1.5 s (captured_0016)

Question: velocity of the ball at 1.5 s, in m/s. Prior: g = 9.8 m/s². depth_info at 1.5 s: ball 1.402 m, near person 0.843 m, far person (receiver) 2.372 m.
The file rate and question_fps are both 24, so t = 1.5 s is **frame 36**, just after the ball's image apex. The ball is in free flight there with mild blur.
Camera: f = 0.5959·1280 = 763 px, principal point (640, 360).

## Findings / corrections to the scene record
- The track in scene/tracks/ball.csv is correct for frames 31–42. I checked frames 34–37 on zoomed crops.
- **Likely dropped capture frame between frames 35 and 36.** The horizontal image steps are 61, 53, 51, 42, **79**, 32, 28, 22, 18 px. One missing frame fits that step series (~40 + 37). In the 3D ballistic fits, 1 missing frame gives clearly lower image residuals (gap 0: about 7 px rms; gap 1: about 2.4–4 px).
- Ball size from the record is noisy. I re-measured it with a radial-edge robust circle fit (circle_fit.py, circles.csv) on the sharp frames.
  - Diameters for frames 37, 38, 39: 95.6, 92.1, 88.9 px. Frame 36: 98.6 px, which is blurred.
  - From frame 40 on, the receiver's arms contaminate the fit.

## Main route (direct_v.py)
1. Depth: d ∝ 1/(diameter·cos^k θ), where θ is the off-axis angle and k = 1 or 1.5. The constant K is anchored by d(36) = 1.402 m, using the diameter at frame 36 either measured or extrapolated from frames 37–39.
   - Resulting depths for frames 36–39: 1.402, about 1.47, 1.54, 1.61 m. The ball recedes about 0.07 m per frame.
   - Implied ball diameter: about 0.16 m.
   - Check: frames 45–48, ball in the receiver's hands, give a depth of about 2.2–2.4 m, consistent with the receiver at 2.372 m.
2. Back-project the centres (circle fit or the scene track) and work out the 3D velocity at frame 36:
   - forward difference 36→37: 1.83–2.18 m/s
   - local quadratic fit over frames 36–39: 1.95–2.27 m/s
   - linear fit: 1.94–2.11 m/s
   - Central value: about 2.1 m/s.

## Second routes / checks
- **Reference-style velocity** (refstyle.py): uniform 1/24 s frames, forward differences.
  - At frame 36 this gives about 2.1–2.2 m/s.
  - With a centred 5-frame smoothing window, the window includes the 35→36 jump, which pushes the value to about 2.5–2.7 m/s.
- **Ballistic 3D fits with |g| = 9.8 m/s²** (fit3d.py, fit_pitch*.py, fit_late.py, fit_gfixed.py, fit_combined.py):
  - Gravity's direction in the camera frame is poorly constrained by the ball alone. The fits range from 1.4 to 3.3 m/s depending on the assumed direction.
  - From the receiver's body (pelvis at 2.372 m, feet below it), gravity is about (0.18, 0.46, 0.87): pitch about 60°. With that direction fixed, the fits give 2.6–3.0 m/s.
  - However, those fits make depth grow faster than the measured ball shrinkage allows: the size constant drifts from 126 to 147 px·m. They would also put the caught ball behind the receiver's body.
  - So I trust the size-based route more.

## Answer
**2.2 m/s.** This is the size-based physical and forward-difference estimate (about 2.1), nudged slightly toward the smoothed reference-style value (about 2.5).

Confidence: moderate, about ±15%. The main uncertainty is the depth rate (from apparent size) and how the reference smoothed across the anomalous 35→36 step.
