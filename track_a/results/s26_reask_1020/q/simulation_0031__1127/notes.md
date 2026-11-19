# Q1127 – speed of the boat at t = 1.0 s (m/s)

Answer: **3.94 m/s**

Time base: question_fps = 24 (the file is 25 fps), so t=1 s is frame 24 and t=2 s is frame 48.

## Measurements
- Boat: I tracked it myself in `track.py` with multi-scale NCC on the cabin template, frames 16–56. Frame 24 is at
  (225.0, 710.0) and frame 48 at (136.9, 670.7), so it moved (-88.1, -39.3) px. That agrees with scene/boat.csv
  (hull centre (228.8, 762.9) → (141.0, 722.2)). The template scale between the two frames is 0.9725, and the depth
  ratio is 130.349/133.743 = 0.9746, so the given boat depths fit the image. The motion is steady (about 3.9 → 3.6
  px/frame, as expected while the boat recedes).
- Person height from head to feet (scene/person.csv, re-checked on a 4x crop) is 77.2 px, at depth ≈ 139.97 m.

## Geometry (`solve.py`)
- Pinhole camera with the principal point at the image centre, no roll, pitched down by θ, focal length f.
- Constraint 1: the boat moves on water, so its 3D displacement between t=1 and t=2 (back-projected with the given
  depths) has zero vertical component. This gives θ as a function of f.
- Constraint 2: an adult's rest height is 1.70–1.80 m. Projecting this, foreshortened by the tilt, must give 77.2 px.
- Result: f ≈ 6170–6510 px (horizontal FOV ≈ 8.7°) and θ ≈ 12°. The tilt matches the look of the cabin roof, which
  appears foreshortened to about 0.25.
- Boat displacement from 1 s to 2 s is 3.92–3.97 m, about the same for the hull-centre and cabin reference points.
  The motion is steady, so the speed at 1 s is about 3.94 m/s. Of this, 3.39 m/s is the change in depth, so the
  answer depends only weakly on f.

## Checks
- Eagle, an independent route: back-projecting it with its own given depths (139.76 → 130.25 m) using the same f and
  θ gives a vertical displacement of only -0.03 m/s. Its flight comes out level and its speed is 11.5 m/s, which is
  plausible for an eagle. This confirms the tilt/focal pair.
- Person: the given distances barely change (139.95 → 139.98 m), but the body clearly moves, so the character's
  origin does not follow it. I did not use those distances for the motion. The body moves 32 px/s in the image
  plane, which is 0.71 m/s at f = 6333. Its apparent size shrinks by 0.86 %/s, so its depth grows by about 1.2 m/s.
  That gives about 1.4 m/s against the prior of 1.3 m/s, within the noise of the size trend.
  - Using the 1.3 m/s prior alone, with all motion across the view, would give f ≈ 3480 px. That makes the person
    3.1 m tall, so I rejected it.
  - The person's image path is not consistent with walking on flat ground (the beach probably slopes), so the
    person's speed was not used to set the scale.

Confidence: moderate to high, roughly ±5 %. The radial part of the speed is exact. The lateral part (≈2.0 m/s)
depends on the assumed person height of 1.75 ± 0.05 m.
