# Q10 – diameter of the ball (m)

Prior: gravity 9.8 m/s². depth_info: none. question_fps 30 (file 29.9977 fps; frame indices used).

## Gravity prior gives no usable scale
The ball's motion is keyframed, not ballistic:
- flight (frames 21–77): vertical pixel acceleration only ~0.17 px/frame², so 9.8 m/s² would make the ball ~2 m wide
- drop after the net (99–116): dy rises to ~13 px/frame and then levels off (not a constant acceleration)
- bounce: rises 29 px in 3 frames, where free fall allows about 6 px
No consistent px/m comes out of gravity, so I took the scale from objects of known size, as the rules allow.

## Measurements (my own scripts: measure.py, profile.py, ballsize.py, ballsize2.py, vp.py, vp2.py, crop.py)
- Ball pixel diameter (difference mask against a ball-free frame, area-equivalent, thresholds 60/90):
  at rest (frame 127–129) 32.6 / 31.2 px; during the drop 32.4 / 30.8 px; early flight 33.5 / 31.5 px.
  I take **31.8 ± 1 px** at the rest/drop depth. The scene record's 29.6 px came from a tight HSV mask and is a slight underestimate.
- Horizon / principal point: the sidewalk seams converge near (547, 540). The camera is level and faces the wall squarely.
- Rim (regulation-shaped, seen near edge-on): horizontal outer extent x 253.75–317.5 = **63.75 px**. After the net the
  ball falls straight down at constant x = 293 to rest, so it sits at the rim's depth.
- Player standing (frame 129): head top ≈ 583, shoe soles ≈ 798, so **215 px**. Ground rows: player 798, ball contact 777.7,
  so the ball is 8.5 % farther than the player ((798−540)/(777.7−540)).

## Scale routes
1. Rim/ball at the same depth: ratio 31.8/63.75 = 0.499. A regulation rim is 0.457 m inside and ≈0.49 m outside
   (with the tube), which gives D ≈ 0.237–0.245 m. That matches a regulation size-7 basketball (0.239–0.243 m).
2. Player: D/H = 31.8/215 × 1.085 = 0.161, so D = 0.245 gives a player 1.53 m tall (inside the 1.5–2.0 m check, but low).
   An assumed 1.75 m player would give 0.28 m.
3. Rim height with D = 0.245 is about 2.24 m (portable or adjustable hoop). The scene is not fully regulation.

The ball/rim ratio is the most direct check (same depth, no focal length needed) and agrees with a regulation basketball,
so I answer 0.24 m.
Confidence: moderate. If the scene scaled the hoop and ball together around a 1.75 m player, the answer would be ~0.28.
