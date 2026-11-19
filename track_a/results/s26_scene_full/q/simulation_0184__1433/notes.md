# Q1433 – height of the box (m)

Video: 3D Blender render, 1920x1080, 24 fps (file rate = question_fps = 24). Static, level camera (no x drift of a
vertically falling object, so pitch < 0.5 deg). The box (black case, green lid, "D5") hangs at f0, falls freely
f0–7, lands on the blue roller ramp at f8, tips to ~30 deg and slides down it, speeding up.
Prior: slide acceleration at t=1.25 s (f30) = 1.58 m/s^2. Depths: 9.194 m at f0, 9.096 m at f12.

## Pixel height of the box (front face plane)
- `edges2.py`: background-difference half-max edges per column at f0, f3, f5, f7, taken relative to the box centre
  found by ECC tracking (with the 0.7 deg in-plane rotation removed).
- Top silhouette sits at a constant −92.5 px from the centre (highest part, x≈570–700; ends of the lid are ~8 px
  lower, which looks like rounded corners). It stays fixed to the front face, so it is the front top edge (camera is
  below the box top).
- Bottom silhouette goes +90.7 (f0) → +84.8 (f7) because the bottom face disappears as the box nears eye level.
  Linear fit against the bottom edge's offset from the horizon gives the front bottom edge at +83.9 px. The slope
  (0.060) gives box depth w ≈ 0.06·Z ≈ 0.54 m.
- Front-face height h = 92.5 + 83.9 = **176.4 px** (±2 px; using the median top instead of the highest part gives ~172).

## Scale, route 1: gravity in the free fall (main)
- `fall_ecc.py`: affine ECC fit of the front face over f0–7. Scale stays 1.000 (depth constant), x stays constant,
  y fits a parabola with residuals of 0.04 px. a = 4.177 px/frame² = 2405 px/s² (other windows give 2402).
- Front-face points have the same depth as the texture that gave this acceleration, so the metres per pixel at the
  front plane = g / a_px = 9.81/2405 = 0.004079 m/px. No depth or focal length is needed here.
- H = 176.4 × 0.004079 = **0.720 m**.
- This route implies f ≈ a·Z_front/g ≈ 2150 px (HFOV ≈ 48 deg).

## Scale, route 2: the prior plus depth_info (check)
- Ramp vanishing point from robust fits to the conveyor edges (`ramp.py`): (−4267, −2433). The slide line's 3D
  direction is (V − c, f). This VP agrees with the template scale growth along the slide to 1 %.
- Template track of the front face over f14–44 (`slide_track.py`), back-projected onto the 3D slide line. The line is
  anchored by the f12 depth 9.096 m, shifted ~0.27 m for the front face (`slide3d.py`, `solve_f.py`). A quadratic fit
  gives the acceleration; f is solved so that it equals 1.58: f ≈ 2106–2154 px depending on the window.
- Z_origin(f0) = 9.194/sqrt(1+r²/f²) ≈ 9.01 m, so Z_front ≈ 8.75 m and m/px = Z_front/f ≈ 0.00406–0.00415.
  That gives H ≈ 0.718–0.732 m (mid 0.724).
- Without the front-face shift the prior is reproduced at f ≈ 2176–2226, which matches f = 2211 from gravity at the
  origin depth. The two routes are consistent.

## Answer
Height ≈ 0.72 m (route 1: 0.720, route 2: 0.72–0.73). Confidence: good, about ±3 %. The main uncertainty is the
top-edge choice (highest part vs rounded corners, 172–176 px).
