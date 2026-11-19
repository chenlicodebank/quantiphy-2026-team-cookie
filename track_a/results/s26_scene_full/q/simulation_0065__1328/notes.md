# q1328 – height of the walking pedestrian (simulation_0065, 3D)

The file and question_fps are both 24, so frame = round(t*24). That puts t=0.58 at f14 and t=1.58 at f38.

## Focal length (main route: the pedestrian's depth_info)
- The pedestrian walks right along the near-right sidewalk, parallel to the cross street. Its depth goes from 25.3568 m (f14) to 25.9200 m (f38).
- I found the horizon and the cross-street vanishing point from the background curbs (`curbs.py`). The near-back curb (slope -0.0395) and the far curb (slope -0.027) cross at about (20300, -200). The forward-road VP from the record is (800, -208). Both agree on a horizon at y ≈ -205 with roll ≈ 0.
- Pelvis x is taken from a linear fit to the white T-shirt centroid track (4.367 px/frame, residual 1 px). That gives u14 = 1896.3 and u38 = 2001.1; I used rows of about 497 and 495.
- Solve (`solvef.py`): P14 = d14·ray(u14). Move along the walking direction w (toward the cross-street VP) until the point projects to u38, then require |P38| = d38. Results:
  - f = 2184 (fitted x, VP 20400); 2206 or 2161 with VP 19500 or 21500
  - f = 2244 using the raw per-frame centroids
  - f = 2236 using the shirt-track slope as the direction
  - **I used f ≈ 2215 ± 60.**
- Cross-checks:
  - The van's motion with a = 4 m/s² (`vanacc.py`, `vanspeed.py`) is consistent: it starts from rest near t = 0, and the depth-based displacement f14→f38 is 4.25–4.32 m against 2·(1.58²−0.58²) = 4.32 m. This is only weakly sensitive to f, so it does not pin f down.
  - At f = 2215 the van is 2.52 m wide mirror to mirror, which is plausible.

## Pixel height (`pedmeasure.py`, `pedheight.py`, `combine_h.py`)
- Head top comes from a background-difference mask (threshold 18). The shadow test is not used for the top because it would erase the dark hair.
- Sole comes from a shadow-suppressed mask (threshold 30, at least 2 px per row), which removes the cast-shadow spike under the feet.
- Head to sole is 150–165 px over the gait (median 158). The record's 148–162 px was a few px short at the head.

## Metric height (`height3d.py`)
- For each frame I reconstruct the pelvis in 3D along the walking line, anchored on d14. This reproduces d38 = 25.915 against the given 25.920.
- I then find how far along the ground-normal "up" axis the head-top and sole rows lie.
- At f = 2215: median 1.79 m, p75 1.81, p90 1.84, min 1.70.
- At f = 2150 / 2280: median 1.85 / 1.74.
- The question does not say which height, so I use the standing or upper-walking height, which is about the median to p75 value.

**Answer: 1.80 m.** Confidence is moderate (about ±4%). The main uncertainty is f, which depends on the pelvis-x proxy (±2 px gives ±35 in f) and the walking direction.
