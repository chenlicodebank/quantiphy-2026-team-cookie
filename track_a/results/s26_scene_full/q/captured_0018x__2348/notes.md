# q_2348 — distance between the pineapple toy and the soccer ball at 3.0 s (cm)

**Main problem:** the clip has only 49 frames (t ≤ 2.04 s), so t = 3.0 s (frame 72) is beyond its end. Both
positions below are extrapolated from the last frames, which makes the answer uncertain (see Confidence).
The file rate and question_fps are both 24.

Pineapple toy = scene/ "yellow_plush" (yellow with green leaves, dropped by the near/right person).
Camera: f = 0.5959·1280 = 763 px, principal point (640, 360).

## Soccer ball (depth_info 2.80 m Euclidean, so Z ≈ 2.73–2.75 m along the optical axis)
- `ball_fit.py`: the fall over frames 30–35 gives 4.79 px/frame², which matches g at 2.75 m (4.72 px/frame²).
  This confirms the scale.
- First rebound (frames 40–48): the apex is at about frame 47 (centre row ≈ 410). The floor-contact centre row
  is ≈ 556–558, so the bounce is ≈ 145 px ≈ 0.52 m high and the coefficient of restitution is e ≈ 0.70.
- The ball drifts toward image-right at 2.2 px/frame (≈ 0.19 m/s). Its width stays at 44–47 px, so its depth
  barely changes.
- Extrapolated to frame 72: further bounces of decreasing height (a 3rd or 4th small hop, roughly 0–0.13 m above
  the floor), u ≈ 600, v ≈ 535 (about 0.08 m above the floor's centre row).
  This gives P_ball ≈ (−0.14, 0.63, 2.73) m.

## Pineapple toy (no depth given, so it is estimated)
- `plush_measure.py`: the toy hits the floor near the right person's feet (bottom row 697 at frame 36, Z ≈ 1.85).
  It bounces back and from frame 40 on it rocks near (840–847, 592–612), with its bottom at rows 616–631.
- Floor-row model (row − 360 = a/Z + b), fitted to the far person's feet (Z ≈ 3.0) and the near person's feet
  (Z ≈ 1.87), or to the ball contact (Z 2.70) and the near person's feet: a bottom row of 616–631 gives
  Z ≈ 2.26–2.47.
- Size check: free-fall width ≈ 28 px at Z ≈ 1.85 against a width of 23–24 px in frames 45–48 gives Z ≈ 2.2.
- Adopted: Z = 2.3 m, image centre (842, 600), assumed at rest by 3.0 s. This gives P_plush ≈ (0.61, 0.72, 2.30) m.

## Result
|P_plush − P_ball| ≈ 0.87 m.
- Toy depth: Z = 2.2 / 2.3 / 2.4 m gives 0.90 / 0.87 / 0.85 m.
- Ball drift: if the ball stopped drifting at frame 48 (u = 552), the result would be ≈ 1.02 m.

**Answer: 87 cm.**

**Confidence:** low to moderate. The time asked is outside the video, the toy's depth is not given, and both
positions after 2.0 s are extrapolated.
