# q_1599 — height of the table lamp (m)

The file and the question both run at 24 fps. Principal point is taken as (960, 540).

## Focal length (focal.py, speedcheck.py)
- I used the cat torso centre from scene/tracks/cat.csv, smoothed with a polynomial fit: (406.8, 841.1) at f0 and (854.7, 810.4) at f24.
  I back-projected these with the given depths 4.199 m and 4.481 m and required |P1-P0| = 0.94 m over 1 s.
  That gives **f ≈ 2090 px**. The prior ranges 0.93-0.95 m/s give 2060-2126.
- Check: I projected the cat onto its 3D path line and computed the mean speed for 0-1 s and 1-2 s.
  At f = 2090 these are 0.936 and 0.928 m/s, so the speed stays nearly constant. At f = 1500 or 2500 it would not.

## Horizon and camera height (horizon.py, consist.py)
- The back-wall/floor line and the right-wall/floor line are perpendicular on the floor.
  With f = 2090 their vanishing points put the horizon at **y_h ≈ 544**, so the camera is about level.
- The cat path's 3D vanishing point (from the depths) is at x ≈ 4990. That point lies on the cat's image line at y ≈ 530-547, which fits.
- Mirror bottom centre, at pixel (1525, 812) and distance 6.407 m: Z = 6.14 m, which gives camera height h ≈ 0.787 m.
- Closest bench leg (front-left), at distance 5.69 m: its origin is at Z ≈ 5.52 m whether the origin is the leg's centre or its top.
  Its foot at y = 838 then gives h ≈ 0.776 m. I used h ≈ 0.78-0.79 m.

## Lamp
- Profiles in code (profile.py, prof2.py) at x = 1370: shade top at y ≈ 398, base contact shadow at y ≈ 661, so **262 px tall**.
- Table top: back edge y ≈ 652, front edge y ≈ 663 at the lamp column. The lamp base sits about 2 px behind the front edge.
- Route 1:
  - Front edge of the table top at the leg column: Z ≈ 5.50 m (leg Z 5.52 minus a small overhang).
  - The bench is rotated about 28° (its length runs toward the vanishing point at x ≈ 4847). Moving 70 px left along the front edge to the lamp column takes about 0.11 m off: Z ≈ 5.39 m.
  - Lamp front contact: Z ≈ 5.39 × 119/117 ≈ 5.48 m.
  - Height = 262 × 5.48 / 2090 = **0.690 m**.
- Route 2:
  - Table-top height H_t ≈ 0.469 m (leg top height 0.39 m plus the 30 px apron and top above it, at Z 5.5).
  - Height = 262/(661-544) × (h - H_t) = 2.24 × 0.318 = **0.712 m**.
- **Answer 0.70 m** (mean of the two routes).

## Confidence
Moderate, about ±5%. The answer depends on the horizon row (±5 px gives about ±4%), on f (∝ 1/f), and on where the lamp sits on the table top.
The scene record's statement that the table top spans y 652-699 is wrong: 652-663 is the top surface, 663-673 the slat front face and 673-693 the apron.
