# q1469 — body length of the dragon (m)

Prior: speed 1.29 m/s. Depth: 5.1661 m at t=1 s (f24), 6.2783 m at t=2 s (f48). question_fps = file fps = 24.
3D Blender render, static camera; the dragon flies away from the camera, up and to the left, seen from behind and below.

## Focal length (from the speed prior and the depths)
- `focal.py`: uses the head-patch point at f24 and f48 with the two distances, and requires a 3D displacement of 1.29 m over 1 s, which gives f ≈ 3280–3310 px.
- `cvfit.py`: fits a constant-3D-velocity pinhole model to the whole head track (f1–71). The image-only value Vz/Z0 = 0.258–0.260 agrees with the 0.274 implied by the depths. With |V| = 1.29 this gives f ≈ 3220–3250 px, and Z0 from t=1 and from t=2 agree (4.10 / 4.11 m).
- I adopt f ≈ 3250 px (HFOV ≈ 43°). The fitted V is about (-0.58, -0.44, 1.07) m/s in camera coordinates, so the body axis is at roughly 36–46° to the line of sight and nose-to-tail is strongly foreshortened.

## Sizes
- **Wingspan** (lateral extent): 1150 px at f0 (Z≈4.1) gives 1.45 m; 713 px at f60 (Z≈6.8) gives 1.49 m; 877 px at f24 (5.17 m) gives 1.38 m. So the wingspan is about 1.45 m.
- **Nose-to-tail** (`tail.py`): I took the tail tip from the mask and back-projected it, assuming the body and tail lie along the flight direction V.
  - f0–f4 (straight tail, small residuals): head patch to tail tip ≈ 0.75–0.76 m.
  - Glide frames f52–71 (tail hanging, 40 px residual): ≈ 0.95–1.0 m.
  - Forward-most head point (horns) to tail tip at f3: ≈ 0.86 m, plus a hidden snout that points away from the camera (~0.1 m).
  - Estimate: nose to tail ≈ 0.95–1.15 m in flight; a rest pose with a straight tail would be a little longer.

## Reading
"Body length" is read as nose-to-tail along the body. The benchmark calls a flying animal's wingspan its "width", so here length is not the wingspan.
- The alternative reading, the longer horizontal AABB extent, would be the wingspan, ≈ 1.45 m.
- Answer: **1.1 m**. This is the nose-to-tail estimate, rounded slightly toward the upper end.

## Confidence
Low to moderate:
- The body axis is heavily foreshortened and the snout is hidden.
- f depends on the speed prior: the lateral part of the motion is small, so a ~5% error in speed gives a ~10% error in f.
- The reading is ambiguous: wingspan 1.45 m versus body 1.0–1.1 m.
