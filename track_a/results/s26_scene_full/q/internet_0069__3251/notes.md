# q3251 – height of the cup (cm)

Prior: acceleration of the cup from 2.00 s to 2.30 s = 0.32 m/s^2. Internet video, so I used one planar scale, prior / pixel acceleration.
Time base: 30 fps (the file's rate is 30.013, effectively the same). 2.00 s is frame 60 and 2.30 s is frame 69.

## Pixel acceleration
I took this from scene/tracks/mug.csv and checked it with `fit.py`. The camera is effectively static: the drift is a few px, against motion of 56-95 px per frame.
- **Right (leading) body edge:** forward-difference velocity is 64 px/frame at frame 60 and 79 at frame 69, which gives 1.67 px/frame^2. A quadratic fit over frames 58-72 gives 1.68.
- **Body centre (frames 62-79):** a quadratic fit gives 1.57-1.59 px/frame^2. The centre velocity goes from 68 at frame 62 to 79.5 at frame 69, which gives 1.64.
- **Left edge:** it gives about 1.04-1.27. It is biased because the apparent width changes with perspective (452 px at the edges, 420 px in the middle) and with motion blur, so I did not use it.
- **Adopted value:** 1.62 px/frame^2, which is 1458 px/s^2. The scale is 0.32 / 1458 = 2.195e-4 m/px.

## Cup height in pixels
At frame 70 (checked on frames/f70.png) the rim top is at y ≈ 503-505 and the base bottom at y ≈ 1068-1075. That gives about 568 px, which is stable to about 1% over frames 62-79.

## Answer
568 × 2.195e-4 = 0.1247 m, which is **12.5 cm**.
The range across reference points is 12.1 cm (right-edge acceleration, 1500 px/s^2) to 12.7 cm (centre fit, 1431 px/s^2).
This is plausible for a coffee mug. Confidence: moderate, about ±5%. The main uncertainty is which reference point the annotator used for the acceleration.
