# q 3144: height of the trash bin (m)

Prior: the scooter rider's average speed is 4.46 m/s. The video is internet footage at 30 fps (question_fps = file fps = 30, so no re-timing). The camera is static (drift ≤ 2 px).

## Scale (speed.py)
I took the mean per-frame horizontal step of the rider/scooter from scene/tracks/rider_scooter.csv:
- rear wheel, frames 0-80: 18.11 px/f, i.e. 543 px/s (544 after subtracting the camera drift)
- scooter centre, frames 0-73: 18.24 px/f, i.e. 547 px/s
- upper-body template track, frames 0-74: 18.19 px/f, i.e. 546 px/s
- I used about 546 px/s, so scale = 4.46 / 546 = 0.00817 m/px. Following the benchmark convention, this one scale is used for everything.

## Bin height (bin_measure.py)
This is the tan/terracotta cylindrical bin at the far left, x about 37-167. I took column profiles at x = 60..140 in frames 0, 20, 40, 60 and 80:
- Top rim, where the green screen changes to brown: the colour change spans y 570-578 and its midpoint is y ≈ 574 (detector gives 571-576).
- Bottom, at the bin base / ground contact: the brown runs down to y ≈ 697, and the dark contact band at 698-704 sits on the asphalt, which starts at 706. I take the base at y ≈ 700.
- Pixel height is ≈ 126 px (plausible range 124-130). The scene record says 125 px, which agrees.

Height = 126 × 0.00817 ≈ **1.03 m** (range 1.01-1.06).

## Checks
- The three speed tracks agree within 1%, and the bin height is stable across 5 frames within ±1-2 px.
- Sanity: the bin stands next to the fence, behind the rider's path. With this single scale the rider would come out at about 2.5 m tall, so this real-world check fails. The prior's speed is probably high for the rider's pixel motion, or the depths differ. The benchmark convention, though, is one planar scale from the prior, so I answer with that scale.
- Confidence: moderate. The pixel measurements are good to about 2%. The main risk is how the annotators measured the pixel speed.
