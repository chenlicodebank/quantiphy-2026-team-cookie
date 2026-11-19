# Q1113 — height of the boat (m)

File is 25 fps and question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48 (taken from the frame column).

## Scale: focal length from the person
- Prior: the person is 1.75 m tall. depth_info puts the person at 114.83 m at t=1 and t=2.
- The person's pixel height comes from a background difference (`person_h.py`). At frame 24 the head top is at
  y≈529.7 and the feet at y≈583.7, so 54.0 px (mid-stride). At frame 48 it is ≈52.6 px. Over the whole clip the
  record gives 52-55 px (integer, inclusive). I took the standing-equivalent height as 54.5 px (the upper end, since
  walking poses shorten the body).
- f = 54.5 × 114.83 / 1.75 ≈ 3576 px. The range is 3543-3630 px across height readings of 54-55.3 px.

## Boat pixel height (vertical bbox: mast top to keel/rudder bottom)
- Frame 24: the mast top is at y≈305 (`mast_prof.py`; the record said 302.6). The dark hull bottom is at ≈626-629
  and the rudder bottom at ≈632 (zoomed crops from `boat_crop.py`). The water surface sits at the keel, and the
  reflection starts right below it, so the visible hull is the whole hull. Bottom ≈630±3 gives 325 px (the record has 323.3).
- H = 325 × 103.157 / 3576 ≈ 9.37 m.

## Second route
- Frame 48 (t=2, depth 106.09 m): the record height is 313.8 px, so 313.8 × 106.09 / 3576 = 9.31 m. At frame 24 the
  record's 323.3 px gives 9.33 m. The ratio of apparent sizes (1.030) matches the ratio of the given depths (1.028), so
  the depths and the pixel tracking agree.
- Plausibility: the boat is about 7.2 m long as projected (249 px), and a mast top about 9.3 m above the keel is
  realistic for a small fishing boat.

Answer: 9.35 m. Confidence is moderate, about ±4 %. The main uncertainty is the person's pixel height (gait, a 54 px
target) and the keel/rudder bottom against the water.
