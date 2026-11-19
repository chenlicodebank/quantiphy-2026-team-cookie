# q_607 — length of the white sofa (m)

Prior: black cat speed = 0.94 m/s. The scene record calls it a "dog", but it is the same and only animal (black,
walks +x along y≈359). The scene is a 2D top-down view and the camera is static. fps = question_fps = 24.

- Cat speed: I fitted lines to the track in scene/tracks/dog.csv. nose_x, mask_cx and torso_cx all give 10.99–11.02 px/frame,
  so 11.0 × 24 = 264.5 px/s and the scale is 0.94 / 264.5 = 3.554e-3 m/px. The speed is constant (no acceleration), so
  the frame does not matter.
- Sofa length (x-extent of the curved cream sofa): measure.py finds the strongest gradient edge on rows 600–820 of
  frame 10. The right outer edge is at x = 1451 (y≈700–740) and the left outer edge at x = 566 (y≈680–690). That gives
  885 px, which matches the scene record's box 565–1452 (888 px). I checked both edges on zoomed crops (frames/L.png, R.png).
- Length = 885 × 3.554e-3 = **3.15 m**. Using the record's 888 px gives 3.16 m.
- Perspective: the sofa's widest outline sits higher than the cat's origin. The wall perspective suggests the camera is
  roughly 10 m up, so this effect is at most about 2%. I did not correct for it (the paper uses one 2D scale).
- Plausibility: the cat comes out at about 0.68 m nose to tail tip and the sofa at 3.15 m, which is a large curved sofa. Both are reasonable.
Confidence: good (±3%).
