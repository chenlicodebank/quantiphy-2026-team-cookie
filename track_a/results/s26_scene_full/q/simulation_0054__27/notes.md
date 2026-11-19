# Q27: distance between the two black lamps (m)

The prior is the orange car's acceleration, −2.86 m/s². The camera looks straight down on the road and does not move.

## Scale from the prior
- `track_tm.py` takes the orange car at frame 60 as a template and finds it in frames 16–90 with sub-pixel matching.
- A quadratic fit of y against frame gives acceleration −0.1832 px/frame². The rms error is 0.06 px, and the value is the same on every window (16–90, 30–90, 16–55, 50–90 and 35–75 all give −0.182 to −0.184). So the deceleration is constant.
- I used question_fps = 30. The difference from the file's 30.003 is negligible.
- a = 0.1832 × 900 = 164.9 px/s², so the scale is 2.86 / 164.9 = **0.01735 m/px**.
- Sanity check: the car is 293 px long, which is 5.1 m. That is plausible.

## Lamps
- These are post-top lanterns with hexagonal heads, standing on the left sidewalk.
- The camera has visible perspective. Each head is pushed outward from its round base plinth, along the line from the image centre:
  - upper lamp: head (196,451), base (~251,465)
  - lower lamp: head (195,981), base (~251,911)
- The offset is 0.175 × the base's distance from the centre for both lamps, which confirms it is perspective and not a tilt.
- The record's 530 px separation is between the lamp heads, and that is inflated by perspective. The world distance between the lamps is the separation of their bases, or of any points at the same height on both posts. So the answer does not depend on whether the origin is at the base or at the centre of the bounding box.
- Base plinth centres, from distance-transform peaks and the disc extents (`bases.py`, `lamps.py`, `frames/bases.png`):
  - upper (251,465)
  - lower (250,911)
  - separation 446.5 ± 2 px, which gives 446.5 × 0.01735 = 7.75 m

## Height correction
- The car's tracked features sit about 0.8–1 m above the ground, while the plinth tops are about 0.3 m up. The ground-plane scale is therefore larger by about (H − 0.3)/(H − zc), where H is the camera height.
- From the lamp head offset (h/H ≈ 0.15) with a 3–5 m post, H is about 25–35 m. That makes the correction about +1.5 to +2.5%.
- Tracking the car's rear, roof and nose separately (`parts.py`) shows only about 1% differences, and the roof track is noisy, so the perspective effect is small. I applied about +1%, giving roughly 7.8 m.

## Second route
- The whole-car template and the rear-only template give the same acceleration to within 0.5%.
- The two ways of locating the bases agree to within 1 px.
- If the lamp heads were wrongly taken as the positions, the answer would be 9.2 m. I rejected that, because the geometry shows the heads are displaced by perspective.

## Answer
**7.8 m**. Confidence is moderate to good. The main uncertainties are the height correction (about ±2%) and the assumption that the lamp origins are vertically above the bases.
