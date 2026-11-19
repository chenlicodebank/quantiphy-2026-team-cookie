# q_658: width of the white sofa (m)

Prior: vacuum diameter = 0.438 m. No depth_info. fps 24 = question_fps, so no retiming question arises.
Camera: static and looking straight down at the room. Floor objects lie in a plane facing the camera, so one scale applies.

## Reading of "width"
The sofa is a large curved (kidney-shaped) sofa whose long side runs along image x. Width = the shorter horizontal
extent of its world AABB = its extent along image y (front to back, from the arm tops to the bulge of the back).
Its length (x extent, 566 to 1451 px, about 885 px) would be about 3.1-3.2 m.

## Measurements (frame 0, scripts edges.py, larm.py, probe.py)
- Bottom edge (outer bulge of the back, dark carpet below it): the largest edge on column profiles, max y = 1058 px at x of about 960-1050.
- Top edge (arm tops): right arm 577.5 px at x 1340-1350 (clear edge against shaded carpet). Left arm about 580 px (sunlit; checked on a 4x crop, larm2.png).
- Pixel y extent = 1058 - 577.5 = 480.5 px (edge midpoints, the same convention as the vacuum rim fit).
- Vacuum diameter (scene track, outer rim circle fit, checked): it grows with distance r from the image centre,
  d = 119.74 + 0.0043 r px (residual 0.25 px). This is perspective of the disc's side wall, which gives
  h_vac/H of about 0.004-0.009 (camera height H of about 13-26 scene-metres if the vacuum is about 0.11 m tall).
  The diameter on the optical axis is 119.74 px, so the scale is 0.438/119.74 = 3.658 mm/px at the vacuum's top height.

## Scale and perspective
- Uncorrected: 480.5 x 0.438 / 119.74 = 1.757 m. Using the vacuum's diameter near the sofa (about 121 px) instead gives 1.739 m.
- Silhouette correction: the sofa's outer bulge sits at a height of about 0.4-0.75 m, while the vacuum rim is at about 0.1 m.
  The bottom edge is 518 px from the image centre and the top edge only 37 px, so the correction factor is
  (H - z_sofa)/(H - h_vac), which is 0.970-0.985. That gives a width of 1.70-1.73 m.
- Answer: 1.72 m (camera height about 18, silhouette height about 0.5 m).

## Second route
- The scene record's loose bbox for the sofa (y 578 to 1060, 482 px) agrees with my code-measured 480.5 px.
- The two arms (577.5 and about 580) give the same top edge. The bottom-edge profile is smooth and peaks at 1057.5-1058.5 over x 940-1050.
- The result does not depend much on which vacuum diameter is used (119.7 to 121 px changes it by about 1%).

Confidence: moderate-high under the AABB reading (±3%). The main uncertainty is the camera height used in the perspective correction.
