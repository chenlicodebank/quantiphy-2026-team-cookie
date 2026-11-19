# Q1039 – minimum distance, pier outer end to boat, t = 3 s

**Answer: 5.68 m** (pier origin to boat origin, 3D). I agree with C1.

## Time base
The file runs at 22.80 fps and the question at 24 fps. I used 24 fps, so t = 3 s is frame 72. The clip ends at
frame 65, so the boat's position is extrapolated with a linear or quadratic fit to the bow track. Both fits agree.
At t ≈ 3 s the boat is directly in front of the pier (closest approach at frame 72-73), so the answer barely
depends on the time base or the extrapolation.

## Where the candidates part ways
The step that splits them is **which point is used for the pier**:
- **C1 (5.68):** the pier object origin, placed at the given 11.579 m along the ray through the pier deck.
- **C3 (3.34):** a constructed "outer (lakeward) deck edge" at 9.3 m depth. It assumes the origin is the deck's
  centre and rescales by perspective.
- **C2 (1.33):** the near deck edge, found from the water-plane height, at about 7.0 m depth.

My own check: the deck's front edge lies at about Z ≈ 7.2-7.7 m. I got this from the water contact under the deck
front at v ≈ 686 (deck front face and its reflection are symmetric about it) and a camera height of about 1.1-1.3 m
from the boat waterline. The deck's front-to-back width ratio is 178/120 px. So the given 11.579 m point is **not**
the lakeward edge. It lies near the shore end or under the deck. The benchmark convention is that the distances
between objects are taken between object origins, and depth_info is the distance to the origin. The only metric
pier position given is that origin, so I used it. C2 and C3 replace the given pier distance with their own surface
point, which the reference convention does not do.

## Measurement (solve.py)
- Boat origin: bow_x from scene/tracks/boat.csv + 324 px (half of the 648 px full length), at v = 697.
- I assumed the boat moves at constant depth: the hull height stays constant to within ±2 px. The two given boat
  distances (7.452 m at frame 0, 6.655 m at frame 24) then give f = 1001 px and Z = 5.85 m.
- Prior check: 0.75 m comes out at 128 px, against about 135 px visible from post top to waterline. That
  visible figure includes about 20 px of near-side top-down view, so the prior is consistent. The boat is about
  3.8 m long, which is plausible for a rowboat.
- Boat at frame 72: u ≈ 572, giving (0.19, 0.92, 5.85) m.
- Pier: the ray through the deck centre (549, 618-645), scaled to 11.579 m.
- Distance: **5.67-5.69 m**.

## Sensitivity and second route
- Moving the boat's origin ±30 px gives 5.62-5.75 m. This changes f to 986-1015 px.
- Choosing the pier pixel row anywhere from 618 to 645 changes the result by ±0.01 m.
- Linear and quadratic extrapolation agree, and frame 72 versus 73 changes the result by less than 0.002 m.

## Alternative reading
If "outer end" means the lakeward deck edge as a surface point, the distance would be about 1.5-2 m (my front
edge at about 7.5 m). It would be about 3.3 m if the origin were assumed to be the deck centre (C3). I did not use
either, because the reference uses object origins.

Confidence: moderate. The numbers are about ±3 %; the main risk is the interpretation of "outer end".
