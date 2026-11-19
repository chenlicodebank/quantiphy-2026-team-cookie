# q1155 – length of the boat (prior: boat speed 4 m/s)

File is 25 fps / 75 frames, question_fps = 24. Frames 1, 26, 51 duplicate 0, 25, 50, so the clip is a
72-frame 24 fps render padded to 25 fps: orig = file-1 (2..25), file-2 (27..50), file-3 (52..74).
Camera is static. Steep aerial view; the depths (~177 m) give a narrow FOV (f ≈ 9000 px), so the view is
nearly orthographic. The boat translates bow-first at constant speed with no rotation.

Method (ratio, same direction, same plane): in a near-orthographic view a horizontal length along the boat's
direction of motion is foreshortened exactly like the motion itself. So L = (pixel extent along the motion
direction) / (pixel step per 24-fps frame) x (4/24 m).
- measure.py / speed.py: colour mask of the boat (red hull + white deck). I made a linear fit of the centroid vs
  original frame index (duplicates dropped, frames to 64 before the bow leaves the image): 8.315 px/frame at
  15.55 deg (rms residual 0.5 px). The windows 0-20 / 20-40 / 40-62 give 8.33 / 8.36 / 8.27, so the speed is
  constant. Scale along the motion is 0.02004 m/px.
- extent.py: the mask extent along the 15.55 deg direction is 495 / 493 / 492 / 491.5 / 490 / 490 px at file
  frames 5-55 (it shrinks slightly as the boat moves away). The bow tip at deck level is at (309,1261) in f25,
  and the aft extreme is the stern gunwale/rail at (775,1422), at a similar height, so no height correction is
  needed. A manual deck-level bow-to-stern estimate gives 495-500 px.
- L = 492 / 8.315 / 6 = 9.86 m (range 9.8-10.0).

Check: the given depths (177.21 m at t=1 s, 178.00 m at t=2 s) plus 4 m of travel give a ray angle of 0.0221 rad
for a 198.6 px centroid shift, so f ≈ 9000 px and s ≈ 50.7 px/m at the boat. The image speed of 199.6 px/s is
then 3.94 m/s, about 0.98 of 4 m/s, which fits a camera pitch of about 53 deg. That pitch also reproduces the
depth rate (+0.79 m/s). The person's ~63 px image height fits a roughly 1.8 m adult at that pitch. A 9.9 m
fishing boat is plausible.
Confidence: good, about ±3%.
