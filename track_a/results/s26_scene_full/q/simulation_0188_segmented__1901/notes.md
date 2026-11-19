# q1901 – speed of the truck at t = 1.5 s (m/s)

Prior: acceleration = 10.757 m/s^2 (exact). Depths: 22.532 m at t=0.5 (f15), 19.525 m at t=1.0 (f30). question_fps = file fps = 30.

## Method
- recon.py: front-hub track (frames 0–46) and rear-hub track (25–54) from scene/tracks/truck.csv. The truck translates
  straight along the direction of its length vanishing point (-3030, 538). For a range of focal lengths
  (800–4000 px) each hub's pixel track was back-projected onto a 3D line along that direction, giving the path
  coordinate s(frame) up to scale.
- s(t) fits a quadratic almost exactly (rms residual 0.06 % of range) for every focal length. The velocity is zero at
  t = -0.010 s (front hub; rear hub, seen only from f25, extrapolates to -0.07 s). So: uniform acceleration from
  rest at t ≈ 0 (frame 0). The pixel steps agree: 0.56, 1.66, 2.59 … px, ratio ≈ 1:3:5.
- Speed at frame 45 by backward difference = a·(45² − 44²)/(2·30) = a·1.4833 = 15.96 m/s (rest at exactly t=0);
  16.06 m/s with t_rest = -0.01; the instantaneous a·t = 16.14 m/s.

## Check
- Depth check: with rest at t=0, the centre moves 0.5·a·(1² − 0.5²) = 4.03 m between f15 and f30. With the given
  depths this means cos(angle between camera→centre ray and motion direction) = -0.785. The back-projection gives
  -0.77 to -0.80 for that angle over the plausible focal range, so the motion and the depths agree.

Answer: 16.0 m/s (between the backward-difference value and the a·t value, all within ±1 %). Confidence: high.
