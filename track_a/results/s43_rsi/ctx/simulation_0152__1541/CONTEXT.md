# Context of question 1541 (organised record; every round adds to it)

## Question
- Text: What is the width, in meters, of the blue car?
- Its own prior: diameter of the tire of the yellow car = 0.764m
diameter of the tire of the blue car = 0.369m
- Its own depth_info: t=1s, distance_blueCarRightFrontTire_camera = 9.312m
- question_fps: 24
- Video: simulation_0152.mp4 (simulation, S3MC)

## The answer currently submitted
0.790563 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 0.753 and an earlier DeepSeek median B = 0.83; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.753 | 0.952 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 0.755 | 0.955 |
| C3 | Claude Opus 5.5 (Claude Code agent), 40_5 fresh per-question run | 0.73 | 0.923 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.66 | 0.835 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 1.0 | 1.265 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 0.95 | 1.202 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 1.1 | 1.391 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 0.85 | 1.075 |

DeepSeek median over its 5 runs: 0.95.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 0.845 (new, confidence medium, follows None)
- Where the answers part: depth ratio near/far front-tyre outer faces: Claude line read the far tyre's right silhouette on its lower-right arc (rows 892-906, the near hub's row) giving k=0.923; the far tyre centre is at row 863
- Fault proven: on the far tyre's lower arc the silhouette is not a fixed outer-face point (k rises 0.920->0.932 with row band); at the far tyre's own equator (u-route) k=0.911-0.916 and the independent vertical route (centre rows 863.2 vs 893.0 from horizon 539.1) k=0.9155-0.918; headlight symmetry gives 0.912 -> width 0.82-0.87 m, not 0.75
- Closure on the prior: 3.4 pct

# Context update: Q1541, round 1

## Established (scripts are in the round folder)
- **Bounding-box width.** It is set by the front tyres' outer faces: W = Z_no·(1/k − 1), where k = Z_near_outer / Z_far_outer.
- **Scale.**
  - The near (right) front tyre's outer circle has radius 53.3 px and centre row 893.0 (free fit of its right arc in frames 33-41, rms 0.1-0.2 px).
  - With depth_info 9.312 m at frame 24 (623.3, 893.0): f ≈ 2625 px, Z_centre 9.155 m, Z_no ≈ 9.085 m.
  - The tyre width (0.14 ± 0.05 m) moves W by only ±0.3%.
- **k from two independent routes.**
  - Vertical route: the far tyre's outer-circle centre is at row 863.2 (range 862.4-863.8). (863.2 − 539.1)/(893.0 − 539.1) gives k = 0.9155-0.918.
  - Horizontal route: the far tyre's right arc (−45°…60° around its own centre) is fitted with a fixed-radius circle, then regressed on the near tyre's lower-left outer edge, giving k = 0.911-0.916.
  - Symmetry check: the headlights sit at 1.0157 and 1.0805 Z_no. Their centre line (1.048) matches the tyre centre line at k = 0.915 (1.046).
- **Result.** W = 0.82-0.87 m; answer **0.845 m**.
- **Closure.** The yellow tyre (r = 99.2 px; depth 10.45 m from the ground-contact rows) comes out at 0.790 m against the prior 0.764 m: +3.4%.

## Ruled out
- **k = 0.923 (C1, C2; W ≈ 0.75).** The far edge was taken at rows 892-906, on the far tyre's lower arc, 30-43 px below its centre. Measured per band, k climbs from 0.920 (rows 888-893) to 0.932 (rows 906-911), so it is not a fixed point. C1's near edge at rows 889-897 is the end of the white sill. C1's "headlights 7 cm off-centre" anomaly disappears at k = 0.915.
- **C3's far-tyre circle with r0 = 55 px.** The far radius is about 48.8 px. C3's roof width is not the bounding box.
- **DeepSeek front-face eyeball widths (C5, C6, C7: 0.95-1.10).** They include the rounded corners and scatter from 0.68 to 1.27 m.

## Open
- The roof or rear box could be marginally wider than the tyres. C3 found the roof at about the tyre width; this was not re-measured with the corrected k.
- The far-centre row varies by ±0.5 px between frames and arc choices. This gives k ±0.002, i.e. W ±0.02 m.

### Round 2 (harness v3; files in context/round2/)
- Answer: 0.845 (new, confidence medium, follows None)
- Where the answers part: depth ratio k = Z_near/Z_far of the front tyres' outer faces: 0.915 (round 1) vs 0.923 (C1/C2), i.e. the far tyre's outer-face centre at row ~863 vs ~866
- Fault proven: C1/C2 read the far tyre's silhouette 28-43 px below its centre, where the nearer inner face takes over the silhouette; own fits give far centre row 862.8-864.0 (k 0.9145-0.918) and an axle-parallax slope of 0.912-0.914, not 0.923
- Closure on the prior: 2.1 pct

# Context update: Q1541, round 2 (verification of round 1)

## Established
- **Round 1's change is verified.** My own code (rowedge.py, nearedge.py, uroute.py) reproduces k ≈ 0.915 by two routes.
- **Answer 0.845 m kept** (decision "new", confidence medium).

### Far front tyre
- Fitted on its outer-face circle, per-row right silhouette, frames 16-18 and 20-22.
- Centre row 862.8 (rows 840-900) to 864.0 (rows 840-910). The second value is an upper bound, because below about v_c + 37 the inner face takes over the silhouette.
- Frames 19, 23 and 24 are contaminated (an edge bulge, background clutter) and give 867-870. Do not use them.

### Near front tyre
- Fitted on its outer face, right arc in frames 33-41: centre row 893.0-893.1, r 52.7-53.6 px, rms 0.2 px.

### Routes for k
| route | method | k | W |
|---|---|---|---|
| V (vertical) | (v_far − 539.1)/(v_near − 539.1) | 0.9145-0.918 | 0.81-0.85 m |
| U (horizontal, independent) | slope of the far circle's centre u on the front-hub u, frames 15-22; insensitive to assumed radius 48-49.8 | 0.912-0.914 | 0.86-0.88 m |

- Per-frame no-intercept ratios (0.917-0.920) depend on the assumed radius. Use the slope instead.

### Scale and closure
- Z_no = 9.085 m (f ≈ 2625 px).
- W = 9.085·(1/k − 1) gives 0.844 m at k = 0.915.
- Closure on the yellow tyre via ground-contact rows (bottom 895.7, r 93-99 px): −3.3 % to +2.1 %. This checks the scale only.

## Ruled out
- **k = 0.923 (C1, C2; W ≈ 0.75).** It needs the far centre at row 865.8 and a horizontal slope of 0.923. Neither route gives it on clean frames.
- **Submitted blend 0.7906.** Its A component (0.753) carries that fault.

## Open
- The far centre row is uncertain by ±0.6 px between row bands and frames, which gives W ±0.03 m.
- The routes spread from 0.81 (V) to 0.88 (U). A third independent route would narrow this. Candidates:
  - the far tyre's ground-contact row (hidden in contact shadow so far);
  - a rear-box near/far edge pair, frames 38-41, if the box is as wide as the tyres.
- I did not re-measure whether the body is narrower than the tyres. C1, C3 and round 1 say it is.
