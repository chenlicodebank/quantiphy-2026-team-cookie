# Q1470: dragon displacement from 0.5 s to 1.0 s (frames 12 to 24 at 24 fps)

Answer: **0.645 m**

## Method
- Prior: speed = 1.29 m/s. Depths: 5.1661 m at frame 24 and 6.2783 m at frame 48. The file and question_fps are both 24.
- I used the head-patch track from scene/tracks/dragon.csv as a stand-in for the origin. The principal point is the image centre.
- If the dragon flies in a straight line at constant speed, the 3D distance between the back-projected positions at frames 24 and 48 must be 1.29 m. That gives a focal length of f = 3309 px (horizontal field of view about 42 deg). See geo.py and geo2.py.
- Check: with this f, the straight-line constant-velocity model reprojects onto the head track over all frames 0–71. Residuals are about 10–30 px, and up to about 70 px in y during the wing strokes because the head bobs. The model's range ratio from frame 51 to frame 71 is 1.15. The rigid-glide bbox-width ratio gives 1.13, which agrees within 2%.
- Displacement: 1.29 m/s x 12 frames / 24 fps = 0.645 m.

## Second route
I back-projected the head at frame 12 directly, using the model range of 4.645 m, and measured to the frame-24 point. This gives 0.669 m. Averaging the head over frames 9–15 gives 0.672 m. The 4% difference comes from the head bobbing with the wings (the head is not the origin), so I answer with the uniform-motion value.

Confidence: high (within about 5%).
