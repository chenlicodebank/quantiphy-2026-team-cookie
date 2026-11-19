# Q815 – length of the rabbit (m)

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Which objects
- Two horses walk +x: the brown one (upper, y≈776) and the white one (middle, y≈865). The brown one is behind the white one
  in the walking direction and also further up the image, so it is "the horse at the back" under either reading.
- Rabbit = small tan/white animal at the bottom (y≈924).
- 2D top-down scene with a static camera, and all animals are on the same ground plane, so one m/px scale applies.

## Scale (horse_speed.py)
- Template-matched the brown horse's trunk (frame-0 template, sub-pixel peak) in frames 0-48. Frame 49 is a loop reset.
  Linear-fit speeds from three templates: 2.632, 2.675, 2.620 px/frame. Net displacement / 48 frames: 2.665, 2.657, 2.634.
  The scene record's centroid gives 2.594 px/frame. I used 2.64 px/frame = 63.4 px/s.
  (Chaining frame to frame underestimates, at 2.19, because the static grass background pulls the match back, so I rejected it.)
- Scale = 0.874 / 63.4 = 0.01379 m/px.

## Rabbit length (rabbit_len.py)
- Warm-colour mask on the rabbit in every frame, x-extent along the motion direction (bbox length).
  At a 30 % threshold: median 34 px (range 31-40 with the gait). At 50 %: median 31 px. The scene record's background-difference bbox gives a median of 36 px.
- I used 34 px, giving a length of 34 × 0.01379 = **0.47 m** (range 0.43-0.50 for 31-36 px).

## Check
- With the same scale, the brown horse is 144 px = 1.99 m long and the white horse 177 px = 2.44 m. Both are plausible horse lengths,
  which supports the scale. The rabbit's ratio to the horse is 34/144 = 0.24.

Confidence: moderate. The main uncertainty is the rabbit's pixel extent (±2 px ≈ ±6 %), plus about 2 % in the speed.
