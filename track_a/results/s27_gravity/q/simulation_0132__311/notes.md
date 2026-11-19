# q_311: diameter of the apple (m). Prior: g = 9.8 m/s^2. No depth_info. 2D convention.

File fps = question fps = 120.

## Scale from gravity
- The apple falls freely from the counter edge (frame ~141) to the floor (contact at frame 191/192). The camera is static, and the apple's apparent size stays constant (no depth change), so one m/px scale applies.
- I fitted a quadratic to the vertical centre position over the fall frames:
  - scene track (circle-fit centre, `fit.py`): 0.442–0.447 px/frame^2 for windows 146–190, 150–190, 155–189 and 148–185.
  - my own segmentation (background difference plus a hue gate, centroid, `measure.py`): 0.439 (150–188, rms 0.22 px) and 0.4475 (165–190, rms 0.26 px). I left out frames before 150 because the counter edge and its reflection contaminate the mask there.
  - Adopted value: a = 0.443 px/frame^2 = 6380 px/s^2, so the scale is 9.8 / 6380 = 1.536e-3 m/px (spread about ±1.5%).

## Pixel diameter
- Scene circle fit: median diameter 60.6 px.
- Tight box: 62 x 65 px, which includes the anti-aliased rim.
- 50%-contrast sub-pixel width at rest (frames 0–5, `width.py`): 63.9–64.1 px.
- In flight, the width varies between 57 and 66 px as the lumpy apple rotates (median about 61 px).
- Adopted diameter: 62.5 px (±2 px).

## Answer
62.5 px x 1.536e-3 m/px = **0.096 m**. The range of readings gives 0.093 m (61 px) to 0.098 m (64 px).

## Plausibility check
With this scale, the counter top (apple bottom at y ≈ 1136) is about 639 px above the floor (y ≈ 1775), which is 0.98 m. That fits a kitchen island, and a 9.6 cm apple is a realistic large apple.

Confidence: moderate to high (about ±4%).
