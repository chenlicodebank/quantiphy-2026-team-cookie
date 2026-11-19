# q2101 – height of the pump bottle (cm)

Prior: the picked bottle (the clear perfume bottle that is lifted) is 11.7 cm tall. This is an internet video, so I used one planar scale from the prior and no perspective correction. Everything was measured on frame 0, where both bottles stand on the tray and are sharp. No time conversion is needed, so the fps / question_fps difference does not matter here.

## Picked bottle (scale reference)
- Top of the metal neck is at y ≈ 1185. It is partly between the fingers. Read on zoomed crops (`crops.py`, `frames/ptop_0.png`).
- Base is at y ≈ 1828. It sits behind the pink perfume bottle. The bottom of the thick glass base is visible at the right edge (`frames/pbase_0.png`).
- Height ≈ 643 px. The scene record gives 637 px (1183→1820). I used about 640 px, ±6 px.
- Scale: 11.7 / 640 = 0.01828 cm/px.

## Pump bottle (large amber bottle with black pump)
- Top of the pump head is at y ≈ 930. This comes from an intensity profile in `profile.py`: the edge is at row 930 at x = 2270.
- Base is at y ≈ 1843, where the bottle meets the tray at its centre (x = 2260), from the same profile.
- Height ≈ 913 px. The scene record gives 900 px from frame 18 (938→1838 after shifting back for camera drift). That fits within the reading error, but my edge profile goes slightly lower.

## Result
Height = 913 × 11.7 / 640 = 16.7 cm.

Range from the two readings:
- my readings (913 / 643): 16.6 cm
- scene record (900 / 637): 16.5 cm
- 913 / 637: 16.8 cm

Second route: the scene record's own pixel values, measured independently, give 16.5 cm, about 1% from my result. The pump bottle's base is about 20 px lower than the perfume bottle's, so the pump bottle is only slightly nearer the camera. The perspective effect is about 1–2%, and it is ignored, following the annotators' convention. A real 250 ml Boston-round pump bottle is about 17–19 cm tall, so the answer is plausible.

Confidence: good, about ±3%.
