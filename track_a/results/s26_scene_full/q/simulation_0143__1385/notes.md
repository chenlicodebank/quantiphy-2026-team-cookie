# Q1385 — acceleration of the man at t = 2.5 s (frame 60, question_fps 24 = file fps)

## Scale
- Prior: man 1.8 m. Frame 0 silhouette height 429 px at depth 7.21 m, so f = 429·7.21/1.8 ≈ 1718 px (hFOV ≈ 58°).
- Check against t = 0.5 s (frame 12): from height I get 7.75 m and from the ground plane 7.66 m (camera height 1.28 m,
  horizon at row 538). The given value is 7.91 m, so the scale is about 2–3 % off. This does not matter at the level of
  uncertainty below.
- Camera is static (scene/ record), and I reused the track in scene/tracks/person.csv (I checked the bboxes on crops).

## Trend (smoothed 3D path: Z from the mean of the height-based and ground-based depths, X from torso_x)
- Speed rises from ~1.75 m/s at 0.5 s to a peak of ~2.9–3.0 m/s near 2.5 s, then falls to ~2.5 m/s (accel.py,
  steps.py, speedcurve.py).
- The trend acceleration at 2.5 s is about 0 to +0.15 m/s² across all fits, because the speed is at its broad maximum.
- The stance-foot plateaus (ground-plane depths 11.0 / 12.49 / 13.96 m at frames ~50 / 62 / 74) give a flat depth speed
  of ~2.95 m/s around 2.5 s.

## Gait oscillation (dominant term in a per-frame pelvis acceleration)
- The feet stay planted during stance (feet_y plateaus), so this looks like mocap root motion. The per-frame
  pelvis speed therefore swings with the steps.
- Head-top bob (phasefit.py): highest (mid-stance) at frames ≈ 50, 62.5, 74.5; lowest (double support) at ≈ 44, 56, 68.
  The period is ~12.4 frames.
- I measured the forward-speed oscillation from the lateral image motion in frames 0–33, while he walks diagonally.
  Amplitude ≈ 0.20–0.22 m/s. The speed is highest near the lowest head position, which matches inverted-pendulum
  walking (centroid-based phase 6.4 versus head-low 6.5; torso-based phase 4.4).
- Acceleration at frame 60 uses the speeds centred at 59.5 and 58.5. That is between the speed maximum (~56) and the
  minimum (~62.5), close to the steepest point. So a ≈ −A·ω = −0.21 × 12.2 ≈ −2.5 m/s² (−1.5 if I use the torso
  phase), plus a trend term of about +0.1.
- I can't measure per-frame depth well enough to check this directly. The height and ground depth cues show the same
  phase, but with an exaggerated amplitude caused by artifacts.

## Answer
The magnitude is ≈ 2.2 m/s² (signed, the man is probably decelerating within the step). Confidence is low. If the
reference used a smooth path instead of the per-frame mocap pelvis, the value would be ≈ 0.1 m/s².
