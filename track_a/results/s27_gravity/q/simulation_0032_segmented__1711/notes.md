# q_1711: height of the person (m)

The file rate and question_fps are both 30 fps. The prior is gravity = 9.8 m/s². The depth_info gives the ball at 13.80 m at t = 1 s and at t = 2 s. The cars named in depth_info do not appear in this clip, so those values are ignored.

## Gravity prior gives no usable scale
The ball's motion is keyframed, not ballistic (see `fit.py`):
- **Flight:** the image acceleration runs from about 208 px/s² early to 63 px/s² late. The x-velocity drops from 11 to 1 px/frame while the ball's size stays constant.
- **Drop below the net:** about 720 px/s² at first, then a constant 12.9 px/frame, then it eases in before reaching the floor.
- **Rebound:** about 9000 px/s².

No single g matches these. Taking the scale from them would make the ball anywhere from 0.04 m to 0.45 m across. So the scale has to come from object sizes.

## Measurements (`measure.py`, `heldball2.py`)
- **Ball apparent diameter in flight:** 35.2 ± 0.5 px from the soft-alpha area over 47 frames, at R = 13.80 m. It is 33.2 px after the net, so R ≈ 14.6 m there.
- **Ball held at frames 0–1:** about 35.5 px tall. In the crouch the player is in profile facing left and holds the ball beside his body. So the ball and the pelvis are at about the same depth, and I take the pelvis at R ≈ 13.8 m.
- **Player standing height (frames 56–127):** 216.5 px, from head top y = 583 to soles y ≈ 799.
- **Head height (crown to chin):** about 30.5 px. The body is about 7.1 heads tall, which is normal adult proportion.
- **Invisible hoop:** the rim edge is at y ≈ 495 and the floor, from the bottom of the bouncing ball, at y ≈ 778. That is 283 px at R ≈ 14.4 m.

## Candidate scales (they disagree; the scene is not consistently real-scale)
| Assumption | f (px) | Person height |
| --- | --- | --- |
| Regulation ball, D = 0.24 m | 2014 | 1.47 m (just under the 1.5 m adult check) |
| Adult head height 0.23 m (head at the ball's depth) | — | about 1.62 m; the ball would then be about 0.265 m |
| Regulation rim height 3.05 m | — | 2.21 m (fails the ≤ 2.0 m check); the ball would be 0.36 m |
| Typical adult character, about 1.8 m | — | ball about 0.29 m, rim about 2.5 m |

For the ball route, f = 35.2·13.8/(0.24·1.005), where 1.005 corrects for the ball being off the optical axis. The person height is 216.5·Z/f with Z = 13.8·cos(8.8°) = 13.64 m.

## Answer
**1.65 m.** No single geometric route is reliable. The ball route gives 1.47 m and the head-proportion route gives about 1.62 m. A realistic adult character would be 1.7–1.8 m. The hoop route, at 2.2 m, is implausible.

I chose a value between the ball and head routes and the adult-person check. This is a judgement call, not a single measurement. Confidence is low to moderate: the true value is probably within ±15%.
