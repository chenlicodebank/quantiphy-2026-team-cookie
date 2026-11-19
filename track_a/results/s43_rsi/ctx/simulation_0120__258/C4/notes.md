TV = the black panel with digits on the left wall (SAM3 'television' 0.94). Scale from the prior: robot cleaner 1 m/s = 201.3 px/s on the floor (own centroid re-measure 8.36 px/frame x 24 fps; robot dia then 0.35 m, a real vacuum). The TV is on a vertical wall, so the floor scale cannot be applied directly: nadir pinhole with nadir point (537,540) from the TV's side edges, wall base at x=295.6 px (sub-pixel, constant) gives wall distance 1.199 m; the invariant W/Xw = dy/(x-cx) = 1.0538 gives W = 1.26 m (top- and bottom-edge routes agree to 0.2%). Cross-check: height 0.71 m -> exactly 16:9, camera 5.6 m, TV 1.42-2.13 m up. Naive planar scale would give an implausible 2.05 m (90-inch) TV.

Final message:
I measured the TV's length as **1.26 m**.

Method summary:
- **Object**: SAM 3 identified the black panel with white digits on the left wall as the television (score 0.94); the right-wall contour panel is wall art.
- **Scale**: the prior (robot cleaner = 1 m/s) gives 201.3 px/m on the floor plane, confirmed independently by re-measuring the robot's centroid (8.36 px/frame) and by the resulting 0.35 m robot diameter.
- **Geometry**: the TV is mounted on a vertical wall, so the floor scale can't be applied directly. Using the nadir pinhole model (nadir point at the image centre, derived from the TV's own side edges) and the sub-pixel wall-base line at x = 295.6 px, the wall sits 1.199 m from the camera axis; the invariant W/X_w = Δy/(x−cx) = 1.0538 then gives W = 1.26 m.
- **Checks**: top-edge and bottom-edge routes agree to 0.2 %; the derived height (0.71 m) makes the panel exactly 16:9 with a plausible 5.6 m camera height; the naive planar scale would imply an implausible 2.05 m (90-inch) TV.
