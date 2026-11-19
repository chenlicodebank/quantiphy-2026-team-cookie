# Q128: distance between the car and the bike at t = 1.0 s (frame 24)

The scene is 2D top-down at 24 fps, and question_fps is also 24, so t = 1.0 s is frame 24.

## Scale from the prior (car acceleration 4.03 m/s²)
- I re-measured the car's front edge x0 in every frame (`measure.py`, same mask thresholds as the record).
- Quadratic fits of x0(frame), in px/frame²:
  - frames 2-53: 0.712
  - frames 0-53, with the start-from-rest time f0 fitted: 0.710
  - local 9-frame fits: 0.57-0.84, but the velocity is linear from 4.1 px/f at f6 to 32.4 px/f at f46, which gives 0.708
  - an early-only fit (0-36) gives 0.68 and a late-only fit gives 0.75.
- I used a = 0.715 px/f² = 411.8 px/s², so the scale is 4.03 / 411.8 = **0.00979 m/px**.
- Sanity check: car length 583 px gives 5.70 m, close to a real Cybertruck at 5.68 m (0.4% off). The bike length 171 px gives 1.67 m and the cyclist speed works out to 4.96 m/s. Both are plausible.

## Positions at frame 24
- Car: front edge x0 = 1592 plus half the length (583/2) gives a centre of (1883.5, 688.5). The car is still cut by the right edge here, so this centre is extrapolated.
- Cyclist: the record's bbox centre is (460, 429), which is about at the saddle/pelvis.
- Separation: dx = 1423.5 px and dy = 259.5 px, so the distance is 1447 px, or **14.16 m**.

## Alternatives and uncertainty
- Using the torso or trimmed-mask centre for the cyclist (x ≈ 451) gives 14.24 m.
- If the car's length at frame 24 were about 590 px (it shrinks slightly over the clip), its centre would move about 3 px, roughly 0.2%.
- The acceleration estimate varies with the fit window (0.68-0.75), which is about ±5% on the scale. The cross-check against the real Cybertruck length agrees to 0.4%.
- Answer: 14.16 m. Confidence: good, within about ±4%.
