# q2036 – length of the white car (prior: lane width = 3.66 m)

Static nadir drone shot of a narrow two-lane country road (file 29.68 fps, question 30 fps; no time dependence).
Internet convention: one scale = 3.66 m / pixel width of the "lane".

Where candidates part ways: which pixel extent is the "lane".
- C1: one half of the road (37.5 px) -> 7.5 m (car 3.6 m wide - impossible).
- C2: whole asphalt road surface (75 px) -> 3.76 m. C3: 79 px -> 3.52 m.
The benchmark rule (unnamed lane = road surface curb to curb) and the plausibility check both favour the whole road.

My measurements (measure.py):
- White car bumper to bumper (diff vs empty-road frame 170): 78 px (f0), 78 (f30), 75 (f60) -> ~77 px.
- Road: grey asphalt edges x≈520 -> 597 on zoomed frame 0 (≈76-77 px); scene record 75-77 px. The outer dark
  kerb/verge lines give 85-90 px (gradient method) - not the driving surface.
- Scale 3.66/76 = 0.0482 m/px -> length = 77 x 0.0482 = 3.71 m (car width ~37 px = 1.8 m, plausible).
- Check: with 75 px road -> 3.76 m; 77 px -> 3.66 m. Kerb-line reading (87 px) would give 3.24 m.

Agree with C2's reading (whole road). Answer 3.72 m. Confidence moderate (scale interpretation).
