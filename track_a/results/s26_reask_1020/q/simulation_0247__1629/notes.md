# Q1629: length of the deer (m)

- The "deer" is the horned quadruped (called "creature" in scene/). It walks left to right across the view. The file and the question both run at 30 fps.
- Scale from the prior (deer speed 1.277 m/s): a linear fit of the mask centroid x over frames 0–74 gives 7.764 px/frame = 232.9 px/s, so the scale is 0.005483 m/px. The trunk centroid gives 7.67 px/frame and the bbox centre 7.62 px/frame, which are 1–2 % lower.
- Length = the world AABB extent along the direction of travel, from the tail tuft to the ear tip. Its pixel width (scene mask bbox, checked on frame 36) has a median of 538 px, a mean of 538, and a range of 496–580 with gait and tail swing. 538 × 0.005483 = **2.95 m**.
- Second-route check (3D): the rabbit's feet are on the same ground line as the deer's, so it is at about the same depth (15.8 m). That gives f = 15.8 / 0.005483 = 2882 px, a horizontal field of view of about 37°. With this f, back-projecting the rabbit's pixel motion from t = 0 to t = 1 s predicts a camera distance of 15.851 m at t = 1 s. The given value is 15.852 m, so the scale agrees.
- Sanity checks: the rabbit comes out at 0.45 m long. The deer's height including the horns is 2.38 m, and its withers are about 1.26 m high. These are plausible.
- Confidence: moderate to good. The main uncertainty is which pose or frame the reference AABB uses; across frames the length ranges from 2.72 to 3.18 m.
