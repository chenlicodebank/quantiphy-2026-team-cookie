# q_1475 – displacement of the whale, 0.5 s → 1.0 s (frames 12 → 24 at question_fps 24, same as the file's fps)

Prior: whale speed = 1.67 m/s (a single exact value, so the swim is constant speed). depth_info: 33.7307 m at t=1 s, 35.1624 m at t=2 s.

## Main route (uniform straight swim)
The head track in scene/tracks/whale.csv drifts steadily up-left (about 35 px per 12 frames) and the head scale shrinks
smoothly, so the whale swims in a straight line at near-constant speed and moves away from the camera.
Displacement = 1.67 m/s × 0.5 s = **0.835 m**.

## Second route (pinhole, check.py)
- Depth rate 1.43 m/s (from depth_info). Lateral speed = sqrt(1.67² − 1.43²) = 0.86 m/s.
- Focal length from head image motion over frames 24→48 (69 px): f ≈ 2766 px (HFOV ≈ 50°, plausible).
- Frames 12→24: head moves 41.6 px → 0.51 m lateral at z ≈ 33.4 m; depth change 0.72 m → 0.87 m.
  The head patch moves about 20% faster in this window than in later ones (34–35 px per 12 frames), which is likely
  head roll/body flex during the tail stroke (the patch is not the rig origin). This gives an upper bound about 5% above the uniform value.

Answer: 0.835 m. Confidence: high (the exact prior plus constant-speed motion; the image check agrees within about 5%).
