# q_2984: sitting height of the baby (cm). Prior: the sofa is 90 cm tall.

**Problem.** This is a segmentation video: the background, including the sofa, was replaced with white. So the sofa's pixel height, which the annotators used as their single scale, can't be measured. Only the man, the baby and the truck are left.

**Baby pixel height** (`measure_baby.py`: foreground mask, then the connected component on the left). From the top of the head to the bottom of the buttocks/floor contact it is 194 px at frame 0 and 194-197 px over frames 0-35. The baby doesn't move. Head (vertex to chin): about 88 px.

**Scale estimates (indirect, because the sofa is missing)**
1. Man's head: vertex to chin is about 125 px, and an adult head is about 23 cm, so about 0.184 cm/px at the man's and truck's depth. The man's crouched height of 444 px then works out to about 82 cm, which is plausible. The truck keeps the same size while it rolls to the baby's feet, but the baby's floor contact (y=443) sits higher in the image than the truck's wheels (y=482), so the baby is probably a little farther away. That gives about 0.19-0.21 cm/px, so 194 px is about 36-40 cm.
2. Baby's head: about 16 cm for a 1-year-old over 88 px is about 0.18 cm/px, which gives about 34-35 cm.
3. Anthropometry: a 1-year-old's sitting height is about 47 cm (crown-rump). Slouched as this baby is, the vertical extent would be about 40-42 cm.

The sofa was most likely behind the baby. That would make its pixel height smaller per cm, which pushes the annotators' value up compared with the true size.

**Answer: 42 cm.** Confidence is low (roughly ±20%) because the prior's reference object is not in the video.
