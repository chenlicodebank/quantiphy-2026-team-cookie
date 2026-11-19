# q2355 – velocity (speed) of the white jar at t = 0.60 s, cm/s

Answer: **285 cm/s** (2.85 m/s).

## Setup
- The lab video plays at 24 fps, and question_fps is also 24, so t = 0.60 s is frame round(14.4) = 14. The jar is the white object
  that the near person (left) throws (`white_ball` in scene/). The "carrot" is the yellow object thrown back (`yellow_fruit`).
- The camera is static. f = 0.5959 x 1280 = 763 px, and the principal point is (640, 360).
- Depth anchors: jar 1.9735 m and carrot 2.63 m at frame 14.
- Frames 12-14 are the release: the jar is still touching the fingers at 14 and is free from 15 on.
  Both objects jump about twice the normal step between frames 11 and 12, which looks like a dropped camera frame. I did not use
  frames 11-12 for motion.
- I checked the track centroids (scene/tracks/white_ball.csv) on zoomed crops (`crops.py`). They sit on the object.

## Routes
1. **Direct back-projection (the reference convention):** I back-projected the track centres with depth. The depth is 1.9735 m at
   frame 14, and the other frames take it from the trajectory model in route 2. The depth changes little (≈1.96-2.02 m)
   over frames 12-17, so its effect on the speed is small.
   - Forward difference at frame 14: 2.97-3.00 m/s.
   - Central difference over frames 13-15: 2.85 m/s.
   - Mean of the forward differences over frames 12-16 (5-frame smoothing): 2.74-2.76 m/s.
   - The result is insensitive to the depth rate: dZ/dt from -0.9 to +0.2 m/s changes the central-difference speed only from about 2.83 to 2.91 m/s.
2. **Ballistic 3D fit** (`joint.py`, `joint_fixed.py`) of the jar (frames 15-25) and the carrot (frames 13-17 and 19-23). The fit shares one
   gravity direction and anchors each object's distance at frame 14.
   - With gravity fixed at 9.8 m/s², the fit picks a 57° camera pitch, and the jar's speed at frame 14 is 2.79 m/s.
   - That pitch contradicts the room geometry (`vp_check.py`). Making the two wall baseboards orthogonal and the radiator edges vertical
     needs pitch ≈33.5° and roll ≈6-12°. The people's depths support the same answer (`people_check.py`): at 57° the near person's pelvis would be
     1.65 m above the floor.
   - With the orientation fixed from the room and the gravity magnitude left free, the fit converges at 0.84 g and the residual is about 1.2 px.
     The jar's speed at frame 14 is then 2.91-2.96 m/s.
   - With gravity forced to 9.8 m/s² and the room orientation, the fit is poor (3 px residual) and gives 3.4-3.6 m/s. I rejected it.

## Result
All the credible estimates fall between 2.74 and 3.00 m/s. I answer the middle value, 2.85 m/s, which is the central difference and is within
about 5% of every one of them.

Confidence: moderate, with an expected error of about ±5%. The spread comes mainly from how the reference smoothed the release frames.
