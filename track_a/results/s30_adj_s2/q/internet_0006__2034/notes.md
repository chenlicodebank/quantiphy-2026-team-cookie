# q2034 – length of the motorcycle (prior: lane width = 3.66 m), internet video, nadir drone shot

File fps is 29.68 and question_fps is 30. No timing is involved, so the difference does not matter.

## Where the candidates part ways
Both earlier sessions measured the motorcycle at about 30–31 px. They differ only in which pixel span gets the
3.66 m "lane width":
- C1 (2.95 m) used one lane, from the centre line to the edge (about 37.5 px). At that scale the white car
  (78 px) comes out at 7.6 m and the dark car (69 px) at 6.7 m, which is implausible and fails the car check
  (car length must be 3–7 m).
- C2 (1.6 m) used the whole carriageway, but measured it at 72 px, which is a little narrow.

I use the whole road surface the vehicles drive on, curb to curb. This is the benchmark convention for a "lane
width" that names no particular lane, and it is the only reading that gives plausible car sizes.

## My measurements
- Road width (road.py, measure.py; median background):
  - The grey asphalt is about 75–78 px wide (left edge x ≈ 519–522, right edge x ≈ 597–600).
  - Including the dark edge strips it is about 82 px.
  - I adopted 78 px, so the scale is 3.66 / 78 = 0.0469 m/px.
- Motorcycle length (measure.py): along the road, the background difference gives 30–32 px at threshold 35 and
  27–30 px at threshold 50, over frames 0–114 (excluding the frames where the cars pass). I adopted 30.5 px.
- Length = 30.5 × 0.0469 = **1.43 m**. Using 75 px for the road gives 1.49 m; using 82 px gives 1.36 m.
  **Answer: 1.45 m.**

## Check
At the same scale the white car is 3.7 m and the dark car 3.2 m. These are plausible for small cars, and the
motorcycle-to-car ratio (0.39) is consistent with them. A car-based scale (a 4.5 m car) would give about 1.75 m,
which is the realistic size of a moped. The prior's scale makes everything somewhat small, but I follow the
single-scale convention.

I agree with C2's reading of the prior (not C1's) and differ only by a slightly wider road width.

Confidence: moderate. The answer hinges on whether the annotator took the lane width as the whole road; the
car-size check supports that reading.
