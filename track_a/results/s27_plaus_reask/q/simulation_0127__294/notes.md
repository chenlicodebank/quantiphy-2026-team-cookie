# Q294: length of the dark green car (m)

The camera looks straight down at the street (2D setup) and does not move. The file and the question both use 24 fps.
The dark green car is the coupe parked at the lower curb on the right (called `dark_sports_car` in scene/; it is
dark green, as the contrast-stretched crop `frames/car_edges.png` shows). It does not move.

## Scale from the prior (bike speed = 24 m/s)
- Pixel speed of the cyclist:
  - scene/ track: mean step 31.64 px/frame over frames 2–53. Over frames 15–51 it is 31.63 px/frame.
  - My own NCC template match (`check_bike.py`, bike + rider template from frame 30): 31.79–31.81 px/frame over
    frames 15–51 (one outlier frame dropped).
  - I used 31.7 px/frame = 761 px/s.
- Scale: 24 / 761 = 0.03155 m/px.
- 24 m/s (86 km/h) is not a realistic speed for a cyclist, so the scene is taken as scaled to the prior, and the
  prior's scale is used as the benchmark rule says. Under this scale the bike (85 px) is about 2.7 m long, which
  confirms the scene is scaled up by about 1.5x.

## Car length in pixels
- Measured in code (`measure_car.py`, `measure_car2.py`) from luminance and chroma profiles along the car's axis
  (rows 740–800), on frames 45 and 5:
  - nose at x ≈ 1686–1687, rear at x ≈ 1916–1917, so about 230 px.
  - The edges drawn on the zoomed crop (`draw_car.py`) put the body at 1687 → 1916, which is 229 px.
- The scene/ record gives 226 px (read by eye).
- I used **229 ± 3 px**.

## Answer
229 px × 0.03155 m/px = **7.22 m**.

The error is about ±2%: ±3 px on the length and about 0.5% on the speed. With the record's 226 px the answer would
be 7.13 m.

If the scene were at real-world scale instead, the bike length would set it (about 1.7 m / 85 px), giving about
4.6 m. That reading is not used, because the prior is exact and sets the scale.
