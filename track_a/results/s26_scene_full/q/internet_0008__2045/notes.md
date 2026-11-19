# q_2045: average speed of the speedboat (m/s)

- The speedboat is the small motorboat crossing the bottom of the frame (frames 224–~348). The camera is static (horizon fixed at row 437, see scene/notes.md). The rate is 30 fps (file = question_fps).
- Scale (internet convention, a single planar scale): sailboat length = 12 m. I measured the silhouette rows in code (`sb_len.py`). The hull/deck rows span about 98–102 px, and the full dark bbox including bowsprit/stern fittings is 103–106 px (record median 105). I used L ≈ 102 px, so the scale is 0.1176 m/px.
- Motorboat track (`track_mb.py` → `mb_track.csv`): dark-blob tracker that uses the bow (right edge, which the trailing wake does not affect). I checked it on overlays (frames/mb*.png). I rejected 11 frames where the wake or the sailboat merged into the blob, and the frames where the bow was off-frame.
- Speed (`speed.py`): the mean of the per-frame speeds over frames 224–343, after 5-frame smoothing, is 7.68 px/frame (vertical drift 0.11 px/f). The image speed grows from about 6.5 to 9 px/f, because the boat approaches the camera and/or accelerates. The net bow displacement gives 7.68 px/f and a linear fit gives 7.63.
- Second route: the record's motorboat bbox-centre slope is 7.68 px/f (an independent tracker), which agrees.
- Result: 7.68 × 30 × 12 / 102 = 27.1 m/s. Range by length reading: 26.3 m/s (105 px) to 28.2 m/s (98 px).
- Confidence: moderate. The main uncertainty is which sailboat pixel length the annotator used (±4 %). The planar scale also ignores that the motorboat is nearer the camera, as the convention requires.
