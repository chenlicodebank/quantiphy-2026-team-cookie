# Q57 – speed of the yellow (tan/peach) car at t = 2.5 s (frame 60)

- 2D near-top-down clip, 24 fps (file fps = question_fps, so no re-timing). "Turing yellow car" = the record's `tan_car`.
  "White car" = `white_van`.
- Scale: van body length = 236 px (threshold-25 body mask at f0 and f71 in the record; my own white-pixel row
  profile gives 234 px at f0 and 231 px at f36). 6 m / 236 px = 0.02542 m/px.
- Car speed: it moves at a near-constant ~6.8 px/frame for the whole clip. Its turn ends around f60.
  - Record track (ref centre), mean step f2–71 = 6.84 px/frame. Centroid = 6.83. Single steps around f60 are noisy (6.0–8.0, ±1 px jitter).
  - My own check (`check.py`, colour mask of the car): centroid x went from 1194.8 at f52 to 1324.6 at f71 = 6.83 px/frame,
    and from f56 to f68 = 6.81 px/frame.
  - Used 6.82 px/frame → 6.82 × 24 × 0.02542 = 4.16 m/s.
- Second route: with the 234 px van length the result is 4.20 m/s, about 1% higher. The mean step over a window and the
  single-frame difference at f60 agree to within the jitter.
- Confidence: good (±3%). The main uncertainty is the van's pixel length (231–236 px).
