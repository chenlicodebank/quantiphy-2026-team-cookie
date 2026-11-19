# q2326 – distance box ↔ pineapple toy at 3.0 s (cm)

- The clip has 49 frames (0–2.0 s at 24 fps, same as question_fps). 3.0 s would be frame 72, which is **past the end**.
  So I used the last frame, f48 (2.0 s). By then the box (white carton) has tipped over and lies on its side by the
  left person's feet, and the pineapple has bounced back and is rolling on the floor. Both are still drifting apart a
  little (box moving left about 9 px/frame, pineapple moving right about 5 px/frame), so the true 3.0 s value may be a
  bit larger.
- f48 pixels (from the scene tracks, checked on zoomed crops in frames/strip.png and frames/f48_low.png): box centre
  (419,594) with bottom at 610; pineapple centre (847,596) with bottom at about 617.
- No depth is given for the box or the pineapple, so I estimated their depths from a flat ground plane (level camera,
  f = 763):
  - m1: fitted to the feet rows of the two people (577 / ~710) and their given depths 3.13 / 2.002 m.
    Z_box = 2.56, Z_pine = 2.49, distance = 1.42 m.
  - m2: fitted to the soccer ball's bounce contact (row 577, depth 2.8 m) and the pineapple's first floor contact
    (row 697, Z ≈ 1.85 m from its fall acceleration against the 9.8 m/s² prior).
    Z_box = 2.40, Z_pine = 2.34, distance = 1.33 m.
  - Check on the pineapple's depth from its size: it is about 30 px wide while held at Z ≈ 1.82 m and about 23.5 px at
    f48, giving Z ≈ 2.32 (agrees with m2).
- The depth estimates from fall acceleration are noisy because of irregular frame timing (a probable dropped frame
  around f35/36).
- Answer: about 1.39 m, the midpoint of the two models with a slight upward lean for the continuing separation.
  **139 cm**. Confidence is low to moderate (±7%), mainly because 3.0 s is outside the clip and the object depths are
  not given.
- Scripts: measure.py, strip.py.
