# q1180 — diameter of the wheel of the moving bicycle (simulation_0045)

Answer: **0.64 m**

The file and the question both run at 33 fps, so t = 1 s is frame 33 and t = 2 s is frame 66.
The asked object is the blue bicycle ridden away from the camera on the road, not the parked cream bike. I measured its rear wheel, the one nearest the camera.

## Wheel size in pixels (manual reads of zoomed crops: frames/z*.png, frames/q10.png)
The bike is seen from behind, so the wheel appears as a thin, nearly vertical ellipse. A wheel standing upright projects its full diameter vertically.
- Axle: a horizontal bar where the rack struts end at the dropouts. Its height scales with the bike, unlike the pedals.
- Tyre bottom: the lowest dark tyre row.
- D_px = 2 × (bottom − axle).

| frame | axle y | bottom y | D_px |
|---|---|---|---|
| 6 | 667.5 | 749 | 163 |
| 10 | 637 | 711 | 148 |
| 15 | 600 | 669 | 138 |
| 20 | 570.5 | 636 | 131 |
| 25 | 544 | 605 | 122 |
| 33 | 511.6 | 563.6 | 104 |
| 40 | 487.5 | 535 | 95 |
| 50 | 457 | 501.3 | 88.6 |
| 60 | 433.4 | 472.7 | 78.6 |
| 66 | 421.4 | 458.1 | 73.4 |

Check: the tyre top sits just under the rack. Reading top to bottom gives the same D_px within 1–2 px at frames 6, 10 and 33.
D_px divided by (bottom − horizon row) stays at 0.296 ± 2 % over all frames, so the reads have no size-dependent bias.

## Camera
- Static camera. Principal point assumed at the image centre (960, 383).
- Horizon / street vanishing point from receding curb and facade lines (vps.py): (580, 205). Left set gives y = 208, right set y = 199.
- Vertical vanishing point from 88 vertical segments (LSD): y ≈ 21 000. The camera looks down by about 5°.
- f from the vanishing points: f² = (Yv − cy)(cy − yh), so f ≈ 1915 px. Assuming those two vanishing points are at right angles gives 1912.
- f from speed and depth (focal3.py, diameter2.py): the depths and the 4.87 m/s speed give an angle of 13.13° between the motion and the line of sight at t = 1. Put the bike origin on the ground at the bike centre and require this angle against the street vanishing point: f ≈ 1800–1830. This route is very sensitive to the given values: a 1 cm change in a depth moves f by several percent.
- Adopted f ≈ 1860 px (HFOV ≈ 54°).

## Depth of the wheel
- The given depths are to the bike origin. Its path is fixed by the depths and the speed.
- Using the ground-contact rows (z ∝ 1/(y_bottom − y_horizon)), the rear wheel is about 0.65–0.9 m closer to the camera than the origin, so the origin is near the middle of the bike.
- The rear-wheel depth from this model was projected through the pitched pinhole camera (diameter.py, diameter2.py).

## Results
- f = 1870, horizon 205, wheel offset fitted at 0.88 m: D = 0.634 m (sd 0.012 over 10 frames, no trend with frame).
- Same but horizon 200: 0.643. Horizon 210: 0.624.
- f = 1830: 0.647. f = 1915: 0.619.
- Wheel offset 0.65 m (from speed and contact rows only, without the depth difference): about 0.645 m.
- Second route, ignoring the wheel offset (wheel at the origin depth): 0.67–0.69. This is an upper bound, but it is contradicted by the size trend.

## Final
0.64 m, about ±4 %. The main uncertainties are the focal length (±3 %) and the depth of the wheel relative to the bike origin (±2 %).

## Caveats
- The scene record's cyclist ground_y is the lowest mask point. It sometimes catches the front wheel or the shadow, so I did not use it.
- The pedestrian's depth_info does not match their pixel heights. The pixel-height ratio between t = 1 and t = 2 is 1.12, but the depth ratio is 1.07, so the pedestrian data was not used for scale.
