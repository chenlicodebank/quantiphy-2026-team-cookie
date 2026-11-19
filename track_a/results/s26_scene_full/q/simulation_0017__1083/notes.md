# q_1083 – height of the person (simulation_0017)

File fps 33.039, question_fps 33.0 (frame numbers used; the difference is negligible here).
The image is rolled 90°: world up = image +x. The person walks along image +y, parallel to the image plane.

## Scale (scale.py)
- Route A, speed prior: linear fits of pelvis_y / head_y vs frame (scene track, frames 6–100) give 7.42–7.67 px/frame,
  mean ≈ 7.55 px/frame = 249 px/s → 1.3 / 249 = 0.00522 m/px.
- Route B, depths only: if the person's z-depth is constant, d² = z²(1 + r²/f²) where r = offset of the pelvis from the
  image centre. With r(f0) ≈ 530 px (pelvis y ≈ 10) and r(f33) ≈ 278 px (pelvis y ≈ 262): z/f = 0.00509–0.00529 m/px,
  z ≈ 4.66 m, f ≈ 890 px. This predicts a walking speed of 1.24–1.29 m/s, which matches the 1.3 m/s prior. The head
  width stays constant over the walk, so the depth really is constant.
- Scale used: 0.00522 m/px.

## Pixel height
- In most frames the bench in the foreground hides the feet below x ≈ 380, so the record's 327 px is too short (the
  soles are cut off). In frames 0–4 the stance shoe is visible next to the bench end (shoe.py, frames/shoe2.png). Its
  flat sole edge is at x ≈ 348.5, and the white midsole may add a few px below that, so the sole is at ≈ 344–349.
- The head top (hair) during single support is at x ≈ 708–712 (track head_top_x, frames 2–4; the maximum over the
  walk is 712).
- Height ≈ 710 − 346 = 364 px (range 359–368).

## Answer
H = 364 × 0.00522 ≈ 1.90 m (range about 1.87–1.92 m). Both scale routes agree to within about 2%. The main
uncertainty is the exact sole position (±4 px) and how far the walking head height falls below the rest standing
height (likely ≤1%).
Confidence: moderate (about ±3–4%).
