# q2600 – height of the pencil bag (cm)

The file is 24 fps, and question_fps is also 24. The pencil bag does not move, so I averaged frames 2–20 (`prof.py`). I also used a hue mask on frame 29 (`seg.py`, overlay in frames/mask.png).

## Measurements (px)
- Pencil bag (yellow pouch lying on the table, zipper strip on top, large front face): the image axis rises to the right
  at about 22 deg, and the axis length is about 107 px.
- Vertical extent per column, from the top of the pale zipper strip to the dark base line: x=665: 37, 680: 37, 695: 39,
  710: 39 (725: 31, near the rounded end). That gives about 38 px vertical, or about 35 px perpendicular to the axis.
  Within that, the pale top strip is about 8–10 px and the saturated front face about 23–27 px.
- Tennis balls at rest: A about 31.5 px, B about 30.2 px. Soccer ball: 105 px.

## Scale: the depth_info and the prior disagree
- With the lab focal length f = 763 px, the prior (6.7 cm) needs Z_A = 763*0.067/31.5 = 1.62 m and Z_B = 1.69 m. The
  given depths are 0.706 and 0.776 m.
- The scene geometry agrees with f about 763 and a camera distance of about 1.6 m. The table's vanishing points give
  f of about 716 px (orthogonality check), and the camera looks down at about 47 deg. A 22 cm soccer ball at f = 763
  would also sit at about 1.60 m. So the given depths are not consistent with the pixel sizes. The bag at 1.05 m would
  also be "behind" the tennis balls, which contradicts its image position.
- Route 1 (real size, image scale from the prior and the soccer ball): about 2.03 mm/px at the bag (Z about 1.55 m).
  The silhouette is 35 px, which is 7.1 cm, and it equals about 0.78*w + 0.63*h for a viewing elevation of about
  51 deg in the cross-section plane. The back face is hidden and the top strip is narrow. A roughly square or slightly
  tall cross-section then gives h of about 5.0–5.8 cm. The range over plausible shapes is 4.4–8.7 cm.
- Route 2 (the method card taken literally): h = 1.05 m * 35–38 px / 763 = 4.8–5.2 cm.

## Answer
5.3 cm, a compromise between the two routes, which agree to within about 10 pct.
Confidence: low to moderate. The cross-section shape (the split between width and height) and the inconsistent
depth_info are the main uncertainties.
