# q_1479 – length of the whale (m)

Prior: whale speed 1.67 m/s. depth_info: origin distance 33.7307 m at t=1.0 s (frame 24) and 35.1624 m at t=2.0 s (frame 48).
File fps = question fps = 24.

## Geometry from the prior + depths
- With straight, constant-speed motion, the 1 s chord is 1.67 m. So the angle between v and the origin ray at t=1 is
  acos((d2²-d1²-1.67²)/(2·d1·1.67)) = 31.7°: radial 1.42 m/s, lateral 0.88 m/s. Extrapolated origin distance:
  32.4 m at frame 1 and 36.55 m at frame 71.
- Camera is static. The whale is seen from above and behind, swimming away toward the upper left; its tail is closer
  to the camera than its head.

## Focal length / FOE (focus of expansion)
- Front-body feature tracks (LK, chained 1→71, `chain.py`, `foe3.py`) converge to an FOE near (-322,-393), but with
  20 px rms: the head and front body also rotate and bob with the swim stroke. The FOE distance along the
  head-motion line is poorly constrained, and f depends on it, via the 31.7° angle between the FOE ray and the
  origin ray.
- `consist*.py` and `scen.py`: if the origin is at the head, f ≈ 2450. At the chest, f ≈ 2800–3300. At the 3D body
  centre, f ≈ 3900–4000 (HFOV ≈ 36°). The 3D centre of the reconstructed whale projects near the image centre,
  about (1290,810) at frame 24, consistent with the origin at the centre.

## Length
- `tri.py` triangulates every tracked point between frames a and b, assuming pure translation by v·Δt
  (|v| = 1.67 m/s, direction = FOE ray). The windows are centred on the tail-stroke reversal (frames 27–28), when the
  tail moves with the body. `scen2.py`: for each assumed origin pixel, the FOE distance is solved so that the depth at
  that pixel equals the given origin distance (0 or 1 m interior offset), then f follows from the angle condition.
- Snout region (985,400) to fluke root (1720,1360) in 3D, origin at the body centre (frac 0.4):
  - window 24-31: 16.3 / 15.6 m
  - window 23-32: 16.6 / 16.0 m
  - window 25-30: 17.8 / 17.1 m
  - window 26-31: 16.6 / 15.9 m
  - window 24-29: 14.7 / 14.1 m
  - mean ≈ 16.0 m. Snout extrapolation along the depth profile (`profile.py`) gives 17.8–18.7 m.
- Origin choice changes this only moderately (head-ish origin ≈ 15 m, mid-body ≈ 16.5–17.7 m).
- Adding the rest of the fluke beyond the tracked point (about 1 m) gives **L ≈ 17 m**, the body length snout to fluke.
- Sanity checks:
  - The 3D flipper length is ≈ 5.2 m, ≈ 0.30 L, a normal humpback proportion.
  - At frame 71, the 1120 px lateral span at f ≈ 3984 means the body lies about 37° from the line of sight. That
    matches the long shadow pointing toward the camera.
- Window 21-28 (tail still moving) gives 12–13.6 m; it was rejected because the tail's own motion biases its depth.

## Confidence
Low to moderate, about ±15%. The depth relief from the flow is sensitive to the small rotations of the front body:
the bas-relief / rotation–translation ambiguity. One example: the left and right flipper insertions come out about
8 m apart in depth. The answer depends mostly on the head-to-tail depth difference (about 13 m) and on the origin
location. The world-AABB "length" also depends on the whale's yaw in the world, which cannot be observed; the body
length is reported.
