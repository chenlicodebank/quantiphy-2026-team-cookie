# q_648 – height of the small robot (m)

Prior: robot speed = 0.82 m/s. 2D scene: the robot walks right-to-left parallel to the wall, and the camera is static. The robot is the only moving object, so it is the "small robot".
Time base: the file's fps and question_fps are both 24.

## Scale (measure.py)
- Horizontal pixel speed from linear fits over the measured frames: ref_x (belly disk) 204.5, mask centroid 204.0,
  bbox centre 203.5 px/s.
- Baselines covering whole gait cycles (0-38, 0-39, 1-40, 4-42, 6-45, 8-46) all give 204.2-205.8 px/s.
- I used 204.5 px/s, which gives 0.82 / 204.5 = 0.00401 m/px. The mean per-frame 2D speed of the disk is 211 px/s, but that is inflated
  by tracking jitter and torso sway, so I did not use it.

## Height
- Pixel height from dome top to foot bottom (scene record, spot-checked on zoomed frames 12 and 24): 297-321 px.
  Median 307.5, mean 309. The maximum of 320-321 px comes at mid-stance with the legs straight (frames 10-13 and 47-49), which is the closest to a rest pose.
- Standing (max) reading: 321 x 0.00401 = 1.29 m. Mean reading while walking: 309 x 0.00401 = 1.24 m.
- Answer: 1.26 m, between the two readings and within about 2.5% of each.

## Check
Three different reference points (disk, mask centroid, bbox centre) and several baselines agree on the pixel speed
within 1%. The height reading (rest pose or walking average) is the main uncertainty, at about ±3%.
