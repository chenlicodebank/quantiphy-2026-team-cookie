# Q373: width of the billiard table (m)

**Setup.** This is a top-down 2D render with a static camera. The prior is that the ball diameter is 0.0757 m. No depth_info is given. The table's long side runs horizontally in the image, so its width (the shorter horizontal extent) is its vertical pixel extent.

**Measurements (frame 39, scripts `measure.py` and `rail.py`):**
- **Outer edge of the wooden rail (table bounding box).** I measured the R−B brownness profile averaged over the columns x 300–850 and 1050–1600, avoiding the pockets. The half-maximum crossings are at y = 83.5 and y = 999.5, giving **916.0 px**. Both column ranges agree to within 0.03 px, and this matches the record's 84–999.
- **Ball diameter.**
  - The static balls measure 48 px in their bounding boxes: black 48.0 px area-equivalent, yellow 48.6 px.
  - The red, orange and white balls come out at 49–51 px, inflated by shadow and rim.
  - The record gives a median of 48.4 px for the moving ball.
  - I used **48.2 px**.
- **Scale.** 0.0757 / 48.2 = 1.5705e-3 m/px.

**Answer.** Width = 916 × 1.5705e-3 = **1.439 m**. This is the whole table's bounding box, including the rails, as the convention "sizes are the object's world bounding box" requires.

**Sensitivity and alternatives.**
- With a ball diameter of 48.0 px the width is 1.445 m; with 48.6 px it is 1.427 m, so the answer is within ±1%.
- If only the felt playing surface counted (790 px), the width would be 1.241 m. I don't use this reading, because the table object's bounding box includes the rails.
- Length (1672 px) = 2.63 m. The length-to-width ratio of 1.83 is plausible for a pool table.

**Check.** The two independent column ranges give the same 916 px rail extent. The ball sizes agree across five static balls and the moving one. **Confidence:** high for the bounding-box reading, but it rests on the assumption that the rails are included.
