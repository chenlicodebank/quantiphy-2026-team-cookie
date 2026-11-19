# Q1535 – distance between the pillars on one side (m)

Video: 3D Blender render, 24 fps (file fps = question_fps = 24). Static, level camera looking down the aisle,
principal point (960, 540) (vanishing point). Each side has a row of pillars at the same lateral offset: a near
pillar (only its aisle-facing face visible, at the image edge, with a "B1"), a mid pillar, and a third one at
the back wall. The answer is the spacing of adjacent pillars along the aisle (near → mid).

## Scale (prior + depth_info)
- Frame 12 (t = 0.5 s), left front tyre (the visible side of the car is its left side): tyre outer
  diameter 179 px vertically (top 702, bottom 881), rim centre (1657, 791). 3D distance 11.38 m → depth along
  the axis Z = 10.93 m, so f = 179·Z/0.764 = 2561 px (HFOV 41°). Camera height h = 0.764·(881−540)/179 =
  1.455 m (the wheel centre gives the same: 1.453 m).
- Check against the second given depth: B1 sign on the back wall at 23.44 m → the predicted wall/floor line at
  row 699, and the measured line is at about 697–699. ✓
- Floor depth: Z = f·h/(v − 540), with f·h = 3728 px·m.

## Pillars (frame 41, car gone; profiles measured in code: pillars.py, corners.py)
- Base of the mid pillar's front face: row 771.5 (both sides) → Z_mid_front = 16.10 m.
- Corner columns of the aisle-facing faces: left near far corner x = 95.3, left mid front/back corner 391.5 /
  427.3; right near far corner 1831.2, right mid front/back corner 1534 / 1496.3.
- Lateral offset X = Z·|x−960|/f = 3.57 / 3.61 m. Pillar depth along the aisle = 1.08 / 1.13 m.
- The near pillar's front corner falls just outside the frame (x ≈ −5), so I compared back corners:
  Z_near_back = 10.59 / 10.61 m and Z_mid_back = 17.18 / 17.23 m.
- **Spacing: left 6.60 m, right 6.63 m** (with the tyre-based f·h).

## Second route / checks
- Using the B1 wall depth instead of the tyre for f·h (wall line at 697.5): 6.53 / 6.56 m.
- Mid → third pillar spacing (front corners): 6.67 m, which agrees with a regular pillar pitch.
- Answer: mean ≈ 6.58 m. Confidence: good (about ±3 %). The main uncertainties are the contact/base rows (±1–2 px)
  and the corner columns (±0.5 px).
