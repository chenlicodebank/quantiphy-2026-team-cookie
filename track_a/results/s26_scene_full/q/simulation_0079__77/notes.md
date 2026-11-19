# Q77: speed of the bike at 1.0 s (m/s)

The prior is that the bike is 1.7 m long. There is no depth_info. The camera is static and top-down, so this is a 2D case and one scale is used.
The file and the question both run at 24 fps, so t = 1.0 s is frame 24.

## Measurement (measure.py)
- I made an HSV mask of the light-cyan bicycle in the lane at y 540-760 and took its tip-to-tip x-extent in frames 8-31.
- Pixel length near frame 24 (frames 20-28) is 408.2 px on average. Over the whole frame the mean is 409.7 px.
  The scene record gives 412 px, but the bike reads about 2% longer on the right side of the frame. I used the local value of about 409 px.
- Centre motion: a linear fit over frames 20-28 gives -51.25 px/frame, and the fit over frames 8-31 gives -51.26 px/frame.
  The one-frame difference at frame 24 is 52.0 px, within about ±1 px of tip noise. The motion is constant velocity.
- Speed = 51.25 px/frame × 24 fps × 1.7 m / 409 px = **5.11 m/s**.

## Second route
The scene record, measured independently from the tips and bike centre, gives -51.3 px/frame and a length of 412 px, which works out to 5.08 m/s.
The raw one-frame difference gives 52 × 24 × 1.7 / 408 = 5.20 m/s. All three agree within about 2%.

Confidence: high, with an error of about 2%, mostly from the scale.
