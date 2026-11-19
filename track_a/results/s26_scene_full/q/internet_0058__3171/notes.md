# q_3171: height of the person (prior: g = 9.8 m/s^2)

Time base: 30 fps for both the file and the question. A woman at 1.68 m and the ball's arc give a plausible scale, so no re-timing.

Scale from gravity (fit.py): I fitted a parabola to the ball centre (scene/tracks/ball.csv, cy_stab and raw) during free flight.
- Frames 27-58: 2.24 px/frame^2 = 2016 px/s^2 (rms 0.5 px).
- Frames 30-55: 2028. Frames 23-42: 2008-2018. Frames 23-63: 2000. Frames 42-63: 1920 (worse fit near the catch).
- Mean of the second differences over 23-63: 2.196 px/frame^2 = 1976 px/s^2.
- Adopted value: 2015 px/s^2, so the scale is 9.8 / 2015 = 0.004864 m/px.

Person height in pixels: standing upright, frames 36-60, from the cap top to the bottom of the shoes.
- Recorded values are 341-352 px, about 345 px at frame 45.
- At frame 45 (2x zoom crop) I checked the cap top at about 545 and the feet at about 890.

Height = 345 x 0.004864 = 1.68 m.

Second route: scaling with the second-difference g (1976 px/s^2) gives 1.71 m. Using 340-352 px gives 1.65-1.71 m.

Confidence: moderate-good, within about 3-5 %. The ball flies close to the person's depth plane.
