# q3118 — height of right basketball stand (m)

Prior: rider average speed = 2.9 m/s. Internet video, single planar scale (annotator convention). fps = question_fps = 30.

**Scale (measure_stand.py).** The rider's reference point (bbox centre, stabilised track from scene/tracks/rider.csv)
moves on average 15.88 px/frame. The front wheel, rear end and centroid give 15.86-15.89. Camera drift is small (<13 px total).
That is 476.3 px/s, so the scale is 2.9 / 476.3 = 0.006089 m/px.
Sanity checks: scooter 177 px gives 1.08 m, and the person (cap to soles, 275 px) gives 1.67 m. Both are plausible.

**Stand pixel height.** I measured from the pole base, where it meets the court, to the top edge of the backboard, using
intensity profiles in code:
- Frame 0: top 510.5 (mid-board; the edge is slightly tilted, 512.5 to 508.5), base about 1164, so 653.5 px.
- Frame 46: top 507.5, base about 1162.5, so 655 px.
- Frame 93: top 506.5, base about 1163.5, so 657 px.
- I used 655 px.

**Answer.** 655 × 0.006089 = **3.99 m**.
For comparison, a regulation backboard top is about 3.95 m (rim at 3.05 m), so the value is consistent. I used a second
route, the second-frame and last-frame measurements, and it agrees within 0.5 %.
Caveat: the hoop sits at a slightly different depth than the rider. Following the convention, I applied no perspective correction.
Confidence: good (±3 %).
