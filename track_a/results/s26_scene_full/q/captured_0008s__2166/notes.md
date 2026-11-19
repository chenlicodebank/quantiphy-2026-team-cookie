# q_2166: basketball's initial distance from the desk (cm)

The file runs at 24 fps and question_fps is 24, so the two rates agree. Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Reading of the question
depth_info gives the ball and the desk depths both at t=1.0 s (frame 24). I take this as the annotators' "initial" moment, taken just after release; the ball leaves the hand at frames 21-22.
The distance is the 3D distance between the ball centre and the desk centre, each back-projected with its measured
camera distance (the lab method card).

## Measurements (scripts m.py, m2.py)
- Ball centre at frame 24 is (528.6, 152.5) px (scene track; confirmed on frames/f24.png). Back-projected with depth 1.401 m it is (-0.196, -0.364, 1.339) m.
- Desk centre: the board's top-surface corners are BL(479,416), BR(683,379), FR(755,542) and FL(432,604). The diagonals intersect at (586.8, 465.2), and the plain image centroid of the corners is about (587, 485-490). Back-projected with depth 1.725 m.
- Distance: 70.6 cm using the diagonal intersection, 74.0-75.0 cm using the visual centroid. Answer: 72.5 cm, the middle of that range.

## Checks and other readings
- Ball diameter from the given depths and the pixel diameter is 0.218 m at t=1.0, 0.219 m at t=1.2 and 0.226 m at t=1.5. This is consistent with a basketball, so the depths and f agree.
- Using the held position at t=0 instead, with depth from size about 1.39 m: the 3D distance to the desk centre is about 80 cm.
- At impact (frame 30, depth 1.564), the ball centre is 0.20 m from the desk centre. That is plausible for a ball of 0.11 m radius landing slightly off-centre.
- The free-fall route with g = 9.8 (release at about frame 21.5, impact at frame 30, so about 0.35 s) gives a drop of about 0.6 m for the centre, plus 0.11 m of ball radius to the surface, about 0.7 m. This roughly agrees.

Confidence: moderate. The main uncertainties are which moment counts as "initial" (t=1.0 vs t=0, giving 72 vs 80 cm) and which point was clicked as the desk centre (±2.5 cm).
