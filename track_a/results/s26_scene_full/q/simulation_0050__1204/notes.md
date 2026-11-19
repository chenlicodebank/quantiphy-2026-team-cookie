# q1204 — width of the telephone booth (m)  → answer 1.17 m

Prior: walking person's speed = 1.236 m/s. Depths: bike 11.896 m (t=1 s), 14.642 m (t=2 s); human 15.865 m (t=1 s), 16.671 m (t=2 s).
The file and the question both use 33 fps, so t=1 s is frame 33 and t=2 s is frame 66. The camera is static.

## Camera calibration (from image geometry alone)
- **Vertical direction:** 25+ vertical edges (buildings, booth, pillars) traced with sub-pixel precision (m8). Their slopes change linearly with x, so they converge on a zenith vanishing point at about (630, −24585).
- **Booth front face / street:** 4 horizontal booth edges give a vanishing point at (−2734, 569) (m17, m18). The traced curb-top and curb-bottom lines (m13, m19) pass through the same point (571.9 / 571.5). So the booth front is parallel to the street.
- **Booth side face:** 4 edges give a vanishing point at (1887, 505).
- **Result:** the orthocentre of the three vanishing points lands at (978, 383), i.e. the image centre, with **f ≈ 1830–1850 px**. Each pair of vanishing points with a centred principal point gives f = 1831 / 1844 / 1851. I used f = 1840 and c = (960, 383), and also tried (1830, 978.5, 383).

## Metric model (m20)
- **Road height:** the bike depths plus its wheel-contact pixels give the camera height above the road: 1.109 / 1.103 m at t=1 / t=2 (they agree).
- **Curb:** the curb bottom edge back-projected onto the road plane runs parallel to the street (0.6°). Fitting the curb-top line gives a curb height of 0.14 m.
- **Sidewalk:** its plane sits 0.967 m below the camera.
- **Check against the prior:** the walker's feet placed on the sidewalk give a path 0.61 m behind the curb at both t=1 and t=2 (so he walks parallel to it). His speed (m25) is 1.213 m/s from the t=1→t=2 displacement and 1.21–1.22 m/s from a fit over frames 0–98, against the 1.236 m/s prior (−1.5%). This is independent of the human depth_info. At f=1800 it gives 1.23–1.25 m/s.
- **Conflict:** the human depth_info (15.9 / 16.7 m) does NOT fit the image geometry; the walker is at about 12.4 m. It would need f≈3015 with a principal point shifted about 170 px. That alternative breaks the vertical-edge convergence, makes the booth's faces meet at 68° instead of 90°, and puts the sidewalk below the road. So I left the human depths out. The bike depths and the speed prior agree with each other within 2%.

## Booth (m22–m26)
Booth body edges, traced in code: left x = 153.29 − 0.0198·y, corner x = 240.66 − 0.0166·y, right x = 339.08 − 0.0135·y (scatter about 0.1 px).

- **Corner position:** the corner's ground contact (230.0, 640.5) is placed on the sidewalk plane. It sits right at the curb edge (setback about 0.01 m) and 17.2 m from the camera.
- **Face widths:** each face is measured by solving for the edge x-positions along the street direction and across it. This avoids back-projecting on a grazing plane.
- **Booth height:** about 3.0 m.

Results at f=1840 (cyclist-depth scale):

| part | along the street (front face) | across the street (side face) |
|---|---|---|
| body | 1.107 m (the same at 25 / 50 / 75 % of the height) | 1.157 m |
| roof (outermost: x = 145 / 237.4 / 338) | 1.160 m | 1.177 m |
| plinth | 1.130 m | 1.208 m |

- **Rescaled to the speed prior (×1.019):** roof 1.18 along × 1.20 across.
- **Sensitivity:** f from 1800 to 1880 changes the result by ±0.6%. Moving the base row by 1 px changes it by ±0.9%. Moving the roof corner by 0.5 px changes it by ±0.5%.

## Answer
The bounding-box width is the shorter horizontal extent. That is the extent along the street (the front face), including the roof overhang. It is 1.16 m on the cyclist-depth scale and 1.18 m on the speed-prior scale, so I answer **1.17 m**.

- Other reading: the body without the roof is 1.11 m wide; the side extent is 1.18–1.21 m.
- The two horizontal extents differ by only about 3%, so whichever is called "width", the answer stays within about 4%.

**Confidence:** moderate. The scale is consistent to about 2% between two independent inputs (bike depths and walker speed). The main risk is the inconsistent human depth_info, in case the reference used it.
