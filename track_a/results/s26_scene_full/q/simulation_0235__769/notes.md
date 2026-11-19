# q_769: length of each small window pane (m)

Method: a 2D scene facing the camera, so I used one m/px scale taken from the basketball (prior: diameter 0.282 m).
- The ball measured by `measure.py` (HSV mask, largest blob): its bbox is 108x108 px at frames 0, 10 and 40, and its area-equivalent diameter is 107.3–107.7 px. I used 107.7 px, which gives 0.002618 m/px.
- The ball is at the wall's depth. At the bounce (frame 24) the ball's bottom is at y≈921, the same as the wall-foot line (917–921). One scale therefore covers both the ball and the wall windows.
- Panes: I took dark-glass widths along rows y=120 and y=320. The full panes measure 196, 200, 203, 205, 201 and 198 px (the spread comes from the recess bevel on either side of the image centre). The panes near the centre average about 203 px. The heights are 147–150 px from column scans. "Length" is taken to be the longer, horizontal side.
- Result: 203 px × 0.002618 = 0.53 m. (The height would be about 0.39 m.)

Check: a 3x zoom crop of the pane at x 1007–1219 (about 205–210 px including the inner shadow) agrees with the scan. The scene record's 208x150 px is consistent too.
Confidence: moderate. The main uncertainty is whether the reference counts the frame or bevel; a pane including its frame would be about 0.57 m.
