# q1200 — distance between the near door's left pillar and the far door's right pillar

Answer: **3.28 m**

The answer is the 3D distance between the centres of the two pillars. The file rate and question_fps are both 33.
The camera is static, so all measurements were taken on frame 98, where the pedestrian no longer covers the stoops.

## Which objects
- **Near door**: the arched stone door of the grey townhouse on the right. It has a pilaster on each side with a carved
  corbel on top.
  - Its **left pillar** is the farther pilaster, at image x ≈ 1478/1491–1520, centre ≈ 1502.
  - "Left" means the same pillar under both readings: facing the door from the street, the farther pillar is on your
    left, and it is also the one on the image left.
- **Far door**: the door of the green clapboard house just beyond it. It has two round columns with capitals, at
  x 1327.5–1348 and 1367.5–1392.
  - Its **right pillar** is the nearer column, centre x ≈ 1380.
- Each door has a stoop that runs perpendicular to the facade, from the sidewalk up to the door.
  - The near stoop has stone newels with urns. The far stoop has wooden posts on stone pedestals.
  - The handrails visibly end at the door pillars, so each stair's two sides line up with that door's pillars.

## Scale and camera (prior and depth_info only)
- **Horizon**: vh = 535.5, the vanishing point of the facade and curb lines (vp.py, 34 line segments). The VP is at
  (959, 534–535.5): the camera looks straight down the street and is level.
- **f·h (focal length × camera height)**: the cyclist's tyre-contact track gives 1/(y − vh) linear in frame (refit.py,
  rms 0.85 px). With the prior speed of 4.87 m/s, Z_road = C/(y − vh) with C = f·h = 3011.
  - Check with the bike's depth_info: its distance grows 4.84 m between t=1 and t=2, which gives C = 2993 (0.6 % lower).
  - The bike's absolute distance is about 0.6 m larger than the tyre-contact Z. This fits an origin ahead of the rear
    tyre.
- **Focal length**: from the manhole circle, f = (v − vh)·W/H = 1899 px. That gives a camera height of 1.59 m, a cyclist
  of 1.7 m and a pedestrian of about 1.75 m, all plausible.
  - f only enters through small terms (the sidewalk height term, X and Y).
- **Sidewalk height**: the left curb face is about 0.08 of (v_bottom − vh), so s ≈ 0.13 m (curbprof.py).
  - Sidewalk points therefore use Z = C(1 − 0.08)/(v − vh).
- **The human depth_info is not usable here.** It gives 19.0 m at t=1, but the pedestrian's feet on the ground plane
  and his change in size (the bike's size change matches its depth) put him at about 12 m. The origin of that
  human model seems to sit away from its body. It is not used.

## Measurements (frame 98, bottoms.py, urns.py, pilprof.py)
- **Newel pedestal bottoms on the sidewalk** (the face toward the camera):
  - Near stoop: urn A side at y 787 and urn B side at 826, giving Z of 11.16 and 9.69 m (pedestal centres).
  - Far stoop: dark post at y 709 and light post at 726.3, giving Z of 16.07 and 14.62 m.
  - Both stairs come out about 1.46 m wide.
  - Check: the urn bulb widths are 39.2 and 45.0 px, a ratio of 1.148, against a depth ratio of 1.152 from the bottoms.
    The urn centres both sit at X ≈ 2.03–2.06 m, the street end of the stoop.
- **Facade plane**: assuming each door is centred on its stair, both doors put their pillars at X ≈ 3.21–3.23 m
  (f·X = 6141 near and 6102 far). The facades line up.
  - The far columns then land at Z 16.15 and 14.54 m, matching the stair sides.

## Pillar centres (camera frame, metres)
- **Near-left pilaster**: Z between 11.26 (one facade plane taken from the far door) and 11.33 (door centred on its
  stair). The rail on plane Z = 11.16 ends at this pilaster's near side face, so its centre is about 0.1 m farther,
  near 11.29.
- **Far-right column**: Z = 14.54 (facade model) to 14.62 (rail plane).
- **Heights**: the pillars' mid-heights differ by about 0.16 m, and their X by about 0.02 m.
- **Distance**: 3.21 (centred model), 3.28 (one facade plane), 3.33 (rail plane plus half the pilaster width).
  The answer is **3.28 m**.

## Sensitivity and confidence
- **Horizon** (534.3 to 537.5 px): ±0.2 %, because C is refitted with it.
- **Sidewalk height** (s/h from 0.06 to 0.09): −1 % to +2 %.
- **Pedestal bottoms** (±3 px): ±2–3 % each.
- **Pillar centres** (±3 px): ±1–2 %.
- **Model choice**: the rail-plane-only reading gives 3.46 m, an upper bound.

Overall uncertainty is about ±5 %. The main risk is in identifying the objects: whether "far door" means the green
house door, which is the most likely reading.

## Scripts
getframe.py, zoom.py, curbprof.py, bottoms.py, urns.py, pilprof.py, vp.py, refit.py, compute.py (first pass), and
compute2.py (final).
