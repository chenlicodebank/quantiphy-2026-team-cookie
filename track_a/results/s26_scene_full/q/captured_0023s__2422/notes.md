# q_2422 — width of the slope (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px.
"Width" of the slope (white ramp board) = horizontal extent across its face (side to side), as in the method card for upright/flat boards.

Measurement (measure.py, frame 48, book gone from the ramp): white mask (S<40, V>200), longest run per row.
- Far (top) edge, rows 358-361: 143-145 px (row 357 is 139 because of the rounded corners). Depth to far slope = 1.2010 m
  -> 1.2010 x 144 / 762.8 = 22.67 cm.
- Near (bottom) edge, rows 470-478: 181-183 px (rows >480 are the table's reflection of the board). Depth to near slope
  = 0.9555 m -> 0.9555 x 182 / 762.8 = 22.80 cm.
- Line fit to the side edges extrapolated to the corners gives 22.4 (far) / 23.1 (near); the bottom right edge
  is vertical near the bottom, so direct row widths are preferred.

Second route: the two edges with independent depths agree within 0.6%. Answer 22.6 cm (mean of ~22.4-22.8, allowing
for the 1 px anti-aliasing margin at each side). Confidence: good (±3%).
