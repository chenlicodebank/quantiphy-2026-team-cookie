# Q1593 — length of black cat incl. tail (m)

File fps 24 = question_fps 24; frames 0-49.

## Method
- Focal length (`solve_f.py`): origin proxy = torso centroid from scene/tracks/cat.csv at f0 and f24, back-projected
  with depths 4.199 m (t=0) and 4.481 m (t=1). Required |P24-P0| = 0.94 m (speed prior x 1 s, constant straight walk)
  -> f = 2099 px (HFOV 49 deg). Using mask centroid / bbox centre instead: f = 2161 / 2145.
- Check of the constant-velocity straight-line model: projecting the linearly interpolated origin into every frame
  reproduces the tracked torso u within ~10 px over all 50 frames (extrapolated to f49 too).
- Check of f: floor height below camera from cat paws (f0: 0.82 m, f24: 0.81 m) matches the mirror bottom-centre
  point back-projected at its given 6.407 m depth (0.82 m) — consistent.
- Length (`measure_len.py`): own background-difference mask per frame; every mask pixel is intersected with the cat's
  vertical sagittal plane (through the origin, containing the 3D heading, ~26 deg into depth), and the extent along the
  heading is taken (nose tip to rearmost point: raised tail tip / extended hind paw).
  Nose stays at +0.34 m ahead of origin in every frame (stable geometry); rear end varies with gait.
- Results: torso-origin f=2099: median 0.698 m (range 0.66-0.74; f0 0.710, f24 0.684).
  Mask-centroid f=2161: median 0.676 m.

## Answer
0.69 m (between the two origin proxies). Camera assumed level (horizon ~y 600, pitch < 2 deg — negligible).
Confidence: moderate-good (~±5%); main uncertainty is f from the speed prior and gait-dependent extent.
