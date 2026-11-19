# Q1188: length of the moving bicycle (m)

Prior: the moving bicycle's wheel diameter is 0.65 m. File fps = question fps = 33.

## Method
- Object: the dark-blue bicycle ridden right to left. I measured frames 40-70, where the bike is clear of the walker (f13-33) and of the pink parked bike (f73 on).
- `circfit.py`: a gradient circle fit on each wheel. It locks onto the silver rim/tire edge (r ≈ 44 px), which gives the wheel centres.
- `outer.py`: radial edge search for the OUTER tire edge (dark tire to lighter background) on the front wheel's left side and the rear wheel's right side. The outer radius uses the fitted centres. Overlay checked in `frames/outer_55.png`: the circles sit on the outer tire edge.
- Length in px = (rear centre x + rear outer r) − (front centre x − front outer r). Nothing sticks out past the tires: the rack, reflector, lamp and fenders all lie inside the wheel extents (checked on zoomed crops, `frames/c50.png`). So length = wheelbase + one wheel diameter.
- Scale: the wheel diameter, measured horizontally. The bike's heading is about 6° off the image plane (from the depth_info: depth goes from 12.62 to 13.21 m while it travels about 4.8 m sideways; `geom.py`). The horizontal wheel extent and the bike length are foreshortened by the same factor, so their ratio is scale-free.

## Measurements
| Frames | L/D | Length |
|---|---|---|
| f40 | 253.5 px / 97.75 px = 2.593 | |
| f50 | 248.0 / 96.0 = 2.583 | |
| f60 | 242.5 / 94.75 = 2.559 | |
| f70 | 237.0 / 93.25 = 2.542 | |
| median, f40-70 | 2.572 | 0.65 × 2.572 = **1.672 m** |
| f40-50 window | ~2.585 | 1.680 m |
| f60-70 window | ~2.556 | 1.661 m |

## Second route
- Mask extremes: leftmost and rightmost tire edge points (the `extremes` column) give the same pixel length as the centres-plus-radii route, to within 1 px.
- Depth/pinhole route at f66 (t = 2 s, depth 13.21 m): the wheel gives f ≈ 1900 px, so the length is about 239 px × 13.2 / 1900 ≈ 1.66 m. This is consistent, though not independent of the prior.

## Notes
- The scene record's "length ≈ 257 px at f35" comes from a bbox that includes walker and shadow pixels. Its Hough radii (about 48) are noisy.
- A small yaw (about 6°) could change a world-axis bounding box slightly. This is ignored.

**Answer: 1.67 m.** Confidence: good, about ±3%.
