# Q596: length of the white sofa (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 (file) = question_fps 24, so no re-timing.

## Scale (measure.py)
Black cat segmented as the largest blob with gray < 60 in rows 250–480 on all 50 frames.
Linear fits of x(frame):
- head front edge: 10.975 px/frame (residual 0.57 px)
- body centroid after opening: 10.944
- full centroid: 10.962
- mean per-frame step: 10.92–10.98
y is constant (355–361), so the motion is purely along +x.
That gives 10.97 px/frame = 263.3 px/s, so the scale is 0.94 / 263.3 = 0.003570 m/px in the cat's plane.

## Sofa extent (sofa_edges.py, frame 0)
The sofa is static, and its long axis runs along image x.
I found the silhouette edges from row gradient profiles in y = 600–860:
- left outer arm: x ≈ 566–568 (minimum at y ≈ 700)
- right outer arm: x ≈ 1451–1452 (y ≈ 700–720)

Length ≈ 884 px. This agrees with the scene record's 883–885 px.

## Result
- Planar: 884 × 0.003570 = 3.156 m.
- Perspective: the camera looks straight down, and the walls show perspective. The sofa's widest silhouette sits at arm height (~0.4–0.6 m), which is above the cat's body (~0.2 m), so the sofa outline is slightly magnified relative to the cat-plane scale.
- Camera height: the leaning picture frame (top ≈ 1.09× radial magnification at the wall) and the unseen wall tops suggest a camera height of roughly 6–12 m. That makes the correction about 2.5–5%. At ~8.5 m it gives about 3.05 m.
- Answer: 3.09 m. This is between the planar value (3.16) and the perspective-corrected one (~3.04), and within ~2.5% of both.

## Second-route check
Using the cat's front-edge slope against the body-centroid slope changes the scale by less than 0.3%. The sofa edges from the scene record mask (560–1442) and from my gradient edges (567–1451) give 882–885 px.
Sanity check: the cat's body is about 156 px ≈ 0.56 m, which is a realistic size, and a 3.1 m curved sofa is plausible.

Confidence: good, about ±5%. The main uncertainty is the perspective height correction.
