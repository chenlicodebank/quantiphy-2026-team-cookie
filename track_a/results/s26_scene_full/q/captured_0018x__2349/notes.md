# q_2349: distance between the pineapple toy (yellow_plush) and the tennis ball at 3.0 s

**Main problem:** the clip has only 49 frames (0–48, which is 0–2.0 s at 24 fps). The question asks about t = 3.0 s, which is frame 72 and lies past the end of the clip. So the answer comes from the end-of-clip state plus an extrapolation. The file fps and question_fps are both 24.

## Depths (depth_info gives only the soccer ball and the two people)
- The camera is level (the far person's centre row is 376, close to cy = 360). Its height is about 0.84–0.89 m, worked out from the far person's feet (y = 577 at Z = 3.13) and the near person's feet.
- **Tennis ball depth Z ≈ 2.5 m**, from three routes:
  - Gravity fit, frames 28–35 (gfit.py): 3000–3130 px/s², giving Z = 2.39–2.51.
  - Size: diameter 20.5 px for a 6.7 cm ball gives 2.49.
  - Floor row: bottom y = 616 at impact gives Z ≤ 2.65.
- For comparison, the gravity method on the soccer ball, allowing for the dropped frame at 35→36, gives about 3.0–3.1 m against the given 2.8 m. So the gravity-based depths may be up to about 10% high.
- **Plush:**
  - It was held at about 2.0 m and hit the floor at frame 36 (bottom y = 697, about 2.0 m).
  - It then bounced away from the camera. From frame 43 on it lies and slowly tumbles on the floor with its bottom at y ≈ 617–631. That is the same floor row as the tennis ball's contact point, so the plush ends up at about the tennis ball's depth (floor-row ratio, which does not depend on the camera height).

## Positions and distance (back-projection, f = 763, principal point (640, 360))
- **Frame 48 (last frame):**
  - Plush centre (846, 595), Z ≈ 2.49.
  - Tennis ball x = 747, resting row 606, Z = 2.5. At this frame the ball is in its second bounce.
  - Distance: **32.4 cm**.
- **Extrapolated to frame 72:**
  - The plush was still drifting right and away at about 2–3 px per frame at frame 48, so I assumed about 10 px more.
  - Tennis-ball bounce model with restitution e ≈ 0.72: at frame 72 the ball is about 0.06 m above rest. Its x drifts to about 741.
  - Distance: **38.7 cm**.
- **Answer = mean of the two = 35.6 cm.**

## Confidence
Low to moderate. The time asked is outside the clip, the depths of both objects are inferred rather than given, and the plush may have kept rolling. The plausible range is about 30–42 cm.
