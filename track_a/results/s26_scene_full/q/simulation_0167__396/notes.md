# Q396 – length of the bike (m); prior: bike speed = 5.52 m/s

Top-down 2D render, 24 fps (file fps = question fps), static camera. The bike (delivery cyclist) rides along +x in the lower lane.

## Scale (from prior)
- Cyclist pelvis track (scene/tracks/cyclist.csv, checked): linear-fit slope 14.415 px/frame, mean per-frame step 14.44,
  net 14.42 px/frame over 79 frames -> 346 px/s (`speed.py`).
- m/px = 5.52 / (14.42 x 24) = 0.01595 m/px.
- Sanity checks: lane 194.5 px -> 3.10 m; police car 289 px -> 4.61 m. Both plausible.

## Bike pixel length (rear-tyre tip to front tip)
- Background-difference row profiles along the bike axis (`extent2.py`), frames 10-19: 105-109 px. The front end sometimes picks up shadow.
- Visual checks on 5x crops with the endpoints marked (`view2.py`): frame 3 ≈104-105, frame 15 ≈105, frame 18 (bike under the image centre) ≈104.5,
  frame 40 ≈105, frame 50 ≈109, frame 72 ≈116.
- The apparent length grows toward the right edge because of perspective: the tall front (crate/rider) is pushed radially outward.
  That gives ≈12 px over ≈980 px of travel, the same ratio as the car's roof-vs-bumper shift in the record (16 px over 1425 px).
  So the undistorted value is the one near the nadir (x≈960, frames 15-19), ≈105 px (±3).
- The magnification from the height of the speed reference point vs. the bike ends is ~1% (camera height ≈85x the 1 m height difference), so it is negligible.

## Answer
105 px x 0.01595 m/px = 1.675 m -> **1.68 m**.
Second route: the frame-40 and frame-3 crops give the same 104-106 px, i.e. 1.66-1.69 m. A typical bicycle is 1.7-1.8 m long, which is plausible.
Confidence: moderate-high (±4%). The main uncertainty is where the dark rear tyre ends on the dark asphalt.
