# q_2609 — soccer ball diameter (cm)

Prior: tennis ball diameter = 6.7 cm (exact). depth_info: left tennis ball (A) 0.706 m, right tennis ball (B) 0.776 m at
t=1.2 s (frame 29), pencil bag 1.05 m, soccer ball 0.894 m. File fps = question fps = 24.

## Pixel measurements (my own edge profiles, crops.py / measure.py)
- Soccer ball (static): horizontal edges at frame 29, row 318: x 552.5 to 647.5 → 95 px. Radial-edge circle fit: 96.9 px
  (all angles), 94.8 px (excluding the shadowed bottom). Frames 0/15/48 agree within ±1.5 px. Used 95.5 px, centre (600, 318).
- Tennis A at rest (frame 15): x 449.5–482.5 → 33.0 px (vertical about 30 px, but the top is cut by segmentation and the bottom has a shadow).
- Tennis B at rest: x 804–836.5 → 32.5 px. The scene/ free-fit radii (13.5–14.5) miss the pale rim and are too small.

## The depth_info is inconsistent with the image
- Method card (f = 762.8 px): tennis A = 0.706·33/762.8 = 3.05 cm, not 6.7 cm (factor 2.2 off). The soccer ball would be 11.2 cm.
- Ordering: depth_info puts the soccer ball (0.894 m) farther than both tennis balls, but tennis ball A visibly passes
  **behind** the soccer ball (frames 31–48, frames/occ.png), and the soccer ball's table contact is lower in the image.
  So the soccer ball is nearer than the tennis balls. This contradicts the given distances, so I did not use them.

## Method (geom.py): pinhole + table plane, scale from the prior
- Table edges fitted in code (table.py): side vanishing point (687, −248), far/near-edge vanishing point (−16870, −231).
  The orthogonal-vanishing-point focal length is about 680 px, consistent in size with the lab f = 763 px.
- The plane normal comes from the horizon line (camera tilt ≈ 39°). Each tennis ball's distance comes from its pixel width and the 6.7 cm
  prior, using an exact sphere projection (tennis A 1.64 m, B 1.68 m). The table plane sits one tennis-ball radius below their centres; A and B
  agree within 3.5 cm on the plane height.
- Soccer ball: solved for the radius R such that the sphere on the centre ray, matching the 95.5 px width, has its centre R above
  the table plane → **D = 17.2 cm** at 1.385 m (17.6 using plane from A only, 16.9 from B only).
- Sensitivity: f = 680 → 17.3; f = 900 → 17.2; f = 350 → 17.9; horizon shifted ±80 px → 16.9 / 17.5. A ±1 px error in the tennis width
  changes D by about 3 %.

## Second route
Same-depth image ratio: 6.7 × 95.5 / 32.75 = 19.5 cm. This is an upper bound, because the soccer ball is nearer than the
tennis balls (occlusion). The plane route puts its depth ratio at ≈ 0.85, giving 17.2 cm. Both point to a small (about size 2) ball.
The depth_info route (24.5 cm using f fitted from the tennis balls, or 11.2 cm using the lab f) is rejected: it contradicts the prior and the occlusion.

Answer: 17.3 cm. Moderate confidence. The main risk is that the reference answer was built from the inconsistent depth_info.
