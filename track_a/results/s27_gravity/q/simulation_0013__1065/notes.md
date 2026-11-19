# q1065 – body length of the bird (simulation_0013)

File rate 21.75 fps, question_fps 24. Time base: file frame i is treated as t = i/24 (54 frames, retimed file).
Depth at t = 1 s is file frame 24.

## Focal length from gravity (prior g = 9.8) and the nest depth
- Re-segmented the nest myself (nest_seg.py, nest_ov.py; background = median of frames 45-53). The scene track's
  frame 33 centroid is wrong (its mask has extra area on top: y0=658 vs the true 694), so I did not use it.
- Free fall is clean only in frames 29-33: the nest leaves the branch at about frame 27, and from frame 34 it squashes
  and its speed drops (a collision).
  Mask-centroid y values 593.4, 643.4, 704.5, 782.2, 874.2 give per-frame steps 50.0, 61.1, 77.7, 92.0.
  A parabola fit gives a = 8288 px/s² (frames 29-33) or 8934 px/s² (frames 30-33). I took a ≈ 8500 ± 450 px/s².
- The nest's apparent size stays the same over frames 30-33 (about 360 px across), so its depth Zc is roughly constant.
  Zc ≈ 4.895 m × cos(off-axis angle) ≈ 4.82 m. Assuming instead a constant Euclidean distance of 4.89 m at frame 31
  gives the same 4.82 m.
- f = a·Zc/g ≈ 8500 × 4.82 / 9.8 ≈ 4180 px (range 3970-4390).
- Check: the nest then measures 360 × 4.82 / 4180 ≈ 0.42 m across, which is a realistic nest. Its total drop
  (1483 px ≈ 1.7 m) also fits a free fall of about 13-14 frames, from leaving the branch at about frame 27 to landing
  at about frame 40.5.

## Bird pixel length (beak tip to tail tip)
I read these on 4× zooms with a 10 px grid (birdzoom.py) and checked them against mask extents (bird_len.py). I used
wing-up frames, where the wings do not cover the tail or beak.
- Frame 10: 106 px; frame 12: 115; frame 20: 136; frame 24: 130; frame 27: 138; frame 29: 130; frame 43: 149;
  frame 46: 151-157.
- Pixel length × camera distance (linear in t from the given 35.96 m and 34.077 m):
  - frames 10-12: about 3700-4000;
  - frames 20-46: about 4400-5080, mostly about 4850.
- Over 0-1 s the 3D path heads about 36° toward the camera (from the given depths and f). That foreshortens the body
  by about 0.83 early on, so frames 10-12 corrected give about 4500-4800.
- Later the pixel speed rises from 13.8 to 19.7 px/frame, so the bird turns to fly more across the view (near side-on).
  That is consistent with the larger pixel lengths later on.
- Adopted pixel length × Zc ≈ 4800 px·m.

## Answer
L = 4800 / 4180 ≈ 1.15 m (range about 1.08-1.22 from the uncertainty in a and in the heading).

Scale caveat: a 1.15 m crow-like bird is about 2.5× a real crow. The bird-to-nest size ratio (about 2.8) does not
depend on f, so the bird model is oversized relative to a realistic 0.4 m nest. The gravity scale is internally
consistent (pixel acceleration, fall height against fall time, nest size), so I kept the gravity scale.
Confidence: moderate (±10-15%).
