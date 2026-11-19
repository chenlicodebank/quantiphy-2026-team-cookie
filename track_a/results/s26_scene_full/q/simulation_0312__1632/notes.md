# q_1632 — width of the star (prior: height = 0.2 m)

File fps 24.008, question_fps 24.0 (t=1 s -> frame 24, t=2 s -> frame 48; same frames either way).

## Method
- `tips.py`: per frame, segment the star (|RGB - bg| > 45, 8x upsampled soft mask), find the 5 tip points
  (radial maxima of the contour around the centroid), and fit a 2x2 affine map from a regular unit pentagram
  (tip radius 1) to the tips. Frames 10-71 give 5 clean tips; RMS residual 0.3-1 px late, ~2 px early.
  A small residual means the tips are an affine (≈ orthographic) image of a regular 5-point star.
- For a planar shape that is rotated out of the image plane, the larger singular value of the affine equals
  f·R/Z (no foreshortening along the tilt axis) and the smaller one is foreshortened by cos(tilt).
  - frame 24 (Z = 6.552 m): σ1 = 26.47 px -> σ1·Z = 173.4
  - frame 48 (Z = 8.345 m): σ1 = 20.48 px -> σ1·Z = 170.9  (agree within 1.5 %)
  - σ2·Z changes (98 -> 117) because the tilt changes; σ2/σ1 ≈ 0.56-0.72, so the tilt is about 45°.
  Since σ1·Z stays constant, the face is a regular star (an anisotropic star would not keep σ1·Z constant
  while rotating). The image bbox ratio of about 0.7 is foreshortening, not the true aspect ratio.
- Regular star with tip radius R: face height (top tip to bottom tips) = R(1+cos36°) = 1.809R, and
  face width (tip to tip) = 2R·cos18° = 1.902R. So width/height = 1.0515.
- Height 0.2 m -> R = 0.1106 m -> width = 0.2103 m.

## Check (second route)
- Implied focal length f = σ1·Z / R = 1568 px (frame 24) and 1545 px (frame 48), which is consistent.
  That gives hFOV ≈ 38°, which is plausible. The σ1 ratio between frames (1.292) reproduces the given depth
  ratio (1.274) to within 1.5 %.

## Readings
- Face width (horizontal extent across the upright star's face, the convention for flat objects): **0.210 m** (answer).
- Raw image bbox width/height at t=1 is 33/47, which would give 0.14 m, but that value is foreshortened by the
  ~45° tilt, so I rejected it.
- Thickness reading (shorter horizontal extent if the star stands upright): the side wall seen at frame 0 is
  roughly 0.15-0.3 of the face height, which is not measured precisely. I did not use this reading.

Confidence: moderate-high on the regular-star geometry; the main risk is the size naming convention.
