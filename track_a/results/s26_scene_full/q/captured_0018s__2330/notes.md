# q2330: pineapple toy (yellow_fruit) to tennis ball (green_ball) distance at 3.0 s

**Main problem:** the clip has only 49 frames (0–2.04 s at 24 fps; the file rate and question_fps are both 24).
t = 3.0 s is frame 72, which is not in the video, so the answer is an extrapolation from the state at f36–48.

Camera: f = 0.5959·1280 = 763 px, principal point (640, 360).

## Depths (neither object's depth is given)
- **Floor plane from the people.** I took each person's given distance as their pelvis distance and converted it to forward
  depth: near person 1.817 m (feet at row 716), far person 2.966 m (feet at row 577). That puts the horizon at v = 357
  and the camera 0.855 m above the floor. Ground-contact depth is Z = 0.855·763/(v_bottom − 357).
- **Tennis ball:** the ground model gives Z = 2.52 (bounce bottom at row 616). Gravity fits of the free fall
  (f28/29–35) give 2.41–2.56. Its 22 px diameter at a 6.7 cm ball size gives 2.32. I used Z ≈ 2.48.
- **Pineapple toy:** the ground model at its first bounce (f36, bottom 697) gives 1.92, and the gravity fit gives 2.28.
  The toy then hops and tumbles away from the camera. Its bottom row rises to 617–631 and its width shrinks from 30 to 23 px,
  so Z ≈ 2.5 at f48, and it is still moving away (about 0.03 m/frame) and to the right (+5 px/frame).
- The method works on the soccer ball too: its gravity fit gives 2.2–2.6 m and the floor model 2.7–2.97 m, against a given 2.70 m.

## Positions
- **Tennis ball:** it bounces in place at x ≈ 747; the apex at f45 is about 0.58 m high. Projecting the bounces forward
  (restitution e² ≈ 0.53) puts it close to the floor at f72. I used its resting centre (747, 613) at Z = 2.48, which gives
  (0.35, 0.82, 2.48) m.
- **Pineapple toy at f48:** centre (847, 596) at Z = 2.53, which gives (0.69, 0.78, 2.53) m.
  - With the toy left where it is at f48, the distance is **34 cm**.
  - Letting it move on, slowing to a stop (x ≈ 870, Z ≈ 2.7, on the floor), the distance is **52 cm**.
- If the f48 frame were taken literally, with the ball in the air (cy 442), the distance would be about 61 cm. I rejected this
  because the ball should be near the floor by f72.

## Answer
**42 cm**, a compromise between the 34 cm and 52 cm estimates. Confidence is low: the asked time lies outside the video,
so the answer depends on where the toy stops.
