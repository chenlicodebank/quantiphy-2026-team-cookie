# q_2701 — white cup rim diameter (cm)

File fps = question fps = 24. Static camera. f = 0.5959 x 1280 = 762.75 px, principal point (640, 360).

## Measurement (measure_cup.py)
- Median of every 4th frame (ball is not in front of the cup in most of them), crop around the cup.
- Sub-pixel gradient edges per row: rim / metal band rows y 380-394 give left 723.9-724.0, right 794.4-794.6,
  **width 70.6 px** (rows 378: 69.3 at the rounded top; the body below tapers to 67.8 px by y 418).
  Matches scene/ record (x 724-794, 70 px).
- depth_info: white cup 0.8740 m (range to the centre). Converting range to camera Z along the ray of the cup
  centre (759, 437) / rim level (759, 387): Z = 0.859-0.863 m, use 0.861.
- Diameter = 70.6 x 0.861 / 762.75 = **7.97 cm**.
  (Using the range directly instead of Z: 70.6 x 0.874 / 762.75 = 8.09 cm.)

## Check with the prior (measure_card.py)
- Credit card = dark navy card with yellow sticker lying near the table front (x 517-620, y 533-554).
  Long-edge pixel length 94-102 px (top/bottom edges), ~98 px mean. Range 0.6867 m -> Z = 0.665 m.
  98 x 0.665 / 762.75 = 8.54 cm vs prior 8.56 cm (0.2 % off). With range instead of Z: 8.82 cm (+3 %).
  So the Z conversion reproduces the prior; used for the cup as well.

## Confidence
Edge widths ±1 px (±1.5 %), focal/depth convention ±2 %. Answer 7.97 cm, likely within ~4 %.
