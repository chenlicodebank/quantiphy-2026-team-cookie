# Q1109: eagle speed at t = 1.0 s

Time base: question_fps = 24, so t = 1 s is frame 24 and t = 2 s is frame 48. The file says 25 fps; I used the frame
indices from scene/ and ignored its seconds.

## Scale and focal length
- Person: the given distance is 114.832 m at 1 s and 114.836 m at 2 s, so it is essentially constant (the character origin
  stays put). In the image the person moves about 0.53 px/frame (12.7 px/s), and the mask height stays at 54.5 px
  (measure.py, frames 0-72, re-measured from a median background; it agrees with scene/).
- The prior can't give the focal length. If the 1.3 m/s were all lateral motion, f would be about 1120 px and the
  person would be 5.6 m tall, which is impossible. So I took the scale from the person's height, as the rules say:
  - I assumed a walking mask height of about 1.75 m (an adult of about 1.8 m standing).
  - f = 54.5 x 114.83 / 1.75 ≈ 3576 px, so the horizontal field of view is about 15.3°.
- Check: the eagle's maximum bbox span is about 48 px at about 111 m, which gives roughly 1.5 m. That is plausible for a
  rendered eagle.

## Eagle velocity
- Positions: I back-projected the bird's smoothed mask centroid (scene/tracks/bird.csv, which I checked) with the given
  distances: 116.05 m at frame 24 and 108.28 m at frame 48. For frames in between, the distance is interpolated linearly.
- Image velocity at frame 24: 10.9-11.1 px/frame in x and -0.4 px/frame in y (linear fits over ±2, ±4 and ±6 frames).
- The distance to the camera shrinks by 0.324 m/frame (7.77 m/s). The bird is near the image centre at frame 24, so this
  is almost all motion along the depth axis.

## Results (speed.py)
- Backward difference, frames 23→24: 11.46 m/s.
- Local-fit velocity: 11.53-11.62 m/s.
- Second route, the mean 3D velocity from frame 24 to 48 (two given distances): 11.48 m/s, with velocity
  (8.18, 0.16, -8.06) m/s.
- Sensitivity: an assumed height of 1.70-1.80 m gives 11.3-11.8 m/s. The depth component (about 8 m/s) comes straight
  from depth_info and does not depend on f.

**Answer: 11.5 m/s.** Confidence: moderate-good. The main uncertainty is the person's height used for f (about ±3% on the
answer); a non-uniform depth rate near t = 1 s is a smaller one.
