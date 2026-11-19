# q3074 – diameter of the white (ping-pong) ball, prior g = 9.8 m/s^2

Internet video, 30 fps (file fps = question_fps; no re-timing needed). Camera drift is small (handled by the
scene record's frame-0-stabilised track). Following the annotators' convention I used one planar scale from the prior.

## Scale from gravity (fit_g.py)
I fitted a quadratic in y to the measured (not arc-filled) ball centroids of each arc between bounces, using scene/tracks/ball.csv:
- arcs 49-60: 19.80, 60-71: 18.84, 71-81: 19.44, 81-91: 19.12, 91-100: 19.09 px/frame^2 (clean arcs, rms 0.3-1.2 px)
- later arcs in front of the white bowl are noisier (17.6-25.0) because there are only 4-5 points and the segmentation is white-on-white.
- the fall after the throw (frames 43-49) has second differences of about 20.1.
- second-difference means on the clean arcs: about 19.4.
I take a = 19.5 +- 0.4 px/frame^2, which gives 17,550 px/s^2 and a scale of 9.8/17550 = 0.558 mm/px.

## Ball pixel diameter (prof.py, diam.py, views.py + zoomed crops)
I found the edges at half-maximum on luminance profiles through the ball centre. Because they sit at half-maximum, motion blur shorter than the
diameter does not change them:
- frame 0 (in the hand, sharp, vertical): 75.8 px; frame 54: 76.1; 65: 73.7/75.0; 66: 72.5 (vertical); 75: 75.7/77.5; 76: 73.9/72.9; 77: 74.1.
- I also checked frame 76 by eye on a zoomed grid: about 75 wide x 73 tall. The scene record says 73-75 for frames 55-86 and about 78 in the hand.
- Profiles where the background is a similar brightness (frames 85-96 and the bowl region) are unreliable, so I left them out.
I take D = 75 px (+-1.5).

## Result
D = 75 px x 0.558 mm/px = 41.9 mm, about **4.2 cm**.
Second route: using only the frames around 49-81 (a = 19.36 px/frame^2, D = 74.5 px) gives 4.19 cm. Taking the extremes
a = 19.26-19.75 gives 4.14-4.24 cm. As a sanity check, a regulation table-tennis ball is 4.0 cm, so the result is plausible.
Confidence: good (about +-4%).
