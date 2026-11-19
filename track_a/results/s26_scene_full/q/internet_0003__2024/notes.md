# Q2024 – pizza cutter velocity at 0.2 s (cm/s); prior: Monopoly money width = 7.5 cm

## Time base
File fps 18.314, question_fps 24. The cutter's per-frame steps are smooth (30–40 px/frame in frames 0–14, with no
1-1-1-2 pattern), so no frames were dropped: every file frame is an original frame, and the odd 18.31 rate comes from
re-timing. I used the original 24 fps. So t = 0.2 s is frame round(4.8) = 5, and dt = 1/24 s.
(With 18.31 fps the answer would be about 30 cm/s.)

## Cutter speed (pixels)
Track: scene/tracks/pizza_cutter.csv, stabilised columns x_s0, y_s0 (the camera is handheld and drifts about 60 px).
I spot-checked the reference point (front of the black hub guard at the axle) on frame 4 in a zoomed crop: it is
within about 15 px of the recorded point and on the same feature.
Steps (px/frame) for frames 3–7: 35.7, 36.5, 34.2, 36.4, 40.5. The forward difference at frame 5 (p6 − p5) is
36.4 px; the local mean is about 35.8. I used 36 px/frame × 24 = 864 px/s.
Check by a second route: the back-of-hand track moves 40 px/frame here. The hand also rotates (net path 794 px against
745 px for the cutter), so I used the cutter point.

## Scale (one factor from the prior)
"Width" is the bill's short side. The long-side reading is ruled out: it would make the cutting hand about 9 cm long.
Measured short sides:
- 500 bill in the middle of the pile (bill500c.py, straightened profile, frame 27): 149 px. The record gives about
  150 px for the top 500 bill and about 150 px for the 100 bill.
- Lone "1" bill at the right (bill.py, segmented quad at frames 20 and 27): 172–178 px, so about 174 px.
The two disagree by 15%. The aspect ratios also differ (500 bill 2.18, 1 bill 1.74), and the frame is 2732 px wide,
about 1.067 × 2560, so the image is probably stretched horizontally. That fits the pizza being 1015 px wide and 964 px
tall. I don't know which bill the annotator measured, so I used 155 px, weighted toward the pile bills.
Scale = 7.5 / 155 = 0.0484 cm/px.

## Answer
864 px/s × 0.0484 = 41.8 cm/s, reported as **42 cm/s**.
Range by bill: 43.5 cm/s (149 px) and 37.2 cm/s (174 px).
Confidence: moderate. The main uncertainties are which bill sets the scale (±8%) and the time base.
