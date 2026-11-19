# Q838: length of the front horse (m)

- The horses move right (+x). The back horse is the red horse on the left; the front horse is the dun horse in the middle. fps is 24 and question_fps is 24, so there is no re-timing.
- I used the 2D convention: one scale, taken from the prior (the back horse's speed is 0.874 m/s).
- The red horse's speed over frames 0-48 (m.py) is 77.4 px/s from a linear fit of the torso centroid and 77.3 px/s from the mask centroid. The bbox-edge values range from 75.5 to 76.8 px/s. I left out frame 49, where the animation loop resets. Taking 77.3 px/s gives a scale of 0.874/77.3 = 0.01131 m/px.
- The dun horse's length (x extent of the mask, tail to snout) has a median of 229 px over 50 frames (range 218-243, changing with gait). I checked the mask by eye at frame 24: the zoomed crop shows about 218-224 px, and the mask gives 224 px.
- Length = 229 × 0.01131 = **2.59 m**. This is a plausible horse length.
- Second check: the scale from the centroid speed gives the same value within 1%.
- Uncertainty: the dun horse's hooves are at y = 634 and the red horse's at y = 630. The dun horse may therefore be a few percent closer to the camera, which would mean about −4% if the horizon is near the image centre. I did not correct for this, following the single-scale 2D convention. The length also varies ±5% with gait.
- Confidence: medium-high.
