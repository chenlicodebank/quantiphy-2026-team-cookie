# q 2746 – diameter of the tape (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). Camera static.
Method card: f = 0.5959 x 1280 = 762.8 px; size = depth x pixel extent / f.

## Tape
Clear packing-tape roll standing on its flat face (axis vertical), between jar and card tent; static.
Horizontal silhouette width = outer diameter. Measured in `measure.py` on the mean of frames 0, 10, 48:
max-gradient (sub-pixel) left/right edges on rows 440-479 -> L ≈ 551.7, R ≈ 628.0, width 76.4 ± 0.5 px
(the scene record's eyeball value was 78 px). Crop check: frames/tape_crop.png.
Diameter = 0.973 m x 76.6 / 762.8 = 0.0977 m ≈ 9.8 cm (78 px would give 9.95 cm).

## Check (credit card prior)
Credit card = dark navy card at the table front (depth 0.69 m). Expected long-edge pixel length 0.69 -> 85.6 mm
→ 0.0856 x 762.8 / 0.69 = 94.6 px. Measured long-edge horizontal extent ≈ 90-100 px (rows 532-550, avg ≈ 97;
the yellow note and the slight in-plane rotation make this less precise) → 8.8 cm, 2-3 % above the prior, consistent with
the focal length. The silhouette correction for a cylinder of r ≈ 5 cm at 0.97 m is negligible (<0.2 %).

Answer: 9.8 cm. Confidence: good (±3 %).
