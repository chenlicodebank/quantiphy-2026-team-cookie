# q2368: diameter of the white jar (cm)

- In scene/ the "white jar" is recorded as `white_ball`. Zoomed crops (frames/crops.png) show a white cylindrical jar
  with a dark lid, thrown by the near person. The "carrot" is the scene's `yellow_fruit`.
- The file rate and question_fps are both 24. t = 0.60 s is frame 14, where the jar's depth is 1.9735 m.
- Camera: f = 0.5959 x 1280 = 762.8 px.

## Measurement (alpha_width.py, f14check.py)
- Soft matte: alpha = 1 - (G - max(R,B))/250 against the flat green background. Skin pixels (R - B > 25) are
  excluded. The jar's main axis comes from PCA on the white mask.
- Width: alpha integrated along slices perpendicular to the axis, skipping any slice that touches skin. For a cylinder,
  the silhouette width perpendicular to its projected axis equals the diameter. The motion is along the axis, so blur
  does not widen this width.
- Median cross-axis width by frame: f12 31.3, f13 31.5, f15 29.4 (mid-section 31.3), f16 31.2–31.5,
  f17 31.1–31.5 px (counting pixels with alpha > 0.5 gives about the same). Frame 18 overlaps the fruit, so it is
  not used.
- f14 reads wider (36.5 px). In the crop the jar is visibly smeared there, probably by rotation blur at release, and it
  is next to the hand. Frames f12–f17 around it all give a steady ~31.4 px, which also means the depth stays about
  constant (~1.97 m) over f12–f17. So I used 31.4 px.
- The outer-hull minimum caliper is about 34 px in f15–17. This is an upper bound: it includes the blurred corners.

## Result
D = 1.9735 m x 31.4 / 762.8 = 0.0812 m, i.e. **8.1 cm**.
- If the f14 width were used, the result would be 9.4 cm.
- With the caliper upper bound it would be 8.8 cm.

## Check / confidence
- Second route: five frames on either side of f14 (before release f12–13 above the hand, and in flight f15–17) agree
  within ±0.2 px. The ~31.4 px width is therefore stable.
- The main uncertainty is the edge definition (±1.5 px, about ±5%) and the depth during f15–17 (assumed equal to
  the depth at f14).
- Confidence: moderate to good (about ±8%).
