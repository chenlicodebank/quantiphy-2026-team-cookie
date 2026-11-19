# q_1739: boat length (m)

The prior is boat speed = 4 m/s. The time base is question_fps = 24. The file runs at 25 fps and repeats one frame every 25 (frames 1, 26 and 51), so there are 72 unique frames, each one 1/24 s render step.

## Method
- **Boat motion.** The template-matched track in scene/tracks/boat.csv gives a straight path. The boat moves 596.1 px in 71 render steps, or 8.396 px/step (201.5 px/s). The x component is 8.08 px/step (194.4 px/s).
- **Scale.** The prior speed and the given depths at t = 1 s and t = 2 s give a focal length of f = 9070 px (HFOV 9.7 deg) by solving |P(2 s) - P(1 s)| = 4 m (geom.py). The velocity in camera coordinates is (-3.80, -1.01, +0.73) m/s.
- **Camera tilt.** The camera looks down at about 54 deg, assuming the boat moves horizontally and the camera has no roll. The mast appears vertical in the image, which supports zero roll.
- **Length by the ratio method.** The boat's long axis is parallel to its velocity, so length = 4 m/s x (pixel extent along the motion) / (pixel speed). Foreshortening cancels in this ratio.
- **Why the image-x extent.** The mask extent along the image motion direction is 507 px (measure_len.py). That value is inflated because lower hull points appear further aft, since the motion direction has an image-y component. World vertical projects onto image y only, so I used the image-x extent with the x speed instead.
  - Bounding-box width of the mask is 476 px (bow tip at the sheer to the aft bulge of the stern hull).
  - The x speed is 194.4 px/s.
  - L = 4 x 476.2 / 194.4 = **9.80 m** (xratio.py).
  - By window: frames 0-25 give 9.76, frames 25-50 give 9.85, and frames 50-65 give 9.78.
- **Gunwale-only reading.** Measured from the bow tip (413, 1288) to the stern gunwale (882.5, ~1442) at frame 12 instead, the length is about 9.66 m. The dark rounded stern hull sticks out about 9 px further aft, and it belongs in the bounding box, so I answer with the full extent.

## Checks
- The focal length gives about 50 px/m at the boat. The person (mask about 60 px long, seen from about 54 deg above) comes out roughly 1.8 m tall, and walks at about 1.2 m/s. Both are plausible, so the scale holds.
- A 9.8 m fishing boat is a realistic size.
- The plain motion-direction projection gives 10.06 m, which is the upper bound inflated by the vertical offset.

Confidence: good, about ±3%.
