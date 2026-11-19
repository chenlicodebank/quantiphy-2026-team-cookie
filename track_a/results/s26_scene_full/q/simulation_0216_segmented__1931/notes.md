# q_1931 — height of the table lamp (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.
The scene is a 2D side-on view with a static camera, so one metres-per-pixel scale comes from the cat's speed.

## Measurements (measure.py)
- Cat pixel speed, from scene/tracks/cat.csv (I checked the track against frames; it is the cat in all 50 frames):
  - mean per-frame speed: cx 428.6 px/s, dark_cx 430.5 px/s, bbox_cx 425.9 px/s
  - linear fit of x(t): 423.6, 427.3 and 421.4 px/s
  - adopted value: 426 px/s (±1%)
- Scale = 0.94 / 426 = 0.002207 m/px.
- Lamp pixel height, from my own row profile of the per-pixel-maximum image (this removes the cat): shade top at
  y ≈ 501–502 and base foot on the console top at y ≈ 789. That gives 287–288 px, which matches the record's bbox
  (503–789, 287 px).
- Height = 287.5 × 0.002207 = **0.633 m**.

## Check
- Second route for the scale: the linear-fit and per-frame-mean speeds differ by less than 1.5%, giving 0.628–0.638 m.
- Sanity check: the cat's length from tail tip to nose is 294 px, which is 0.65 m and plausible. A 0.63 m table lamp
  is also plausible.
- Caveat: the lamp stands slightly behind the cat's walking line (the furniture feet sit about 33 px higher in the
  image than the cat's paws). Under perspective this would make the true height a little larger. I followed the
  benchmark's 2D convention and used a single scale.

Confidence: moderate-high (±5%).
