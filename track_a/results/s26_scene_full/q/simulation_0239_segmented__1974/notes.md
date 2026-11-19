# Q1974: length of the house (m)

Prior: brown horse speed = 0.874 m/s. The clip is 2D, so I used one metres-per-pixel scale. fps 24 = question_fps, so no re-timing.

## Scale (m1.py, from scene/tracks/horse_brown.csv, frames 0-48; frame 49 is a reset artefact)
- The nose (bbox x1) advances very steadily: 837 -> 964 px over 48 frames = 2.65 px/frame.
- Centroid over whole gait cycles (period about 20 frames): 8->48 2.628, 4->44 2.634, 2->42 2.666 px/frame. Over 0->48 it is 2.555, because the gait phase biases the endpoints.
- Adopted 2.64 px/frame = 63.4 px/s, giving 0.874 / 63.4 = 0.01379 m/px.
- Sanity check: horse length about 148 px = 2.0 m and width about 40 px = 0.55 m, which is plausible.

## House (m2.py, foreground mask of the largest component, frames 0/24/48)
- Bounding box x 618/620-1423, so the width is 804-806 px; y 24-744 (721 px). The widest part is the eave band at row about 400 (796 px across the mask row; the bbox spans 805 px).
- Length = the longer horizontal extent = 805 px x 0.01379 = **11.1 m**.
- Other readings: the main block alone (about 700 px) gives 9.65 m. The y extent (721 px) gives 9.9 m.

## Check
Using the centroid's 0-48 rate (2.555 px/frame) would give 11.5 m. The whole-cycle and nose rates agree at 2.63-2.65, so I use 11.1 m.
Confidence: moderate. The main uncertainties are perspective (the roof is closer to the camera than the ground the horse walks on) and whether the reference counts the eaves.
