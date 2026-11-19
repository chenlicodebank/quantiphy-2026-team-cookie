# q_2815 – width of the book (cm)

The book is the flat white printed rectangle that scene/ calls `white_card`. It lies on the floor near (665, 614) px and does not move. The file and question_fps are both 24.
Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360). Book depth at 0.4 s = 2.082 m.

## Measurement
- `seg_book.py`: takes the median of 6 frames, fits a polynomial background in an ROI and thresholds the residual at 15/20/30/45. The
  mask outline was checked on `frames/book_seg.png`. It fits a 4-corner quad to the mask:
  (666,576), (701,637), (661,654), (630,588) at threshold 20. The two long sides measure 70 and 73 px, and the short sides 38 and 43 px. The image is clearly a
  trapezoid because the book is seen obliquely on the floor.
- `geom.py`: the floor plane comes from the given depths. The ball centre is one radius above the floor (r = 12.6 cm, from its pixel
  size), the cup centre is half its height above the floor (15.5 cm tall) and the book lies on the floor. The camera comes out about 1.66 m above the floor, tilted down about 34°.
  The quad's corners are back-projected onto that plane, giving sides of 20.9 / 11.3 / 21.5 / 10.6 cm. The corner angles are 86–92°, which checks the plane, and
  the reconstructed centre depth is 2.085 m (given: 2.082).
- Second route (`rect_check.py`): instead, choose the plane tilt that makes the back-projected quad as rectangular as possible (tilt 42.7°). This gives
  short sides of 11.7 / 10.7 cm and long sides of 18.9 / 19.4 cm. Adding the trashbin's motion direction as a constraint on the plane gives a short side of 11.4 / 10.5 cm.
- The short side is about 11 cm on every route: mean of the two short sides 10.9–11.2 cm, threshold spread ±0.3 cm. The length is
  about 19–21.5 cm and depends more on the tilt.
- The naive minimum-area-rectangle width (48 px → 13.2 cm) is inflated by the trapezoid shape, so it was rejected. The plain
  fronto-parallel edge lengths (9.8 and 11.25 cm) average 10.5 cm.
- Scale check against the prior (`prior_check.py`): back-projecting the trashbin centroid at constant depth 2.73 m with this f gives
  0.99–1.04 m/s at 0.4 s (prior 0.9962), so the focal length and depth scale are consistent.

## Answer
Width (shorter horizontal side) = **11.0 cm**. Length ≈ 20 cm, given for reference only.
Confidence: moderate (about ±8%). The visible edge thickness of the book and the 1-px blur at the mask edge add up to about 0.5 cm of uncertainty.
