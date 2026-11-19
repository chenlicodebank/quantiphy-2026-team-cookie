# Q336: total distance the man walked (m)

Prior: walking speed = 1.693 m/s. The clip is 2D, the camera is static, 24 fps (same as question_fps), and has 80 frames.
On the contact sheet (frames/sheet.png) the man is already walking at frame 0 and still walking at frame 79, with no start or stop.

Method (measure.py, using scene/tracks/man.csv, head_cx, which is smooth; pelvis_x = head_cx + a constant):
- Per-frame step: mean 18.78 px/frame, range 16–24 (gait modulation). The speed is the same in both halves (18.79 vs 18.82 px/frame), so the walk is constant.
- Route 1: the path length is the sum of 79 per-frame displacements = mean speed × 79/24 s = 1.693 × 3.2917 = 5.573 m.
- Route 2: the scale from the prior is 1.693 / (18.78 × 24) = 0.003755 m/px. Total pixel path 1484 px × scale = 5.573 m. Both routes agree because the speed is constant.
- The vertical bob (~19 px amplitude, a slow sinusoid) would add <0.5 % to the path, so I ignored it.

Answer: 5.573 m. Confidence: high. The only open question is whether the reference counts 79 or 80 frame intervals (80 would give 5.64 m, +1.3 %).
