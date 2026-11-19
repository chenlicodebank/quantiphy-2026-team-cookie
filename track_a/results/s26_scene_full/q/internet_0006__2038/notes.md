# Q2038 – length of the black (dark) car, prior lane width = 3.66 m

Top-down drone shot of a static two-lane road (camera drift < 2 px). Single planar scale from the prior.

## Lane width (prior object), measure2.py
Per 60-px row band of a median background (frames 0/60/171): asphalt edges found by a saturation threshold, centre
line found as the brightest column (the dashes). Clean bands give left edge x≈521, right edge x≈596, centre line x≈559.
Road (asphalt) width median is 75 px. The edge-to-centre-line half-widths are 37–40 px, median about 38 px per lane
(left lane 38, right lane 37.5).
Scale = 3.66 m / 38 px = 0.0963 m/px.

## Dark car length
From the scene record (dark_car.csv; mask bbox along the road on clean frames): 68–72 px, median 69 px. The zoomed
crop at frame 30 agrees (≈1578→1648, about 70 px).
Length = 69 × 0.0963 ≈ 6.65 m.

## Checks / ambiguity
- Car width 36 px × 0.0963 = 3.5 m. The car fills most of its lane, which fits a narrow country road. The 3.66 m prior is
  a standard US lane value, not the true width here, so the absolute size is inflated. The answer follows the
  annotators' single-scale convention.
- Other reading: if "lane width" meant the whole road (75 px), the length would be 69 × 3.66/75 ≈ 3.37 m. That reading was
  rejected because the road has a centre line, so it has two lanes.
- Confidence: moderate. The pixel measurement is good to about 3%, but which reading of "lane width" the annotators used is
  the main uncertainty.
