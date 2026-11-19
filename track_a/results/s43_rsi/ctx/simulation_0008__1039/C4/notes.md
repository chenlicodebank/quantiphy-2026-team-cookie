3D pinhole reconstruction: f=958 px and boat depth 5.78 m solved from the two exact boat distance priors (7.452 m at frame 0, 6.655 m at frame 24) plus the boat's pixel track (bow tip x0=993-10*frame, full extent 620 px); camera 1.34 m above the water plane. Pier outer (front) deck edge at v=633, u=548 gives depth 9.56 m from the 11.579 m pier prior and 9.65 m independently from the pier's mirror-reflection waterline (v_w=673), so 9.60 m. Boat at t=3 s (frame 72, question_fps 24) is at (0.26, 0.94, 5.78) m, pier end at (0.08, 0.93, 9.60) m -> distance 3.82 m; sensitivity across alternative boat-centre and pier-depth routes 3.77-3.87 m.

Final message:
I measured the scene in 3D and answered.

**Method summary**
- **Scale/camera:** solved focal length (f ≈ 958 px) and the boat's depth (5.78 m) from the two exact boat–camera distance priors (7.452 m at t=0, 6.655 m at t=1 s) together with the boat's pixel track (bow tip exactly 10.0 px/frame, full extent 620 px). Camera height above the water plane = 1.34 m, cross-checked against the far-shore waterline and the given stairs distance.
- **Pier outer end:** the deck's front edge (v=633, u=548) is at 9.56 m depth from the 11.579 m pier prior, and independently 9.65 m from the pier's mirror-reflection waterline (v_w=673, measured on both front posts). Adopted 9.60 m, deck 0.41 m above water.
- **Boat at t=3 s:** frame 72 at question_fps 24 (7 frames past the clip end), extrapolated with the exact constant pixel velocity → (0.26, 0.94, 5.78) m.

**Answer: 3.82 m** (sensitivity across alternative routes 3.77–3.87 m, ~3 % confidence).
