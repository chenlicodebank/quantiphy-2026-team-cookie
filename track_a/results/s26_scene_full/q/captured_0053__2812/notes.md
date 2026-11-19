# q 2812: distance between the white cup and the basketball (m)

The file and the question both run at 24 fps. I used frame 10 (t = 0.4 s). Both objects are static.
Camera: lab card, f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

Pixel centres (from measure.py, colour masks at frame 10, overlay in frames/masks.png):
- Basketball: orange mask, bbox 952-1022 x 340-400, centre (986.5, 369.5). This matches scene/ (987, 369).
- White cup: the low-saturation mask leaked a little onto the bright carpet. Its centroid is (566.3, 420.2). Read by eye
  on zoomed frames, the cup spans about x 552-578 and y 403-447, so the centre is about (565, 426). scene/ gives (565, 430).

Back-projection: depth_info is the Euclidean distance to the centre along the ray (cup 2.516 m, ball 2.925 m).
- With the mask centroid for the cup: 1.470 m.
- With the visual centre (565, 426): 1.476 m.
- A few px of change in the cup centre moves the result by less than 0.5 %.
- If depth were wrongly treated as z, the result would be 1.63 m. That is not the convention, so I rejected it.

Answer: 1.472 m. Confidence: good. The result depends mainly on the given depths and the lab focal length.
The trashbin velocity prior (the blue moving object) is not needed for this static distance.
