# Q56: walking pedestrian speed at t = 1.0 s (frame 24, 24 fps)

The video is a 2D top-down view. File fps and question fps are both 24.

Scale: the "white car" is the white van (the only white vehicle). measure.py measured its body length in the frame
column profile (min-channel > 200) at f0, 24, 36, 60 and 71: 232–236 px. The record gives 236 px at threshold 25.
I used 236 px, so 6 m / 236 px = 0.02542 m/px.

Walker (person in the white top on the SE sidewalk): I used the torso centroid from scene/tracks/pedestrian_sidewalk.csv
as the pelvis proxy. Linear fits of x against frame:
- f14–34: 2.045 px/frame
- f18–30: 2.034 px/frame
- f20–28: 2.014 px/frame
- whole clip: 2.045 px/frame

Vertical drift is about 0. The one-frame torso steps near f24 are 1.84–2.51 px, which is gait noise.

Second route: the mask-centroid fits give 1.83–2.08 px/frame, which agrees with the torso fits.

Speed = 2.03 px/frame × 24 × 0.02542 = 1.24 m/s. This is a plausible walking speed.

Confidence: moderate-high, about ±5%. The main uncertainties are the van length (±2 px) and gait variation in the
reference one-frame difference.
