# Q2236 — length of the pen (cm)

The file and the question both run at 24 fps. The pen is static, so I measured it on frames 0, 24 and 40 (they match to within 1 px).

## Measurement (pen.py)
- I took the darkness profile of the pen against the table (rows 430–446) and found its connected blob. The dark body is x 441–489. Including the
  thin tip at the left (x≈434) and the silver tip at the right (it ends at x≈501.5, where the table starts again at 502), the pen spans
  x ≈ 433.5 → 501.5. It is nearly horizontal: y drops from ≈441 to ≈437. Length ≈ 68 px (±1 px; edge blur may add about 1 px).
  See frames/pen_0.png.
- I used the lab camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360).
- From depth_info, the distance to the pen at t=0 is 1.6725 m. The pen centre is at (468, 439), so the ray factor is sqrt(1+0.225²+0.104²) = 1.030
  and the axial depth is Z = 1.623 m.
- The pen lies horizontal in the image, so it is roughly perpendicular to the optical axis, and its length = Z·Δu/f = 1.623·68/763 = **14.47 cm**.
- With the method card's simple formula (Euclidean distance × px / f) the length is 14.91 cm. I answer with the geometric
  value, 14.5 cm. The two readings differ by 3%.

## Check
- To check the scale, I back-projected the ball's track with the given depths: frame 0 (545, 294.5) at 1.818 m and frame 14
  (t=0.6, (548, 354)) at 1.7288 m. That gives a displacement of 0.164 m. With release at frame ≈7.6 (motion first seen at frames 7–8),
  s = ½at² gives a ≈ 4.6 m/s², which matches the prior. So the f / depth scale is consistent.
- A pen of about 14–15 cm is plausible.

Confidence: moderate-high (±4%).
