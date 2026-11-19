# Q810 – length of the brown horse (m)

Prior: "speed of the horse at the back = 0.874 m/s". The scene is a 2D top-down render, at 24 fps (file rate = question_fps).
There are two horse-like animals, brown and white, plus a small animal. The brown horse is the rear one: it is leftmost while all of
them walk +x, and it is also the upper one in the image. So the prior refers to the brown horse itself.
Sanity check: if the prior referred to the white animal (4.6 px/frame), the brown horse would be only 1.1 m long, which is
implausible. Using the brown horse gives about 2.0 m, a normal horse length.

## Speed (px)
- Track from scene/tracks/brown.csv (frames 0-48; frame 49 is a loop reset and is excluded).
- Linear fit of the centroid gives 2.70 px/frame. The net centroid displacement over frames 0→48 gives 2.59 px/frame. Same-gait-phase
  pairs give 2.61-2.78 px/frame.
- Linear fit of the nose (front edge), which is the steadiest point and was measured in seg.py: 2.667 px/frame. Same-phase pairs give 2.63-2.73.
- Adopted speed: 2.67 px/frame = 64.0 px/s. Scale = 0.874 / 64.0 = 0.01365 m/px.

## Length (px)
- seg.py: a colour mask (red-brown body plus white nose and hooves) on every frame. It gives the x-extent from the rear hoof or rump to the nose.
- 142-167 px over the gait (the maximum is when a hind leg is stretched back). Median 146, mean 149. The CSV bbox_w median is 144.
- Adopted length: 146 px × 0.01365 = 1.99 m. The range over the gait is 1.94-2.28 m.

## Answer
2.0 m. Confidence: moderate. The main uncertainties are which frame or pose the reference uses for the bounding box (±5%) and the speed fit (±3%).
