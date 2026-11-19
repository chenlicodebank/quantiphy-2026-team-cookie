# q_2964 — How tall is the shooter (cm)? Prior: ball = 24 cm

The clip is 2D internet footage (segmented). I used one scale taken from the ball's pixel diameter, following the internet convention.
- Ball diameter, from the free-flight frames 46-92 in scene/tracks/ball.csv: median bbox width 17 px, height 16 px,
  equal-area diameter 16.6 px. The mean is 16.5 px and I used about 16.8 px. A 4x-zoomed crop at frame 57 shows a ball about 16-18 px across.
- Player standing height, frames 0-11, head top to soles: median 112 px (range 111-113). I checked this on a 4x crop at frame 3,
  where the head top is at y≈476 and the soles at y≈588.
- Height = 112 / 16.5-17 x 24 = 158-163 cm. **Answer: 160 cm.** It is plausible for a person.
- Second route: frames 0-11 also give ball sizes of about 16-17 px (equal-area diameter), which leads to the same range.
- Confidence: moderate. The ball is only about 17 px across, so ±1 px on the ball gives ±6 % on the answer.
- question_fps (30) and the file rate (30.0003) are essentially the same. The answer does not depend on time.
