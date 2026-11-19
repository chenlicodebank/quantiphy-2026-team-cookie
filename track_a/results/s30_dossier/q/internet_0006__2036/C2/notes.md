# q_2036 – length of the white car (internet_0006)

Prior: lane width = 3.66 m. No depth_info. The file runs at 29.678 fps and the question uses 30 fps; the clip has no time dependence for this size question.

Scene: a static nadir drone shot of a narrow two-lane country road running vertically. The camera drift is under 2 px (scene/camera_shift.csv).

## Measurements (measure.py)
- Road asphalt width, edge to edge, from band-averaged horizontal grey profiles on frame 170 (no cars present):
  72–78 px across bands (outliers of 84–85 px where the dark gutter or verge is included). Taken as **75 px**,
  which agrees with the scene record (75–77 px). The centre line is at x≈560, so one half (one lane) is ≈37.5 px.
- White car bumper-to-bumper length from a column profile against the empty-road background:
  79 px (f0), 78 px (f30), 76 px (f60), 76 px (f90). Mean ≈ **77 px**. The record gives a median of 78; lens
  stretch makes the car read longer near the frame edges.
- Car width is 35–40 px, which nearly fills one painted half of the road.

## Scale choice
- Reading A: "lane" = the whole road surface, curb to curb (75 px = 3.66 m): 0.0488 m/px, giving a car length of 77 × 0.0488 = **3.76 m**
  and a width of about 1.8 m. Both are plausible, and this matches the rule for unnamed lanes.
- Reading B: "lane" = one half of the road (37.5 px): 0.0976 m/px, giving a car length of 7.5 m and a width of 3.6 m. This is implausible
  (a car longer than 7 m), so it is rejected.
- Second check: with 78 px (the record's median), Reading A gives 3.81 m. Using the 87 px outer kerb lines would give 3.27 m.

Answer: 3.76 m. Confidence: moderate. The scale depends on the lane interpretation. The real car looks like a
saloon of about 4.5–4.8 m, so the road is probably wider than 3.66 m in reality, but the single-scale convention gives about 3.76 m.
