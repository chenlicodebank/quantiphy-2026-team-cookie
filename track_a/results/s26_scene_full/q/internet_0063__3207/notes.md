# q_3207: height of the water bottle (cm), prior g = 9.8 m/s^2

## Method
The bottle is held horizontally against the wall, then dropped. The camera is rotated 90°, so gravity points to image +x. The fall happens in the wall plane, so this is treated as planar: one scale = 9.8 m/s² / (pixel acceleration of the fall).

**Pixel acceleration** (`track.py`, `fit_track.py`): I tracked the blue cap centroid myself in frames 36–56. The blob stays only ~30 px wide, so blur is short. Frame-to-frame dx in frames 41–53: 13, 27, 39, 50, 63, 76, 89, 101, 114, 124, 142, 146, 153 (impact at ~52/53). Quadratic fits:
- 41–50: 12.45 px/frame²
- 41–49: 12.58
- 42–51: 12.57
- 43–50: 12.41
- 41–52: 12.43

The y-component is about −0.3 px/frame², which is negligible. The scene-record centre track (`fit_record.py`) gives 12.2–12.6 over the same windows. The centre accelerates slightly less than the cap because of the small rotation (1°→11°). I adopted **12.45 px/frame²**.

**Time base:** file fps is 30.016 and question_fps is 30, a difference of 0.05%. I used 30. So a = 12.45 × 900 = 11205 px/s², and the scale is 9.8 / 11205 = 8.75e-4 m/px.

**Bottle height** (long axis, cap end to base), measured in code (`length.py`) in held frames:
- Blue-cap left edge to the base-end edge (dark base ring to bright wall) along rows 570–590: 253–254 px in frames 5, 15, 30 and 38. The cap end may be slightly covered by the thumb.
- Floor frame 66 (bottle upright near the wall plane), read by eye: about 253–258 px.
- Scene record: 258 ± 4 px.

I adopted **256 px**.

## Result
Height = 256 × 8.75e-4 m = 0.224 m, so the answer is about **22.5 cm**.

## Check / confidence
- Range across fit windows and reference points: 12.2–12.6 px/frame² for the acceleration and 253–260 px for the length. That gives 22.0–23.2 cm.
- A real Evian 500 ml bottle is about 21 cm, which is plausible within the ~7% expected from the planar convention and possible out-of-plane motion.

Confidence: moderate-high (±5%).
