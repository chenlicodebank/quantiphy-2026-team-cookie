# q1411: speed of the astronaut at t = 2 s (m/s)

**Answer: 2.39 m/s.** Expected error about ±8%.

**Time base:** the file and the question both run at 24 fps, so t = 2 s is frame 48. Frame 47 to frame 48 is the backward difference.

## Method (3D pinhole)
1. **Relative depth.** I tracked a rigid block on the suit (helmet plus backpack, fixed to the torso) in every frame 14-79.
   - I used ECC affine alignment against frame 48 (`ecc_scale.py`, giving `ecc_scale.csv`), started from a scale/rotation template match (`scale_match.py`).
   - Image scale goes as 1/Z. Results: s24 = 0.953, s48 = 1.000, s79 = 1.185. The astronaut moves diagonally toward the camera.
   - The shadow row moving down the image (1032 at frame 17, 1041 at frame 58, 1047 at frame 79) agrees that it comes closer.
2. **Depth at frame 48.** depth_info gives 18.147 m at t = 1 s (frame 24). That is a Euclidean distance; the Z component is 18.129. So Z48 = 18.129 × s24/s48 = 17.28 m.
3. **Focal length from the 2.2 m height prior.**
   - In the upright walking frames 72-79 the bbox height is 427-439 px. With each frame's Z from the scale ratio, f = h·Z/2.2 comes out at 2924 px (2868-2972 depending on whether the horizontal, vertical or mean scale is used).
   - The walking pose has bent knees and a stride, so I added 3% to reach rest standing height: **f ≈ 3010 px** (horizontal FOV about 42°).
   - Cross-check: the crouched landing at frame 16 gives a similar implied f (about 2980). The mid-air frames give larger values (3100-3350) because the toes are pointed and the legs are extended, so they don't represent standing height and I didn't use them.
4. **Pixel motion at frame 48.** Mask centroid (pelvis proxy): du = 14.3, dv = 7.8 px/frame. The rigid-block centre gives 14.0 and 7.85, and the local rotation is small.
5. **Local depth rate.** r = −dlnZ per frame near frame 48, from the scale slope over frames 40-56. Different features disagree:
   - helmet: 0.0020
   - backpack: 0.0016
   - helmet plus backpack: 0.0032
   - larger block: 0.0040
   - over the whole flight, frames 24→58: 0.0025; frames 17→58: 0.0030

   I used r = 0.0027, which gives dZ ≈ −0.047 m/frame (about −1.1 m/s).
6. **Speed.** P = ((u−cx)Z/f, (v−cy)Z/f, Z) with the principal point at the image centre, and speed = |P48 − P47| × 24 (`speed.py`).
   - Result: **2.387 m/s** with the centroid, 2.393 m/s with the block centre.
   - The mean of the per-frame speeds over frames 46-50 is 2.386 m/s. Frames 44-52 range from 2.36 to 2.42.

## Sensitivity and second route
- **Depth rate:** r = 0.0016 gives 2.26 m/s and r = 0.0040 gives 2.64 m/s. This is the largest uncertainty, because body rotation contaminates the scale measured from each feature.
- **Focal length:** ±4% in f gives ±3% in speed (2.32-2.47 m/s).
- **Reference point:** the centroid and the rigid-block centre agree to within 0.3%.
- **Not usable as a check:** the projective-timing fit of the image x motion (which would have given the depth rate without f) failed. The animation's horizontal image speed halves abruptly at frame 29 in mid-air, so the motion isn't constant-velocity physics.

**Confidence:** moderate. The main risks are how the 2.2 m height maps to pixels (rest pose versus walking pose) and the local depth rate.
