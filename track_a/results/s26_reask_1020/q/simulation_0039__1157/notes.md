# Q1157 – length of the eagle (m)

Answer: **0.83 m**

## Time base
File is 25 fps (75 frames) but question_fps = 24. File frames 1, 26, 51 duplicate 0, 25, 50, so the
72 unique frames are the original 24 fps frames: orig n -> file n+1 (n<=24), n+2 (25..48), n+3 (>=49).
So t=1 s = file frame 25, t=2 s = file frame 50.

## Scale (focal length) from the prior, boat speed 4 m/s
- Boat hull centroid / hull x0 / x1 tracks (scene/tracks/boat.csv, edge-truncated and duplicate frames removed)
  fitted linearly against the original frame index: 8.32 px/frame (centroid and mean of x0/x1/centroid agree).
- 3D: P = depth x unit ray (principal point 768,768); depths 177.2077 (t=1) and 177.9993 (t=2).
  Solve |P(48) - P(24)| = 4 m -> f = 9029 px (9021 with the alternative slope); used f = 9025 px (HFOV ~9.7 deg).
- Plausibility with this f: boat hull 495 px -> 9.7 m (fishing boat), person shoulder width 28 px -> 0.57 m,
  eagle max wingspan 90 px -> 1.78 m, eagle speed 11.6 m/s: all realistic.

## Eagle length
- measure2.py: dark-blob mask (threshold halfway between local background and black, also 35/65 % checks),
  extent of the mask projected on the body/flight direction (12 deg below image x, tail at left, beak at right,
  checked on 8x zoom crops f19, f40, f45, f57) for file frames 5-60 (skip f24-25 where it overlaps the
  person's shadow, and edge frames). Tail-to-beak extent 39-43 px in most frames; 45-48 px only at f31-35
  when the wingtips sweep forward. Median 41.1 px (thresholds 35/50/65 %: 40.4 / 41.1 / 42.0).
- Per-frame metric length = px x eagle depth(t) / f, depth linearly interpolated from the given 179.27 (t=1)
  and 177.10 (t=2): median 0.81 m.
- Foreshortening: eagle 3D velocity (back-projected with its depths) = 11.6 m/s with -2.17 m/s along the line
  of sight; this matches level flight over the ground plane, which is tilted to the image plane (the boat's
  depth also changes 0.79 m per 4 m). The body lies along the flight direction, so the image shows 0.982 of
  its length -> 0.81 / 0.982 = **0.825-0.828 m**.

## Check
Second route (other frame window): frames 37-60 alone give 41-42 px -> 0.83 m; frames 5-23 give 39.8 px
-> 0.80 m (slightly farther, same answer within 3 %). Value is within the real eagle range (0.7-1.0 m),
consistent with its 1.8 m wingspan.

Confidence: moderate-high (~±5 %); main uncertainty is whether the reference length includes wing poses
(the along-track extent reaches 0.96 m at f33-34) rather than beak-to-tail.
