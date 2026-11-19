# Q573: length of the wooden bench (m). Prior: black cat speed = 0.94 m/s

The fps (24) and question_fps (24) agree, so no re-timing.

## Object
The "wooden bench" is the slatted wooden piece at the right that scene/ calls the "side table" (x≈1457–1919+, y≈779–993).
The dog is clear of it at frame 48, so I used frame 48. The bench's right end touches the image edge. Its front-right
corner is just outside the frame, but the right edge of the top surface (a receding line) is visible at rows 786–796.

## Camera geometry (measured: slats.py, seg.py, ends.py)
- The slat gaps on the top surface are receding lines. With vx = 960, their slopes give vy ≈ 530–548. So the
  vanishing point is ≈ (960, 540): the camera is level and centred, with the horizon at y = 540.
- Check: the front-left leg foot is at (1542, 993) and the rear-left foot at (1505.5, 966). Scaling about (960, 540)
  gives the same ratio in x (0.937) and in y (0.940).
- The top surface's back edge is at y≈779 and its front edge at y≈796. Its depth ratio, 0.934, matches the leg feet
  (0.940), so the top and the legs span the same depth range.
- That gives (H − h_top)/H = (796−540)/(993−540) = 0.565 from the front, and (779−540)/(966−540) = 0.561 from the
  back. I used 0.563.

## Bench length
- For points on the top plane, world X ∝ X' = (x−960)/(y−540).
  - Back-left corner (1457, 779): X' = 2.08. Front-left corner (1488, 796): X' = 2.06.
  - Right edge (1887, 786), (1897, 790), (1910, 794) and back-right corner (1879, 783): X' = 3.74–3.78.
  - So ΔX' ≈ 1.69.
- Check by symmetry: the slat gaps (pitch 29.3 px), the apron (1506–1911) and the legs all put the centre at x ≈ 1706–1711.
  Mirroring the left end about that centre gives ΔX' ≈ 1.72. I used 1.70.
- Cat: nose x is linear at 17.76 px/frame (rms 0.7). The centroid (17.81) and torso (17.86) agree.
  Its paws touch the floor at y ≈ 1016–1023, so I put its midline lane at y ≈ 1018.
  - Scale at the cat: 0.94 / (17.78 × 24) = 0.002203 m/px.
- Length L = 0.002203 × ΔX' × (1018−540) × 0.563 = 0.002203 × 1.70 × 478 × 0.563 ≈ **1.01 m**.

## Second route
- The bench is 1.70 × 256 ≈ 435 px long at the depth of its front edge (same depth as the front leg feet, y = 993).
  The cat's m/px scaled to that depth is 0.002203 × 478/453 = 0.002325, which gives 1.01 m.
- Moving the horizon to 530 changes the result by less than 1%.
- A naive single-scale 2D estimate (≈440–465 px × 0.0022) would give 0.97–1.03 m, close to this.

Confidence: moderate-good, about ±4%. The main uncertainty is where the bench ends (right end at the image edge;
slat symmetry versus measured edge differ by about 2%).
