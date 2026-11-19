# Q821 – length of the antelope (m)

Prior: antelope speed = 1.277 m/s. No depth_info was given. This is a 2D scene: the antelope walks left to right, parallel to the image plane, and the camera is static. fps = question_fps = 30, so no re-timing is needed.
The antelope is the large horned creature in scene/ (`creature`); the other animal is the rabbit.

## Scale (from the speed prior)
`speed.py` uses the landmark tracks from scene/ and fits a straight line to each over frames 0–74:
- Shoulder: 6.61 px/frame (mean step 6.63; smoothest, residual 1.6 px).
- Hip (≈ pelvis/root): 6.76 px/frame.
- Mask centroid: 6.74. Muzzle bbox x1: 6.56. body_mid: 6.2–6.4 (noisy template, residual 7.5 px, so not used).
- Adopted: 6.65 px/frame = 199.5 px/s. Scale = 1.277 / 199.5 = 0.00640 m/px (±1.5% depending on which point is used).

## Length in pixels (world AABB horizontal extent, tail tip to muzzle)
- Scene record bbox length: median 486 px. Its x0 is sometimes biased by bush glints near (130–160, 1510–1540), and the tail swing changes x0.
- Checked by eye on zoomed crops (`views.py`, framekit):
  - f12: ~145 → 636 (491 px)
  - f15: 163 → 656 (494 px; the snout reaches ~656 against the grey mountain)
  - f27: ~239 → 730 (491 px)
  - f57: ~450 → 929 (480 px)
- Adopted: 488 px. My own threshold mask (`seg2.py`) loses the thin tail and dark legs, which gives about 389 px, so I rejected it.

## Answer
488 px × 0.00640 m/px = **3.12 m**.
- Second route: the record median of 486 px with the shoulder speed (6.61 px/frame) gives 486 × 1.277 / 198.3 = 3.13 m.
- Alternative reading: body only, rump to muzzle without the tail, is about 340 px, which gives about 2.2 m. I did not use this, because an AABB includes the tail.

Confidence: moderate. The scale is good to about 2%. The main uncertainty is whether the reference length includes the tail and what pose it was taken in.
