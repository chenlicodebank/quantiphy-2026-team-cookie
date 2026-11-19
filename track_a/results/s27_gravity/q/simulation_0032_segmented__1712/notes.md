# q_1712 — initial velocity of the ball (m/s)

File fps = question_fps = 30. Script: `measure.py` (ball mask centroid/diameter per frame, quadratic fits around release).

## What the clip shows
A basketball player shoots a red ball. The ball is held in frames 0–23 and released at frame 24. I read
"initial velocity" as the launch (release) speed, because frames 0–2 show a held ball at rest (about 0 m/s).

## The gravity prior gives no usable scale
The flight is not ballistic in the image. The image acceleration is about (−0.2 then +0.15, +0.2) px/frame², and
x speeds up early, then slows down. The ball also slows down before it reaches the floor.
- At the ball's real scale (below), the image acceleration is about 1.2–1.5 m/s², not 9.8 m/s².
- If 9.8 m/s² were forced as the scale, the 33 px ball would be about 2 m across, which is impossible.

So the motion is animated rather than simulated, and the prior is not usable. As the rules say for this case, I took
the scale from the regulation basketball and the given depth.

## Scale
- Ball diameter in flight (frames 24–78): 32.7 px from the mask area, and about 33 px from the bbox height. The
  scene record's 35 px used a looser threshold.
- Depth is about 13.80 m at t = 1 s and at t = 2 s, so the ball moves essentially in a plane parallel to the image.
- Focal length = 33 × 13.8 / 0.24 ≈ 1900 px.
- Metres per pixel = 0.24 / 33 = 0.00727 m/px.
- Check with the player: 217 px head to sole → 217 × 13.8 / 1900 ≈ 1.58 m. That is plausible, a bit short. A 1.7 m
  player would give 0.0078 m/px.
- The depth_info also lists orange and green cars, which do not appear in this video. I ignored them.

## Velocity
- Quadratic fits of cx and cy over frames 24–32, 24–36, 24–40 and 25–35, evaluated at release (frame 23.5–24),
  give |v| = 10.71–10.88 px/frame, about 10.75 px/frame = 322 px/s.
- Backward differences give 9.8 px/frame at frame 24 (frame 23 is the hand-occluded fit), then 10.4, 11.1 and 11.0.
- The depth component is about 0 (the given distances at t = 1 and 2 s agree to 5 mm, and the ball's size is
  constant).
- With the ball scale: 322 × 0.00727 = 2.35 m/s. With the player scale (1.7 m): 2.52 m/s.

**Answer: 2.4 m/s**, mostly the ball scale.

Confidence: moderate. The main risk is how "initial" is defined: if it means t = 0, the ball is held and the answer is
about 0. The scale uncertainty is about ±7%.
