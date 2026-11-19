# Q2043: average speed of the black car (m/s); prior: lane width = 3.66 m

**Where the candidates part ways.** C1 (31.8) and C2 (17.4) agree on the pixel speed, about 11.86 px/frame. They differ
only on what the 3.66 m "lane width" covers in pixels:
- C1 used half the road, from an edge to the centre line: about 41 px.
- C2 used the whole paved strip: 75 px.

**Which reading.** I took the whole road surface, edge to edge (the benchmark convention for "width of the lane", curb to curb).
- Plausibility check with the car's 74 px length: the half-road scale makes the car 6.6 m long (+47 % over a typical 4.5 m car,
  so implausible). The full-road scale makes it 3.45 m (a small car, but plausible).
- So I agree with C2's reading. My strip width is slightly larger than theirs.

**My measurements.**
- Road width (road_width.py): I found the asphalt edges where saturation crosses its half level, in 20-px row bands every
  60 px over frames 15, 60, 150, 200 and 260. Rows hidden by the tree are excluded as outliers.
  - Median 78.4 px (IQR 77.6–79.8).
  - Scale = 3.66 / 78.4 = 0.0467 m/px.
- Pixel speed (speed.py, scene track blue_car, frames 0–127 while the car is fully in frame):
  - mean per-frame displacement: 11.86 px raw, 11.81 px background-stabilised;
  - net displacement per frame: 11.84 px; linear fit: 11.91 px.
  - I used 11.84 px/frame × 30 (question_fps; the file is 29.943 fps, a 0.2 % difference) = 355 px/s.
- Speed = 355 × 0.0467 = **16.6 m/s** (about 60 km/h, plausible on a rural road).

**Second route.** The car-length scale (a 4.5 m car over 74 px) gives about 21.6 m/s. That check only supports full road
rather than half lane; the answer itself uses the prior's single scale, as the convention requires.

**Confidence.** Pixel speed is good to about 1 %. Road pixel width is good to about 3 %, depending on where the edge is taken (C2: 75 px,
C1: 82 px). The main risk is the lane interpretation: the half-lane reading would give 31.8 m/s.
