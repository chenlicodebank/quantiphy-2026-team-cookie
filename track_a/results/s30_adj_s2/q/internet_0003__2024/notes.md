# Q2024: pizza cutter velocity at 0.2 s (cm/s); prior: Monopoly money width = 7.5 cm

## Time base
The file runs at 18.314 fps; question_fps is 24. Following the rules, t = 0.2 s is frame round(0.2*24) = 5 and
dt = 1/24 s. Both earlier sessions did the same.

## Where the candidates part ways
They part ways on the scale only. Both measured about 37 px/frame.
- C1 (42): 7.5 cm over the bill's short side, taken as 155 px.
- C2 (31.3): took the scale from guessed "standard" objects (wine glass, board, pizza), which gives 0.0351 cm/px.
  This breaks the internet-video rule that one scale comes from the prior, and the 214 px it uses for the $1 bill
  is a bounding-box extent of a rotated bill, not its width. Rejected.

## My measurements
- Cutter (track.py): I template-matched the hub guard frame to frame and removed camera drift with the median of 4
  static background patches. Stabilised steps: 3->4 38.5, 4->5 37.8, 5->6 36.6, 6->7 41.8 px. The record's x_s0/y_s0
  gives 36.5, 34.2, 36.4 and 40.5. Forward difference at frame 5 is about 36.5 px/frame and the local mean is about
  37. I used 36.5 px/frame × 24 = 876 px/s.
- Bill width (crops.py, gridded 1:1 crop of frame 27): the short sides of the pile bills are top 500 about 150 px,
  middle 500 149–153 px, and 100 about 150 px. The lone 1 bill is 171–176 px (305 × 173; its aspect differs, so it
  is a different shape or seen at a different angle). The pile bills are the prominent "Monopoly money", so the width
  is 150 px and the scale is 7.5/150 = 0.050 cm/px.
- Sanity check: the cutting hand is about 380 px long (fingertips to wrist), which is 19 cm, a normal hand. The pizza
  is 990 px, which is 49.5 cm (large but possible). At C2's scale the hand would be 13 cm, which is too small.

## Answer
876 px/s × 0.050 cm/px = 43.8 cm/s, reported as **44 cm/s**.
Using the 1 bill instead would give 38 cm/s; using the local-mean step of 37 px would give 44.4 cm/s.
I agree with C1's method; the difference is a slightly narrower bill width (150 px against 155 px).
Confidence: moderate. The main uncertainty is which bill the annotator measured.
