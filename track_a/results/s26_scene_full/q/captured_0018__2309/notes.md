# q_2309 — distance tennis ball ↔ soccer ball at 3.0 s (cm)

**Problem:** the clip has 49 frames at 24 fps (0–2.04 s). The file rate and question_fps are both 24. At 3.0 s the
frame would be 72, which does not exist. So the answer is taken from the end of the clip (frames 44–48), where both
balls have bounced and are near the floor, plus a check against both balls lying on the floor.

**Method (lab method card):** f = 0.5959·1280 = 762.8 px, principal point (640, 360). Each centre is back-projected
as ((u−cx)/f, (v−cy)/f, 1)·Z. Pixel centres come from scene/tracks (they were checked on frames).
- Soccer ball: Z = 2.80 m (given in depth_info).
- Tennis ball: no depth was given. I estimated it three independent ways:
  (a) apparent size: Ø 23–24 px with a real 6.7 cm ball → 2.18 m;
  (b) floor geometry: the soccer ball's floor contact (y=565 at 2.8 m, horizon y≈342) gives a camera height of
      0.82 m, and the tennis ball's floor contact at y=615 then gives 2.29 m;
  (c) arm geometry: the ball is held at arm's length from the near person (2.002 m) towards the far person
      (3.13 m), which gives ≈2.29 m.
  I used Z ≈ 2.25 m. If the near person's 2.002 m were used directly, every distance would be about 17 cm larger.

**Distances (Z_tennis = 2.27 / 2.22):** frame 0: 92 / 94 cm; frame 40: 93 / 95; frame 44: 87 / 89.5; frame 46: 85 / 88;
frame 48 (last): 83.6 / 86.3. With both balls at rest on the floor: ≈82 cm. Late in the clip the soccer ball drifts
right, towards the tennis ball, so the distance is shrinking.

**Answer:** 85 cm. This is the value from the end of the clip, the closest available time to 3.0 s.
**Confidence:** low to moderate. The asked time is outside the video. The answer stays within about ±10 % for any
late-clip or at-rest configuration, as long as Z_tennis ≈ 2.2–2.3 m.
