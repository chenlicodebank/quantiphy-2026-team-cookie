# Q387 – width of the road the bike crosses (simulation_0165)

Question: width (m) of the road the bike rides across. Prior: bike speed = 5.52 m/s. No depth_info. fps = question_fps = 24.

## Geometry
- The camera is static and looks straight down a street. The cyclist rides left to right across that street, through
  the intersection, at one depth: image rows stay horizontal, the bike's pixel size stays constant, and the tyre
  contact is at row y = 739.5 (darkest tyre rows 736-739 under both hubs at frames 48, 60 and 70; `tyre.py`).
- So the road being crossed is the street running away from the camera. Its width is the horizontal pixel distance
  between its two curbs, measured on the bike's contact row. That row and the bike's motion are at the same depth,
  so one m/px scale applies to both.

## Scale
- Bike speed from the scene record's line fits: hubs move 21.015 and 21.023 px/frame, and the bbox edges 20.96 and
  21.07, so 21.02 px/frame x 24 = 504.4 px/s. The motion is uniform.
- 5.52 / 504.4 = 0.010944 m/px. Sanity check: the 66 px tyre is 0.72 m across, and the 163 px bike plus rider is
  1.78 m long.

## Road edges (frame 5, `hough.py`, `edges2.py`, `edges3.py`)
- Edges on the near part of the street were found with subpixel edge profiles, then fitted as lines and
  extrapolated to y = 739 (the curbs are interrupted inside the intersection).
  - Left curb bottom (curb meets asphalt): x = 648.2 (std 0.5 px).
  - Left outer edge of the white edge line: x = 656.9 (std 0.2 px).
  - The two left lines meet at a vanishing point of about (962, 537), which matches the Hough estimate (958, 540).
- Right side: the edge detections were noisy, so each clean point was joined to the vanishing point.
  - Right curb bottom: points at x = 1600 and 1700 give x@739 = 1463.7 and 1464.8.
  - Right white line: x@739 = 1454-1455.
- Width at y = 739: curb bottom to curb bottom is 816 px, or 818 px after correcting to y = 739.5 (factor
  (739.5-537)/(739-537)).
- Cross-check: the curb top edges give 862 px on the near part of the street (Hough: 624 to 1486) and 865 px on the far
  part (635 to 1500). The two parts agree, so the street has the same width on both sides of the intersection.

## Result
- Curb to curb (asphalt surface): 818 px x 0.010944 = **8.95 m**. This is the answer.
- Other readings:
  - Between the outer edges of the white lines: about 800 px = 8.76 m.
  - Curb top to curb top: about 864 px = 9.46 m.
- Confidence: moderate-high on the measurement (about ±1%). The main uncertainty is which edge the reference treats as
  the road's edge (±5%).
