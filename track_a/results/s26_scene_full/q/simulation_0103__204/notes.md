# q_204 — boat length (m), prior: shark acceleration = 1 m/s^2

2D side-view render, static camera, 24 fps (file rate = question rate, so no re-timing).

Scale from the prior (measure.py):
- Shark x position tracked by subpixel template matching of the shark's front body. The template is taken from frame 27 and is independent of the record. Quadratic fits of x(t):
  - frames 2–53: a = 87.04 px/s^2
  - frames 2–27: 86.67
  - frames 27–53: 88.33
  - frames 5–50: 86.80
  - The fit residuals are about 0.12 px rms, so the acceleration is uniform.
- Second route: a fit to the record's mask-centroid track gives 87.46 px/s^2 for frames 2–53.
- Adopted a = 87.0 px/s^2, so the scale is 1/87.0 m/px = 0.01149 m/px.

Boat length: the stern-to-bow horizontal extent is 858 px (record, frames 21–53). I checked it visually on frame 53, where the stern is at x ≈ 594 and the bow tip at x ≈ 1452. The rudder is included because it lies inside that span.

Length = 858 / 87.0 = 9.86 m.

Sanity check: the shark's length of 260 px gives 3.0 m, which is plausible. A 9.9 m fishing boat is also plausible.

Caveat: the boat (at the surface) and the shark (underwater) could in principle be at different depths. The scene is 2D, so one scale is used. Confidence: good, about ±3%.
