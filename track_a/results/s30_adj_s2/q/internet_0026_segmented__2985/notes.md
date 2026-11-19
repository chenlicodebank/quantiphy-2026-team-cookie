# q2985: distance between the baby and the man (m)

**Prior:** sofa total height = 90 cm. The sofa was removed in this segmented clip; only the man, the toddler and the toy truck remain. Because the sofa's pixel height can't be measured, the scale has to come from body sizes, the standard-object route.

**Time base:** the file runs at 30.0003 fps and question_fps is 30. The distance is static, so time does not matter.

## Where the candidates part ways
- C1 (1.47): centroid-to-centroid distance 700 px × 0.0021 m/px.
- C2 (1.87): pelvis-to-pelvis distance 780 px × 0.00239 m/px.

They differ in two steps: the reference point and the scale.

## My measurements (measure.py)
**Pixel distance.** Foreground connected components, frames 5-35, every 5th frame:
- Centroid-to-centroid distance: 698 → 717 px. It grows only because the camera zooms in about 1.8%.
- Bbox-centre distance: about 660 px.
- In frame 0 the man's blob merges with the truck, so I discard that frame.

I adopt **700 px** between body centres, which is the natural "position of a person".

**Scale (m/px).** Body parts measured on zoomed frame 9:

| Reference | Pixels | Assumed size | m/px |
|---|---|---|---|
| Man's head, crown to chin | about 125 | 0.23-0.24 m | about 0.0019 |
| Man buttock-to-knee | about 267 | 0.60 m | 0.00225 |
| Man shoulder-to-hip | about 245 | 0.50 m | 0.0020 |
| Toddler head | about 78 | 0.165 m | 0.0021 |
| Toddler leg, hip to sole | about 180 | 0.37 m | 0.0021 |
| Toddler seated height | 192 | about 0.50 m | 0.0026 |

The median is about 0.0021-0.0022 m/px. I adopt 0.0022, a slight allowance for the sofa probably standing a little behind the people, which would make the annotators' m/px a bit larger.

C2's 0.00239 m/px would make the man's head about 0.30 m from crown to chin, which is too large. I reject it.

## Answer
700 px × 0.0022 m/px = **1.54 m**

**Second route:** using C1's body-proportion scale of 0.0021 gives 1.47 m, within 5%. Using pelvis points (about 830 px) with 0.0021 gives about 1.74 m. I don't adopt that, because the "position" of a person in a planar annotation is the body centre.

**Confidence:** low to moderate, with about ±15% uncertainty from the scale. The prior's object is not visible, so the annotators' sofa pixel height cannot be recovered. I agree with C1's method, with a slightly larger scale.
