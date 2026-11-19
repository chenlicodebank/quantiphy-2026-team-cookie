# q_2173 — max rebounce height of basketball above desk (cm)

The file and the question are both 24 fps, so t = frame/24. I used the circle-fit centres from scene/tracks/ball.csv and
checked them visually on frames 30 and 36. The first impact is at frame 30 (cy 421, ball on the tabletop) and the first
apex at frame 36 (t = 1.5 s, matching the "max rebounce" depth). The second apex (frame 46) is much lower, so the
maximum is the first rebound.

Reading of the question: the rebounce height above the desk is the gap between the desk and the ball's bottom at the apex.
That equals the vertical rise of the ball centre from impact (centre one radius above the desk) to the apex.

## Route 1: 3D back-projection (measure.py, measure2.py)
- f = 0.5959*1280 = 763 px, principal point (640, 360). Apex: (548.9, 306.2) at a distance of 1.5225 m.
- Impact frame 30: depth not given. From apparent size (k = dist*r calibrated on the given frames 29 and 36) it is
  ~1.598 m; values from 1.564 to 1.616 give a rise of 0.236-0.259 m.
- Vertical direction: the tabletop vanishing-line normal (tilt 23.6 deg) gives 0.247-0.251 m. The fall direction gives
  0.245 and camera -y gives 0.233.
- Ball diameter check: 2*r*dist/f = 0.206-0.214 m, which is plausible.
- The free-fall drop from frame 24 to 29 is 0.48 m by back-projection against 0.51 m expected with g = 9.8, so the
  scale agrees within about 6%.

## Route 2: physics with the prior g = 9.8
- Parabola fit of cy over frames 31-40 puts the contacts at frames 30.08 and 41.12 (flight time 0.460 s) and the apex at
  frame 35.6.
- h = g*T^2/8 = 0.259 m.

## Answer
About 0.25 m, so **25 cm**. Route 1 gives 0.24-0.25 m and Route 2 gives 0.26 m.

Other readings, each a possible reference:
- Ball centre height above the desk at the apex: rise + radius, about 0.35 m.
- Rise measured from the t = 1.2 s position (frame 29, still above the impact point): about 0.19 m.

The desk distance of 1.725 m does not agree with the tabletop plane estimate (that plane gives 1.56 m at the desk
centre), so it was not used. Confidence: moderate.
