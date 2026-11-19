# Q1194: height of the moving bicycle (handlebar top to the bottom of the wheel)

Answer: **1.60 m**

## Setup
- 3D Blender render, 1920x766 px. The file and the question both run at 33 fps, so t=1 s is frame 33 and t=2 s is frame 66.
- Prior: the walker is 1.8 m tall. The depths are given to the bike and to the walker at t=1 and t=2.
- The camera is static. The principal point is taken as the image centre (960, 383).
- Pitch comes from the vertical vanishing point. Building, plank and kiosk edges give a vertical VP at about
  y≈8500 (verticals.py, verticals2.py). That is a small down-pitch of about 8°. I also tested VP values of 6500 and 11000.
- Model (model.py): full pinhole geometry. Each object's origin is back-projected with its given distance. Image rays
  for the top and bottom points are intersected with the world-vertical line through that origin. Off-axis angles are
  large here (about 25° for the walker and about 33° for the bike), so this matters.

## Focal length (walker)
- I used the walker's head-top to lowest-foot pixel heights at manual keyframes 21–77 from scene/tracks/walker.csv.
  I spot-checked them on crops at f33 (≈198 px) and f66 (≈212 px).
- The walker's distance is interpolated linearly between the two given values.
- Result: f ≈ 1164 px if the walking height is 1.80 m, and 1181 px if it is 1.78 m (sd 27 px, over the gait cycle).

## Bike pixel extent (my own crops, crop.py)
| frame | handlebar/grip top y | front-tyre bottom y | extent |
|---|---|---|---|
| 31 | 416 | 549.5 | 133.5 px |
| 33 | 425 | 560.5 | 135.5 px |
| 35 | 432 | 574.5 | 142.5 px |
| 37 | 440 | 585.5 | 145 px |

- I multiplied each extent by the bike distance, interpolated linearly. The product averages about 1.8% above the
  value from f33 alone.
- I tried automatic detection of the tyre bottom (wheel.py), but the cast shadow made it too noisy.

## Bike height
The given distance is to the bike origin, but the handlebar and front-wheel contact are nearer the camera than that
origin. The offset δ is the distance from the origin forward to those front features:
- **Evidence for δ.** I fitted 1/height (head to ground) over frames 0–60 in a straight line. It gives a size ratio
  t2/t1 of about 1.425, while the given depths imply 1.398 after the cos correction. That points to δ≈0.65 m.
- **Results (Vy 8500).** Height H by walker height and δ:

| walker height | δ=0 | δ=0.4 | δ=0.65 |
|---|---|---|---|
| 1.80 m | 1.64 m | 1.60 m | 1.57 m |
| 1.78 m | 1.62 m | 1.58 m | 1.56 m |

- **Other frames.** The average over f31–37 adds about +1.8%.
- **Final:** about 1.60 m. The plausible range is 1.55–1.66.

## Consistency warning (checked, not used)
The visual ground plane does not match the depths:
- On the walker's ground plane, the bike's wheel contact would be only about 10.4 m from the camera, against a given 16.49 m.
- On that plane the handlebar would be at about 1.0 m, a normal real bike.
- The given depths, though, change by 4.56 m in 1 s. That cannot come from a fixed offset of the origin, because the
  bike's visible motion on that plane is only about 3.1 m.

So the cyclist asset is effectively about 1.55x larger and farther away than the walker. The pinhole relation with
the given bike depth and the walker-derived focal length is what sets the answer.

Confidence: moderate (about ±5%).
