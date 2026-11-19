# q1646 — diameter of the cart's wheels (m)

Prior: bird length 1.19 m. depth_info: bird 34.584 m (t=0), 33.999 m (t=1); cart 30.374 m; house 55.083 m.
File fps is 22; question_fps is 24, so t=1 s means frame 24. Principal point is assumed at the image centre (960, 977).

## Bird scale → focal length
- The bird flies side-on, left to right, so its length (beak to tail, the body axis) lies along image x. I used
  frames where the wings are edge-on or down, so the wings do not add to the extent. Bbox widths from
  scene/tracks/bird.csv, checked on crops (crops2.py → frames/edge*.png): f1 139, f2 149, f11 141, f18 143, f19 142,
  f20 143, f27 146, f28 150, f35 135, f36 130, f44 149 px. I took the median, about 143 px (±4).
- Pinhole, Euclidean distance: D = L·sqrt(f² + r²)/p, where r is the bird's offset from the principal point.
  - t=0 (f0, r ≈ 637 px): f ≈ 4107.
  - t=1 (f24, r ≈ 247 px): f ≈ 4078.
  - The two give f ≈ 4090 px (horizontal field of view ≈ 26°). The two depths agree within 0.7%, and the bird stays
    nearly parallel to the image plane.

## Wheel
- Near wheel, measured from intensity profiles over a 4-frame average (profile.py):
  - Vertical, through the hub at x≈1733: top outer rim edge y≈1061, bottom edge 1267.5 (against white), so ≈206 px.
  - Horizontal, through y≈1162: x 1629 to 1831, so ≈202 px.
  - The ellipse is nearly a circle (the wheel almost faces the camera), so the diameter is ≈206 px (major axis).
- Cart depth: Z = 30.374/sqrt(1+(790/4090)²) ≈ 29.82 m, taking the cart origin near the hub and cart centre.
- Diameter = 206 × 29.82 / 4090 ≈ 1.50 m.
- The near wheel sits about half a track width closer to the camera than the cart origin. A 0.3–0.5 m offset gives
  1.475–1.485 m. Answer: 1.49 m.

## Check
- Second route: the bird's edge-on extents in the later frames (f35–45, 130–149 px) give the same scale within ±4%.
- A partial-arc ellipse fit to the white-background rim was unstable and was discarded (wheel.py). The profile edges
  agree with the record's hand-read size of 192–200 × 205 px.
- Sanity check: the cart box is about 400 px, which is about 2.9 m. That matches a scene scaled about 2× real size
  (a crow at 1.19 m).

Confidence: moderate, about ±5%. The main error sources are the bird's pixel length (±3%) and where the cart
origin sits relative to the wheel (±2%).
