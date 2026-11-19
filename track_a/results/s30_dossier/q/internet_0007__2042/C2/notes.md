# Q2042 — length of the black car (prior: lane width = 3.66 m)

The video is a top-down drone shot of a narrow two-way road with a dashed centre line. The camera is almost static. The file
runs at 29.943 fps and the question at 30 fps; that difference doesn't matter for a size.
- **Black car** = the dark (blue-black) car in the left lane, which drives toward the top (scene "blue_car"). It is the only dark car;
  the other one is white.
- **Lane width.** One half of the road (about 37 px) would give a car 7.4 m long, which is impossible. The whole asphalt surface
  (curb to curb, about 74 px) gives a car 1.73 m wide across 35 px, which is realistic. So the prior's "lane" is the whole road surface.

## Measurements (frame 200 for the road; frames 0–80 for the car, where it is clean and unoccluded)
- **Road width** (roadwidth.py): grey-level profile across the road, with each edge at half contrast between the asphalt and the verge,
  over 64 row bands (excluding the SLOW marking). Median **74.2 px** (p10–p90 71.3–76.4). Spot checks with profile.py:
  y=700 → 76, 900 → 72.5, 1400 → 72, 1700 → 74. The record's 71 px was slightly narrow.
- **Car length** (measure2.py): colour-distance profile along the road through the car centre, with each bumper at half contrast,
  frames 0–80 every 5. Median **74.2 px** (range 71–77). The record's difference-mask length is 74 px (p10–p90 73–74), which
  agrees.

## Answer
Scale = 3.66 / 74.2 = 0.0493 m/px. Length = 74.2 × 0.0493 = **3.66 m**. The car is almost exactly as long as the road is wide.

## Checks
- The car's width of 35 px (including mirrors) gives 1.73 m, which is plausible.
- The two independent car-length methods (mask 74 px, half-contrast 74.2 px) agree.
- Uncertainty: a road width of 71–76 px gives 3.57–3.82 m.

Confidence: moderate-high on the convention, and about ±4 % on the pixel measurements.
