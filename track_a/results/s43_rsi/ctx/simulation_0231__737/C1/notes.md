# Q737 – width of the orange chair next to the blackboard (simulation_0231)

Prior: speed of the black cat = 0.714 m/s. No depth_info. fps = question_fps = 24, so there is no re-timing.

## Object
The orange wooden chair stands against the wall to the right of the blackboard (x 1600–1797, y 745–1015, frame 24).
It faces the camera and does not move. Its backrest is the widest part: the orange mask is x 1600–1755 in rows
745–800, about 153 px (`chair_profile.py`). The seat's front edge is about 140 px wide and the front legs are
1652–1793 px apart. Both are nearer the camera, so in world units they are narrower than the backrest.

## Scale from the cat
- Cat pixel speed (scene/tracks/cat.csv, `cat_speed.py`): a linear fit of the torso centre, dark centroid, mask
  centroid, nose and torso rear gives 8.86–9.00 px/frame, mean about 8.93 px/frame = 214.3 px/s. The speed is
  constant (quadratic term ≈ 0).
  Metres per pixel at the cat's depth: 0.714 / 214.3 = 0.003332 m/px.
- The scene is not exactly 2D: the chair is nearer the camera than the cat. Depths were found by perspective:
  - Vanishing point from Hough lines on the ceiling seams (`vp.py`): (961, 540). This is the image centre, so the
    camera is level and the horizon is at y = 540.
  - Floor–wall line at y 951, so the wall depth Z_w ∝ 1/411.
  - The chair's back-right leg meets the floor at y 991, so Z_chair_back = 411/451 Z_w = 0.911 Z_w. The front
    legs meet the floor at y ≈ 1015 (0.865 Z_w). Check: the x-shift of the leg pairs gives a back/front ratio of
    1.059, against 1.053 from the floor rows.
  - Desk top: rear edge at y 733 (it hides the bottom of the board frame), front edge at y 766. The kick-plate
    shadow ends on the floor at y ≈ 1026. That makes the desk front 0.846 Z_w and the rear 0.99 Z_w, so the desk
    stands against the wall. The desk height comes out at 0.53 H, which is plausible.
  - The cat's stance paws touch down at y 739–742, so its midline is about y 740.5. That puts the cat at
    193/200.5 Z_w = 0.963 Z_w (desk rear at the wall) or 0.953 Z_w (from the desk front and floor contact).
    I used 0.958 Z_w.
- Scale at the chair's backrest: 0.003332 × 0.911 / 0.958 = 0.003169 m/px.

## Answer
Width = 153 px × 0.003169 = **0.485 m**. Without the depth correction it would be 0.51 m.

Sanity check: this scale gives a camera height of 1.44 m, a desk height of 0.76 m, a chair seat height of 0.41 m,
a chair-back height of 0.78 m and a cat torso length of about 0.49 m. All are plausible.

## Confidence
Moderate to good, about ±5%. The main uncertainties are:
- the depth ratio between the cat and the chair (±1.5%);
- the backrest edge pixels (±1%);
- whether the reference speed includes the cat's vertical bob (+≤1%);
- whether "width" means the backrest's x-extent, which is the bounding-box x-extent if the chair is axis-aligned.
