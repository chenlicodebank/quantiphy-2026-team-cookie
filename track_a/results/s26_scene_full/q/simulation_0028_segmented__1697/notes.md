# q_1697: height of the rock (m)

Prior: eagle length 0.8 m. depth_info: eagle at 100.14 m (t=1 s) and 99.52 m (t=2 s). The file runs at 25 fps and the
question at 24 fps; this only matters for which frame the depths refer to (frames 24 and 48).

## Method
- The eagle is seen from the side, flying left to right, so its body length lies along image x.
- Eagle pixel length: the horizontal extent of the 50%-coverage mask (min channel) on white-background frames 0-20
  (measure.py). Values were 22-29 px over the wingbeat: 22-23 px with the wings down (body only) and 28-29 px with the
  wings swept forward. The mean was 24.8 px. scene/ bbox_w (threshold <232, including antialiasing) gave 23-30 px.
- Eagle depth: Z is about 99.85 m at frame 24, from back-projecting the 100.14 m distance. It is about 100.6 m around
  frames 0-20, since the eagle approaches the camera by about 1.3 m/s (checked with the t=2 s depth).
  Focal length: f = 24.8 x 100.6 / 0.8 ≈ 3110 px (HFOV ≈ 17°).
- Rock: one silhouette, static. Vertical pixel extent is 285 px (y 25-309), measured in code on frames 50-70 with no
  bird present.
- The rock's depth is not given. The eagle flies just in front of it (overlapping from frame 21 on), so the rock is
  assumed to be at the eagle's depth, about 99.9 m.
  H = 285 x 99.9 / 3110 ≈ 9.15 m. Answer: 9.1 m.

## Checks and uncertainty
- Using the bbox_w median (about 27 px) instead gives 8.4 m. Using only body-only frames (about 22.5 px) gives 10.1 m.
- Main risks:
  - The rock may be farther away than the eagle. If so, it is larger.
  - The image vertical extent includes some of the rock's top surface, because the camera looks slightly down on it.
    If so, the true vertical extent is smaller.
- Confidence: low to moderate.
