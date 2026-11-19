# q1575 — width of the table (desk), simulation_0206

The question asks: "What is the width of the table in meters?" Width means the desk's front-to-back depth (its shorter horizontal side).
Answer: **0.85 m**.

## Inputs
- 3D Blender render, 2124x1080, 24 fps (the file rate equals question_fps).
- Prior: the typewriter falls with a = 9.8 m/s² until it lands at about 0.44 s.
- Depths: typewriter 4.32 m at t=0 and 4.501 m at t=0.5; gun 4.704 m; desktop far-right corner 5.009 m; desktop closest corner 3.593 m.
- Principal point taken at the image centre (1062, 540).

## Desk-top corners (frame 0, gamma-enhanced zooms: crop.py, multi.py)
Corners are taken on the outer edge of the top face:
- FL (front-left, closest) = (700, 876)
- BL (back-left) = (471, 686)
- FR (front-right, the tip at the right of the image) = (1997, 652)
- BR (back-right, where the back rim meets the right-side edge, just right of the brass rod) = (1591, 521)

**Which corner is "far right":** I put FL at 3.593 m and solved the parallelogram FL + BR = FR + BL for the other depths (rect.py).
- This gives |BR| = 5.01–5.02 m for any f, which matches the given 5.009 m.
- FR comes out at about 4.40 m, so the given "far right" corner is the back-right one.

This is an independent check of the corner set.

## Focal length
- **Right angle at FL (rect.py):** f ≈ 3600 px. This is sensitive to the corner pixels: 4 px moves it by ±300 px (sens.py).
- **Fall alone (fall_fit*.py):** f ≈ 2800–3200, but poorly conditioned.
- **Fall with the desk normal as world vertical (combo.py, joint.py):** f ≈ 3470–3520 px (horizontal FOV about 34°) for both the bbox-centre track and the bottom-edge track, with t0 ≈ 0.04 s.
- **Sanity checks at f = 3500:** typewriter about 0.36 m wide, lamp about 0.38 m tall, desk about 1.65 m long. All are realistic.

## Width
In joint.py, the desk is a rectangle with FL at 3.593 m and BR at 5.009 m. The corners are allowed to move with a 3 px prior, and the fall must follow g along the desk normal.

| Variant | Camera roll | Width |
|---|---|---|
| Free roll | 2.35° | 0.868 m |
| Roll held near 0 (prior), or the fall's x-path added | 0.8–1.3° | 0.80–0.83 m |
| Plain corners at f = 3500 | — | 0.86–0.90 m |

Evidence that roll is near zero:
- The typewriter falls with x drifting only −6.5 px, which is what zero roll predicts.
- The lamp stem's tilt matches zero roll.
- The thin brass rod disagrees.

Using the outer edge of the molding instead of the top-face edge adds about 1.5%.

I took a value between the two clusters: 0.85 m. The front-right and back-right corners are each about 5 px uncertain because of the rounded tip and the brass rod next to BR.

## Open issue
The gun depth is not reproduced. The ray through the gun's image centre meets the desk plane at about 4.43 m, not 4.704 m, at any f. Most likely the gun's origin is not at its visible centre, so I did not use it for the scale.

The typewriter's rest pixel at 4.50 m is consistent with an origin near its base.

## Confidence
Moderate: the width is probably within ±6%.
