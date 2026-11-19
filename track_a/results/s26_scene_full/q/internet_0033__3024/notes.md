# q 3024 – size of avocado (cm); prior: fork = 20.3 cm

Internet footage, overhead view of the table, so the annotator convention applies: one planar scale = 20.3 cm / fork pixel length.
This is a static size question, so the fps vs question_fps difference does not matter.
scene/ had no fork measurement. Its avocado tray bbox (~143 x 283 px) is for the whole tray. I measured both from scratch on frame 0,
using zoomed crops with grids (view.py, strip.py, avo_seg.py).

## Fork (prior object), frame 0
- Fork resting on the top-right (pink diner) plate rim, fully visible: handle end (1831,207) to tine tips (1720,293), 140.4 px.
- Independent second fork, held level by the bottom diner over the spaghetti plate: tine tips x≈995 to handle end x≈1134 at y≈1245, ~139 px.
- Other forks are partly hidden by hands in every frame (checked frames 0-46). One example is the fork beside the seafood plate, whose handle is always under the hand.
- Fork pixel length used: 139.7 px, so the scale is 0.1453 cm/px.

## Avocado, frame 0 (black tray with 6 avocado halves)
Long-axis tip-to-end lengths read on 5x zoomed crops (avo_seg.py colour mask merged the halves together, so I measured each half by eye on the grid):
92, 105, 94, 95.5, 101 px, plus one half partly covered (>=89). The mean of the fully visible halves is ~97.5 px; I used 97 px.
Size = 97 x 0.1453 ≈ 14.1 cm. Across the halves the range is 13.4-15.3 cm.
Sanity check: a 14 cm avocado is realistic.
Other reading: the width across a half is ~55-60 px, about 8-9 cm. I answer with the length, the longest extent.

Confidence: moderate. Uncertainty comes from which avocado half and which fork the annotator measured (about ±8 %).
