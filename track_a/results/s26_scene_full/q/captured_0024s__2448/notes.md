# q_2448 — height of the book (cm)

Video: lab capture, 1280x720, 24 fps (same as question_fps), f = 0.5959*1280 = 762.8 px, principal point (640,360).
The teal hardcover book slides down a white board onto the table (scene/ record checked: correct object and frames).
The book lies flat the whole time, so **height = vertical extent = thickness**, by the task's size convention.
Other reading: "book height" in the publishing sense is the long cover side. At rest that edge is ~150 px at Z~0.98 m,
which gives ~19-20 cm. Not used.

## Measurement (band.py, profile.py)
The front face of the book (page block between the top and bottom cover-edge lines) shows as two dark lines.
Per-column profiles give:
- Rest (frame 46, cols 515-575, clean sections): centre-to-centre spacing 11.3 px; outer half-max extent 13.5 px.
- On the ramp before sliding (frame 18, cols 728-800): spacing 7.7 px; outer extent 10.1 px.
The outer extent (top edge of the top cover to bottom edge of the bottom cover) is the book's real thickness. The
spacing between line centres leaves out about one cover-board thickness, so it is a lower bound.

## Scale
Route A (ramp, from the book's own depths): 3D centres P24 (d=1.0685) and P29 (d=0.977). The line through them is the
ramp path (24.9 deg slope with a level camera). P18 is extrapolated on that line (d about 1.116 m). The thickness vector
is the ramp normal x h, projected into the image: 9.26 px per 1.5 cm across the edge line.
-> outer 10.1 px gives 1.63 cm (spacing gives 1.25 cm).
Route B (rest): the book's table contact row (~484) equals the row of the board's lower edge midpoint (650,484). With
slope_near = 0.99 m that gives Z = 0.977, and Z_rest = 0.98 for any horizon between 300 and 366 (geom.py).
-> outer 13.5 px gives 1.74 cm (spacing gives 1.46 cm).
The book depths sit about 5 % closer than the board depths. On the book-depth scale Route B gives about 1.65 cm.
Vanishing-point and table-corner geometry were too noisy to use (the table distances do not fit the corners).

## Answer
Thickness ≈ 1.65 cm (routes 1.63 / 1.74 on the outer extent). Confidence: moderate, about ±10 %. The main error sources
are 1-px edge uncertainty on a ~10-13 px band and the rest-depth estimate.
