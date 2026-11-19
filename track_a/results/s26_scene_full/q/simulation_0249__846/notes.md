# Q846: speed of the rabbit at 1 s (m/s)

Prior: the horse at the back moves at 0.874 m/s. depth_info: none. fps = question_fps = 24.

The scene is 2D, filmed top-down, with three animals walking toward +x. "Horse at the back" = brown_horse: it is the trailing horse (x ~ 600-830 px, while the tan horse is at ~1000-1360 px) and it is also in the upper lane. The rabbit is small_brown_animal (bottom lane, ~64x33 px).

## Measurements (measure.py)
I tracked each torso by template matching between consecutive frames, with sub-pixel peak fitting, and compared the result with the scene/ tracks.
- brown_horse, frames 0-48 (frame 49 is an animation-loop reset back to the frame-0 pose, so I excluded it):
  - template: 4.54 px/frame
  - core centroid: 213/48 = 4.44 px/frame
  - bbox centre: 206/48 = 4.29 px/frame
  - adopted: 4.50 px/frame = 108 px/s
- Scale: 0.874 / 108 = 0.00809 m/px. Sanity check: the horse's length of 246 px gives ~2.0 m and the rabbit's 64 px gives ~0.52 m.
- rabbit, frames 0-49:
  - template: 7.58 px/frame
  - core centroid: 376/49 = 7.67 px/frame
  - bbox centre: 374/49 = 7.63 px/frame
  - Long-run speed is very steady: core displacement is 76-77 px per 10 frames in every block.
  - adopted: 7.62 px/frame = 182.9 px/s

The torso's per-frame steps oscillate with the gait (5.6-9.6 px/frame, period ~12 frames). At frame 23->24 the torso step is 8.4 px/frame. I assumed the Blender origin moves uniformly and used the steady long-run rate. If it instead followed the torso bob, the answer would be ~1.63 m/s.

## Answer
1.48 m/s: 182.9 px/s x 0.00809 m/px. The ratio route gives the same: 0.874 x 7.62/4.50 = 1.48.

Second route: using only the core centroids gives 0.874 x 7.67/4.44 = 1.51. Using only the bbox centres gives 1.55. Using only template matching gives 1.46.

Confidence: moderate. The main uncertainties are the horse's mean speed (~±3%) and whether the reference used the instantaneous gait-modulated step at frame 24.
