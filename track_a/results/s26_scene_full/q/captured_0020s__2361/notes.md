# q_2361 — distance between the two people (cm)

File fps = question fps = 24. Lab camera: f = 0.5959*1280 = 763 px, principal point (640,360).
Depths from depth_info: near person 1.580 m, far person 3.237 m (people stand still, so time does not matter).

Method (dist.py): back-project each person's centre pixel, ((u-cx)/f, (v-cy)/f, 1) normalised x depth
(depth = Euclidean camera distance), then take the 3D distance.
Centre pixels (frame 0, checked on frames/f0.png and the scene/ person tracks, which are static over the clip):
- near person (cut by the left edge): mask centroid (149,463); also tried torso (110,420), chest (90,380), hip (180,540)
- far person (head cut by the top edge): mask centroid (709,116); also tried hip (710,95), torso (705,50)

Results (cm): every combination falls between 238 and 249; mask centroid to mask centroid gives 238.5, and
torso/hip choices give 239–245. Answer: 241 cm. The depth difference (1.66 m) dominates the result, so the
choice of centre pixel changes it by only a few percent.
Second-route check: the spread over these point choices is about ±3%. 2.4 m is also a plausible distance for an
underarm throw between two people. Confidence: good (likely within 5%), assuming the reference clicked torso or
pelvis centres.
