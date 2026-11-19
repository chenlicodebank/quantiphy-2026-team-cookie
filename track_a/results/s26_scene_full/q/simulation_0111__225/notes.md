# q_225 – width of the boat (m)

Prior: boat speed = 2 m/s. 2D top-down scene (canal seen from above), static camera, 24 fps (file fps = question_fps).

## Scale (from the prior's speed)
- Template matching of the boat (measure.py) between frames: 5→60: 5.449 px/frame; 20→60: 5.449; 5→40: 5.452; 205→210: 5.43.
- The scene record's linear fit of the bow tip over frames 2–210 gives 5.496 px/frame.
- Adopted speed: 5.47 px/frame = 131.3 px/s (spread ±0.5%), so the scale is 2 / 131.3 = 0.01523 m/px.

## Boat width (beam)
- The widest row of the thresholded hull is 84 px in every frame tested (5, 20, 24, 40, 60, 205, 210).
- The half-maximum edge crossing gives 83.3–83.9 px. The principal-axis width in the record is 84.9 px; the boat is tilted only about 3.5°.
- Adopted width: 84 px.

## Answer
84 px × 0.01523 m/px = **1.28 m**.

Second route: the record's own values (84.8 px, 131.9 px/s) give 1.286 m. All variants fall within 1.27–1.30 m.
For a sanity check, the hull length of 233 px is about 3.5 m, which is a plausible size for a rowboat.

Confidence: high, about ±2%.
