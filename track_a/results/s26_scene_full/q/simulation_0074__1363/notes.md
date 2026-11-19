# q_1363 – average speed of the walking pedestrian (simulation_0074)

Answer: **1.20 m/s**

Time base: file fps = question_fps = 24, so t = frame/24. t=0.58 s -> frame 14, t=1.58 s -> frame 38 (exactly 1.000 s apart).

## Focal length (kerbs.py)
- Fitted 8 kerb edges (sub-pixel edge points, rms 0.3-2 px) in two orthogonal road directions.
  Vanishing points: VP1 (-1330, -271), VP2 (2685, -271). Both lie on a level horizon (y = -271), so the principal point at the image centre and orthogonal roads fit well.
- f^2 = -(VP1-c)·(VP2-c) -> **f = 1792 px** (HFOV 62 deg). Non-degenerate line pairs give 1770-1815.

## Pedestrian track (ped_tm2.py)
- Head+torso template tracking, chained over key frames 2/14/26/38/47 (offsets between keys measured on overlapping frames, std ≤ 0.12 px). Frames 0-51 clean; after that the lamp post interferes, so the scene record's mask centroid (offset-matched) is used for 51-71.
- Pelvis at frame 14 located by eye at (935, 199) (belt line, body centre). Pelvis at frame 38 = that + tracked shift (-42.67, -8.07) px, with a small scale correction -> (892.3, 190.4).
- Frame 0 and frame 1 are identical (whole-frame mean abs diff 0.02 vs 0.32 for frames 1-2): either a duplicated first frame or a start from rest.

## Speed
- Route A (given depths): P = depth x unit ray. |P38 - P14| = **1.206 m in 1 s**. The displacement is level: its vertical part is -0.004 m, so the given depths agree with a walk on flat ground under f = 1792. It is also parallel to the kerb (0.3 deg). Moving the pelvis pixel by ±5 px changes the result by under 0.1 %. Using f = 1770 or 1815 gives 1.213 or 1.198.
- Route B (depths plus the kerb direction only, no pixel shift): 1.203 m/s.
- Route C (pixel shift plus the kerb direction only, no depth at frame 38): 1.210 m/s. It predicts a depth of 37.901 m at frame 38 against the given 37.896 m.
- Whole clip (along_path.py, position along the kerb line from pixel u): the fit over frames 1-71 gives 1.197 m/s. Sub-windows give 1.19-1.22 (template) and 1.15-1.26 (noisier centroid). The net distance from frame 1 to 71 is 3.51 m over 70 frames, i.e. 1.203 m/s. So the speed is constant across the clip.
- Under the convention (mean of per-frame speeds over frames 1-71), the frozen frame 0->1 step would lower the result by 1.4 % (to 1.186). Gait bob and sway of the pelvis would raise the per-frame path length by about 1 %. These roughly cancel, so the answer is 1.20 m/s.

## Scene-record corrections
- The record's pedestrian bottoms/heights are unreliable (bin occlusion, shadows); here only head and torso tracking was used. The record's centroid x agrees with the template track to about 1 px after an offset.

Confidence: high on the 1.20-1.21 constant walking speed. About ±2 % comes from the frame-0 convention and gait effects.
