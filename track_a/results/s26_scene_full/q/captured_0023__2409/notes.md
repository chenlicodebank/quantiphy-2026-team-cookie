# q2409: length of the book (cm)

File fps = question_fps = 24. Lab camera: f = 0.5959 x 1280 = 762.75 px, principal point about (640, 360).

## Main route (t = 1.6 s, frame 38, book at rest on the table, depth 0.851 m)
- measure.py: background difference against frame 0, plus horizontal gradient edges across bands of rows through the book.
  - Left end at x ≈ 478-482 and right end at x ≈ 652-654 (frames 38, 42 and 47 agree). The pale cord at x 440-478 is excluded.
  - Pixel length ≈ 174.5 px (range 172-176). The scene record gives bbox 478-651 and a minAreaRect length of 172-174.
- L = 0.851 x 174.5 / 762.75 = 0.1947 m.

## Second routes
- Book held at the ramp top (f0-20): the cover runs x 528/530-655, about 126 px, with the long axis horizontal.
  - Depth: not given directly, so I interpolated 1/Z linearly in image y between the ramp top edge (y 356, 1.201 m) and the ramp foot (y 482, 0.9555 m).
  - The book centroid is at y 368, which gives Z ≈ 1.17 m and L ≈ 1.17 x 126 / 762.75 ≈ 19.4 cm.
  - Check on the interpolation: at t = 1.2 s the centroid is at y 435, which gives Z ≈ 1.03 m. The given depth is 1.02 m.
  - The ramp edges are 145 and 183 px wide, a ratio of 1.26. The depth ratio is 1.257, so the depths are consistent.
- t = 1.2 s (f29), depth 1.02 m, length 147 px (motion-blurred): L ≈ 19.7 cm.
- The pixel-length ratio between the rest and ramp-top positions is 174.5 / 126 = 1.385. The depth ratio is 1.375, which is consistent.

## Caveat
On the table the book is seen nearly edge-on. The back edge of the cover looks a few percent shorter than the front edge, so if the pixel length were taken at mid-depth the answer would be about 18.7-19 cm. The routes agree on about 19.5 cm.

Answer: 19.5 cm. Confidence: good (about ±4%).
