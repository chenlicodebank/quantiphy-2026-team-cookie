# q_1776: height of the green car (m)

**Answer: 1.25 m.** Confidence is low to moderate: the plausible range is about 1.1–1.4 m.

The file's fps and question_fps are both 24. t = 0.58 s is frame 14 and t = 1.58 s is frame 38.

## Objects and the depth labels
- The green car is the parked teal BMW-style coupe at the upper right. It is static.
  - On a median background image, its mask has bbox x 1441–1625 and y 334–413.
  - Near-side wheel contacts: front (1512.9, 413), rear (1591.4, 397). The roof top silhouette is at y = 334, x 1528–1558 (`greenmask.py`).
- The prior is about the white car, which is the van: it accelerates from rest at frame ~1, in a straight line.
- **Depth labels look swapped.** The "white car" depths (19.65 → 16.55 m) don't fit the van; the "yellow car" depths (23.59 → 19.99 m) do. Evidence:
  - With the labels as given, the taxi (lower in the image, nearer the centre) would be farther away than the van and the pedestrian.
  - With the labels as given, the van's acceleration comes out at 3.2–3.3 m/s² for any plausible f.
  - With the depths swapped, the van gives a = 3.95–4.08 m/s² for f = 900–1100. The early (2–40) and late (30–71) frame windows agree, and t0 ≈ 0.03 s (`vanfit2.py`).
  - So I used 23.59/19.99 for the van and 19.65/16.55 for the taxi.

## Focal length
- Van kinematics (a = 4 m/s² from rest at t0 ≈ 1/24 s): the 14→38 path is 4.17 m, which needs f ≈ 975 px. The box-model fit of the van's right edge across all frames gives a = 4 at f ≈ 950–1000.
- Pedestrian sanity check at f = 975: height ≈ 1.7 m, pelvis 0.91 m.
- I used f = 975 px (HFOV ≈ 96°), with the principal point at the image centre.

## Ground plane
- **Up vector:** fitted from three things:
  - The van, bike and pedestrian 3D path directions must be horizontal (from the depths plus pixel tracks).
  - The pedestrian's lean in the image (a vertical vanishing-point cue). Head→feet gives 19.8°; head→hip 22.4°; neck→hip 16.8° (`pedlean.py`, `pedlean2.py`).
- **Camera height:** from the pedestrian's foot rows, with the feet directly below the 3D pelvis track (`final.py`). This gives hc ≈ 6.5 m and pitch ≈ 27°.
- **Green car:** the two wheel contacts are intersected with the ground plane, giving the car axis, wheelbase and a distance of about 22 m.
  - The car centre is placed 0.27 × wheelbase toward the far side.
  - The roof silhouette point is assumed 0.19 × wheelbase beyond the centre line, plus a 1.5 % × wheelbase crown drop.
  - H is solved so that point projects to y = 334 (`final3.py`, `final4.py`).

## Results and sensitivity (f = 975)
| Lean | H |
|---|---|
| 17° | 1.36 m |
| 19.8° | 1.25 m |
| 22.5° | 1.15 m |

- Changing f by ±50 px moves H by about ∓0.1 m.
- The roof-offset assumptions move H by ±0.03 m.

## Second routes and checks
- **Vehicle-origin plane:** van, taxi and bike origins at a common height h0, with the pedestrian's feet on the ground (`final3.py`). At f = 1000 this gives H = 1.18 m, with a predicted lean of 21.3°, close to the measured lean. This agrees with the main route.
- **Shape checks pointing to a lower lean (higher H):**
  - The green and purple parked cars come out parallel only if the lean is about 15–17°.
  - Both cars come out perpendicular to the van's road at a lean of about 17–20°.
  - The green car's wheelbase/height ratio matches a real E24 coupe (≈1.95) at a lean of about 17°.
- **Right-angle checks pointing to a higher lean (lower H):** the front-face edge versus the wheel line on both parked cars suggests a lean of 23° or more. These edges are short and rounded, so I gave them little weight.
- **Contact-point check:** the vehicles' lowest-pixel ground contacts land 0.8–3 m in front of their origins. This is consistent with the origins being at the rear axle, or with the plane placing points slightly too near. The bike, which has small offsets, gives a distance ratio of 1.00–1.02.

The final 1.25 m is the central value (f = 975, lean 19.8°).
