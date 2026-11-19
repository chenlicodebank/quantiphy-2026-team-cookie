# Q340: average speed of the rocket from beginning to end (m/s)

The prior is rocket length = 2.9 m. This is a 2D side view with a static camera, 24 fps (the file and the question
agree), 29 frames.

## Definition used
Average speed is the mean of the per-frame speeds over frames 1-28. The path is a straight line: the axis-fit
residual is under 0.05 px. So the average equals (s(28) - s(0)) / 28 x 24, where s is the centre's position along
the flight axis.

## Track
- The track comes from scene/tracks/rocket.csv. It was checked on frames: `frames/early.png` (early.py) and the
  frame-16 crop.
- **Frames 4-7 are biased low by 10-20 px.** The emerging nose is partly hidden behind the grey launcher rail
  (early.png), so the nose-minus-L/2 centre lags. These frames were left out of the fits. Frames 8-25 are reliable to
  about 1-2 px.
- **Motion model.** The per-frame advance rises from 33 to 62 px and the acceleration itself decreases. This is
  Blender's default Bezier (ease-in/out) keyframe curve, which is exactly a smoothstep in time.
  - smooth.py fits s = A + D * smoothstep((f - k0) / (k1 - k0)).
  - Frames 8-24: k0 = 1.65, rms 0.9 px. The start at frame 1.6-2.5 agrees with the truck starting to rock at frame 2.
  - Frames 13-24 and 10-25 give similar fits.
- **Endpoints.** s(0) is -472 to -489 px (the rocket is at rest in the pod). s(28) is 608 to 614 px (extrapolated
  over the 3 frames after the rocket leaves the image). Mean speed is 926 / 936 / 946 px/s across the fit windows,
  so about **936 px/s**.
- **Cross-check.** Cubic polynomial fits (kin.py) over 8-24 and 13-24 give s(0) of about -470 to -483 and s(28) of
  about 611 to 614. That is the same span to within 1-2%.

## Scale
- The rocket length along its axis is 202 px at the 50% level of the band profile. This value is stable over
  frames 16-21: 199-202 px.
- The tapered nose and motion blur make the true tip slightly longer, so L = 203 ± 3 px was used.
- Low-threshold extents with blur removed (length.py) are noisy and broadly consistent.
- Scale = 2.9 / 203 = 0.01429 m/px.

## Answer
936 px/s x 0.01429 = **13.4 m/s**.

## Confidence
- Moderate-good, about ±4%.
- The main risks are the length convention (axis length vs. a world AABB) and extrapolating frames 26-28.
