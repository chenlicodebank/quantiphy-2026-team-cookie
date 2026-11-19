# Q2517: velocity of the red ball at t = 0.4 s (cm/s)

The file runs at 24 fps and question_fps is also 24, so t = 0.4 s is frame 10. The depth_info times map to frames 5, 10, 14 and 19 (round(t*24)).
Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Track
I used the ball centres in scene/tracks/ball.csv (an upper-arc circle fit). For frames 6-14 I drew them on the frames (crops.py -> frames/crops.png),
and they sit on the ball. Pixel steps around frame 10 are about 11-16 px/frame in u and -5 px in v. The 11->12 step jumps to 50 px,
which looks like uneven frame timing rather than a tracking error.

## Route 1 (vel.py): back-projection with depth interpolated from depth_info
I treated depth_info as the range to the ball centre along its viewing ray and interpolated it between frames 5/10/14/19.
The velocity at frame 10 is a smoothed difference over 5-7 frames: a centred difference, the mean of the forward differences, or a local quadratic fit.
- Linear depth interpolation: 148-154 cm/s. PCHIP or cubic interpolation: 155-165 cm/s.
- Using the unrounded times (4.8, 9.6, ...) gives 143-152 cm/s.
The depth change dominates the motion: dZ/dt is about 1.2-1.4 m/s, against a lateral speed of about 0.35 m/s.

## Route 2 (vel_plane.py): the ball centre moving on a horizontal plane
I modelled range as R = C*|ray| / (v - y0) and fitted it to the four given depths (y0 = 339, close to the horizon at 329 in the scene notes).
It reproduces them within 1-4 %. That gives 128-143 cm/s, or 120-133 cm/s with y0 fixed at 329.

## Consistency
The ball's pixel diameter times the given depth gives 7.6-8.6 cm, against the 7 cm prior. The pixel sizes are inflated by motion blur,
but they confirm the trend that the ball recedes quickly around frame 10.

## Answer
150 cm/s. This is between route 1 with linear interpolation (about 150) and route 2 (about 135-143); the cubic variants give up to 165.
Confidence: moderate, about ±10 %. The answer depends mostly on how depth is interpolated between the given times.
