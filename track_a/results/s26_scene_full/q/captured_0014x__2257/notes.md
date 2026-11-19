# Q2257 – height of the cup (cm), captured_0014x (lab, 24 fps = question_fps, 1280x720)

Scale: the lab camera, f = 0.5959*1280 = 762.8 px, principal point (640,360). depth_info gives cup distance = 1.727 m at t=0.
The prior (ball acceleration) is not needed for a size.

## Pixel measurements (mean of frames 0, 10, 40; cup is static) – cupmeasure.py, cupmeasure2.py
- Rim top (cup vs white background, saturation step): v = 335.5
- Rim width (outer): u 449.5 – 489.5 (≈40 px); rim ellipse bottom ≈ 354 (visual, blurry)
- Bottom front edge (bright cup V≈205 vs table V≈165), at u≈469: v ≈ 401.5; the cookie hides the rest of the bottom,
  and the lowest point of the bottom ellipse is estimated at ≈402.
- Left side edge runs 454 (v360) → 460 (v376) → 463 (v390) → 466 (v397): the tumbler tapers toward its base.
- Raw bbox height 335.5–402 = 66.5 px (the scene record says 58 px visible height; that was too short at the bottom).

## Geometry – cup3d.py, cup3d_edges.py
The camera looks down on the table, so the image extent includes the rim ellipse. Table plane from the table-top
corners (vanishing points, f fixed): the two table directions come out 89.3° apart (check that f and the corners are consistent),
normal (up) = (-0.053, -0.852, -0.521); the ray to the cup is 30.5° above the table plane.
3D model: a vertical (frustum) cylinder with its centre on the cup's ray at 1.727 m, fitted to rim top, rim left/right, and lowest bottom point:
- no taper: H = 11.5 (bottom 400) / 12.0 (bottom 402) cm, R_top = 4.3 cm
- bottom radius 0.8×top: 12.0 / 12.6 cm
- bottom radius 0.7×top: 12.8 cm (bottom 402) – this taper reproduces the observed left-edge slant best.

## Second route
Rim centre (≈345.5) to bottom-ellipse centre (≈395): ≈50 px image length; ÷cos(30.5°) → 58 px; × z (1.685 m)/f → 12.8 cm.
With the elevation implied by the observed rim ellipse ratio (~0.45 → 26.7°) it gives 12.3 cm.
A plain bbox reading (66.5 px × 1.727/763) would give 15.0 cm, but that includes the rim ellipse and the bottom ellipse seen from above, so it overstates the height.

Answer: 12.7 cm (range 12.0–13.0). Confidence: moderate. The bottom edge is partly hidden by the cookie and the rim is blurry.
