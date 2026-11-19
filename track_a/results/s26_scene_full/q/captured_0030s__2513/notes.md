# q_2513: speed of the red ball at t = 0.4 s (cm/s)

Lab video, 24 fps (the file and question_fps agree), 1280x720. t = 0.4 s means frame round(9.6) = 10.
Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
depth_info: f5 0.8715, f10 1.1660, f14 1.3720, f19 1.3150 m.

## Checks
- Ball track: scene/tracks/red_ball.csv (circle-fit centre, cy_corr). I checked frames 8-13 visually (frames/f08..f13.png).
  The ball is sharp at f10, centre (431, 438). The step from f11 to f12 is large (50 px vs 16 and 33 px around it),
  so f11 is probably a lagging or blurred measurement.
- Prior check: depth from size, 0.07*f/diam, gives 0.891 / 1.165 / 1.317 (occluded) / 1.248 m at f5 / 10 / 14 / 19.
  This matches depth_info at f10 to 0.1 % and at f5 to 2 %.
  Per-frame depth from size is too noisy to difference (it gives per-frame speeds of 60-340 cm/s).

## Method
Back-project the centres, P = ((u-cx)/f, (v-cy)/f, 1)*Z, with Z(frame) taken from a smooth curve through the 4 given
depths. Velocity at f10 = 5-frame-smoothed positions, forward difference (or the central difference over f8-f12).
Near f10 the depth rate (about 1.3-1.5 m/s) dominates. The lateral part is about 0.35 m/s.

| depth model | speed at f10 (cm/s) |
|---|---|
| natural cubic spline / Lagrange / PCHIP through the given depths (Z convention) | 151-153 |
| same, but treating depth as Euclidean distance | 163-165 |
| linear interpolation of the depths | 133-139 |
| sinusoid through the 4 depths | 152-164 |
| sinusoid fitted to size-based depth | 128-134 |
| 3D harmonic-orbit fit to (u,v) plus the given depths (frames 0-24 / 2-20 / 4-18) | 140 / 143 / 150 |

## Answer
150 cm/s (the smooth-depth back-projection, cross-checked by the 3D orbit fit at 140-150).
Confidence: moderate, about ±10 %. Only 4 depths are given, so the depth rate at f10 is not pinned down:
the depth models give 130-165 cm/s.
