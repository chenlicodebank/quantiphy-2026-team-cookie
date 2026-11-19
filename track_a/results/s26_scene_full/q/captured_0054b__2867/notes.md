# q 2867: soccer ball displacement between 1.0 s and 1.4 s (m)

Frames: question_fps = file fps = 24, so t=1.0 is frame 24 and t=1.4 is frame round(33.6) = 34. Camera f = 0.5959*1280 = 762.8 px,
principal point (640, 360). The only soccer-ball depth is R = 3.254 m at t = 2.0 (frame 48).
(There is a skipped capture at 35->36. It lies outside 24-34, so it does not matter here.)

## Measurements (my own scripts)
- `radial.py`: edge-based circle fit (strongest radial colour edge per ray, robust fit) for frames 25-45. The fits
  look good on `frames/radial_*.png`.
- `grey2.py`: frames 46-48, where the ball is drawn as a flat grey disc. Fit there gives (834.3, 370.0) with d = 45.5 px at frame 48.
  **The scene record is wrong here**: it gives a diameter of 37-39 px for 46-48. Its colour rule loses part of the disc.
- Frame 24: the ball has just been released and its right side is hidden by the crouching person. A fit on the free
  left/top/bottom arc (`rest.py`) and a look at the zoomed frame give a centre of about (926, 607). The full-circle fit,
  which the occluder pulls left, gives (917.5, 605.6). The answer moves only 0.001 m between the two.
- Frame 34: (885.6, 490.8), d = 54.9 px. Both fits agree.
- `lines.py`: the 600-px floor/baseboard edge is straight to within 1 px (sagitta < 1 px), so the image has no
  noticeable lens distortion and pinhole geometry applies.

## Route A, main: floor plane from the vertical vanishing point (`vp.py`)
- The vertical edges of the cabinets and door frame (Hough, `frames/vlines.png`) meet at a vertical vanishing point
  of about (480, 1510). That gives the floor normal in camera coordinates (optical axis 57 deg from straight down).
- The ball centres lie on a plane parallel to the floor, so Z = h/(n·x_n). Setting R48 = 3.254 m gives h = 1.67 m,
  so the camera is about 1.77 m above the floor, which is plausible.
- Result: R24 = 2.41 m, R34 = 2.72 m, displacement 0.475-0.482 m depending on which line set is used
  (all lines 0.4752; left wall only 0.4816; without the right-hand posts 0.4766).

## Route B, check: depth from apparent size (`solve.py`, `solve2.py`)
- Sizes are corrected for the off-axis pinhole stretch (factor (1/cos + 1/cos^2)/2) and anchored at R48 = 3.254 m.
  This implies a ball diameter of 0.183 m. Without the correction it is 0.194 m.
- The depth at frame 24 has to be extrapolated, because frames 24-27 are occluded or blurred. Depending on the
  extrapolation the displacement is 0.444-0.489 m: angle vs frame, linear 0.449 / quadratic 0.489; 1/Z plane fit 0.447-0.458;
  3D line 0.444.
- `compare.py`: the floor-route depths and the corrected sizes give a nearly constant ball diameter over frames
  28-48 (0.181 ± 0.004 m), so the two routes agree.
- Without the size correction the displacement is about 0.57 m. That reading is ruled out: the image is undistorted,
  so the physical stretch is real, and the floor route agrees with the corrected sizes.

## Answer
0.477 m (route A, central value). Route B brackets it at 0.44-0.49 m.
Confidence: moderate (about ±6%). The main uncertainty is the depth at frame 24, which can only be inferred because
the given depth is for frame 48 only. The given basketball depths (2.24 m at 0.5 s, 1.81 m at 1.0 s) disagree with its
shrinking image, so the depth_info itself may be noisy.
