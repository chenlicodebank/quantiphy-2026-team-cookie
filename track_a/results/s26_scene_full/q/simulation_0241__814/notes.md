# Q814 – length of the white horse (m)

Prior: speed of the horse at the back = 0.874 m/s. The scene is a 2D top-down view at 24 fps (file fps = question fps), and the camera is static.
- I take "horse at the back" to be the brown horse. It is behind the white horse in the walking direction (both walk +x), and it is the upper/rear one in the image. The white horse is ahead.
- Brown horse centroid track (scene/tracks/brown.csv, frames 0-48; frame 49 is a loop reset, excluded):
  - net mean speed = 2.59 px/frame = 62.2 px/s
  - linear fit = 2.70 px/frame = 64.9 px/s (the body-only centroid gives the same 64.8)
  - Windowed speeds rise from about 2.4 to about 2.9 px/frame across the clip, so I used about 2.65 px/frame = 63.6 px/s.
  - Scale = 0.874 / 63.6 = 0.01374 m/px (range 0.01348-0.01405).
- White horse length = x-extent of the full-silhouette mask (bbox_w; it walks along +x), checked visually at frame 36 (tail about x 1045 to head disc about x 1235):
  - median 177 px (mean 176.7, range 159-190 with gait)
  - body-only median 165 px
- Length = 177 x 0.01374 = **2.43 m**.
  - With the net-mean scale: 2.49 m. With the fit scale: 2.39 m.
  - Max-pose extent 190 px gives 2.61 m; body only gives 2.27 m.
- Sanity check: a real horse is about 2.4 m long, so the result is plausible. On the same scale the brown horse is about 1.95 m long.

Confidence: moderate, about ±5%. The main uncertainties are the speed ramp in the prior horse and whether the head and tail are included in the length.
