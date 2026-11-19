# q_1900 – speed of the truck at t = 1 s (m/s)

Prior: constant acceleration a = 10.757 m/s^2 (exact). question_fps = file fps = 30.

## Method
- Start of motion: front-hub x track (scene/tracks/truck.csv, frames 0-15) fitted with x0 + c·(i - i0)^2:
  i0 = 0.25 frame (max residual 0.46 px); free quadratic gives rest at frame 0.25. Per-frame steps
  0.56, 1.66, 2.59, 3.77, ... grow linearly with first step ≈ half the increment → truck at rest at frame 0
  (small offset explained by perspective growth of pixel motion as it approaches).
- Hence p(i) = ½ a (i/30)^2 along a straight line (no turning; VP stable). Speed convention = backward
  difference at frame 30: (p(30) - p(29))·30 = a·29.5/30 = 10.578 m/s. (Instantaneous a·t = 10.757, 1.7% higher.)

## Check with depth_info
- Displacement 0.5 s→1 s under this model = 4.034 m. With |P1| = 22.532, |P2| = 19.525 this requires the
  angle between the camera ray and the motion direction ≈ 38°, consistent with the truck driving toward the
  camera and rightwards (VP of travel at x ≈ -3030 px). Front wheel radius px ratio f15→f30 = 1.136 vs depth
  ratio 1.154 (consistent within the ±2 px noise).

Answer: 10.578 m/s. Confidence high (both conventions within 2%).
