# q3121: distance between the two basketball stands (m)

Prior: the scooter rider's average speed is 2.9 m/s. Internet video, so I used one planar scale from the prior. The file and the question both give 30 fps, so no re-timing was needed.

## Speed in pixels (measure.py, scene/tracks/rider.csv, frames 0-93)
I took the mean of the per-frame backward-difference speeds, in background-stabilised coordinates:
- bbox centre: 15.88 px/frame
- front wheel: 15.86
- rear end: 15.89
- centroid: 15.96

I used 15.87 px/frame = 476.1 px/s. In raw image coordinates (camera drift not removed) it is 15.75 px/frame. The drift is 12.6 px over the clip.

Scale = 2.9 / 476.1 = 0.006091 m/px.

## Stand separation in pixels (frame 0)
I found the poles in code as dark columns in rows just above their bases (y 1100-1150):
- Left pole: x 656-676, centre 666.3
- Right pole: x 3397-3418, centre 3407.3

Separation: 2741 px. The camera drift does not matter here because both poles are static and measured in the same frame.

## Answer
2741 × 0.006091 = **16.7 m**.

## Check
- With the raw-coordinate speed instead (472.4 px/s), the answer is 16.83 m, so the result moves by less than 1 %.
- With the front-wheel or rear-end track instead of the bbox centre, the answer stays within ±0.2 %.
- The pole bases (y 1150-1163) are only slightly behind the rider's ground line (y 1177), so perspective error is small, and I applied no correction, following the annotators' planar convention.

Confidence: good, about ±3 %.
