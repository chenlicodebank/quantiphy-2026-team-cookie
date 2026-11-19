# q_1752 — width of the rock (m)

Prior: boat length = 10 m; depth boat-camera 173.71 m (t=1 s, frame 24), 174.55 m (t=2 s, frame 48). File fps = question fps = 24.
No depth is given for the rock, so its range has to come from the camera geometry.

## Camera (solve.py)
- Boat centroids at frame 24 (359.6, 925.6) and frame 48 (274.6, 901.2) are back-projected with the given depths.
  The boat moves along its own axis, so its bow-to-stern segment (deck-level ends (252,883) and (459,955) at frame 24)
  is parallel to the motion vector. Setting that segment's length to 10 m gives f = 3830 px (horizontal FOV 16 deg).
- The water is horizontal, so the motion vector is horizontal. That gives a camera pitch of 55 deg down and a camera height
  of about 151 m above the boat. Speed comes out at 4.08 m/s, which is plausible.
- Check: the boat's across-axis image extent (~117 px) fits a ~3.5 m beam plus hull and cabin seen at about 60 deg depression.

## Rock (rock.py)
- Rock bbox 493 x 440 px, centroid (625, 205) (from the scene record; it does not move).
- The near-base silhouette point (560, 451) meets the water plane at a range of 188 m. The centroid ray meets the plane
  at 198 m, but the rock's centre sits above the water, so it is nearer than that. Estimated range to the rock centre: ~192 m (+-5).
- Horizontal (camera-x) extent: 493 px x 192/3830 = 24.7 m.
- Ellipsoid-moment check: the image covariance gives an x extent of ~501 px, i.e. 25.1 m. The front-to-back extent depends on the
  unknown rock height. It is longer than the x extent unless the rock is more than ~20 m tall, so for a boulder of moderate
  height the shorter horizontal extent (= width) is the x extent, ~25 m.
- Another reading: if the rock were very tall (height > 20 m), the width would be the front-to-back extent, which would be smaller.

Answer: 24.8 m. Confidence moderate. The camera yaw relative to the world axes is unknown, the rock's range is inferred
(not given), and f relies on the boat's deck-end points.
