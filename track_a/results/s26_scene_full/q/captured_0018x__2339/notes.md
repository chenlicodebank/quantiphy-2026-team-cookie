# q_2339 — shoe length of the left person (cm)

The left person is the far person, so depth_info gives Z = 3.130 m. Intrinsics: f = 0.5959 x 1280 = 763 px, principal point (640, 360). The file and the question both run at 24 fps.

## Measurement (crop.py, frame 0; the person is static and frame 10 looks the same)
- I masked non-white pixels (gray < 235) in the crop x 330-440, y 520-590 and took each row's extent (printed by crop.py; zoom image in frames/shoe_0.png).
- Near shoe (her left foot, three stripes visible): heel at x ≈ 347-348 (rows 560-566), toe at x ≈ 398-399 (rows 568-575). Horizontal extent ≈ 52 px.
- Far shoe: its toe reaches x = 419 and its heel is hidden behind the near shoe.
- Straight method card: 52 x 3.13 / 763 = 21.3 cm.

## Corrections
- Yaw: the toe of the near shoe sits about 4 px lower than its heel (sole bottom: row ~571 at the heel, ~575 at the toe). Camera height from the feet row: h = (577 - 360) x 3.13 / 763 ≈ 0.89 m, so a point on the ground moves dv/dZ ≈ -69 px/m. The toe is therefore about 6 cm nearer the camera than the heel, which gives a yaw of about 16° and a length of 21.3 / cos16 ≈ 22.2 cm.
- Depth of the near foot: the two feet straddle the body centre in depth. The far shoe's toe sits about 8 px higher, so roughly 12 cm farther away. That puts the near foot about 6 cm closer than 3.13 m: Z ≈ 3.07 m, giving 21.8 cm.
- Range from pixels: 21-22.5 cm.

## Sanity check on scale
- Left person's height: 404 px x 3.13 / 763 = 1.66 m (plausible).
- Right person: 615 px x 2.002 / 763 = 1.61 m (feet cut off). Both agree with the scale.

## Answer
The pixel estimates (21.3-22.2 cm) are lower bounds: foreshortening and segmentation trimming can only shorten the shoe. A real three-stripe sneaker for an adult woman is about 23-25 cm. I answer 23 cm, slightly above the pixel route.
Confidence: moderate (±10%).
