# q_2279 — shoulder breadth of the person (cm)

Prior: g = 9.8 m/s^2; no depth_info. The file and the question are both 24 fps.

## Scale (gravity.py)
I fitted quadratics y(t) to the bear's free-flight track from scene/tracks/teddy_bear.csv (toss 1: frames 17-22;
toss 2: frames 53-58). Pixel acceleration by reference point:
- cy: 2973 and 2931 px/s^2
- top edge: 3065 and 3086 px/s^2
- bottom edge: 2880 and 2777 px/s^2
- centroid: 2722 and 2907 px/s^2

Using cy, the scale is about 0.00332 m/px, with a spread of 0.0032-0.0036. That puts the bear plane at
Z = 763 * 0.00332 = 2.53 m from the camera.

Sanity check: the person's height of 508 px works out to 1.69 m, which is plausible. So the body is at roughly the
bear-plane depth (at most a few percent farther away).

## Shoulder width in pixels (widths.py)
I measured the silhouette row width at shoulder level (y about 240-260), outer sleeve to outer sleeve:
- frame 0: 293 to 402 px, 109 px
- frames 30 and 70: 288-289 to 396-397 px, about 107-108 px

This converts to 108 * 0.00332 = 36 cm projected width.

## Correction for torso rotation
The torso is turned about 30 degrees toward image right (3/4 view). For an elliptical shoulder section with a depth of
about 24 cm, the projected width is sqrt(W^2 cos^2 + D^2 sin^2) = 36, which gives W of about 39 cm. Adding about 2-3%
because the body is slightly farther away than the bear's flight plane gives about 40 cm.

## Answer and confidence
Answer: 40 cm. The uncorrected silhouette alone gives 36 cm.

Confidence is moderate. The rotation angle and torso depth are judged by eye, and only one reliable frame view of the
person is available.
