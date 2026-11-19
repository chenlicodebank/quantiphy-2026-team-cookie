# q 3169: the person's average walking speed from 3.50 s to 5.00 s

Time base: the file and the question both run at 30 fps. That rate gives a ball diameter of 0.24 m (the size of a real basketball) and a person about 1.70 m tall, so the timing is plausible. 3.50 s = frame 105 and 5.00 s = frame 150.

## Scale from gravity (prior 9.8 m/s^2)
`fitg.py` fits parabolas to the ball's bg-fixed centre y in each free-flight arc (degraded frames left out):
- Shot, frames 55-96: 2.058 px/frame^2 (2.063 over frames 60-90)
- After bounce 1, frames 100-133: 2.099
- After bounce 2, frames 138-162: 2.036
- After bounce 3, frames 167-186: 2.104

I used g of about 2.06-2.065 px/frame^2, which is 1855 px/s^2. That gives 0.00528 m/px.
Sanity checks: the ball is 46 px, or 0.243 m; the person is 322 px tall, or 1.70 m.

## Person displacement
- Route A (`torso.py`): I took the centroid of the person's foreground columns in rows 640-740 (the torso and hips), found by differencing against a frame where the person stands elsewhere and keeping only the part inside the tracked box.
  - Frame 105: x = 651.1. Frame 150: x = 1031.4. The raw shift is 380.3 px.
  - The camera drifted 5.3 px to the left over that span (camera_shift.csv: dx goes from -10.62 to -15.93), so the shift against the background is 385.6 px.
  - Averaging ±2 frames around each end gives the same value.
  - Speed = 385.6 x 0.00528 / 1.5 = 1.36 m/s.
- Route B (the record's box centre, bg-fixed): 406.6 px, or 1.43 m/s. The box centre moves with how far apart the legs are in the stride, so I trust the torso centre more.

Answer: 1.36 m/s. Confidence: moderate. The uncertainty is mainly which reference point the annotators used (about ±5 %).
