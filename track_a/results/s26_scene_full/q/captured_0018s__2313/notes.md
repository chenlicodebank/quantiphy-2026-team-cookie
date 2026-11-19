# q2313 – height of the right person (cm)

Right person = near person (black t-shirt), depth_info 2.002 m. File fps = question fps = 24. f = 0.5959*1280 = 763 px, c = (640, 360).

## Measurements (person_extent.py, frames 0/10/20/48 – she stands still)
- Head (hair) top y = 102 (f0–20; 107 at f48 after moving her head).
- Far (front) shoe sole bottom y ≈ 673; near (back) shoe is cut by the image bottom edge (sole ≥ 720).
- Left (far) person: top 173, shoe bottom 577, depth 3.13 m.

## Route 1 – method card (depth × pixel extent / f)
Extent 102 → ~718 (visible bottom; the real sole is a little lower) = 615–618 px → 2.002*615/763 = 161.4 cm (162 at 618 px).

## Route 2 – ground-plane geometry
Left person's feet at 577 at Z=3.13 m → camera height = 3.13*217/763 = 0.89 m. Ground under the right person's
centre plane at Z=2.002 m → y = 360 + 763*0.89/2.002 = 699, which matches the midpoint of her two soles (673, ~722) → ≈697,
so depth_info works like the Z-depth of her centre (the Euclidean reading, Z = 1.82 m, does not fit the feet as well).
Height = 2.002*(698 - 102)/763 = 156.4 cm (camera height 0.89 m + 0.677 m above the optical axis).

## Checks
- Gravity check: the soccer ball's free fall f30–35 gives 2859 px/s² → Z = 9.8*763/2859 = 2.62 m vs given 2.80 m (about 7%), so f = 763 holds up reasonably well.
- Left person comes out at 3.13*404/763 = 166 cm, which is plausible.

## Answer
Route 1 (161–162) and route 2 (156.4) differ by about 3%. Route 1 overstates because the near foot is closer to the camera than her
centre. I answer between them: **159 cm**. Confidence: about ±4%.
