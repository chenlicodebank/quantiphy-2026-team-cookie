# q_2296 — length of the white box (cm)

The file and the question both run at 24 fps. Focal length f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Pixel length (profile.py)
- The box is held upright, facing the camera, in frames 0–28. Intensity profiles down columns x = 478–489 put the
  top edge at y ≈ 239.5 and the bottom edge at ≈ 291.5 (frames 0, 10, 20, 26 all agree), so the length is
  **52–53 px** (taken as 52.5). The record's 57–58 px includes blur and shadow.
- Lying on the floor in frame 48 the box spans about 56 px horizontally. This includes a little of the end face, and
  the box is a little nearer the camera there.

## Depth of the box (no depth_info is given for it)
- From the floor plane (horizon y = 342 from the wall vanishing point in scene.json):
  - Soccer ball: distance 2.80 m, so Z = 2.756 m along the optical axis. Its bounce falls between frames 39 and 40
    (centre 541 going down at 44 px/frame, then 531.5 coming up), so the contact is at y ≈ 576. That gives
    f·h = 2.756 x 234 and a camera height h ≈ 0.85 m.
  - The box lands upright at frame 39 with its bottom at y = 598, which gives Z ≈ 2.52 m.
- From where the hands are: the far person's centre is at 3.13 m and the near person's at 2.002 m. Assume the far
  person faces the near person, with the ball in the left hand at 2.8 m. Putting the right hand (box) at image
  u = 481.5 then gives a hand spacing of 0.31 m and Z ≈ 2.49 m.
- Using the far person's feet as the floor reference instead (pelvis at 3.13 m) gives Z ≈ 2.69 m. This is less
  reliable because the pelvis and the feet are not at the same depth.
- Gravity fits (fitfall.py, with the dropped frame between 35 and 36 corrected for) agree for the ball and the
  near objects to within about 9%. For the box the fit is noisy (the hand hides it early on, and the translucent box
  blurs) and gives 3.1–3.7 m. That contradicts the floor contact, which shows the box nearer than the ball, so I did
  not use it.
- I used Z ≈ 2.53 m.

## Result
- Length = 52.5 x 2.53 / 763 = 0.174 m.
- Check: lying in frame 48, 56 px at the floor depth of 2.42 m (contact y ≈ 608) gives 0.178 m.
- Answer: **17.5 cm**. The width across the face is about 21 px, roughly 7 cm.
- Confidence: moderate. The uncertainty in depth is about ±7%; using Z = 2.69 m would give 18.5 cm.
