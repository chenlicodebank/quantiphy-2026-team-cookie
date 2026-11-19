# q2989: average speed of the toy truck (cm/s)

**Prior.** The sofa's total height is 90 cm. **The sofa is not visible**: this is the segmented version, so the background, including the sofa, was replaced with white. Because of that, the sofa's pixel height cannot be measured, and the scale had to be estimated from body references.
- Man's head, crown to chin, frame 15: about 127 px. At about 23 cm, that gives about 0.18 cm/px. The man is the closest object (feet at y ≈ 500).
- Child's head, frame 15: about 70 px tall and 67 px front to back. At about 15.5 cm, that gives about 0.22 cm/px. The child is farther back (seat at y ≈ 440).
- The truck sits between them (wheels at y ≈ 478). I chose 0.205 cm/px, which makes the truck about 42 cm long and 35 cm tall, plausible for a toddler dump truck. The sofa is probably behind the people, which would make the annotators' scale larger, so this choice leans slightly high.

**Motion.** I used scene/tracks/truck.csv, checked against the frames. The camera pans and zooms to follow the truck: the man and child shift +40 to +57 px. I followed the "measure against the background" convention and used the camera-stabilised centre (`cx_from_front_stab`). It moves 772 → 480 px over 35 frames, which is 250 px/s. The mean of the per-frame speeds is the same, 251 px/s. The raw image motion would be 208 px/s.

**Time base.** fps = 30.0003, the same as question_fps = 30. Every fifth frame is a duplicate, which suggests 25 fps footage resampled to 30 fps. Duration is preserved, so real time is 1.2 s.

**Answer.** 250.2 px/s × 0.205 cm/px ≈ 51.3 cm/s.

**Second route.** The front bumper, stabilised, gives 249 px/s, so the answer holds to within 1%.

**Confidence: low.** The scale is the main uncertainty, roughly ±20%, because the prior's object is missing. A further ±17% depends on whether the annotators corrected for the camera pan; the raw motion would give about 43 cm/s.
