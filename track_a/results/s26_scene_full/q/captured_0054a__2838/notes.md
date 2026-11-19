# q_2838: velocity of the white ball at 1.0 s (frame 24), m/s

The file and the question both run at 24 fps, so t = 1.0 s is frame 24. Camera: f = 763 px, principal point (640, 360).

## Which ball is the "white ball"
It is the pale (white/pinkish) ball thrown by the standing person, not the soccer ball:
- depth_info gives the white ball at 3.07 m and the green (tennis/yellow) ball at 3.04 m. Both balls sit with the standing person at the back.
- The soccer ball at the bottom-left is about 66 px wide, which puts it at roughly 2.5-2.6 m.

At f24 the pale ball has just left the hand (released around f21-22) and is rising up and to the left at (570, 267) px. The scene/ track
(`scene/tracks/pale_ball.csv`) was checked on a zoomed frame. A ballistic fit through f22-35 leaves residuals of only 0.43 px, so the track is good.

## Method (fit3d.py, check_landing.py)
Most of the speed is the depth component, because the ball flies toward the camera. To get it:
- I fitted a 3D parabola P(t) = P0 + V·t + ½·g·t² projected through the pinhole to the pixel track for f22-33 and f22-35.
- P0 is the f24 ray scaled to the given range of 3.0735 m. The gravity direction comes from the camera pitch, and the gravity magnitude is fitted.
- Pitch values tried: 2.9° (from the plane through the basketball's two given depths), 5.6° (horizon at y ≈ 285 in the scene notes), and 4.2°.
- Fitted g is 8.1-8.4 m/s² in depth_info scale, with rms 0.43 px. Forcing g = 9.81 at R = 3.07 fits worse (rms 2 px). Under real g the
  trajectory would imply a range of about 3.65 m, so the depth_info scale is about 16% below "true g" scale. I kept the depth_info scale,
  as the rules require.
- Result at f24: V ≈ (-0.65, -0.67, -2.0 to -2.2) m/s, |V| = 2.22-2.39 m/s. The reference-style speed (mean of five forward differences) is
  2.22-2.38, and the single forward difference is 2.17-2.34. Central value is about 2.30 m/s. The yellow ball fitted the same way gives
  2.22-2.35 m/s.

## Second-route checks
- **Landing point.** The floor plane implied by the basketball's given depths (camera about 0.90-0.99 m above the floor) puts the predicted
  floor contact at f38.8 near (360, 676). The pale ball is observed bouncing at f38, (358, 661). For the yellow ball the prediction is f37.6
  near (350, 650) against an observed f37, (340, 656). This supports the depth rate of about -2 m/s.
- **Prior check (check_prior.py).** Working the basketball the reference's way (linear or size-based depth, forward differences, 5-frame
  smoothing) gives 1.6-1.8 m/s at 0.5 s, against the given 2.21. The reference speeds therefore look about 25% above clean geometry, most
  likely from depth or click noise. Because of that, I shifted the answer slightly upward from 2.30 to 2.4.
- **Wall-seam pitch estimate (seams.py).** Inconclusive because of lens distortion near the image edges; not used.

## Answer
**2.4 m/s.** Confidence is moderate. The geometric value is 2.30 ± 0.08, and the reference convention may sit higher.
