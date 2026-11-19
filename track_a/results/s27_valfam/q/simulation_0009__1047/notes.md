# q_1047 – width (shorter side) of the wooden pier

**Answer: 1.64 m.** The plausible range is about 1.59–1.69 m.

The file runs at 22.853 fps, but question_fps is 24. "t = 1 s" is therefore taken as frame 24, and the scene/ frame column is used rather than its seconds.

## Geometry used
- The pier deck is a horizontal rectangle. Its short side is the left end, which is seen strongly foreshortened: it runs left and away from the camera.
- Edges were fitted in code on a time-averaged frame (frames 40–65, static scene; `vp.py`). Sub-pixel gradient peaks were fitted with lines and outliers rejected:
  - A, front top edge of the deck: y = −0.13771 x + 764.48 (rms 0.14 px).
  - C, bottom of the front beam: slope −0.1407.
  - B, back top edge: slope −0.1228.
  - D, bottom edge of the left end face: y = 0.2557 x + 637.76 (rms 0.5 px).
- Corners (`corner.py`, `final.py`):
  - Far-left top corner FL = (294.65, 705.25).
  - Near-left top corner NL ≈ (343, 717.2). It was found in two ways that agree within 0.6 px: A crossed with the end-face top line, and D crossed with C, raised vertically onto A.

## Camera
- **Level camera.** Vertical edges are essentially parallel: cabin posts, window and corner edges, and the pier posts all lean with dx/dy ≈ 0.000–0.008 (`verticals.py`). A camera pitched up to put the horizon at y = 614 would make them lean about 0.025–0.06.
- **The scene/ record's horizon is wrong.** Its horizon at y = 614.6 and its "motion VP" (−103, 615) come only from the template scale s(t). That s(t) also implies a depth ratio of 1.151 between frames 0 and 24, while depth_info gives 1.112. The scale track is biased, so neither number was used.
- **f and horizon row vh, solved jointly:**
  1. The pier's long-side and short-side vanishing points lie on the horizon and are orthogonal. This gives f as a function of vh: f = 1003 at vh = 540, 986 at 543, 970 at 546, 953 at 549.
  2. The boat gives a second relation (`boat_vp.py`). Its two given distances (11.827 m at frame 0, 13.154 m at frame 24) plus the 1.5 m/s prior give f = 920–978. Its motion is then horizontal (slope ≈ 0°), with its vanishing point at row 538–549.
  3. Both relations hold together at f ≈ 1003 / vh ≈ 539 (waterline point) and f ≈ 952 / vh ≈ 549 (box-centre point). The displacement over the second is 1.49 m in both cases, matching 1.5 m. I used f ≈ 980 (HFOV ≈ 58°) and vh ≈ 544 ± 5.
- **Water-plane check (`water_check.py`).** The camera height above the water was found in two ways that agree for every vh:
  - From the pier, using the mirror midpoint of the end face and its reflection (water at y = 729.4): 3.30 m.
  - From the boat waterline at its given distance: 3.33–3.41 m.
  - The agreement is best for vh ≈ 535–545. The deck sits 0.42 m above the water.

## Width
- The camera height above the deck plane was set so that the deck centroid is 18.92 m from the camera (H ≈ 2.88 m). FL and NL were then back-projected onto that plane (`width.py`, `final.py`).
- The two back-projected deck edges come out at 89.5–90°, which confirms the rectangle.
- Results: W = 1.602 (vh 540), 1.629 (543), 1.657 (546). Long side L ≈ 5.0 m.
  - Taking the pier origin 0.3 m lower changes W by less than 0.3%.
  - Changing the near-corner definition changes W by less than 0.1%.
- The dominant uncertainty is the horizon row, about +0.9% of width per pixel. This gives ±3–4%.

## Confidence
Moderate to good. The answer assumes the pier is aligned with the world axes, so the bounding-box width equals the deck width.
