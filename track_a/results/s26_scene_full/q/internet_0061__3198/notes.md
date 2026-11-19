# q 3198 – distance of the acorn bottom above the chair surface at t = 1.40 s (cm)

## Geometry
- The video is turned 90°: gravity points to the **right** in the image. From release (frame 39) to impact (frame 45) the acorn
  speeds up steadily to the right (35 → 90 → 122 → 165 → 200 → 228 → 275 px/frame). A throw seen from above could not speed up
  like that, so the fall happens in the image plane. The acorn's "bottom" is the right (leading) edge of the white dome, and the
  "chair surface" is the backrest mesh it lands on (right of the rail). Its apparent size stays the same (dome ~200 px), so its
  depth is constant and the planar convention holds.
- Time base: 1.40 s → frame 42 (30 fps and 30.013 fps both give 42).

## Scale (from the prior g = 9.8 m/s²)
- I read the cap/dome boundary (a sharp edge) at row y≈520 on 2× gridded crops (`zoom.py`, frames/z39–z45.png):
  290, 380, 502, 667, 867, 1095, 1370 px for frames 39–45.
- A quadratic fit gives a = 36.3 px/frame² (35.8 over 39–44, 36.3 over 40–45). The record's centres give 35.6.
- So the scale is 9.8 / (36.3 × 30²) = 3.00e-4 m/px. Sanity check: the 279 px toy comes out at 8.4 cm, which is plausible.

## Distance
- Dome leading edge at frame 42: ≈862 px (solid edge; motion blur reaches ~890).
- Dome leading edge at contact with the backrest: ≈1570 px. Frame 45 is the rightmost and sharpest frame (the toy is nearly
  stopped in the mesh); it rebounds at frame 46.
- Gap: 708 px × 3.00e-4 = **21.2 cm**.

## Second route (kinematics)
- Velocity at frame 42 ≈ 182 px/frame. Projecting 3 frames ahead to impact: 182×3 + ½×36.3×9 ≈ 710 px, which is the same
  ~21.3 cm.
- If the impact is placed partway through frames 45–46 (~0.3 frame later), the gap grows to ~810 px, or 24 cm.

## Other readings
- If "chair surface" means the seat/back rail line at x≈1300 rather than the landing point, the answer would be
  ≈440 px ≈ 13 cm. I did not use this reading.

Confidence: moderate. The scale is good to about ±5%; the main uncertainty is where exactly the surface/contact point is.
