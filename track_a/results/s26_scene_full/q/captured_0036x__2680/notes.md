# q2680 — length of the table (m)

Answer: **0.73 m**. File fps = question fps = 24. t=0.9 s is frame 22 and t=1.4 s is frame 34.

## Why I did not use a single pixel extent × depth / f
The table's long axis points away from the camera, and the camera sits only about 17 cm above the top with about 1.7° of pitch.
At that angle the length is badly foreshortened, so I reconstructed the table-top plane instead.

## Method
1. `geom.py`: on frame 48 (no ball), I fitted the table-top edges with subpixel accuracy.
   - Left and right side edges: residuals about 1.2 px.
   - Back silhouette edge and front top edge (the brightness drop to the dark front band): residuals 0.4–0.65 px.
   - Corners: BL (415.0, 438.9), BR (757.1, 445.1), FL (187.2, 585.6), FR (998.4, 591.8).
   - Vanishing point of the side edges: (576, 335).
2. `recon.py`: I used f = 0.5959·1280 = 762.8 px, with the principal point at (640, 360).
   - d1 is the side-edge direction, taken from the vanishing point.
   - d2 is the front/back edge direction, given by d1 × the normal of the front/back edge's back-projected plane.
   - The plane normal is n = d1 × d2.
3. Scale: I placed the ball centre at the depth_info distance on its pixel ray (frame 22: (569.6, 453.2), 1.010 m; frame 34: (836.5, 513.2), 0.716 m). The table plane lies 0.02 m (the ball radius) below the centre.
   - Camera height above the table top: 0.1747 m from frame 22 and 0.1711 m from frame 34. The two depths agree to within 2%.
4. I back-projected the corners onto the plane.
   - Side (front-to-back) extent: 0.720 m when depth is read as Euclidean distance, 0.740 m when read as z-depth.
   - Front edge width: 0.555 m, back edge width 0.555 m. Front and back agree, which supports the rectangle assumption and the given f.
   - Length is the longer horizontal extent, which here is the side running away from the camera: **about 0.73 m**. The width is about 0.56 m.

## Second route (independent scale)
`route2.py` takes the scale from the ball's apparent diameter at rest in frames 0–12 (25 ± 1 px), which puts the ball 1.22 m from the camera.
- Camera height: 0.172 m.
- Length: 0.717 m (range 0.69–0.74 for 24–26 px).
- Width: 0.552 m.

This route agrees with the depth_info route.

## Confidence
Moderate to good, roughly ±4%. The main sensitivity is the grazing viewing angle: a horizon error of a few pixels changes the far-edge depth by about 3%. The corners are rounded and bevelled, which adds less than 1 cm.
