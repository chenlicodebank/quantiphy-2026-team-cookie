# q_663: speed of the vacuum cleaner at t = 2 s (m/s)

Prior: vacuum diameter = 0.438 m. No depth_info. 2D top-down clip. File fps = question_fps = 24, so t = 2 s is frame 48.
Convention: speed(48) = |p(48) - p(47)| x 24, with one m/px scale from the vacuum's pixel diameter.

## Measurements (my own: measure.py)
- I fitted a circle to the disc rim. I cast 360 rays from the centre, took the gradient-peak edge (the 50 % brightness
  transition, refined to sub-pixel) on each ray, and fitted by least squares with outlier rejection.
  - Frame 47: centre (968.06, 381.05). Frame 48: centre (946.67, 386.92). The step is **22.17 px**.
  - Diameter at frames 45-50 is 120.5-120.7 px. At frame 48 it is **120.61 px**. The vacuum is near the image centre
    there, so the side wall barely shows. Near the dock (x ~1620) it reads 123 px because the side wall shows (perspective).
- The scene record (scene/tracks) agrees: the step is 22.14 px and the diameter 120.61 px at f48. Its centres match mine
  to within 0.25 px.
- Scale = 0.438 / 120.61 = 3.632e-3 m/px.
- Speed = 22.17 x 24 x 3.632e-3 = **1.932 m/s**.

## SAM 3 check (check_sam.py)
- The text prompt "robot vacuum" found nothing. A box prompt with the phrase "white disc" found the disc (score 0.97) on f47 and f48.
- SAM centroids: f47 (968.4, 381.8) and f48 (947.1, 387.7). The step is 22.1 px, which agrees with mine to 0.3 %.
- The SAM mask extents are 125-126 px, about 4 % more than my 120.6 px. A brightness profile through the centre at f48
  explains why. The disc-to-floor transition sits at x ≈ 886.5 and 1007.5, and at y ≈ 326.5 and 447.5, so the disc is
  about 121 px across. The SAM mask runs on to x = 1010 and y = 449. That takes in the dark rim and shadow line (grey
  ~64-85) outside the disc on the shadow side. My 120.6 px is the correct diameter, and the mask is inflated by ~2 px per side.

## Second route and sensitivity
- Second route: the SAM centroid step (22.1 px) gives 1.926 m/s, and the record step (22.14 px) gives 1.930 m/s.
- The vacuum is accelerating smoothly (steps of 21.7, 22.2 and 22.6 px around f48). A centred mean of the f47->48 and
  f48->49 steps would give 1.953 m/s. The benchmark convention is the backward difference, so I answer 1.932.
- Using the 123 px half-max edge diameter would give 1.89 m/s, about 2 % lower.
- Confidence: high, within ~2 %.
