# q_2269 - shoulder breadth of the person (cm)

Prior: g = 9.8 m/s^2; no depth_info. File fps = question fps = 24.

## Scale from gravity (fitg.py, fitg2.py)
Toy free-flight frames 16-22 and 51-59 (scene/tracks/toy.csv, diff masks). Joint parabola fit (common
acceleration, separate offset/velocity per toss):
- top edge of toy (best_y0): 2925-2969 px/s^2, rms 0.4 px, stable across frame windows; single tosses 2880-3045.
- centroid/bottom edge vary 2500-3600 because the toy rotates and its tail/paws swing; not used.
=> a = 2950 px/s^2 -> 9.8/2950 = 3.32 mm/px (at the toy's depth).
Check: person height 507 px -> 1.68 m (plausible). With f = 763 px this scale means a depth of about 2.53 m.

## Shoulder width in px (shoulder.py)
Row gradient edges at the shoulder level (y 228-248) on frames 0, 5, 35, 70:
- frames 0/5: left 295-298, right 393-400 -> 96-104 px (about 100-102 at y 236-248)
- frames 35/70: 291-295 to 387-391 -> 93-98 px (body turned a bit more)
Outer shoulder (deltoid/sleeve) width is about 102 px; acromion-to-acromion would be about 91 px.

## Result
102 px x 3.32 mm = 33.9 cm. The person stands slightly turned and a little behind the toy's plane, so I
applied a small upward correction (about 3%) -> **35 cm**.
Second route: person height 507 px at the same scale gives 1.68 m, and a shoulder/height ratio of 0.20-0.21
is typical. Confidence: moderate (±10%). The main uncertainties are the body rotation and which shoulder
definition is meant.
