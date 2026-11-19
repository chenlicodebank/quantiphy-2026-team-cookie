# q_1654 — height of the bench seat (m)

File fps = question fps = 33, so the record's frame numbers and times agree.

## Camera
- Focal length (focal.py, solve.py): pinhole with principal point (540,540). Pelvis pixel at frame 0 (u=-1.5) and frame 33
  (u=252), the given depths 5.424 / 4.886 m and |P33-P0| = 1.3 m (1 s at 1.3 m/s) give a unique f = 909 px
  (900-918 for a pelvis-x error of ±8 px). The person's camera-axis depth then comes out constant: Z = 4.65 / 4.65 m.
  That agrees on its own with the record's finding that his apparent size stays constant. Horizontal FOV ≈ 61°.
- Tilt: the receding side edges of the bench base meet at (540, 543), so the camera is essentially level (horizon v0 ≈ 540-543).
- Camera height: sole row 731 at Z 4.65 gives hc = (731-v0)·Z/f = 0.96-0.98 m.
- I did not use the "art display panel" depth (4.223 m) because it contradicts the occlusion order: the person, at about
  4.7 m, passes in front of both paintings. It probably refers to an object that is not in the segmented video.
  The pedestal and sculpture depths (5.96 m) fit (Z ≈ 5.9 m, behind the person; the floor there projects to v ≈ 690-700).

## Bench
- Profiles (profile.py) at x = 210/420/650/860 show the flat cushion top (uniform brightness) from row 698 (back top
  edge) to row 752 (front top edge), the cushion lip down to the seam at 778, the slab face 780-821 and the base down to
  row 966.
- The top plane at height H gives Zback/Zfront = (752-v0)/(698-v0) = 1.34.
- The bench origin is taken at the bbox centre: centre depth = mean(Zfront, Zback), centre height = H/2, and its distance
  must equal 2.267 m. Solving gives Zfront = 1.84 m, Zback = 2.47 m (seat depth ≈ 0.63 m) and H = hc - (752-v0)·Zfront/f = 0.54-0.55 m.
- Variants: origin at the bottom centre gives 0.56-0.57; f ±9 px or v0 540/543 changes H by only ±0.01.
- Check: the base front-bottom edge (row 966) on the floor would be at Z = 2.09 m, which lies inside [1.84, 2.47], so the
  model is consistent. The bench length is then about 1045 px × 1.84/909 ≈ 2.1 m, a plausible size.

Answer: 0.55 m (the full bench height from floor to cushion top; "seat height" means the same value here). Confidence: moderate, about ±5%.
