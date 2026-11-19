# q1774 — width of the green car (simulation_0066_segmented)

The file and the question both run at 24 fps (t = 0.58 s is frame 14; t = 1.58 s is frame 38).
The green car is a static teal sedan (BMW E34-like), far right at x 1440–1625, y 334–414. It has no depth given,
so its scale has to come from a reconstructed camera.

## Camera (3D pinhole, cx, cy = image centre)
- **Focal length.** Features on the white van (KLT, 60 points, frames 4–64) were fitted as a rigid body moving in pure
  translation with a = 4 m/s² (the prior). The start time was free; the best fit is about frame −0.5, reprojection rms 1.39 px.
  - This gives the 3D feature cloud for any f. The centre of the cloud (mid-range of the features) must sit at the given
    van distances, 23.59 m at frame 14 and 19.99 m at frame 38.
  - The 14 → 38 pair matches at f ≈ 1000–1060 if the origin is the box centre, or 965–1020 if it is the bottom centre.
  - **Result: f ≈ 1010 ± 50 px.**
  - Earlier routes agree. The simple origin-displacement method (van at rest at frame 1) gives f ≈ 980. The pedestrian
    then measures 1.68 m at most while walking, which is plausible.
- **Pitch.** The van's focus of expansion is at about (615, 75), which puts the horizon at row about 75. Pitch ≈ 24.7°.
- **Roll.** Roll is 0. Roll ≠ 0 (suggested by the van wheel-rim ellipses) makes the camera-height estimates from the
  pedestrian and the cyclist disagree badly (7.6–8.1 vs 6.0 m) and gives absurd car sizes. With roll 0 they agree.
- **Camera height.** Hc ≈ 6.35 m, from the pedestrian's pelvis depth plus foot row, and the cyclist's origin plus wheel
  contact (4 estimates, 6.2–6.6).

## Green car
- **Route 1: 3D box fit.** The box sits on the ground plane and was fitted to:
  - the near-side wheel contacts (1514, 414) and (1592, 398.5);
  - the leftmost silhouette point (1440, 384), the far front corner at headlight height;
  - the rightmost point (1625, 365), the rear near corner;
  - the roof top row 334;
  - the slope of the front lamp band.

  At f = 1010 this gives L 4.19, W 1.44, H 1.38 m. The overlay (frames/overlay_1.44.png) matches the front-face direction.
  Varying the assumptions (corner heights, overhangs, f 960–1060) gives W 1.31–1.58.
  The box W is the body width at the rounded front corner, so it is a slight underestimate.
- **Route 2: wheelbase.** The wheelbase from the two ground contacts is 2.39 m. Typical E34 proportions then give a body
  width of about 1.51 m, and about 1.70 m including mirrors (mirror span / wheelbase ≈ 0.71).
- **Mirrors.** The asked size is the world-space bounding box, which includes the side mirrors (a near-side mirror is
  visible at the A-pillar). Body only: about 1.50 m. Including mirrors: about 1.68 m.

## Answer
**1.62 m.** This weights the mirror-inclusive bounding box (about 1.68) above the body-only width (about 1.50).

Confidence: moderate, about ±10%. The answer is dominated by uncertainty in the focal length and the pitch, and by
whether the mirrors count.
