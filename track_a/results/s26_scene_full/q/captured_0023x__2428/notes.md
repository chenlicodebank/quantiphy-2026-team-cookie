# q_2428 — width of the book (cm)

The file is 24 fps, the same as question_fps, and the camera is static. The camera model is f = 0.5959 × 1280 = 762.8 px with the principal point at (640, 360).
"Width" here means the shorter side of the cover (the shorter horizontal extent when the book lies flat). The length is about 19.7 cm (177 px × 0.851 m / f on the table).
Because the cover is strongly foreshortened in every frame, it cannot be measured as depth × px / f directly. I measured it in 3D on known planes instead.

## Route 1: on the board at rest (frame 0), `board_route.py` and `board_width.py`
- **Board plane:** I took the board top edge (row 356.5, frame 48) at slope_far = 1.201 m and the bottom edge (row 482.5, frame 0) at slope_near = 0.9555 m.
  This gives a slope length of 0.302 m, inclined 31.3° from horizontal, with the bottom 0.151 m below the camera. That matches the table height from the table depths (0.151–0.154 m).
- **Book profile:** in each image column, the cover runs from its top edge at row 348.5 to the cover/side dark line at row 378–379, and the book bottom on the board is at row 386.
- **Solving:** I solved for the thickness t so that the cover plane (board plane + t·n) and the side face both fit. This gives t ≈ 1.25–1.4 cm.
  Width = the 3D distance between the two cover edges on the cover plane = **8.55–8.8 cm, median 8.57 cm**.
- **Check:** the book's upper edge lands 0.301–0.306 m up the 0.302 m slope, so it is flush with the board top, as seen in the video. The geometry is consistent.

## Route 2: on the table at rest (frame 46), `table_geom.py` and `width.py`
- **Table plane:** the horizon comes from the table side edges' vanishing point, (598, 349), which gives a pitch of about 0.8°.
  The table depths (0.704 and 0.725 m, taken as the front corners) put the table 0.151–0.154 m below the camera.
- **Top face:** at x = 562 it runs from row 480.9 (back edge) to row 496.9 (front edge). The side face runs from 496.9 to 509.8.
- **Result:** with the top plane at 0.152 − 0.014 m, width = **8.75 cm**.
- **Using the book depth instead:** if I take the plane height from the book-centre depth (0.851 m at t = 1.6), the result is 9.4–10.1 cm.
  But that depth puts the book centre 0.159 m below the camera, which is below the table surface. It is inconsistent with the table and board depths by about 8 cm in range, so I did not use it.

## Answer
Combining the two consistent routes (8.57 and 8.75) gives **8.65 cm**. Confidence: moderate, about ±5%.
