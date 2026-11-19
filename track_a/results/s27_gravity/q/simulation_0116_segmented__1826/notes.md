# q_1826 – height of each door (m)

2D clip, 24 fps (file fps = question_fps = 24), 32 frames. Prior: the football falls with g = 9.8 m/s².

## Scale (measure.py, ball_track.csv)
I re-tracked the football myself (mask min(RGB) < 240, largest component at x >= 880) and fitted
y(t) = y0 + v0 t + a t²/2 to the centroid:
- centroid, frames 0-31: a = 1797.5 px/s² (residual 0.6 px); frames 0-25: 1797.1; frames 5-25: 1797.7; frames 0-15: 1794.3; frames 16-31: 1803.4
- bbox-centre fits: 1795-1808 px/s²
-> a = 1798 px/s², so the scale is 9.8 / 1798 = 5.45e-3 m/px.

## Door height
I took row profiles of the yellow cabinet/door masks on frame 5 (columns 600-860):
- lower door: the mask starts at y 1374 (partial anti-aliased rows 1374-1377) and the last full row is 1717. The edges at 1376 and 1718 give a height of 343 ± 2 px.
- upper door: the top is at y 824-826. Its bottom edge is ragged because of segmentation artefacts (fragments end at about y 1168), which gives about 343 px. This matches the lower door, so both are the same model.
- height = 343 px × 5.45e-3 = **1.87 m** (with ±2 px: 1.86-1.88 m).

## Checks
- door width 161 px × 5.45e-3 = 0.88 m; 1.87 × 0.88 m is a realistic door.
- football long axis about 65 px, or 0.35 m (a real one is about 0.28 m, so about 25 % larger, within tolerance). This suggests the ball and the doors are at a similar depth, and the scale is plausible.
- The acceleration is stable within ±0.4 % across the frame windows and the reference points.

Confidence: high (about ±3 %). The main assumption is that the ball and the doors are at the same depth (2D scene).
