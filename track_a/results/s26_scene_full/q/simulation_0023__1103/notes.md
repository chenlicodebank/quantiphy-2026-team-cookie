# q_1103: length of the boat (m). Answer: 10.6 m

Time base: the question uses 24 fps, but the file runs at 25 fps. So t=1 s is frame 24 and t=2 s is frame 48. I used the
frame column of the record, not its seconds.

## Focal length (focal.py)
- Assumed the eagle flies in a straight line at a constant 11.84 m/s. Its displacement from frame 24 to frame 48 is
  then 11.84 m.
- Each eagle centroid (record track, checked against the bbox centre) was back-projected with its depth_info distance
  (116.05 m and 108.28 m), with the principal point at the image centre.
- Solving |P48 - P24| = 11.84 m gives **f ≈ 3388 px** (HFOV 16.1°). This is stable between 3378 and 3392 px across
  centroid/bbox and smoothing choices.
- Sanity check: the eagle's wingspan comes out at about 1.8 m (56 px at about 110 m), which is plausible.
- A fit of a constant-velocity line to the eagle's full pixel track only weakly constrains f (check_f.py), so it is not
  a strong second check.

## Boat geometry (boat.py, sens.py, ends.py)
- Boat origin: hull-centre pixel, back-projected with the boat depths 103.157 m and 106.091 m.
  - Displacement from frame 24 to 48: (-2.99, -0.01, +2.76) m.
  - So the boat moves left and **away**, on a horizontal heading 43° off the image plane.
- The image confirms the boat is oblique, with the bow farther away than the stern:
  - the hull stripe is about 8 px higher at the bow, which is what a level camera predicts;
  - we see the near side and the rounded stern quarter;
  - the waterline rises as the boat recedes, which means the camera pitch is about 0.
- Method: assume the hull axis lies along the motion direction. The bow-tip and stern-extreme rays are then intersected
  with the horizontal axis line through the origin.
- The bow and stern x positions were re-measured with a background difference (ends.py) and agree with the record
  within 1–2 px:
  - frame 24: bow 195, stern 446 px;
  - frame 48: bow 109, stern 349 px.
- Silhouette length, bow to stern:
  - frame 24: 10.88 m; frame 48: 10.96 m (frame 0: 10.79 m; frame 74: 11.00 m).
  - It is nearly constant over the clip even though the pixel length drops from 263 to 228 px, which supports the
    heading and f.
  - Mean at the two given times: **10.92 m**.
  - A plain side-on estimate (d·px/f) would give only about 7.6 m. That is wrong because the boat is strongly oblique.
- Stern correction: the stern is rounded. The rightmost silhouette point is the tangent of that curve, which lies past
  the centreline tip by about 0.34·R along the axis. With R ≈ 1 m (half-beam at the stern; the wheelhouse is about
  1.5 m wide), that is about -0.34 m, giving **≈ 10.6 m**.

## Sensitivity and confidence
- L scales roughly as f^-0.75: f = 3100 gives 11.4 m, f = 3700 gives 10.5 m.
- If the eagle's centroid bobbing were real path length, f would be about 3% larger and L about 2% smaller.
- Assumptions: the hull is aligned with the world axis (the bounding-box length equals the hull length), and the
  heading equals the direction of motion.
- Estimated uncertainty: about ±6%.
