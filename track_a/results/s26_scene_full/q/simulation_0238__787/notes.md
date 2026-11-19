# Q787: height of the house (m)

Prior: the horse at the back has a speed of 0.874 m/s. This is a 2D video at 24 fps (file rate = question_fps).

- "Horse at the back" = the trailing horse. Both horses walk right (+x), and the brown/chestnut horse on the left is behind.
  Check: with this scale the brown horse is 183.5 px × 0.0113 ≈ 2.1 m long and ≈ 1.8 m to the top of its head, which is plausible.
  If the tan horse were the reference, the tan horse would be only 1.3 m long and the house 4.4 m tall, which is implausible.
- Brown horse speed in px/frame (frames 0-48; frame 49 is an animation loop reset):
  - linear fit of the record's ref_x: 3.24
  - fit of the torso rear edge: 3.23
  - chained template matching of the torso (tm.py): 157 px / 48 frames = 3.27
  - net ref_x change: 3.15

  I used 3.21 px/frame = 77.0 px/s, so the scale is 0.874 / 77.0 = 0.01135 m/px.
- House height in px: the roof apex tip is at y ≈ 258-260 (column profile plus a zoomed crop) and the wall base is at y ≈ 1040.
  The base is partly hidden by grass. That gives about 782 px, which agrees with the record's 783.
- Height = 782 × 0.01135 ≈ 8.9 m. The speed estimates range from 3.15 to 3.27, which gives 8.7-9.0 m.
- Confidence: moderate-good (±4%). The main uncertainties are the base hidden by grass and gait jitter in the speed.
  The horses walk just in front of the wall, so they are at practically the same depth as the facade.
