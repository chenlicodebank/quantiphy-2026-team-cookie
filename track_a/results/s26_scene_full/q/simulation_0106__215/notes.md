# q215: speed of the left virus at t = 1.0 s (frame 24, 24 fps; file fps = question fps)

Prior: right virus speed = 1.5667 m/s. No depth_info.

## Data
I used the scene/ tracks (body circle-fit centres and radii), which I checked against the frame-by-frame
steps (a.py, b.py). Left virus moves up and right virus moves down; both start at frame 1.
- Frame 1: both centres are at nearly the same image height (570 vs 644 px). Both make the same
  first pixel step (11.52 px/frame) and the same small x drift (-0.4 px/frame), which points to the
  same depth. The body radii are 123.78 and 139.11 px, so the size ratio is R_left/R_right = 0.890.
- The scene has perspective: the left virus grows (124 -> 132 px) and the right one shrinks
  (139 -> 133 px), which fits a camera pitched slightly downward. Raw pixel speeds therefore drift:
  left 11.5 -> 12.9 px/frame, right 11.5 -> 10.3.
- Perspective-free check: b = (v - cy)/r is the camera-frame coordinate in body radii, and it is
  linear in time for both viruses (quadratic term about 3 % or less over the window). So both move
  at constant world speed: left 0.0922 R_left/frame (frames 1-36), right 0.0826 R_right/frame (frames 1-27).
- World speed ratio, left/right = 0.0922 x 0.890 / 0.0826 = 0.993 from the in-plane component.
  Adding the depth component for an assumed focal length of 1000-2000 px gives 0.998-1.013.
  Off-axis sphere enlargement inflates the left virus's apparent growth, so the true value is near
  the low end. The best estimate is a ratio of about 1.00: the two viruses have equal speeds.

## Answer
Left speed = 1.5667 x ~1.00 = **1.5667 m/s**. The speed is constant, so the value at 1.0 s is the same.

Alternative (naive 2D, one m/px scale from the right virus's mean pixel speed of about 11.1 px/frame,
with the left at about 12.2 px/frame at frame 24): about 1.72 m/s. I rejected it because the size
changes clearly show perspective; the pixel-speed drift is a projection effect, not real acceleration.

Confidence: moderate-high (uncertainty about +/-2 % from the size ratio and depth component).
