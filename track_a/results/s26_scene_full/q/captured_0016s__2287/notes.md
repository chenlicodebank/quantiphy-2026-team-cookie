# q_2287 — soccer ball velocity at t = 1.5 s (captured_0016s)

File fps = question_fps = 24, so t = 1.5 s -> frame 36 (ball in free flight, frames 31-40).

## Method
- Ball centres from scene/tracks/ball.csv (auto mask, ±2 px in frames 32-40); checked on 2x crops of frames 35-37
  (frames/f35-37.png): centres (735,122), (812,78), (846,70) agree with the record.
- Camera: f = 0.5959*1280 = 763 px, principal point (640,360).
- Depth: depth_info gives 1.402 m (camera to ball centre) at frame 36. Other frames: distance = 1.402 * d36/d_i, with the
  apparent diameter d_i either raw (diameter_est_px) or from a linear fit of 1/d over frames 32-40 (smoother).
  Points = unit ray * distance. Ball diameter implied: 0.181 m.
- Velocity = forward differences of 3D centres, smoothed over ~5 frames (benchmark convention, frame indices as-is).

## Results (m/s)
| estimate | raw depth | fitted depth |
|---|---|---|
| forward diff 36->37 alone | 1.37 | 1.51 |
| 5-frame mean of fwd-diff vectors (34..39) | 1.92 | 1.86 |
| 5-frame mean of step speeds | 2.17 | 1.94 |
| (P38-P34)/4, (P38-P33)/5 | 2.08 / 2.17 | 2.09 / 2.18 |
| quadratic fit 32-40, v(36) | 2.04 | 1.99 |

Second route / check: quadratic fit of the 3D track gives |a| ≈ 11.5-12 m/s^2 with frame indices as-is, ≈ 8.5-9.3
with one dropped frame inserted between 35 and 36 (the record flags a probable dropped frame: 88 px step vs 58/35);
both are close to the prior g = 9.8, so the metric scale is consistent. With dropped-frame timing the physical speed
would be ≈ 1.6 m/s, but the reference uses frame indices as they are, so the smoothed value ≈ 1.95 is used.

Answer: 1.95 m/s. Confidence moderate (±10-15 %, mostly from the smoothing window around the dropped frame).
