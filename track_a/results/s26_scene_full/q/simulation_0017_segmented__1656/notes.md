# q_1656 – sculpture height (excluding pedestal)

The file and the question both run at 33 fps, so t = frame/33.

## Focal length (measure.py)
- Pelvis track: scene/tracks/person.csv, pelvis_x_smooth, pelvis_y_est ≈ 543 (close to the optical axis).
  t=0 is frame 0 and t=1 is frame 33.
- Prior: speed 1.3 m/s, so the walker covers 1.3 m between t=0 and t=1. Depths are 5.424 m and 4.886 m.
- Solving |d1·ray(u33) − d0·ray(u0)| = 1.3 gives:
  - f = 909 px using the smoothed track (x0 = −1.5, x33 = 252);
  - f = 901 px using a linear fit over frames 5-100 (7.62 px/frame).
  - I used f ≈ 905 px.
- Consistency check: both solutions put the person at constant Z ≈ 4.66 m, walking parallel to the image plane. That
  matches the near-constant apparent size and also reproduces both given distances. With constant depth,
  pixel speed / 1.3 m/s = 193.5 px/m = f/Z, which gives f = 901.
- Person height then comes out at 364 px × 4.66 / 905 = 1.87 m, which is plausible.
- The "art display panel" distance of 4.223 m cannot belong to the paintings, because the person (Z 4.66) passes in
  front of them. It probably refers to the small piece on the right. I did not use it.

## Sculpture
- On bg.png the tip is at y = 297. The base meets the pedestal top face at y ≈ 548, where the row width jumps from
  120 to 168 px. Pixel height is 251 ± 3 px, and u ≈ 528.
- Origin distance is 5.962 m. Taking the origin at the bbox centre (v ≈ 422) gives Z = 5.912 → H = 251 × 5.912 / 905
  = 1.640 m. Taking the origin at the base gives Z = 5.960 → 1.653 m.
- Answer: 1.645 m. The f spread (±0.5%) and the pixel-edge uncertainty (±1.2%) give a total uncertainty of about
  ±2-3%.
