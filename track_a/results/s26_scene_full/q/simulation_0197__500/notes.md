# Q500 – diameter of the bottle's neck (m)

Prior: the "skynova" text on the bottle is 0.00188 m wide horizontally. The text runs vertically on the bottle; only
"NOVA" is in frame (x ~1106–1186, y 2030–2560), and "SKY" is cut off below the frame. Its horizontal (world x) extent
is therefore the letter height across the image.
fps 30 = question_fps, so there's no re-timing issue. The scene is static, so frame 0 is used.

## Measurements (measure.py, frame 0)
- Text: white, low-saturation mask (S<60, V>150), one component per letter. Every letter spans x 1106/1108 → 1184/1186,
  which is 78–80 px. I used 79.5 px, giving a scale of 0.00188/79.5 = 2.365e-5 m/px.
- Neck: the horizontal gradient extent per row across the threaded neck. The widest ring (the lowest thread/bead,
  y 1540–1600) spans x 1180–1960, which is 780 px. This matches the scene record (neck_outer_width 780 px). The upper
  threads are about 690–700 px wide.
- Diameter = 780 × 2.365e-5 = 0.01845 m (about 18 mm, a standard dropper-bottle neck size, so it passes the sanity check).

## Check / uncertainty
The scale was checked across 4 letters (78–80 px, ±1.5%). If "neck" means the narrower upper thread diameter
(~700 px), the answer would be 0.0166 m. I chose the full outer extent (the bbox convention): **0.0184 m**.
Confidence: medium.
