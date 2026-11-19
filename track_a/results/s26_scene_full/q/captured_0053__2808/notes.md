# Q2808 – length of the book (cm)

## Corrections to the scene record
- The moving object the record calls a "blue toy/RC car" is the **trashbin**: a blue bin lying on its side and rolling,
  as in the prior. Its track in scene/tracks/blue_car.csv is the trashbin track.
- The "white box/card" near the bottom centre (around (666, 612)) is the **book**. It lies flat on the floor and is
  rotated about 28 deg in the image. It is static.
- The file rate and question_fps are both 24, so no time-base issue.

## Method
- Camera (lab card): f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Book depth = 2.082 m (from depth_info). Centre back-projected to (0.067, 0.653, 1.976) m.
- Corners (`corners.py`): I fit lines to the sides of a white-cover mask (several thresholds; frames 2, 10, 30, 47;
  the book is static). Then I checked the corners on an 8x zoom (`drawc.py`, frames/book_corners.png). The mask's
  bottom-left corner included the book's visible side face (its thickness). The top-cover corners I used are
  TL (629.5, 588.5), TR (669, 576.5), BR (702, 634), BL (661.5, 647.5).
  - Cover long sides: about 67 px each. Short sides: about 41 px.
- The book is seen obliquely, so its long side (which runs roughly up the image) is foreshortened. I corrected for
  this with a floor plane (`plane.py`, `check.py`):
  - The plane is fitted through the given depths of the book (centre ~1.5 cm up), the cup (centre ~6 cm up) and the
    basketball (centre ~12 cm up).
  - Result: camera height ~1.69 m, floor tilt ~35.5 deg.
  - I back-projected the top-cover corners onto the plane raised by the book's thickness (~2.5 cm).
- Result: long sides 19.4 / 19.4 cm, short sides 11.3 / 10.9 cm, corner angle 86 deg.

## Checks / sensitivity (check.py, tilt scan)
| Floor tilt | Book length | What supports it |
|---|---|---|
| 40 deg | 18.5 cm | plane with no height offsets |
| 36 deg | 19.3 cm | ball centre 0.11 m up; cup centre 0.05 m up – matches the real objects |
| 34 deg | 19.7 cm | |
| 32 deg | 20.1 cm | trashbin centre 0.08-0.11 m up |
| 28 deg | 21.2 cm | book corners exactly 90 deg; weak, because 1 px of corner error shifts the angle by a few deg |

- The ball's own apparent diameter (64-69 px at 2.925 m, so 0.245-0.26 m) confirms the focal length and depth scale.
- Without the foreshortening correction (plain lab card, depth x px / f): 67 px x 2.082 / 763 = 18.3 cm. That is a
  lower bound.
- I weight the ball and cup most (tilt 35-36 deg, 19.3-19.4 cm), and the trashbin and rectangle checks pull the value
  up slightly.

**Answer: 19.6 cm.** Confidence: moderate, about ±5-8%. The main uncertainty is the floor tilt.
