# q_127: distance between the car and the bike at t = 0.5 s (frame 12)

The prior is the car's acceleration, 4.03 m/s². fps = question_fps = 24, so t = 0.5 s is frame 12.
The view is top-down. The two objects are in separate lanes and both move along x.

## Scale (from the prior)
- I tracked one fixed feature on the car: the dark side mirrors, using the intensity-weighted x of rows 560-580 and 797-817 (`mirror.py`).
  - Over frames 16-30 they follow a perfect parabola: a = 0.702 px/frame², rms 0.03 px, starting from rest at frame ≈ 0.
- Template matching of the car front between consecutive frames (`tm.py`) gives 0.7045 for frames 3-25 (rms 0.03).
- From about frame 30 the car's pixel acceleration rises (≈0.78 over f37-53, seen in the mirror, the rear edge and the templates). The cyclist's pixel speed stays constant (21.1 px/frame), so this is not a camera effect.
- I used the constant early phase, which contains t = 0.5: scale = 4.03 / (0.702 × 576) = 0.00997 m/px (≈100 px/m at mirror height).
- If the prior were instead the clip-average acceleration (0.744), the scale would be 0.0094 and the answer 17.7 m. I consider that less likely.

## Perspective
The camera is a perspective camera, not orthographic.
- The car's front face becomes visible when the car is off-axis.
- The low front outline moves about 1.9% slower than the mirror and rear-top features.
- The hood's bright length shrinks from 73 to 60 px as the car approaches the image centre.
- From these, the camera height above mirror height is roughly 20-45 m (≈30 m).

I worked in the mirror-height plane, and the prior scale applies there.

## Positions at frame 12
- **Car centre**
  - The mirror is extrapolated to f12 from the f16-30 parabola: x = 1943.9.
  - The mirror-to-car-centre offset, measured at f50, is +111.3 px. It uses the dark-band front 925.1 (corrected to the mirror plane) and the rear 1502.1.
  - Car centre = 2055.2 px.
  - Check: dark-band front at f12 ≈ 1752 → 1766 in the mirror plane, plus half the length (288.9) = 2054.9. This agrees.
  - The scene record's 2030.5 is too far left, because its front edge (x0) was taken from the shadow.
- **Cyclist**: bbox centre x = 207, y = 429.
  - Its outline is set mostly by the wheel tips, ≈0.8 m below mirror height. Converted to the mirror plane: 960 + (207 − 960) × 1.027 ≈ 187. The range is 174-193 over the possible camera heights.
- Car y = 688.5 (mirror-symmetric centre), so dy = 259.5 px.

## Result
- dx = 1868 px, dy = 259.5 px, giving 1886 px → **18.8 m**.
- Sensitivity:
  - Camera height range: 18.74-18.93 m.
  - No perspective correction (pure 2D): 18.60 m.
  - The scene record's positions with 0.0100 m/px: 18.4 m.
  - A vertical offset between the two origins changes the result by under 0.1 m.
- Plausibility check at this scale:
  - Car length ≈ 5.8 m (a Cybertruck-like pickup).
  - Cyclist speed 5.1 m/s.

Confidence: moderate-good, about ±3%. The main risk is how the prior acceleration was defined.
