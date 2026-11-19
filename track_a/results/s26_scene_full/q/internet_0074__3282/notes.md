# Q3282: total length of the pickleball court (m)

Prior: court width = 6.1 m. Internet video, top-down drone view, so the planar single-scale convention applies.
Scale = 6.1 m / the court's pixel width; length = the court's pixel length (baseline to baseline) x scale.
Time base does not matter for this question (static size).

## Measurement (measure.py)
White-line masks (min RGB > 180) at frames 0, 30, 60, 90 and 121. Row profile over x 900-1150 gives the baselines,
column profile over y 500-950 gives the sidelines.
- Outer edges: L/W = 2001/908, 2009/912, 2020/917, 2029/921, 2033/923 px -> 13.443, 13.437, 13.437, 13.439, 13.436 m
- Line centres: 1992.5/899.5 ... 2024/914 -> 13.51 m
The slow zoom changes the pixel sizes by about 1.6%, but the ratio stays constant.

## Second route
The scene record's court lines (frame 0: 2000/911 px outer edges -> 13.39 m; 1991/902 px centres -> 13.46 m)
agree. Regulation size is 44 x 20 ft (13.41 x 6.10 m), which fits.

## Answer
Pickleball courts are measured to the outside of the lines, so I used outer edges: **13.44 m**
(the line-centre reading would give 13.51 m). Confidence: high, within about 1%.
