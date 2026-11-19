# q_2863 – pink ball velocity at 1.5 s (frame 36), captured_0054ax

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640,360).

## Identification
- "orange ball" = basketball (rolled by crouching person); "green ball" = yellow tennis-type ball; "white ball" =
  the pale pink/whitish small ball (= the asked "pink ball"). Both small balls are in the standing person's hands at
  t=1.0 s, which is why their depths match (3.07 / 3.04 m). The soccer ball sits by the crouching person
  (~2.4-2.5 m from the floor model), so it can't be the 3.07 m "white ball".
- Pink track (scene/tracks/pink_ball.csv) checked on zoomed crops f33-38 (frames/m34.png): correct ball, motion blurred.

## Dropped frames
- Basketball: step f11->12 = 31 px vs 15-18 px neighbours; pink f35->36 = 114 px vs 43 before; yellow f35->36 = 130 px.
  Blur-streak lengths at f36/37 indicate ~65-75 px/frame motion, so this is a missing frame, not real motion.
  A ballistic fit with a free time gap after f35 gives gap = 1.00 frame (pink) and 1.07 frames (yellow).
- Prior check (bball3.py): floor plane (zero roll) through the basketball centres at f12 (2.3557 m) and f24 (1.81 m)
  -> steady rolling speed 1.64 m/s. The prior 2.21 m/s is only reproduced if the f11->12 jump is included in the
  smoothing: 5-frame centred mean of forward differences 2.11, 3-frame 2.29. So the reference averages over
  frame-index differences, gap included.

## Pink ball 3D (fitball.py, pinkvel.py)
- 3D ballistic fit to pink centroids f24-37, distance at f24 anchored to 3.0735 m. Gravity points along the floor
  normal from the basketball plane, and the time gap after f35 is a free parameter. With free g: rms 0.8 px,
  g_fit = 8.0 (yellow: 8.7, rms 0.5 px). The model's floor contact times match the observed bounces
  (yellow f37, pink f38), and the standing person's feet land at ~3.1 m on the same floor model. Fixed g = 9.81 gives
  rms 3.5-5 px with systematic residuals, and the yellow ball would pass below the floor, so the free-g fit is used.
- Positions = observed pixel back-projected at the model depth; f38-39 (post-bounce) use extrapolated horizontal depth.
- Per-frame forward speeds (x24) f33..39: 3.35, 3.44, 7.80 (gap), 4.44, 3.07, 3.74, 3.25 m/s.
  - fwd diff at f36: 4.44; 5-frame centred mean (f34-38): 4.50; 3-frame: 5.10; trailing 5: 4.42.
  - Scaling by the prior's calibration ratio (2.21 / basketball value under the same convention):
    w5 -> 4.72, w3 -> 4.93.
  - Physical instantaneous speed from the model: 4.2 m/s. With fixed g = 9.81 the 5-frame mean is 4.97.

## Answer
4.6 m/s: 5-frame smoothed forward difference (4.50), with a small allowance for the prior calibration (4.72).
Confidence: moderate (about ±10%). The reference's per-frame depth-sensor values on a small blurred ball and its
exact smoothing window are unknown.
