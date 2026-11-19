# q1154 – speed of the person at t = 1.0 s

Time base: file is 25 fps / 75 frames, but frames 1, 26, 51 are duplicates. That leaves 72 unique frames, which is
3 s at question_fps = 24. Mapping true frame k -> file frame: k=0 -> 0; k 1..24 -> k+1; k 25..48 -> k+2; k 49..71 -> k+3.
t=1 s -> k=24 (file 25); t=2 s -> k=48 (file 50).

Scale (measure.py): pinhole camera with the principal point at the centre (768,768). Boat track (scene/tracks/boat.csv
centroid, linear fit over k=1..69, 8.30 px/frame). I back-projected the boat at k=24 and k=48 with the given depths
(177.2077 m, 177.9993 m) and solved for the focal length that makes the 3D displacement over 1 s equal 4 m:
f ≈ 9000 px (9084 using the raw centroids). That is a horizontal FOV of about 9.7°.
Check: the 495 px hull comes out at about 9.7 m, which is plausible for a fishing boat.

Camera tilt (ground.py): the boat's 3D motion vector in camera coordinates must be horizontal. Assuming no roll, this
gives a camera elevation of about 54.5°, so the ray to the person is about 37° from vertical.

Person: the given distances change by only +0.09 m/s, although the body visibly walks toward the bottom of the image
(toward the camera on the ground). This is the "origin stays put" case, so I did not use those distances to get the
body's motion. I used them only for scale (the person is about 183 m from the camera). I intersected the pelvis pixel
track (linear fit, 2.16 px/frame, almost straight down the image) with the horizontal plane through the pelvis at
k=24. Ground speed = 1.306 m/s for windows 23–25, 12–36, 1–47 and 1.301 m/s for 1–71 (f=9084). With f=9000 it is
1.313 m/s. Walking straight on the ground would reduce the depth by about 0.78 m/s, which shows that the given
person depth is not the body's.

Second route / checks:
- With no tilt correction (image-plane motion only, using the given person depths) the speed is 1.05 m/s. That route
  is rejected, because the view is tilted and the walk points toward the camera.
- Person image height is 55–71 px. The 55 px minimum (feet together) gives 1.12 m perpendicular to the ray, i.e.
  about 1.86 m standing height once the ~37° foreshortening is removed. The 63 px median includes stride.
  These numbers are consistent with an adult.
- 1.31 m/s is a normal walking speed.
- Local fits around k=24 vary from 2.25 to 2.46 px/frame because the bird occludes the person at k≈23–25 and the
  centroid jitters with gait. I used the steady long-window rate.

Answer: 1.31 m/s. Confidence moderate: the main uncertainties are the tilt (from the boat's small depth change) and
the principal point.
