# q_1627: length of the rabbit (m)

File fps = question_fps = 24, so frame numbers and times line up directly.

## Focal length from the prior (solve_f.py)
I fitted the brown horse's image position linearly over frames 0-48, leaving out the loop reset at frame 49. I then
back-projected it at t=0 (16.288 m) and t=1 s (16.112 m), using a pinhole model with the principal point at the image
centre, and solved for the f that makes |P1-P0| = 0.874 m (the prior speed is constant):
- torso centroid: f = 2605 px
- mask centroid: f = 2553 px
- bbox bottom: f = 2555 px
- adopted f ≈ 2580 px (horizontal FOV ≈ 41 degrees)

Checks: the brown horse comes out 2.05 m long by 1.62 m tall, and the cream horse 2.45 m by 1.65 m. These are
plausible horse sizes (seen from above), so the scale is consistent.

## Rabbit length (rabbit_len.py, rabbit_crops.py)
- I checked the scene/ rabbit bboxes on 12 frames. They fit the rabbit well, with occasional hind-foot extension
  (e.g. frame 24, w=105).
- bbox_w (nose to tail): median 85.5 px, mean 87.2 px, IQR 83-90 px. The notes say the trailing hind-foot tips are
  sometimes cut off (about 5 px short).
- The rabbit's 3D motion direction, from its given depths (14.257 m at 0 s, 14.412 m at 1 s) and its image track, is
  almost exactly along the camera x axis. So its side-on image width maps straight to its length. Its speed comes out
  about 1.48 m/s, which is plausible for a hopping rabbit.
- Length across the frames: f=2550 gives 0.473 m (median) / 0.484 m (mean); f=2600 gives 0.465 / 0.475 m;
  f=2450 gives 0.49 / 0.50 m.
- Answer: **0.48 m**. This is between the median and the mean, allowing a little for the missed foot tips.

## Confidence
Moderate to good, about ±7 %. The main uncertainties are f (±2 %) and which pose or frame the reference AABB uses
(the rabbit's stretch while hopping changes its length by about ±10 %).
