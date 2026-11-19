# Q90 — width of the black-and-white car (m)

Prior: yellow car length = 5.67 m. 2D top-down render: one metres-per-pixel scale from the yellow length.

Measurement (measure.py): mask = dark (min<100) | bright (max>172) | saturated (S>50), which excludes the soft ground shadow.
- Yellow length (x extent of rows 375–430) near the image centre: 306 / 304 / 304 px (frames 50, 55, 60) -> 304 px.
  Scale = 5.67 / 304 = 0.01865 m/px.
- White truck (frames 36, 40, 44, 48, 60; body near the image centre at frame 40), y extent per column:
  - across the wheels/fenders (front and rear wheel columns): rows 484–595 -> 112 px (the same in every frame)
  - across the mid body/bed: 489–590 -> 102 px
  - across the side mirrors: 475–604 -> 130 px

Widths:
- wheel to wheel (the convention for car width, so this is the answer): 112 x 0.01865 = 2.09 m
- body only: 1.90 m; including the mirrors: 2.42 m (other possible readings)

Check: the white width is 112 px in all five frames, from x≈500 to x≈1180. Using the yellow length of 306 px instead gives 2.08 m.
A pickup 5.67 m long that is about 2.1 m wide is realistic.
Confidence: moderate. The main uncertainty is whether the reference AABB includes the mirrors (+16%).
