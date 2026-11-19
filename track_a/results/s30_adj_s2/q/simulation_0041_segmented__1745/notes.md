# q1745: length of the boat (m). Prior: the person is 1.75 m tall. No depth_info.

File fps = question_fps = 24. Segmented Blender render, 1080x1080. The camera is fixed, uses a long lens, and looks steeply
down on the scene: the top of the person's head, the boat's deck and the cabin roof are all visible. So this is a 3D
oblique view, not a planar 2D scene.

## Where the candidates part ways
- C2 (13.1) used a 2D planar scale: 47.5 px person = 1.75 m. That ignores foreshortening. Seen from above, the
  person's vertical height is shrunk by cos(pitch), while the boat's length lies almost flat in the image plane. This
  is wrong. As a check, it would make the person only 0.7 m wide.
- C1 (10.0) modelled the camera pitch theta. It gives the person's image extent as k(1.64 cos + 0.105 + 0.17 sin) and
  the boat length as x-extent / (k cos psi). It chose theta = 58 deg. I agree with this method.

## My measurements (measure.py, roof.py, hatch.py, scalechange.py)
- Boat x-extent, bow tip to stern, frames 0-4: 336.5 px (thresholds 25 and 40). I subtract about 2 px because the stern
  is rounded, so the rightmost image point is not on the centreline. Image heading = boat motion direction (-396, -111),
  15.7 deg, which matches the long edges of the cabin roof and hatch (14-18 deg).
- Person: minimum image extent at mid-stance 39-40 px (about 39.3 px); maximum 50-51 px; width about 19 px. The person
  walks straight down the image, toward the camera.
- Pitch theta from transverse horizontal edges, using tan(tilt from vertical) = tan(heading angle) / sin^2(theta):
  - Cabin roof aft edge: 55-61 deg.
  - Green hatch lid edges: 50-66 deg, scattered, centre about 60.
  - Person anatomy at 60 deg: width 0.52 m, step 0.80 m, speed 1.1 m/s. This favours 58-62.
  - C1's mast-lean nadir (f cot theta about 5030 px; my global ECC shear gives about 5760) together with FOV >= about
    8 deg gives theta <= about 57.
  - I take theta = 58 +/- 2.
- Perspective factor from person to boat (boat lower in the image, so nearer): 1.035-1.045.

## Result
L = 334.5 / (k_b cos psi), where k_b = ratio x 39.3 / (1.64c + 0.105 + 0.17s):
- theta 56: 10.0 m
- theta 58: 9.6 m
- theta 60: 9.3 m

Second route, scale from the person's width alone (19 px for 0.50-0.55 m): 8.9-9.8 m.

Answer: 9.7 m. This is close to C1 (10.0, same method; small differences in the person's minimum extent and the stern
correction). C2 is rejected because a planar scale is not valid for this steep oblique view.

Confidence: moderate (+/- 7 %). The main uncertainty is the camera pitch.
