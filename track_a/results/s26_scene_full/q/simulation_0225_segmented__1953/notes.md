# q_1953 — spacing between the markings on the pool wall

The question asks: "What is the spacing in metres between the markings on the pool wall?" The prior is a cat speed of 1.041 m/s. There is no depth_info. Both the file and the question use 24 fps.

## Problem
This is the segmented version of the video, so the background has been replaced with pure white. The pool and its wall
are not in it. `residue.py` checks frame 24: every non-white pixel (>3 levels from white) falls inside the box
x 648–1433, y 640–921, which is the loungers, the blue object and the cat. No trace of the wall or its markings remains.
**The asked quantity cannot be measured from this video.** The answer below is an estimate based on the scene's scale.

## Scale (2D, one planar scale from the prior)
- The cat's centroid moves steadily at 5.40 px/frame (from the record's fit, x from 570 to 836 px over 49 frames), which is 129.6 px/s.
- 1.041 m/s divided by 129.6 px/s gives 0.00803 m/px. Using the jittery per-frame mean of 5.56 px/frame instead gives 0.0078 m/px.
- Checks: the cat's length is 107 px, about 0.86 m, and the lounger leg span is about 185 px, about 1.5 m. The scene therefore
  renders at roughly 2 times real-world size.

## Estimate
The only regular spacing visible is the pitch of the front-row loungers. Their centres are at about 855, 1097 and 1340 px,
so the pitch is about 242 px, which is about 1.95 m at this scale. Pool-wall markings such as tile stripes or posts are
plausibly about 1 m in real-world units. At the ~2x scene scale that becomes about 2 m, and lane-type markings would be
larger. I answer **1.95 m**. This is a guess and confidence is very low.
