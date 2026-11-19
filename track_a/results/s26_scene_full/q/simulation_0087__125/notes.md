# q125: length of the car (m). Prior: the car accelerates at 4.03 m/s^2

Time base: fps = question_fps = 24, so no re-timing issue.
Scene: a top-down 2D view. The car is a Cybertruck-like pickup moving −x from rest, and motion starts at frame 1→2.

## Scale from the prior (track_shift.py, fit1.py)
- Per-frame horizontal shift of the car came from cross-correlating each pair of consecutive frames over the car region (SSD, parabolic sub-pixel peak). Results are in shifts.txt.
- The shift grows linearly: a fit of shift(i) = a·i + b gives:
  - frames 2-48: a = 0.712 px/frame², rms 0.11 px
  - frames 2-30: 0.704
  - frames 10-45: 0.711
- Zero speed falls at frame ≈0.5, which matches a uniform acceleration that starts at frame 1.
- Adopted a = 0.709 px/frame² = 408 px/s², so the scale is 4.03 / 408 = 0.00987 m/px.
- The record's edge-based quadratic fit of x0 gives 0.68-0.76. That signal is less reliable: the front edge is contaminated by the shadow and by the bumper face seen in perspective.

## Pixel length (length.py)
- The silhouette length depends on where the car is in the image. Off-centre (f37) a dark front-bumper face is visible through perspective, giving 586-589 px. Near the image centre (f49-53, car centre x≈1100-1250) it is 575-580 px.
- I used the near-centre value, 578 px (threshold 30 on |grey − 140|; the rear edge is sharp).
- The record's median of 583 px mixes positions.

## Answer
578 px × 0.00987 m/px = **5.70 m**.

- Sensitivity:
  - a in 0.704-0.712 gives 5.68-5.74 m.
  - Length 577-583 px gives 5.69-5.75 m.
- Sanity checks:
  - The length/width ratio is 578/214 = 2.70. A real Cybertruck is 5.68 m long, so this is consistent.
  - The camera height estimated from the perspective parallax is about 45 m, so the height difference between the origin plane and the bumpers or roof matters by only about 1-2%.

Confidence: good, about ±3%.
