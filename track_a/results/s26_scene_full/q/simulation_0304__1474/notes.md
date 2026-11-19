# q1474: whale length (m). Answer: 20.1 m

Inputs: speed prior 1.67 m/s; depth_info is the range to the origin, 33.7307 m at t=1 s (frame 24) and 35.1624 m at t=2 s (frame 48).
question_fps = file fps = 24. Static camera, 3D render, one whale swimming away from the camera (up-left in the image, shrinking).

## Geometry
- With a straight path at |V| = 1.67 m/s, the two ranges give the origin's position along its path (s1 = 28.70 m at t=1)
  and the perpendicular distance from the camera to that path, D = 17.73 m. The velocity is about 31.7 deg from the line of sight.
- Head track (`ecc_track.py head`): an affine ECC fit of the head patch, referenced to frame 24, with sub-pixel accuracy (cc > 0.98 for frames 0-54).
  The head moves along -148 deg at 75.4 px/s. Across the motion line the patch scales by s; along it, by s^2.
  This is the signature of a body lying along its own direction of motion as it recedes, which confirms that the whale's axis is parallel to V.
- The image of the axis line is fixed, and it passes through the vanishing point vp of V, which lies on the head's motion line.
  For any point on that line, (image distance a to vp) x (Z / Vz) = K, a constant.
  So **L = |V| (tau_tail - tau_snout) = |V| K (1/a_snout - 1/a_tail)**. This does not depend on the focal length.
- To fix vp, I scanned r = |head - vp| (`scan_vp*.py`). For each r, the head's tau = r / 75.4 px/s, and the focal length f comes from the
  depth/speed geometry. The scan reports where the origin then falls on the body.
  - Solutions exist only for r >= 1880.
  - With the origin at mid-body (fraction 0.5 from the snout), r = 2050, vp = (-638, -606), f = 3833 px (hfov 37 deg), and the origin
    is at pixel (1362, 643) at t=1. That lies on the torso, which is plausible.
  - The head's looming rate alone suggested r of about 1600 (tau 21 s). That is slightly inconsistent with the depth info, probably
    because the head pitches. The constrained value was used.
- Ends of the whale:
  - Snout = the mask point nearest vp along the line.
  - Rear end = the **mean projection of the two fluke-lobe tips**. One lobe tip lies almost on the image axis line, so using the
    farthest mask point would mistake its sideways offset for depth and inflate L by about 2 m (max-tip values were 21-22.5 m).
  - Frames used: 0-7 and 39-54, where the tail is not clipped by the image edge.

## Results (`scan_vp3.py`), L in m for frames 0, 4, 7, 39, 42, 45, 48, 51, 54
- r = 2050 (origin at mid-body): 19.7 19.9 20.1 20.6 20.5 20.3 20.1 19.7 19.3. The mean is about 20.0; the variation comes from the tail stroke bending the body.
- r = 1950 / 2150 (origin at 0.31 / 0.65 of the length): means about 19.8 / 20.2.
- Over the whole feasible range r = 1880-2300, L = 19.1-21.2. The result is insensitive to the unknown origin location.

## Check by a second route
I ignored the depth constraint and used only the head's own looming (vp = (-270, -375), tau = 21.4 s) with the max-tip ends.
That gives 19.7-21.0 m; with the mean-of-tips ends it would be about 1.5 m lower, around 18.4 m. Given the head-pitch bias, that is broadly consistent.

## Confidence
Moderate, about ±8%. The main uncertainties are:
- whether the snout and the fluke tips sit at the same offset from the origin's path (each metre of difference changes L by about 1.7 m);
- the world-AABB convention for "length", assumed here to equal the extent along the body axis with the whale horizontal;
- tail bending (±0.6 m across frames).

The scene/ record covered the right object. Its head-scale track is coarser (steps of 0.005); I replaced it with the ECC track.
