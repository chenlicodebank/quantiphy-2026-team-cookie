# q3286: distance between the ball and the nearest player at 2.00 s

Time base: the file runs at 23.976 fps, and question_fps is 30. The file was made from a ~30 fps source by dropping
every 5th frame (scene notes), so source frame i_src = i + floor(i/4). At t = 2.00 s the source frame is 60,
which is file frame 48 (48 + 12 = 60). round(2.00 x 23.976) also gives 48, so both readings point to **frame 48**.
I checked the frame with view.py (frames/f48.png).

Frame 48 (measure.py, from the scene tracks; checked visually on the crop):
- Ball image centre (993.5, 838.5), just after bounce 1 at frame 45. It is rising toward the far player and its
  shadow is at (873, 841).
- Nearest player: the far player. Body-mask centroid (1015.5, 411.9), which matches the torso/cap on the crop.
- Pixel distance: 427.2 px. (Frames 47 and 49 give 485 and 394 px; the ball moves fast.)
- The near player is about 1690 px away.

Scale: court width 6.1 m. At frame 48 the sidelines are at x = 338.1 and 1248.0 (line centres), so 909.9 px
centre-to-centre and about 918 px between the outer edges. Taking ~914 px gives 6.674 mm/px.
- Using line centres: 2.86 m. Using outer edges: 2.84 m.
- Cross-check: the court length of 2008 px against 13.41 m gives 6.68 mm/px, which agrees.

**Answer: 427 px x 0.00667 = 2.85 m**

Caveat: the distance uses the player's body centre, following the planar annotation convention. If the
player's feet (~(1000, 460)) were used instead, the answer would be ~2.5 m. At frame 60 (reading the file at a
naive 30 fps) it would be ~1.4 m. I rejected that reading because of the dropped-frame structure.
Confidence: moderate (±10%).
