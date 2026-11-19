# q_3120: distance from the bird to the ground (internet_0050)

Time base: 30 fps. The file and the question agree, and the clip is real footage.

## Scale (prior: the rider's average speed is 2.9 m/s)
- I used the stabilised rider track (scene/tracks/rider.csv), which I checked against `measure.py`. The mean forward-difference pixel speed is:
  - 476.3 px/s for the bbox centre
  - 475.8 px/s for the centroid and for the front wheel
  - 476.8 px/s for the rear end
  - 472.2 px/s in raw image coordinates (the camera drifts slightly)
- So the scale is 2.9 / 476.3 = 0.006089 m/px.

## Bird
The bird is perched on the top edge of the left backboard and is static; only its head turns. I measured it in code from dark pixels against the sky (`measure.py`):
- At frame 0, the head top is at y 488 and the feet are at y 525, on the board top at y 526.
- So the bird's centre is at about y 506.5.
- The ground is at the left pole base, y ≈ 1155, where the dark pole meets the white baseline.
- Frames 47 and 93 give the same values shifted by the camera drift of about 6 px, which cancels in the difference.

## Result
- From the bird's centre to the ground: 648.5 px × 0.006089 = **3.95 m** (this is the answer).
- Other readings:
  - from the feet: 630 px, or 3.84 m
  - from the head top: 667 px, or 4.06 m

## Check
Applying the same scale to the hoop reproduces regulation dimensions:
- Rim to ground: 487 px, or 2.97 m (regulation 3.05 m).
- Board top: 629 px, or 3.83 m (regulation about 3.95 m).

So the scale is consistent within about 3 %. The hoop stands slightly behind the rider's path, so the true metric height is a little larger. The annotators' single-scale convention gives the value above.

Confidence: moderate to high, about ±5 %. The main uncertainty is which point on the bird the annotators took.
