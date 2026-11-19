# q1237 – height of the turning yellow car (taxi), simulation_0058

Prior: the white car (the van) accelerates at 4 m/s². The depths at t=0.58 s (frame 14) and 1.58 s (frame 38) are from depth_info.
question_fps = file fps = 24.

## Focal length (f_from_van.py)
- I back-projected the van's box centre at frames 14 and 38 using the given depths (principal point at the image centre) to get its straight-line
  path. For each frame, the van position is the point on that line closest to the ray through the box centre. I fitted a quadratic to s(t)
  over frames 2–71 (the van starts from rest at frame 1, and frame 1 duplicates frame 0).
- a = 4 m/s² gives f = 2237 px (sub-ranges: 2210 / 2182 / 2253). Per-frame speeds rise linearly (0.32 → ~12 m/s), so the motion
  really is uniform. **f ≈ 2230 px.**
- Weak cross-checks: the cyclist and van paths are parallel at f≈2440, but this test is insensitive (1.5° at 2200). The cross-street curb
  vanishing point gives 2085–2390 (noisy). Both are consistent within their errors.

## Camera height (height.py)
- Pitch comes from the horizon row 422.5 (main-road vanishing point), assuming zero roll. Camera height H comes from the cyclist's tyre contacts
  (frames 14 and 38) and the pedestrian's feet (frame 14): H = 2.79 m (values 2.77–2.81) at f = 2230.

## Taxi height
- Sign top (the highest point, which is in the AABB): (592, 529) at frame 14 and (782, 545) at frame 38, read from pixel profiles.
- The 3D sign-top point lies on its pixel ray, vertically above the origin, and the origin's distance equals the depth_info value. The result
  is the height above the ground plane.
  - Frame 14: 1.593 m (1.596 if the origin is at ground level).
  - Frame 38: 1.579 m (1.584).
- Check: the taxi's own tyre-contact rows fall on the ground plane 0.78 m in front of the origin at frame 14 (half-width, side view) and
  2.1 m in front at frame 38 (front-corner wheel in 3/4 view). Both are plausible.
- Sensitivity: h ∝ ~1/f. f between 2180 and 2250 gives h = 1.58–1.62.

**Answer: 1.59 m** (frames 14 and 38 agree within 1%; confidence is good, roughly ±4%, dominated by f).
