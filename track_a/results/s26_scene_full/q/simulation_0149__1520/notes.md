# q_1520 - height of the striped collision-warning marking on the pillar

Answer: **0.745 m**. Confidence: moderate-good, about ±4%.

## What the object is
The pillars carry striped corner guards (in this render they read as yellow/black; there are no other striped
markings on any pillar). The guard starts at the top of a black band and runs down to the floor:
black, then 4 yellow bands alternating with black, then a longer black foot.
Column profiles (measure_marks.py, frame 49, car gone):
- extinguisher pillar, left guard (x 549-560): top 767.0, floor 893.5 -> 126.5 px; right guard (x 696): 769.5-891.5 -> 122 px
- foreground right pillar, guard on its left edge (x 1473-1481): top 729, floor 936.7 (face base edge fit, base_edges.py) -> 207.7 px
- back pillar guard (x 1330): 781-879.5 -> 98.5 px
All of them have the same shape (top black ≈0.7 stripe pitch, foot ≈1.24 pitch), so they are the same model.

## Scale (ground plane, camera height from the tyre prior)
- Horizon y = 829: the ceiling-tube vanishing point (from the record). Checked independently: the line through the
  extinguisher-pillar base and the back-pillar base reaches y 828.7 at x = 4050.
- Camera height (rim2.py): rim ellipse centres frames 17-38 are front 829.5-831.1 and rear 827.2, with hub-to-tyre-
  bottom R ≈ 85-135 px. h = r(1 + (y_hub - y_h)/R) with r = 0.764/2 gives 0.384-0.391 (front) and 0.373-0.379 (rear),
  so h ≈ 0.381 m. The camera sits at about hub height.
- A marking standing on the floor has H = h * m_px / (y_base - y_h):
  extinguisher-left 0.381*126.5/64.5 = 0.747; extinguisher-right 0.381*122/62.5 = 0.744;
  foreground pillar 0.381*207.7/107.7 = 0.735; back pillar 0.381*98.5/50.5 = 0.743.
  These are three pillars at very different depths (about 8.5 to 18 m) and they agree to within 1.5%.
- Horizon sensitivity: if y_h = 827 the answer is 0.738, and if y_h = 831 it is 0.759, because h partly compensates.

## Second route: focal length from depth_info
- t = 0, the car's right-front tyre (image left, x≈60). On a contrast-stretched crop (stretch.py) the rim spans
  y 785-874 (hub ≈829.5) and the tyre bottom is at ≈898, so D ≈ 137 px.
- Focal length from vanishing points (tube VP (4050, 829), and the foreground-pillar face base gives VP (-939, 829)):
  f ≈ 2405 px. With that f, a distance of 14.244 m at x = 60 gives an axial Z ≈ 13.3 m and a predicted tyre size of
  138 px, against the 137 px measured. This reproduces depth_info.
- Camera height from this route: Z * (898 - 829)/f = 0.382 m, which matches route 1.
- The extinguisher-pillar base (y 893.5) is at Z = 13.3*69/64.5 ≈ 14.2 m, so H = 126.5*14.2/2405 ≈ 0.749 m.

## Ambiguity
"The pillar" could mean the centre pillar with the extinguisher (0.747) or the big foreground pillar (0.735). Both
are the same guard. I answer with the mean of the clean measurements: 0.745 m.
The time base does not matter here, because this is a static size.
