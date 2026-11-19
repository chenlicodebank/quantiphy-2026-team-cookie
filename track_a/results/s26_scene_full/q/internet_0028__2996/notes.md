# q 2996 – length of the orange suitcase (m); prior: belt velocity 0.5 m/s

File fps 20.528; question_fps 24 is used for all time conversions (per benchmark convention). Single planar scale from the prior.

## Speed (prior's pixel value)
- The suitcase rides the belt, so its pixel speed is used as the belt speed (scene/tracks/orange_suitcase.csv, tag template, frame column).
- Tag x: f25-69 mean 75.0 px/frame; f47-57 (window where the length is measured) 73.7 px/frame; f51->53 75.5 px/frame.
  Adopted 74.5 px/frame -> x 24 fps = 1788 px/s -> scale = 0.5/1788 = 2.80e-4 m/px.
- No camera motion can be checked (no static background); the whole-image flow is 70-77 px/frame, which matches.

## Length (pixels, f52, fully in view; measure.py + crops frames/left52.png, right52.png)
- Orange body (colour mask, row y~1100): 2090 px (1086-3176); shrinks 2150->2046 over f44-59 (perspective/blur).
- Overall wheel housing -> handle housing: ~965 (blurred to ~860) -> ~3415, about 2455-2500 px.
- Body-only reading: 2090 x 2.80e-4 = 0.58 m; overall: 2455 x 2.80e-4 = 0.69 m.

## Answer
0.67 m. This sits between the two readings and leans toward the overall bumper-to-bumper reading (wheels plus handle
housing) that the annotators used. Second check: f25-69 speed (75.0 px/frame) gives 0.68 m overall and 0.58 m body.
A real large checked suitcase is about 0.68 m long, so the answer is plausible. Confidence: moderate. The main
uncertainties are which length reading the annotators used and which reference point they used for the speed.
