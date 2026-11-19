# q_2986: toy truck length (cm)

Prior: sofa height = 90 cm. In this segmented video the background has been replaced with white, so the sofa never appears. Its pixel height can't be measured, which means the annotators' scale (90 cm / sofa px) can't be reproduced directly.

Truck length in pixels: 207 px bumper to bumper. This comes from scene/ (median over frames 6-35, range 205-210), and I checked it on frames 12 and 30 with a grid: the truck runs from about x 452 to 657 at frame 30. The truck's apparent size stays constant.

Stand-in scale from the man, who is crouched right next to the truck at about the same depth (his hand touches it at the start):
- Head, crown to chin: about 125 px. At about 23 cm for an adult, that is 0.184 cm/px, giving a truck of 38 cm.
- Thigh, knee to hip: about 270 px. At about 45-50 cm, that is 0.17-0.185 cm/px, giving 35-38 cm.
- The man's feet are slightly lower in the image than the truck's wheels, so he is a little closer to the camera. His scale therefore slightly underestimates the truck's size.
- Sanity check: the child's head (about 78 px, with the child slightly farther away) gives a somewhat larger value, about 40-44 cm.
- The truck looks like a large Mega Bloks First Builders dump truck, which is plausibly 35-40 cm long.

Answer: 40 cm. Confidence is low to moderate because the prior's object is missing from the footage.
