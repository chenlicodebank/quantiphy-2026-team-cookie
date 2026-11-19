# q_2458 — height of the book (cm)

I read "height" as the vertical extent of the flat-lying book, which is its thickness (cover to cover).
Under the other reading, height as the book's long side (spine length), the answer would be the book length,
about 18–19 cm (131 px at about 1.1 m). I did not measure that carefully.

Camera: lab Orbbec, f = 0.5959 x 1280 = 763 px, principal point (640, 360). File fps = question fps = 24.
The camera is static and the book is the only moving object (scene/ record checked; its track covers the right object).

## Geometry (geom.py)
- Book centres: t=1.0 (frame 24) (750.5, 396.9) at 1.0685 m, and t=1.2 (frame 29) (669.3, 455.5) at 0.977 m, back-projected.
- Ramp: top-end centre (804, 360.5) at 1.243 m and bottom-end centre (659.5, 478.5) at 0.990 m. Ramp length 0.367 m;
  ramp direction is within 7° of the book's motion. Ramp normal N comes from the image of the ramp's top edge plus
  the ramp direction. Table normal comes from the vanishing points of the table corners. Ramp–table angle is about 28°,
  so g(sin θ − μ cos θ) = 2.8 gives μ ≈ 0.2, which is plausible.
- Rest position on the ramp (frames 0–18): the ray through (783.5, 373.0) meets the plane through P24 parallel to
  the ramp at about 1.123 m. That puts it 6 cm up-slope of P24, which matches ½·2.8·(5/24)² = 6.1 cm.

## Route 1: front side face on the ramp at rest (edges.py, thick.py)
The mean image of frames 0–18 has two lines at every column: the dark top-front edge line and the contact-shadow
line at the bottom. Their sub-pixel separation is 8.5–8.6 px over x = 756–804 (7–7.7 px near the rounded left corner).
Projecting a thickness vector h·N at the front face (depth about 1.08 m) gives 6.28 px per cm, so h ≈ 1.35 cm.

## Route 2: front face at rest on the table, frames 37–48 (table_route.py)
The edge separation is 11.1–12.5 px for x = 520–590. Taking the table plane through the ramp bottom (0.99 m), the
answer depends on the table normal:
- normal from the corner vanishing points: 1.27 cm;
- camera assumed level: 1.35 cm.

plane_check.py checks these two normals against the ramp's top-edge width (0.188 m). The bottom width comes out
0.155 m with the corner normal and 0.214 m with the level camera, so the truth lies between them, at about 1.32 cm.

## Answer
1.33 cm (routes give 1.35 and 1.27–1.35). Uncertainty is about ±7%. The main sources are where exactly the top edge
sits on the dark line (±0.5 px ≈ ±5%) and the plane normals.
