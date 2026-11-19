# q_2311 — distance pineapple toy ↔ tennis ball at 3.0 s (cm)

Pineapple toy = scene/ "lemon_plush" (a yellow plush with dark green leaves). File fps = question_fps = 24.
**The clip has only 49 frames (0–48, 2.04 s), so frame 72 (3.0 s) is not in the video.** The answer is an
extrapolation from the end of the clip.

## State at the end of the clip
- Pineapple: dropped at about frame 27. It hits the floor at frame 36 (bottom y 703, near the camera), bounces back
  and away from the camera, and from frame 41 to 48 it rocks in place around (838–849, 596–613). Its body looks about
  22×35 px there, against 27×42 px when held, which agrees with it being farther away now. I take it as resting at
  body centre (847, 598), with floor contact at y≈622.
- Tennis ball: it bounces straight up and down at x≈749–750 and its size stays constant, so its depth is constant.
  It hit the floor once (bottom y 615) and was coming down again at frame 48.

## Scale and depth
- Floor plane: horizon y = 342 (from scene/ vanishing points), focal f = 763, and Z = h·f/(v − 342).
- Tennis-ball depth from the gravity prior: a parabola fit to the fall (frames 28–35) gives 5.55 px/frame², so
  Z = g·f/(a·24²) = 2.34 m. Then h = 2.34·273/763 = 0.84 m.
- Cross-checks on h: near person (2.002 m, feet at y≈687) gives 0.82–0.83; far person (3.13 m, feet at y≈570)
  gives 0.885; soccer ball (2.8 m, bottom at y 565) gives 0.79–0.81. I used h = 0.835.
- Resulting depths: tennis ball Z = 2.33 m; pineapple Z = 2.275 m (from its floor contact at y 622).
- Caveat: the rebound arc (frames 37–48) gives only 4.26 px/frame². That would mean Z = 3.0 m, which the ball's size
  and the floor geometry rule out, so the camera's frame timing is irregular. scene/ also notes a probable dropped
  frame between frames 35 and 36.

## Tennis ball at frame 72
- I extrapolated the bounces in frame units from the rebound arc: vertex at frame 45.0 and y 424.4, contact-level
  centre y 603.5.
- From the heights, e² = 179/348.5 = 0.514 (rebound height over drop height). That puts the third arc at frames
  67.3–76.7, with frame 72 near its apex, so the centre is at y≈556 (about 0.14 m above contact level).

## Result
- Back-projected 3D centres give **31.0 cm**.
- Sensitivity to the bounce model: with e² from 0.45 to 0.56 the distance is 29.7–31.8 cm, and 29.2 cm if the ball
  is on the floor.
- Sensitivity to scale: depth between 2.13 m (ball-size estimate) and 2.49 m changes the result by about ±7%.

Confidence: moderate. The main risk is that 3.0 s is outside the clip: the pineapple could have moved further, or
the tennis ball could have drifted.
