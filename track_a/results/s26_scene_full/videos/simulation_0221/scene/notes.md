# simulation_0221: measurement notes

**Scene.** A 2D simulation render of a living room seen straight from above (top-down), 1920x1080, 24 fps, 80 frames (0 to 3.2917 s).
The camera is static: phase correlation between frames 0 and 79 on the furniture gives a shift under 0.07 px.
The only moving object is a **white round robot vacuum**. At frame 0 it sits docked against its white charging dock on the
right wall at (1673.5, 423.2) px. It drives left, at first slightly up, and stops in front of the curved sofa at (649.8, 500.6) px.
Everything else is static. Because all the motion is on the floor plane facing the camera, use one m/px scale taken from the
prior object, for example the vacuum diameter of about 121-123 px.

## Files
- `scene.json`: inventory (moving and static objects with pixel boxes and sizes), events, camera, vacuum summary.
- `tracks/robot_vacuum.csv`: one row per frame, 0-79. `x_px, y_px` is the reference point: the centre of a circle fitted
  to the disc's outer rim, which is the object's origin seen from above. `diameter_px` is the fitted diameter. The bbox comes
  from the circle. `mask_len_px = mask_wid_px = diameter` because the object is a disc. `fit_inlier_frac` and
  `fit_resid_px` are the fit-quality figures. `rough_*` is the centroid of the first threshold mask, which is less accurate
  and kept only for reference. `occluded` is 0 in every frame.
- `scripts/`: `bg.py` builds the median background and checks the camera. `track.py` makes the rough threshold mask.
  `track2.py` does the circle fit: 180 rays, the outermost strong edge on each, a least-squares circle and outlier
  rejection. `finalize.py` writes the CSV and prints the per-frame steps and headings. `static.py` gives rough static
  extents. `montage.py` builds the checking images.

## Vacuum motion (pixels; no speeds fitted)
- At rest at frame 0. Starts moving at frame 1 (0.5 px step). It accelerates smoothly to a step of about 20.6 px/frame at
  frame 26.
- It slows to about 15.2 px/frame at frame 39. Frame 39 is also the top of its path: the heading turns from up-left
  (about -167 to -179 deg) to down-left (about +178 to +147 deg).
- It speeds up again to about 23.1 px/frame at frame 50, then slows to a stop at frame 69. From frame 70 on it does not
  move (under 0.1 px per frame).
- Path length is 1053.8 px. Net displacement is 1026.7 px. The vacuum does not rotate visibly: the seam line on its top
  stays vertical on its right side.
- Its apparent diameter is 122.9 px near the dock (x about 1670) and 120.4-120.9 px at x of 650-1100. This 1.5% change is
  a perspective or side-wall effect. Height cannot be seen in a top-down view.

## Reliability
- Vacuum centre: about ±0.3 px. The circle fit was checked visually on overlays every 8 frames; inlier fraction is
  0.77-1.0 and residuals are under 1 px.
- In the sunlit patch (frames about 33-79), the sunlit top surface creates an inner edge. The fit was made to take the
  outermost rim edge so that it does not lock onto that inner edge.
- Diameter: ±0.5 px.
- Static extents were read by eye from 100 px grid overlays and crops, so they are about ±5 px. The sofa and fur
  rug/pouf have curved, fuzzy outlines, so their boxes are loose. The rug is cut off by the bottom of the frame.
- The console table's right end is hidden under the lamp.
- The dock was measured on a 3x crop (±2 px). Its left block is partly hidden by the vacuum in frames 0-3.

## Ambiguities
- The vacuum's shadow is visible in the sunlit area. It is excluded from the fit.
- There is no motion blur problem.
- "Dock" means the small white two-block object at x 1700-1754 by the right wall.
- Other white round objects are static and should not be confused with the vacuum: the round vase (about 75 px) and the
  pleated lamp (about 150 px) on the console at the top.
