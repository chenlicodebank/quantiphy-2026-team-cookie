Prior speed 22.16 m/s + the two given depths fix the 3D flight line (perpendicular distance d=56.12 m, lam0=63.81 m, r=84.98/93.6/102.67/121.83/141.0 m at frames 0/12/24/48/71). Fitting the SAM silhouette-centroid track to a constant-velocity pinhole model with those depths gives f=3390 px (validated: frames 12 and 71 predicted to 2 px; an independent image-speed route gives 3448 px). The jet's nose-to-tail pixel extent (SAM masks, PCA major axis) is 663/621/581/510/455 px, i.e. 16.6-18.9 m perpendicular to the line of sight. Correcting for the body-axis tilt (the LOS rotates 17.8 deg over the clip while the extent grows 14%) gives one consistent length at theta0=58.9 deg: L = 19.40, 19.18, 19.11, 19.17, 19.42 m (mean 19.26, std 0.13). Second route with f=3200/3600 px gives 20.4/18.1 m, so 19.3 +/- 1.2 m; a 19.3 m jet with ~13 m span is a realistic fighter size.

Final message:
I measured the plane's length as **19.3 m**.

**Method summary:**
1. **Scale from the prior/depth_info only**: speed 22.16 m/s plus the two camera distances (102.67 m at t=1, 121.83 m at t=2) fix the straight flight line — perpendicular distance from camera to path d = 56.12 m, and r(t) = 85.0 → 141.0 m over the clip.
2. **Focal length**: fitting the SAM silhouette-centroid track to a constant-velocity pinhole model with those depths gives f = 3390 px (41.4° hfov). Validated by predicting frames 12 and 71 to within 2 px, and cross-checked with an independent image-speed route (f = 3448 px).
3. **Size**: SAM masks at 5 frames give nose-to-tail pixel extents of 663 → 455 px, i.e. 16.6–18.9 m perpendicular to the line of sight.
4. **Tilt correction**: the extent grows 14% while the line of sight rotates 17.8°, which collapses to a single consistent length at a body-axis angle of 58.9°: L = 19.40, 19.18, 19.11, 19.17, 19.42 m (mean 19.26, σ 0.13).
5. **Check**: 19.3 m long with an implied ~13 m span matches a real fighter jet (F-15: 19.4 × 13.1 m), satisfying the standard-object plausibility rule.
