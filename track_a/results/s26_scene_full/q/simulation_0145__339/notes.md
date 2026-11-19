# q339: tire diameter (prior: rocket length = 2.9 m)

This is a 2D side view with a static camera, at 24 fps (the file and the question agree). The truck is seen side-on
and the rocket flies in the same plane, so I used a single metres-per-pixel scale taken from the rocket length.

## Rocket length in pixels
- `rocket_len.py` takes |frame - frame0| along the fitted flight axis and band-sums it (±13 px). The 50% crossings
  give 199-208 px over frames 13-18, which matches the scene record's 202 px.
- `rocket_len2.py` uses the centre-line profile instead (|offset| ≤ 2 px), with ends at 50% of the body level. It
  gives 204.0-210.0 px over frames 15-21, median about 206. The band-summed profile reads the tapered nose a few px
  short, so the centre line is better at the tip. Motion blur is symmetric, so the 50% crossings are blur-invariant.
- Best value: L = 205 px (±3).

## Tire diameter in pixels (`wheel_measure.py`, frame 27, saturation: grey tyre vs orange sand)
- Middle wheel: horizontal extent x 986.5-1084.5, which is about 98 px (rows 823-829).
- Rear wheel: rows 817 and 826 give 99 px.
- Bottom contact is at y ≈ 865.5 and the hub centre at y ≈ 818, so the vertical radius is about 48 (slightly
  flattened at the ground).
- The front wheel's left edge is lost in the shadow, so I did not use it.
- Best value: D = 98.5 px (±1.5).

## Answer
D = 98.5 / 205 × 2.9 = **1.39 m**. With the record's 202 px it would be 1.41 m, so the range is about 1.37-1.42 m.

Second route: the record's independent reading (wheel 98 px, rocket 202 px) gives 1.41 m, which agrees within 2%.
Confidence: good, about ±3%.
