# q 2521: width of the table (cm)

The file and question_fps are both 24 fps. Lab camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360).

## Method
1. Table top edges (edges2.py), measured on a median of frames 0, 8, 44, 46 and 48: the side edges come from the R−B (wood vs grey wall) step, the back edge from the same step, and the front top edge from the luminance drop onto the dark front face. Fitted corners: BL (578.8, 423.1), BR (847.3, 427.4), FL (464.1, 482.8), FR (956.2, 494.9). Overlay: frames/edges.png.
2. Plane orientation (geom.py): the vanishing points of the side edges (721, 349) and of the front/back edges (−6682, 308) give two directions with cos = −0.002 at f = 763. This checks the focal length and the rectangle shape. The table normal is their cross product.
3. Scale: the camera's height above the table plane is h = n·C + r, using the ball centres from the scene/ tracks. Yellow tennis ball, Z = f·0.067/diam, frames 16-42: h = 0.1714 m (std 2 mm). White ball, scaled so its distance at frame 38 (t = 1.6 s) is 1.19 m: h = 0.1716 m. The two agree.
   - The depth_info labels look swapped. At frame 38 the yellow ball (50.8 px) is about 1.01-1.02 m away, which matches 0.994 m (6.6 cm at 0.994 m). The white ball (24.5 px) at 1.19 m is 3.8 cm, ping-pong size. Under the literal labels the tennis ball would be 7.9 cm, which contradicts the exact 6.7 cm prior.
4. Corners are found by ray–plane intersection. Table top: front-to-back 78.5 cm (both sides), left-to-right 60.2 cm (front and back edges both 60.2).

## Answer
Width means the shorter horizontal extent, which here is the left-right edge: **60.2 cm**. The other reading, the front-to-back depth seen from the camera, is 78.5 cm. That is the longer side, so it is the length.

## Second-route check
- Lab method card: front edge length 492 px at a mean corner depth of about 0.94 m → 60.4 cm. Back edge 268.5 px at about 1.72 m → 60.5 cm.
- At frame 42 the yellow ball sits at the front edge, rolling off. Its diameter-based depth (Z = 0.915) matches the front-edge depth recovered from the plane (Z ≈ 0.91-0.97 across the edge).

Confidence: good, about ±3%.
