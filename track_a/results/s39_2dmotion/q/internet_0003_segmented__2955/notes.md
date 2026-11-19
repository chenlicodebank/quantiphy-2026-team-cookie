# q_2955 — velocity of the pizza cutter at 0.2 s (cm/s); prior: money width = 7.5 cm

File fps 24 (48 frames); question_fps 30 → t = 0.2 s → frame round(0.2·30) = 6; speeds use px/frame × 30.
Frame 6 is an exact duplicate of frame 5 (the file has duplicates at 2, 6, 11, 15, ...).

## Scale (money.py, SAM 3 "banknote" on frame 6)
- Top 500 note (fully visible, ~2.5° tilt): saturation profiles down columns x=885/900 give its top edge at y≈193 and
  its bottom edge at y≈262.5 → about 69.5 px across (perpendicular). The rotated 500 note below it is ~70-71 px across.
- SAM 3 mask k0: box height 70.4 px, vert 71, PCA width 73.2 (the PCA width is inflated by the tilt/blurry edge;
  the box height agrees with mine to within 1.3 %). scene/notes.md said 64 px; I checked a 4× zoom (frames/money2.png)
  and the note really runs from y≈193 to 262, so 64 is too small.
- Note width used: 69.75 px → 7.5/69.75 = 0.1075 cm/px. Sanity check: the pizza is 472 px ≈ 51 cm, so it's a large pizza.

## Cutter motion (track.py, track_hand.py)
- The SAM 3 "pizza cutter" track's box takes in the cut slit behind the cutter (x0 stays at ~498), so its centre isn't usable.
  The scene front-point and dark-blob centroid are biased because the hand covers more and more of the guard (area 1268→600 px).
- My own tracker template-matches six patches on the guard and hand, corrected for camera drift (glass and money patches,
  about -1.3 px/frame vertically). Patches with good correlation (r ≥ 0.96) give a step of 18.5-19 px per new frame
  for frames 3→4→5→7→8→9 (direction ~42° below +x).
- Because of the duplicated frames, the per-file-frame displacement around frame 6 is: 4→8 14 px/f, 3→9 15.6-16 px/f,
  2→10 13.8 px/f, 1→10 14.0 px/f. The long-run fraction of new frames is 37/48 = 0.77, and 0.77 × 18.5 = 14.3 px/f.
  I take 14.5 px/frame.
- v = 14.5 px/frame × 30 frames/s × 0.1075 cm/px = **46.8 cm/s**.

## Second route and alternatives
- Using the scene's background-stabilised front point instead: f3→f9 is 85.5 px / 6 = 14.25 px/f, which gives 46 cm/s. This agrees.
- The raw one-frame forward difference at frame 6 (p7 − p6 = 18.5 px) would give 59.7 cm/s. Using the file's 24 fps
  instead of 30 would give 37.4 cm/s. I chose the smoothed value at question_fps.

Confidence: moderate. The scale is good to about 3 %; the main uncertainty is the time base and how the duplicated frames are handled.
