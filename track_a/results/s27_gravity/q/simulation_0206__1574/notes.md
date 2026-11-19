# q_1574 — length of the table (desk), metres

The file rate and question_fps are both 24. The camera is static and the principal point is assumed to be at the image centre (1062, 540).

## Image points (frame 0, read on contrast-enhanced zooms: crops*.py)
- Desk-top outer corners: near front-left N (700, 878); front-right FR (1997, 653); back-right BR (≈1590, 528; partly hidden behind the phone and brass stand, cross-checked by intersecting the back-edge and right-edge lines, giving ≈1577, 527); back-left BL (471, 688).
- Gun centre: (1430, 627). Typewriter at t = 0 (frame 0): (1243.5, 49). At t = 0.5 (frame 12): (1234, 608.5), from scene/tracks.

## Focal length and tilt (two independent routes)
1. **Free fall** (fall.py): I fitted a pinhole model with g = 9.8 m/s² straight down, the depth of 4.32 m at t = 0, and the bbox centre in frames 2-9. Result: f = 2787 px, pitch 12.7°, release time t0 = 0.00 s, residual 2.1 px rms. With the pitch fixed anywhere from 10° to 15°, f comes out between 2730 and 2840. Tracking the top edge instead gives 2520 and the bottom edge 3030; they bracket the centre value because the box rotates as it falls.
2. **Desk plane** (grid.py, sens.py): the desk plane passes through N at 3.593 m. I required the gun (4.704 m) to sit about 2 cm above that plane and the desk-top corner to be a right angle. Result: f ≈ 2800, pitch ≈ 13.1°. This agrees with route 1.
   - Checks, all consistent: the typewriter origin at t = 0.5 (4.501 m) comes out 9.5 cm above the desk, which is plausible for its centre. The fall from frame 0 to frame 12 is 0.89 m, so it would land at about 0.426 s, between frames 10 and 11 as the video shows.

The joint fit (joint.py) gives f = 2790, pitch 13.06°, all residuals ≈ 0, and length (N→FR, front edge) **2.27 m**, width (front-to-back) 0.99 m, corner angle 90.1°.

## Sensitivity
- Corner pixels ±3 px change the length by ±0.015 m.
- Changing f by ±160 px changes the length to between 2.17 and 2.37 m.
- Changing the gun's height above the desk from 0 to 4 cm gives 2.21 to 2.32 m.

## Inconsistency (not resolved)
The given `distance_desktop_corner_far_right_camera = 5.009 m` does not fit the solution. On the fitted plane the back-right corner is at 5.58 m and the front-right corner at 4.84 m. Forcing the fit to honour 5.009 needs a pitch of about 15-16° and f about 3000-3070. That leaves the gun 4-5 cm below the desk surface, breaks the right angle, and makes the landing too early, while giving a length of about 1.96-2.05 m. I trust the four mutually consistent constraints (fall, gun, typewriter at rest, right angle) and treat the 5.009 value as referring to some other bounding-box point.

The objects look 15-25% larger than typical real ones at this scale (a 0.49 m lamp, a 0.45 m typewriter); the scale was nevertheless taken from the exact prior and the given depths.

**Answer: 2.25 m.** Confidence is moderate, with an uncertainty of about ±0.1 m; the alternative reading would give about 2.0 m.
