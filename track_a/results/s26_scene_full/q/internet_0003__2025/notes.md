# q2025 – pepperoni diameter (cm); prior: Monopoly money width = 7.5 cm

Internet video, near top-down static scene (handheld drift ~1 %, irrelevant for a static size ratio). The time base
does not matter for a size question. Single planar scale from the prior, as the annotators did. All measurements on frame 29.

## Scale (prior object)
"Width" of a bill = short side (7.5 cm is close to a real Monopoly bill's short side; the long side is ~2x that).
- 500 bill on top of the pile (upside down): left short edge (1862,378)->(1870,525) = 147 px (zoom frames/b500top.png).
- 500 bill in the middle (rotated -13 deg, "MONOPOLY" header): short edges 150 and 147 px; long side ~300 px.
- 100 bill: ~152 px, but partly overlapped.
- 1 bill (isolated on the wood, bill.py, minAreaRect): 315 x 179 px (area/length 169 px). It is ~15 % wider than the
  500s for unclear reasons (looks slightly larger overall); treated as an outlier.
Used short side = 148 px (500 bills) -> 7.5/148 = 0.0507 cm/px.

## Pepperoni
pep_radial.py: for 18 clearly visible slices, rays from a rough centre, strongest dark->light step in L (pepperoni ->
cheese), robust circle fit (overlay frames/pep_radial_f29.png, the fits sit on the edges). Diameters 122-137 px,
median 128.5, mean 128.6, std 4.0 (ellipse axes median 124 / 133). The cleanest slices (A, C, E, G, I, N) give 125-132.
Pepperoni D = 128 px.

## Answer
128 px x 7.5/148 = 6.49 cm -> **6.5 cm**.
Other reading: scaling from the 1 bill (~172 px) would give 5.6 cm. Using the long side as "width" (~305 px) would give
3.1 cm, but then the pizza (~990 px across) would be only 24 cm across, so this reading is rejected.
Check: pizza diameter 990 px -> 50 cm, i.e. pepperoni/pizza = 0.13. A large pizza, but plausible.
Confidence: moderate. The pepperoni pixel size is solid (±3 %); the main uncertainty is which bill the annotators measured.
