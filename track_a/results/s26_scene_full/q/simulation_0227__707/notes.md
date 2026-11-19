# q_707 — length of the swimming ring (flamingo float), metres

Prior: black cat speed = 1.041 m/s. fps = question_fps = 24, so no retiming. No depth_info.

## Measurements (scripts in this folder)
- **Cat pixel speed** (`cattm.py`, `catspeed.py`): I template-matched the cat's torso and head over all 50 frames using three
  reference frames (0, 24, 49). The linear-fit slope is 5.39–5.40 px/frame, and the net displacement over 49 frames is
  5.415 px/frame. The scene record's body-centroid slope is 5.39. The full-mask centroid and box give 5.50–5.53, but tail
  and paw motion inflate those. I used **5.40 px/frame = 129.6 px/s**, which gives 0.00803 m/px at the cat's depth.
  The paw line stays at y ≈ 918 throughout, so the cat walks at a constant depth, parallel to the image.
- **Ring horizontal extent** (`ring4.py`, `ring2.py`, `ring3.py`): the left edge is at x = 642–643, found with a blue−green
  colour score because the shaded purple side is dark. The right edge is at x ≈ 800–801, from the brightness and
  background-difference profiles. That gives **158.5 px** (the record's box gives 159 px, 643–801). The neck and head stay
  inside the ring's horizontal extent. The ring is circular, so length = outer diameter.

## Perspective (cat and ring are at different depths)
The camera is level: verticals stay vertical, and a deck seam extended converges near (942, 540). So the horizon is at
y ≈ 540 = cy (`levels.py`). On the ground planes, depth ∝ height / (y − 540):
- the cat's paws are at y = 918.5 on the deck;
- the coping's front top edge is at y = 925 and the wall's waterline at y ≈ 972, so (H + c) / H ≈ 1.12;
- the ring's front waterline is at y ≈ 1016 and its widest row (equator) at y ≈ 987.

Two ways to get Z_cat / Z_ring_centre:
- from the equator row: 1.05–1.085;
- from the front waterline plus the ring radius, with f between 1500 and 2500 px: 1.06–1.085.

Moving the horizon by ±20 px keeps the ratio between 1.05 and 1.085. I used **1.065**.

## Result
- Ring length = 158.5 px × 0.00803 m/px / 1.065 = **1.195 m**, answered as **1.20 m**.
- A single 2D scale with no depth correction would give 1.27 m. I rejected that reading because the perspective is clear:
  the deck seams converge, the cat is on the deck behind the coping, and the float is in the water in front of it.

## Confidence
- The pixel measurements are good to about 1%.
- The depth-ratio correction is the main uncertainty, about ±2–3%.
- The overall answer is likely within about 4%.
