# q_2643: soccer ball displacement, t=0.4 s to t=0.9 s (cm)

The file and the question both run at 24 fps. t=0.4 s is frame 10 (round 9.6) and t=0.9 s is frame 22 (round 21.6).
Intrinsics: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Positions
- **Frame 10:** the ball is at rest at person_A's foot, before the kick at frame 11. I read row and column profiles (`profiles.py`): top edge y ≈ 646.5, left edge x ≈ 402, right edge x ≈ 471. That puts the centre at about (437, 681), with a horizontal width of about 69 px (scene record: 68.9 px). The bottom is cut off by the image border.
- **Frame 22:** centre (614.9, 482.5) and diameter 52-53 px, from an edge circle fit (`fitcirc.py`) that agrees with the scene record.

## Depths
- **depth_info:** the second t=1.4 entry is labelled "soccer" twice. Size consistency shows that 2.373 m is the soccer ball and 2.602 m is the basketball (`geom.py`). With that reading, the soccer ball's effective diameter comes out as 16.8 cm at frame 22 and 16.6 cm at frame 34. The basketball comes out as 22.2 cm and 22.4 cm, against the prior of 23.2 cm (pixel fits read about 4 % small).
- **Depth at t=0.4 (not given):**
  - **Route 1, apparent size with off-axis correction.** At frame 10 the ball is 26.5° off-axis, so its image is an ellipse stretched 1/cos θ along the radial direction. I converted the 69 px horizontal width to a 66.7 px minor axis. Then tan α = minor x cos θ / 2f, scaled against frame 22 (d = 2.477 m), gives d10 = 2.150 m.
  - **Route 2, floor plane (`plane.py`).** I fitted the floor plane to about 70 rolling and resting centres of both balls (depths from size, calibrated to the given depths). This gives a camera height of 1.72 m and a pitch of about 33°. Intersecting the frame 10 ray with the soccer-centre plane gives d10 = 2.143-2.156 m.
  - The naive size ratio without the off-axis correction would give 1.885 m (displacement 90 cm). I rejected it because the floor plane contradicts it.

## Result
The displacement is |P22 - P10| with P = d x unit ray. Route 1 gives 79.4 cm and route 2 gives 79.3-79.6 cm.

**Answer: 79.4 cm.** Confidence is moderate. The main uncertainty is the depth at frame 10, which is inferred rather than given (±3 %).
