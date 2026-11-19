# q2954: wine glass diameter (cm), prior: money width = 7.5 cm (internet, segmented, 2D/planar convention)

File fps 24, question_fps 30. Both objects are static, so the time base does not matter.

## Where C1 (14.7) and C2 (6.9) part ways
Both measured the glass at about the same pixel size (133 to 135 px across the bowl, perpendicular to the glass axis).
They differ only in which side of the Monopoly note is the "width":
- C1: the short side (~69 px), giving 0.109 cm/px.
- C2: the long side (~146 px), giving 0.051 cm/px.

## My reading: width = short side (agree with C1's reading)
- The benchmark's naming convention says that for an object lying flat, length is the longer horizontal extent and
  width the shorter. A 7.5 cm width also fits how people think of a banknote (about 15 x 7.5 cm). A note that is
  7.5 cm long would be odd.
- I checked the scale against other objects in the scene, but they don't settle it. With either scale they come out
  about 30-40 % off typical sizes, in opposite directions:
  - Board squares (~50 x 86 px): about 5.4 x 9.3 cm with the short-side scale, 2.6 x 4.4 cm with the long-side
    scale. Standard board squares are about 4.1 x 6.6 cm.
  - Pizza (456 px): 50 cm vs 23 cm.
  - Pepperoni (~45 px): 4.9 cm vs 2.3 cm.
  - Fist (~150 px): too big with the short-side scale, too small with the long-side scale.

  The scene's own scale is about 0.08 cm/px, so the real notes are about 12 x 5.6 cm. Since the scene can't decide,
  I follow the naming convention.

## My measurements (measure.py, frames 0, 10, 30 and 47)
- Top 500 note, short side: top edge y ~196, bottom edge y ~266 at x 876-903, with a ~3 deg tilt. That gives 70 px
  (range 69-72; column extents of 73-76 px include edge blur and part of the board). The rotated 500 note gives 65-70 px.
- Glass: it stands upright and is seen from above. The rim/bowl circle shows its true diameter in the direction
  perpendicular to its axis on the image. The bowl mask's extent perpendicular to the axis is 133.7, 132.6, 132.9 and
  131.6 px in frames 0, 10, 30 and 47, so I use 133 px.
- 133 x 7.5 / 70 = 14.25 cm. With the note at 69-72 px the range is 13.9-14.5 cm, and C1's 135/69 gives 14.7.

Answer: 14.3 cm. My confidence is moderate. The main risk is the width reading: under the long-side reading the
answer would be about 6.8 cm.
