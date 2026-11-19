# q_1672 — average speed of the boat (m/s)

File is 25 fps (75 frames); question_fps = 24 is used for all times: t=1 s -> frame 24, t=2 s -> frame 48.
Track frame indices from scene/tracks were used (not their seconds column).

## Method (3D pinhole, principal point = image centre 480,480)
- Eagle (bird) pixel position at frames 24 and 48: quadratic fit over ±4/6/8 frames of the centroid (or bbox centre),
  excluding mast-overlap and edge-cut frames: (471, 372.4) and (741, 370.2).
- Back-project with the given eagle depths (116.0475 m, 108.2756 m) and solve the focal length so the 3D displacement in
  1 s equals the prior speed 11.84 m/s (constant-speed eagle): f ≈ 3385 px (3380–3393 across variants; HFOV ≈ 16°).
- Boat (hull centre) at frames 24 / 48: (320.8, 580.1) / (229.3, 575.6); back-projected with depths 103.157 / 106.0906 m.
  3D displacement over 1 s = 4.065 m -> 4.065 m/s. Varying the boat reference point (hull centre, mask centroid, bbox
  centre) and fit windows: 4.052–4.072.

## Second route
- Whole clip: per-frame boat positions (hull centre) with depth linearly interpolated/extrapolated from the two given
  depths; mean of per-frame speeds = 4.072 m/s (median 4.105, noisy), net displacement 0->74 / time = 4.053 m/s.
- Boat pixel speed is steady (4.0 -> 3.3 px/frame, decreasing consistently with receding), so motion is near-uniform.

## Answer
≈ 4.07 m/s. Confidence: good (main uncertainty: assumption that eagle moves at constant speed in a straight line between
t=1 and t=2, and the unknown exact origin point, both small).
