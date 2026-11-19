# q_2859 – soccer ball velocity at t = 0.5 s (captured_0054ax)

question_fps = file fps = 24, so t = 0.5 s is frame 12. Camera f = 0.5959·1280 = 762.8 px, principal point (640, 360).

## Checking the time base with the prior (orange ball = basketball)
- `bb_check.py`: I back-projected the basketball's circle-fit centre using depths 2.3557 m at f12 and 1.81 m at f24 (linear in between).
  That gives 2.36 m/s for f11→f12 (the release jump) and about 1.6 m/s afterwards. This is close to the prior of 2.21 m/s at 0.5 s,
  so frame 12 is the right frame. Ball diameter from f12 is 0.239 m, which fits a basketball.
- The depth_info "white" and "green" balls (about 3.05 m at 1.0 s) are the two small thrown balls near the standing person.
  They are not the soccer ball, which is about 2.4 m away (0.22 m ball at about 70 px diameter). No depth is given for the soccer ball.

## Soccer ball at frame 12
- On the zoomed frame (frames/soc12.png), the soccer ball sits on the floor under the crouching person's left hand. It does not start
  moving until frame 23 (the push), and leaves the hand at frame 29.
- Circle-fit centres from scene/tracks/soccer_ball.csv for f10–f14: (154.92,597.72), (154.43,597.85), (154.07,597.88), (154.26,598.19),
  (154.30,598.12). The mean per-frame displacement is 0.33 px. At Z ≈ 2.4 m, that is 0.33·2.4/763·24 ≈ 0.025 m/s.
- Second route (`soccer_rest.py`): sub-pixel phase correlation of the patch texture on the lower ball, relative to frame 12. The texture
  shifts about 2 px between f9 and f12 (a slight rotation under the hand). Central differences at f12 give 0.019–0.041 m/s, and the mean of
  the per-frame forward speeds over f10–14 is 0.045 m/s. Texture motion overstates centre motion a little, because part of it is rotation.
- The true velocity is essentially zero (the ball is at rest, 0.02–0.04 m/s of jitter or small wobble).
  The reference answer, made from clicked centres smoothed over 5 frames, should be a small number of the same order.
  Answer: 0.04 m/s.

## Confidence
Low for the exact number. The ball is clearly stationary at 0.5 s, so the reference value is a noise-level quantity, and any
small positive answer has a large relative error against it. If the question meant the basketball instead, the answer would be about
2.2 m/s (the prior). I did not use that reading.
