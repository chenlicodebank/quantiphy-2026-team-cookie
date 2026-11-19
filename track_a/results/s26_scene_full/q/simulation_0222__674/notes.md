# Q674: width of the white sofa (m). Prior: robot vacuum diameter = 0.438 m. No depth_info.

The camera looks straight down from overhead; it is static, at 24 fps. The cream crescent sofa is at the bottom centre.
"Width" here means the shorter horizontal extent, which is the sofa's front-to-back depth (the image y extent). The
length is the image x extent: about 886 px, or about 3.3 m.

## Measurements (scripts are in this folder)
- `sofa_extent.py` and `prof.py` take gray profiles on frame 0 (the robot is at the dock, far from the sofa).
  - Front edge (the arm fronts at x≈640–680 and x≈1335–1350): a sharp step at y = 578 (the dark contact shadow above it).
  - Back edge (x≈1000–1050): the 50% crossing between the sofa and the carpet is at y ≈ 1058.4.
  - Raw extent: 480.4 px. The left and right ends are at x≈565 and x≈1451.
- Robot: the circle-fit diameter of the top disc is 117.8 px (from scene/tracks; the edges look sharp on zoomed crops).

## Perspective (this matters because the sofa back is tall)
- `robot_edge.py` / `robot_prof.py`: the robot's inward rim is wider than its tangential rim, which shows a side face.
  The difference grows linearly with radial distance: 3.3 px at r = 676 down to about 0.5 px at r ≈ 300. The slope is
  about 0.0064, so h_robot/D ≈ 0.006 and the floor-level robot diameter is 117.1 px. Floor scale = 0.438/117.1 =
  3.74 mm/px.
- Glass/ladder shelf in the top-right corner: the top/bottom x offsets give k ≈ 1.18 at its top, so H_shelf/D ≈ 0.15.
- The sofa's back outline (y=1058, 518 px from the image centre) is the back's outermost bulge, at an estimated height
  of about 0.6–0.7 m. Its magnification comes out as:
  - Robot route (sofa outer height ≈ 6.5 × robot height): k ≈ 1.04, giving a back offset of 498 px and a width of 460 px.
  - Shelf route (sofa ≈ 0.36 × shelf height): k ≈ 1.058, giving 490 px and a width of 452 px.
  - The front edge is only 38 px from the image centre, so its correction is negligible.
- Corrected width: about 456 px (range 452–462), which is 456 × 3.74 mm ≈ 1.71 m.

## Answer: 1.71 m
- With no perspective correction: 480 × 0.438/117.8 = 1.785 m. This is an upper bound.
- The answer most likely lies between 1.69 and 1.79 m. The main uncertainty is the height-based perspective correction,
  because the heights of the sofa, robot and shelf are not observable. The answer could be about 3–5% off.
