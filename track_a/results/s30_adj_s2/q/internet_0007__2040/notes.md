# Q2040 – length of the white car (prior: lane width = 3.66 m), internet drone clip

The view is top-down. One scale comes from the prior, following the annotators' planar convention. The file runs at 29.94 fps and the question at 30 fps; this does not matter for a size.

## Where the earlier answers part ways
Both sessions measure the car at about 61 px. They differ only on which pixel span the "lane width" means:
- C1 (5.95 m) uses half the road, from the centre dashes to the edge, about 37.5 px.
- C2 (2.96 m) uses the whole asphalt strip, about 76 px.

## My measurements (roadw.py, meas2.py)
- Car length: a row-brightness profile through the car at a threshold of 30% of the contrast, taken at frames 120–280 in steps of 20. It gives 60–62 px with a median of **61 px**. Frame 220 sits on the SLOW marking and was left out. The scene record's mask gives 60–63 px.
- Road width, edge to edge:
  - The strongest gradient near the car's rows gives a median of **75 px** (IQR 73–77).
  - A grey-asphalt saturation threshold gives 64–73 px.
  - The scene record gives 71 px.
  - I use **74 px**.
- Car width: 30 px.

## Which reading is right
I read the prior as the whole drivable road surface, curb to curb, and agree with C2:
- This is the benchmark's stated convention for a road's "width of the lane".
- The half-road reading gives a scale of 0.098 m/px. That would make the white car 3.0 m *wide* and 6 m long, and the blue car 7.3 m long. A 3 m wide car is physically impossible.
- The whole-road reading gives a car 1.5 m wide and 3.0 m long, and a blue car 3.7 m long. These are small but possible.

## Answer
61 / 74 × 3.66 = **3.02 m**.

Second route: a road of 71–77 px gives 2.90–3.14 m, and a car of 60–62 px gives 2.97–3.07 m.

Confidence: the measurement itself is good to about ±4%. The main risk is that the annotator instead measured one lane, which would give about 6 m.
