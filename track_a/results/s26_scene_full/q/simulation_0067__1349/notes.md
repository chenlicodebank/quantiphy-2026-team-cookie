# Q1349 — width of the white car (the white cargo van), metres

Answer: **2.02 m** (body width across the rear, corner to corner; mirrors not included).

The file is 24 fps and question_fps is also 24, so frame = round(t*24): t=0.58 → frame 14, t=1.58 → frame 38.

## Camera (3D scene, static camera)
- **Focal length.** I fitted lines to 6 vertical poles on the clean background (`poles.py`, `vp2.py`). They meet
  at a vertical vanishing point of about (1064, 2644). The road vanishing points give a horizon at y ≈ -45. Together
  these give f = sqrt((cy − y_h)(y_v − cy)) ≈ 1090–1125 px. The two road directions, assumed to be at right angles,
  give f ≈ 1107. I used **f = 1100 px**, principal point at the image centre, no roll.
- **Pitch.** The pitch comes from the horizon (y = −45). I checked it on the van's own track (`accelcheck.py`): with
  this horizon the motion is constant-acceleration from rest at t ≈ 0. Horizons of −25 and −65 break this.
- **Camera height.** From the pedestrian (pelvis depth from depth_info, feet on the ground; `hc.py`) the camera is
  about 7.1 m above the ground, and the pelvis height comes out at about 0.9 m, which is plausible.

## Width measurement (`tltrack.py`, `width.py`, `heading.py`)
- **Rear corners.** The left-rear corner is the outer edge of the left taillight. The right-rear corner is the right
  edge of the van's silhouette at taillight height (`masks.py` hulls). I measured them at frames 30, 38 and 46.
- **Heading.** I tracked the lower left taillight, which stays at a fixed height, over frames 22–50 and projected it
  to a top view. The path is a straight line (lateral rms ≈ 0) with heading −37.3°.
- **Width in model units.** Each rear corner is a vertical edge, so in the top view it lies along a known direction
  from the camera. Requiring the line between the two corners to be perpendicular to the heading gives the width in
  units of (camera height − taillight height): 0.369, 0.359 and 0.349 at frames 30, 38 and 46.
- **Scale from the prior (main route).** The same taillight track gives the acceleration in those units: 0.720
  units/s². The prior of 4 m/s² then sets 1 unit = 5.556 m, so **W = 0.359 × 5.556 = 2.00 m**.
- **Sensitivity to focal length.** For f from 1050 to 1150 px, W ranges from 2.12 to 1.89 m.

## Second route (depth_info) and the disagreement
- **Origin at the box centre does not fit.** I solved for the scale and the origin's offset from the rear so that
  the given van depths (10.624 m at frame 14, 12.810 m at frame 38) are reproduced (`depthscale.py`,
  `originfit.py`). With the origin at the box centre, every f gives impossible geometry (negative offset from the
  rear, or a taillight near the ground).
- **Origin at ground level fits.** At f = 1100 the solution puts the origin 1.24 m ahead of the rear, which is about
  the rear axle of a Chevy Express. The taillight height comes out at 1.11 m. This gives W = 2.15 m, but the implied
  acceleration is 4.32 m/s², not 4.
- **The two scales are about 7–8% apart.** I did not find the cause. The record's simple ground-plane track of the
  van also gave acceleration between 4 and 4.5 m/s² at f ≈ 1100.

## Answer and confidence
- I answered between the two routes, weighted toward the prior route: **2.02 m**. The prior is exact and that route
  does not depend on where the van's origin is.
- As a sanity check only, a real Chevy Express is about 2.01 m wide without mirrors.
- The reading of "width": I measured the body width (the guidance says a car's width runs wheel to wheel). If the
  reference box includes the side mirrors, the true value could be about 2.3–2.4 m.
- Confidence: moderate, roughly ±8%.

## Record corrections
- The record's van bounding-box centre is a poor stand-in for the origin. It is clipped by the image edge up to
  frame 14 and shifted by perspective, so I used rear-corner features instead.
- The record's focal estimate of about 1100 px is confirmed by 6 pole lines.
