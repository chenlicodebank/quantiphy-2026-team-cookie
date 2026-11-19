# q_3093 — cup displacement between 1.00 s and 1.10 s

The question's rate and the file's rate are both 30 fps, so 1.00 s is frame 30 and 1.10 s is frame 33.
The camera is static (see scene/notes.md), and the mug slides horizontally to the right.

Scale: prior height of the cup = 10.5 cm. The body's pixel height (rim to base) is 568-570 px in the record
(frames 30 and 33). My own measurement (measure.py, background difference against empty frame 50,
central columns) gives 567 px. I used 568 px, so the scale is 0.01849 cm/px.

Displacement in pixels, frame 30 to frame 33:
- record body centre: 540.3 -> 862.6 = 322.3 px
- my wall-band edges (rows 330-470): left 320 -> 641 = 321 px, right 772 -> 1091 = 319 px, centre 320 px
- vertical drift: about 6 px, which is negligible
- by eye on gridded frames: the knot moves about 985 -> 1300 (about 315 px), and the left edge moves about 298 -> 628 (about 330 px)

I used 321 px, giving 321 x 10.5 / 568 = 5.93 cm. The record-based route gives 5.95 cm.
Confidence: good (about ±3 %).
