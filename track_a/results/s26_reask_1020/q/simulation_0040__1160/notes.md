# Q1160 – eagle wingspan (prior: eagle length 0.8 m)

The file and question_fps are both 24 fps. The scene is a 3D Blender render with a static camera. One black eagle flies from left to right and leaves after frame 67.

## Measurements (scripts in this folder)
- `profile.py` / `geom.py`: I made a background-difference mask of the eagle (median background per crop, |diff| > 20).
  - **Wingspan in pixels** = the longest chord of the mask (wingtip to wingtip).
  - **Body length in pixels** = the longest run along the body axis, measured from the tail/feet to the beak.
  - The pale beak and feet are included; they are lost if only dark pixels are kept.
- **Body length**: 30–31 px in every frame checked (4–6, 17, 29–32, 40, 52–56, 63). It is rigid and stable.
- **Projected wingspan**: changes with the wing beat. The peaks are 57.4 px (frame 5), 57.5 px (frame 31) and **64.0 px (frame 54, the most spread pose)**. The image vector at frame 54 is (−22, 59), so the span runs mostly along image y.
- **Depths**: the eagle is at 179.3 m (t = 1 s) and 177.1 m (t = 2 s), so the depth effect is only about 1%. Both lengths are taken in the same frame, so the ratio needs no focal length. For reference, f is about 6900 px (hFOV about 9°).

## Camera tilt (important)
The camera is oblique, not looking straight down.
- The walker is seen as a full standing figure, 39–50 px from head to feet, which is about 1.0–1.3 m at the eagle-derived scale.
- In the image, the wing span is not perpendicular to the body (71–87°).
- Horizontal lengths along image y are therefore foreshortened by sin(e), where e is the camera elevation.

I estimated e three ways:
- Eagle flying at constant altitude, using its two depths and back-projected centres (frames 24 and 48): e ≈ 51°.
- Walker's minimum apparent head-to-feet length, assuming a height of 1.75–1.8 m: e ≈ 59°.
- Requiring span ⟂ body on the ground (noisy, and affected by roll): 45–65°.

I adopted e ≈ 55°, s = sin(e) ≈ 0.82, and treated the wings as horizontal at full spread.

## Result
At frame 54 I mapped the image vectors to the ground as (x, y/s):
- span (−22, 72) → 75.2 px
- body (29.1, 11.1) → 31.1 px

Wingspan = 0.8 × 75.2 / 31.1 ≈ **1.93 m**. Sensitivity to the elevation:
- e = 51° → 2.01 m
- e = 58° → 1.88 m
- frame 54 under its own level-bird angle (e ≈ 66°) → 1.77 m
- straight-down view, which the walker clearly rules out → 1.68 m

The smaller beats at frames 5 and 31 give about 1.77 m. The wings are less spread there, so I did not use them for "fully spread".

## Checks
- Realistic eagle proportions (length 0.8 m, wingspan about 1.8–2.2 m) are consistent with this result.
- Eagle speed comes out at about 10.7 m/s, which is plausible.
- Walker speed comes out at about 1.1–1.3 m/s, which is plausible.

Answer: **1.92 m**. Confidence is moderate: the camera elevation and the bird's roll could shift the answer by about ±7%.
