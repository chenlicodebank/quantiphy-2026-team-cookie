# Q2109 — pencil length (mm), prior: mouse width = 57 mm

The camera is static and looks straight down on the desk. The mouse and the pencil both lie on the desk and do not move, so I used one planar scale for both (internet convention). The fps difference doesn't matter because this is a size question.

## Measurements (measure.py, frames 0 and 35)
- **Mouse** (white, at about (1598,1338)): a white, low-saturation blob, fitted with minAreaRect at thresholds V>150/170/190.
  - Width (short side): 101.6–103.5 px. I used **102.5 px**.
  - Length: 197–199 px.
  - Frames 0 and 35 agree.
- **Pencil** (yellow body with a black end, left of the teacup): I took an intensity profile along the line from (797,1162) to (998,922), averaged over 5 px across the pencil, and compared it with the desk 15 px to either side.
  - The pencil starts at t ≈ −4 (sharp tip) and ends at t ≈ 313 (black end). That gives 316 px at frame 0 and 318 px at frame 35.
  - Allowing for the blurred tip, I took **315 px**. The record in scene/ reads it by hand as 306 px, which is a little short.
- **Scale:** 57 / 102.5 = 0.556 mm/px.
- **Pencil length:** 315 × 0.556 = **175 mm**.

## Check
- The mouse's length/width ratio is 1.93. A Magic Mouse (57 × 113.5 mm) has a ratio of 1.99, so the width measurement is consistent.
- Scaling from the mouse length instead (113.5 mm / 198 px) gives 180 mm. That is within 3%.
- 175 mm is a typical pencil length.

Confidence: good (±4%).
