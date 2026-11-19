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
