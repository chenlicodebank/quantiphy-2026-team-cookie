# q1508 — height of the man (simulation_0141), answer 1.82 m. Confidence is LOW.

The file and the question are both at 24 fps. The camera is static and points straight down the corridor (VP 959,539; horizon y≈536).
The man walks straight away from the camera along the optical axis: (u−cx)/h_px stays at −0.42 ± 0.02, so his X is constant.

## What the image and priors fix
- Height in the image comes from scene/tracks/man.csv `height_px` (head top to sole). I re-checked it against the series: the head-top bob has a
  12-frame period, and the head is highest (mid-stance) near frames 0, 12.5, 24.5, 37 and 49.5.
- Depth with the off-axis correction (pelvis r ≈ 330 / 276 px, which is a small correction for f > 1000):
  Z0 ≈ 4.07 m and Z12 ≈ 4.96 m.
  - Product of focal length and height: 716·4.07 = 2914 and 602·4.96 = 2986, so **f·H ≈ 2950 px·m**
    (≈2980 for rest standing height).
- How well the priors agree (fit.py):
  - Image size ratio Z12/Z0 is 1.19–1.20, against 1.21 from depth (≈2 % apart).
  - Depth change of 0.88 m in 0.5 s means 1.76 m/s, against the 1.693 m/s prior (4 % apart).
  - Z0/v from the 1/h_px fit is 2.5–2.7 s, against 2.3–2.4 s from the priors.
  - Overall the priors agree to within about 5–10 %.
- **The focal length cannot be identified.** The man's motion is purely along the line of sight, so every metric cue (depths, speed, step length,
  plateaus of the floor contacts) fixes only f·H (or f·h_cam) and Z. The only part that depends on f, sqrt(1+r²/f²), would need d > Z, but the data
  push it the other way. So f has to come from a shape assumption about the scene.

## Scene cues for f (tiles.py, trans.py)
- Floor tiles:
  - Longitudinal seams sit at s=(x−959)/(y−536) = −1.502, −0.802, −0.098, 0.602, 1.304, a spacing of 0.7015 h_cam.
  - Transverse seams sit at y = 1064, 1003, 955, 916 (≈885, 856), so Δ(1/(y−536)) = 2.46e-4.
  - This gives a tile length of 0.54 m along Z (no f needed) and a tile aspect W/L = 2840/f ≈ 0.96·H[m].
  - Square tiles would make H ≈ 1.0 m, which is impossible for a 0.85 m step at 2 steps/s, so the tiles are rectangular.
  - A 2:1 tile gives H ≈ 2.07 m, and a 1.75:1 tile gives H ≈ 1.82 m.
- The pillar and truss shapes are unknown, so they could not be used.

## Answer
I used f ≈ 1620–1640 px (hFOV ≈ 60°, ≈30.5 mm on a 36 mm sensor). This matches an adult-male character asset (step 0.85 m ≈ 0.47·H at 1.69 m/s)
and a 1.75:1 floor tile. H = 2980/1640 ≈ 1.82 m.
The second route (gait plausibility and the tile aspect) only bounds H to about 1.75–2.05 m. The answer depends on a focal length that the given
data cannot determine.
