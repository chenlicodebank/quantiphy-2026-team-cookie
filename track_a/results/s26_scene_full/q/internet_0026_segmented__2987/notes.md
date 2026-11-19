# q_2987: toy truck height (cm)

Prior: the sofa's total height is 90 cm. **The sofa is not visible.** This is the segmented version of the video, so the background (sofa included) was replaced with white. Because the sofa's pixel height cannot be measured, the annotators' scale cannot be reproduced directly.

Truck height in pixels, from scene/tracks/truck.csv (mask bbox, checked on frame 15 with a grid): 170 px (median of frames 6-35; range 169-173).

To get a scale I used body references in the same 2D plane:
- Man's head, crown to chin (head tilted), about 125-130 px. At about 23 cm this gives about 0.18 cm/px, so the truck is about 31 cm. The man is slightly nearer the camera (his feet are lower in the image), so this route reads low.
- Man's crouched height (bbox) is 447 px. A deep squat of about 100-108 cm gives 0.22-0.24 cm/px, so the truck is 38-41 cm.
- Child's head, front to back in profile, is about 77 px. At about 17 cm this gives 0.22 cm/px, so the truck is about 37 cm. The child sits slightly farther from the camera, so this route reads high.

The sofa was presumably behind the people. Being farther from the camera, it would give a larger cm/px under the annotators' single-scale convention. I therefore picked the upper-middle of the range: **36 cm**. That is also plausible for a large ride-on-style plastic dump truck.

Confidence: low to moderate (likely within ±20%). The prior object is absent from the footage.
