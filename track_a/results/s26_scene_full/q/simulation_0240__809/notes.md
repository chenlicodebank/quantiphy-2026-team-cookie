# Q809: length of the rabbit (m). Prior: speed of the horse at the back = 0.874 m/s

Time base: fps = question_fps = 24, so no re-timing.

## Objects
- The "horse at the back" is the chestnut horse. It trails on the left, and its hooves are highest in the image (y≈1048-1050), so it is also the farthest from the camera.
- The rabbit hops in front, at a ground contact of y≈1066-1068.

## Scale from the prior
- Chestnut mask centroid: 234.1 → 385.5 px over frames 0-48, which is 3.154 px/frame. The bbox centre gives 3.125 px/frame. I used ≈3.14 px/frame = 75.5 px/s. Frame 49 is a loop reset and was excluded.
- Scale at the chestnut horse: 0.874 / 75.5 = 0.01158 m/px.

## Perspective (not a pure 2D plane)
- `vert.py`: the house wall edges are perfectly vertical (x is constant to ±1 px from y 640 to 1030). That means the camera is level, so the horizon is at the image centre, y = 960 (assuming no lens shift).
- For a level camera, m/px at an object = camera height / (contact row − 960).
  - Chestnut: 1049 − 960 = 89.
  - Rabbit: 1067 − 960 = 107.
  - So the rabbit's m/px is 0.832 × the chestnut's.
- Consistency check: with this correction the two horses' heights agree (chestnut 166 px → 1.92 m; pale 177 px at contact 1057 → 1.88 m). Without it they come out as 1.92 m and 2.04 m. The house comes out at about 7.7 m wide and 10 m tall, which is plausible.

## Rabbit length
- Horizontal extent of the scene track: median 45 px (range 38-54, varies with the hop pose).
- My own colour mask on frames 40-49, where the rabbit is clear of the brick wall: 42-56 px, median 46 px.
- Used 45.5 px.

## Answer
- 45.5 × 0.01158 × 0.832 = 0.438 m, rounded to **0.44 m**.
- Without the depth correction (single 2D scale) it would be 0.53 m. I chose the corrected value because the level-camera geometry and the matching horse heights support it.
- Confidence: moderate. The main uncertainty is the depth correction (±5%) and the hop pose (±8%).
