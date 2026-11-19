# q_3159 – height of the person riding the scooter

Time base: the file and the question are both 30 fps, so no re-timing.

## Scale from the prior (average speed 2.64 m/s)
`speed.py` uses scene/tracks/scooter_rider.csv. I subtracted the camera drift (`bg_dx`) and took the mean of the
per-frame speeds over frames 0–57 (the rider moves steadily to the right; no bounces or occlusions):
- cx: 327.1 px/s (323.2 px/s without the drift correction)
- front and rear wheels: 329.1 and 325.0 px/s; body centroid: 326.1 px/s

I used ≈ 326 px/s, so the scale is 2.64 / 326 = 0.00810 m/px.

## Rider height in pixels
- Cap top to ground (wheel bottoms): 205 px at frame 0, 212 px at frame 30, 215 px at frame 57.
- The person stands on the deck, which is about 10–12 px above the ground (zoomed check at frame 30: cap top ≈ 545,
  shoe/deck ≈ 745, wheel bottoms 758).
- Person alone, head to feet: about 194 px (frame 0), 201 px (frame 30) and 203 px (frame 57). I used 199 px for
  the clip as a whole.

## Answer
Person height = 199 × 0.00810 ≈ **1.61 m**.
If the height is read from the cap top down to the ground, including the deck (≈ 211 px), it would be ≈ 1.71 m.

## Check
Bollards at about the rider's depth are 96–100 px tall. At this scale that is 0.79 m, a typical bollard height,
so the scale is consistent.

The rider grows about 5 % in pixel size over the clip, which adds about ±3 % uncertainty. Confidence: moderate.
