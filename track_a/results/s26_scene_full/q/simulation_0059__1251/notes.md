# Q1251: height of the traffic light (m). Answer: 4.5

File fps = question_fps = 24, so no time-base conversion was needed. The 3D Blender scene has a static camera.
Prior: the white car (the white cargo van) accelerates at 4 m/s^2. depth_info gives the depths of the human (pedestrian),
the yellow car, the white car and the bike at f14 and f38.

## Focal length (focal_van.py)
- I back-projected the van's bbox centre (from scene patch_cx plus a constant offset; v = 745.5) at f14 and f38, using
  the given depths 43.812 and 43.003 m. These two points define the van's 3D line. I put every frame's ray onto that
  line and fitted s(t) as a quadratic over f2-71 (residuals <= 1-3 cm).
- Solving 2a = 4 m/s^2 gives **f = 2210 px** (HFOV 52 deg). The vertex is at t0 = -0.04 s, consistent with a start
  from rest at f1. The final speed of 11.84 m/s matches 4*(2.96+0.04) = 12.
- Second route: the van and the cyclist ride along the same cross street, so their 3D lines should be parallel
  (f_parallel.py). They are parallel at f ~ 2500, and at f = 2210 they are 1.35 deg apart. This check is weak:
  1 deg corresponds to about 200 px of f, and the two paths need not be exactly parallel. I kept 2210.

## Camera geometry (final.py)
- Horizon: the four identical lamp posts give base_y = vh + k*pixel_height, which yields vh = 704.6 (residuals
  < 0.3 px). The road vanishing point is 702. **The horizon is below the image centre, so the camera is pitched UP
  by ~4.3 deg** (scene notes say "down"; that is wrong).
- Road-level camera height: I took the ground contact under each origin, at the origin's horizontal distance. The
  cyclist's wheel bottom (f14, f38) gives 1.74 m. The van's near-side tyres (y 799, 1 m nearer than the origin)
  give 1.77 m. Mean 1.75 m.
- Curb: the curb-face strip of the main road's right curb is 11 / 16.5 / 17.5 px tall at x = 1700 / 1900 / 2000.
  That is 0.064 x the camera height, i.e. ~0.11 m, so the camera is 1.64 m above the sidewalk.
- The pedestrian's soles (y~815, partly behind the garbage bags) would give 1.50 m above the sidewalk. I did not use
  this because the feet are probably clipped.

## Traffic light
- Right main traffic light (x 1652, with the pedestrian-crossing sign on top), measured in code on f70 / the clean
  background:
  - top (sign tip) y = 501
  - base y = 824.0, standing on the right sidewalk just inside its cross-street edge (y 818)
- Ground intersection of the base: 31.9 m from the camera. Vertical line up to the top ray: **4.50 m**.
- Left two-head traffic-light pole (x 750, top 513, base 817.5): **4.49 m** at 33.1 m. Both poles agree.
- Sensitivity:
  - f +-60 px: +-0.12 m
  - vh 702-709: +-0.03 m
  - curb +-0.005 x h: +-0.02 m
  - using the pedestrian's ground level instead: ~4.1-4.2 m (discarded, see above)

Confidence: moderate-good. The answer is 4.5 m (range ~4.4-4.6).
