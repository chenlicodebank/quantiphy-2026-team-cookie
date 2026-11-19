# q_2988: speed of the toy truck at 0.50 s (cm/s)

**Time base.** The file runs at 30.0003 fps and the question at 30 fps, so I used 30 fps; t = 0.50 s is frame 15. The clip repeats every 5th frame (a 25 to 30 fps conversion), so I fit over several frames instead of taking a one-frame difference.

**Pixel speed** (`speed.py`, using the truck track in scene/tracks/truck.csv; I checked it on overlays and crops). I fit a quadratic to the truck's x position and took its slope at frame 15, using windows of 10-20, 12-18, 5-25 and 13-17 frames:
- Raw image, bbox centre or front bumper: 216 to 234 px/s, about 222 px/s.
- Camera-stabilised (against the background; the hand-held camera pans to follow the truck): 250 to 271 px/s, about 257 px/s.
- I used about 250 px/s. This leans to the stabilised value, because the convention is to measure against the background, but the camera fit is uncertain because it assumes the people stay still.

**Scale.** The prior's object, a 90 cm sofa, is **not visible**: the background was replaced by white. So I estimated the scale at the people's depth from body sizes:
- Man's head, crown to chin (tilted head): about 110 px, for about 23 cm, giving 0.21 cm/px.
- Man crouched: 444 px tall, for about 100 cm, giving 0.22-0.23 cm/px.
- Man's thigh, knee to buttock: about 260 px, for about 58 cm, giving 0.22 cm/px.
- Toddler's head: about 70-75 px, for about 16 cm, giving 0.22 cm/px.
- Check: at 0.22 cm/px the truck would be about 45 cm long, which is plausible for a large toddler dump truck.

The sofa is probably in the background, behind the subjects, so it would look smaller in the image. That means the annotators' scale (90 cm divided by the sofa's pixel height) is likely somewhat larger than the scale at the subjects' depth. I therefore used 0.24 cm/px, about 1.1 times the scale at the subjects' depth.

**Answer:** 250 px/s × 0.24 cm/px ≈ **60 cm/s**.

**Second route.** Raw pixel speed at the subjects' scale: 222 × 0.22 = 49 cm/s. Stabilised speed with a scale set by a sofa farther back: 257 × 0.26 = 67 cm/s. The answer of 60 sits in the middle of these.

**Confidence:** low to moderate. The main uncertainty is the sofa's pixel height, which cannot be measured in this segmented clip; it could be 20% or more.
