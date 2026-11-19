# Q1088 – height of the central sculpture (excluding pedestal)

File fps 33.039; question_fps 33 used for times (t=1 s -> frame 33). Image rolled 90 deg: world up = image +x.

## Geometry / camera
- Wall verticals (shelf dividers along image x) do not converge (<3 px over 400 px, edges.py) -> camera
  pitch ~0. The cubby inner faces (cubby.py) put the horizon at x ~546, so principal point taken as (540,540).
- Person walks at constant camera Z, parallel to the image plane (head width constant; head_y slope 7.62 px/frame
  identical in frames 5-35, 35-65, 65-100).
- Unknowns f, Z, origin offset from head line, solved from three equations: d(t=0)=5.424, d(t=1)=4.886 and
  1.3 m/s (= 7.616 px/frame * 33). Results: Z_person = 4.655 m, f = 900 px, origin y(0)=1.9, y(33)=253
  (scene track pelvis_y at f33 is 254.6-259, which agrees).
- Route 2 (depths only, head line as origin, focal.py): f = 888-913 depending on the fit window; implied speed 1.31 m/s.
  So f is 900 +-15 px.

## Sculpture
- Measured on the median background (sculpt.py): the wing tip (highest point) is at x = 783; the sculpture's
  bottom edge on the pedestal top is a straight line at x = 532 (the light pedestal block ends at 531).
  Pixel height 251 px.
- Origin depth 5.962 m, origin near pixel (657,538), r ~117 px -> Z_s = 5.962/sqrt(1+(117/900)^2) = 5.912 m.
- H = 251 * 5.912 / 900 = 1.649 m (f=888 -> 1.67; f=913 -> 1.63).

## Caveats
- Assumes the wing tip is at about the origin's depth (unknown); pedestal top / sculpture base edge +-3 px.
- Confidence: moderate, about +-5 %.

Answer: 1.65 m
